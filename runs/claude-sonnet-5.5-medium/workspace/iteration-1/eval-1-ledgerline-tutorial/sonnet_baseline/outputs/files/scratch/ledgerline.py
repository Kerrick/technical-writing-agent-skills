"""ledgerline: a small in-memory double-entry-free ledger for learning."""
from collections import defaultdict
from dataclasses import dataclass
from decimal import Decimal

__version__ = "2.1.0"


@dataclass(frozen=True)
class Entry:
    account: str
    amount: Decimal
    memo: str = ""


class Ledger:
    def __init__(self):
        self._entries = []

    def add(self, account, amount, memo=""):
        """Record an entry. `amount` must be a Decimal, int, or str.

        Floats raise TypeError because they cannot represent cents exactly.
        """
        if isinstance(amount, float):
            raise TypeError("amount must be Decimal, int, or str, not float")
        entry = Entry(account, Decimal(amount), memo)
        self._entries.append(entry)
        return entry

    def entries(self, account=None):
        """Return entries in insertion order, optionally for one account."""
        return [e for e in self._entries if account is None or e.account == account]

    def summarize(self, accounts=None):
        """Return {account: total} sorted by account name.

        Accounts with no entries are omitted, even if named in `accounts`.
        An empty ledger returns {}.
        """
        totals = defaultdict(Decimal)
        for e in self._entries:
            if accounts is None or e.account in accounts:
                totals[e.account] += e.amount
        return dict(sorted(totals.items()))
