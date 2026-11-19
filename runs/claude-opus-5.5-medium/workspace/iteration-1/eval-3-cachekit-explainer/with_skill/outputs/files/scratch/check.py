"""Run the page's doctest transcripts, then its plain code blocks."""
import doctest
import re
import sys

sys.path.insert(0, "evals/developer-docs/files")
PAGE = "outputs/caching-in-cachekit.md"

text0 = re.sub(r"^```.*$", "", open(PAGE).read(), flags=re.M)
test = doctest.DocTestParser().get_doctest(text0, {}, PAGE, PAGE, 0)
runner = doctest.DocTestRunner(optionflags=doctest.ELLIPSIS)
runner.run(test)
result = runner.summarize()
print("doctest:", result)

text = open(PAGE).read()
blocks = re.findall(r"```python\n(.*?)```", text, re.S)
plain = [b for b in blocks if ">>>" not in b]
print("plain blocks:", len(plain))
for b in plain:
    ns = {}
    exec(compile(b, "<block>", "exec"), ns)
# exercise the sketch against the real thing
ns = {}
exec(compile(plain[2], "<sketch>", "exec"), ns)
calls = []
f = ns["cached"](60)(lambda a, k=None: calls.append((a, k)) or a)
f(1, k="x"); f(1, k="y"); f(k="z", a=2)
print("sketch calls:", calls)
from functools import _lru_cache_wrapper
print("memoize type ok:", isinstance(plain and __import__("cachekit").memoize(len), _lru_cache_wrapper))
