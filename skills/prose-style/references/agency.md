# Agency

Read this before drafting or reviewing anything longer than a short reply. It covers which things may be the subject of which verbs. Each rule's examples are marked correct or wrong.

## What gives agency

1. You give a thing agency whenever you credit it with an act, a choice, a want, speech, or ownership, in any of these places:
   - a verb, in a main clause or a relative clause: "Use the bedtime that the phone's settings name" is wrong;
   - a possessive, when the thing can't own or do what follows it: "the manifest declares its dependencies" is wrong, because the app has them, while "the manifest declares your app's dependencies" is correct. A possessive is fine when what follows only belongs with the thing or is part of it: "the phone's settings" and "the map's scale" are fine phrases;
   - a "by" phrase: "the port is set to 8080 by the config file" is a close call, and "the port is set to 8080 in the config file" is correct;
   - a noun or an adjective that gives a thing a mind or an intent: "the spreadsheet has an opinion about the budget" and "the policy has a reason for the limit" are wrong.
2. There is no agency in verbs of being, having, containing, form, position, size, and route: "the file lists three items", "the file contains three items", "the chapter ends with a question", "the window faces the garden", "the file takes up 3 MB" are all correct. "The file names three items" is wrong, because naming is a choice.
3. Judge the sense of the verb the sentence uses. "The stairs take you to the tenth floor" (route), "the recipe makes twelve muffins" (yield), and "the spreadsheet tracks every expense" (running record) are correct. When a person who does the act is in view, credit them instead: once the pilot is in the discourse, write "the pilot tracks every flight in the logbook".
4. Verbs of evidence fit evidence: "the data suggests a downward trend" and "the study finds that sleep improves memory" are correct.

## Who can act

5. People, organizations of people, animals, running programs, machines, devices, physical forces, and natural events can act. Code that executes is a program, interpreted or compiled, so a script or a Rake task can be the subject of what it does. Documents, files a program reads, records, settings, values, and states can't act, except as rule 11 allows.
6. Verbs that need a mind never fit a document, file, or record: wants, knows, hopes, feels, prefers, promises, demands, refuses, names. The one exception is an instrument whose content appoints someone, under rule 11: a will can name an executor. "Belongs to" names an owner, so only something that can own may follow it: "the house belongs to her grandmother" is correct, "the key belongs to the shed" and "indentation belongs to the file" are wrong.
7. A program can take a mental verb that names what it literally does: "the server remembers your last login", "the app forgets your password after a week", "the compiler thinks the variable is unused" (a conclusion that may be wrong), "the spam filter decides which emails you see" are correct. "The backup script wants the disk to be mounted" is correct and "hopes" is wrong: a program can need a condition, but it can't hope. Whether "senses", "understands", or "knows where you are" fits depends on what the program actually does.
8. Credit whoever performs the act. A person acting through a tool gets the verb: "the pen signs the contract" is wrong for a ballpoint and correct for an autopen; "the oven bakes the bread" is wrong, while "the dishwasher washes the plates" and "the spell checker corrects your spelling" are correct. When the sentence doesn't say which kind of tool, the verdict depends on it.

## Files that programs read

9. When a program reads a file and acts on it, the program is the actor and the file is what it reads:
   - "The crontab runs the backup at 2 a.m." is wrong; cron runs it.
   - "The MX record routes mail to the backup server" is wrong; the sending mail server routes it. "The MX record lists the backup server as a mail host" is correct.
   - "The `.gitignore` excludes build output" is wrong; Git ignores the files that `.gitignore` lists.
   - "The firewall rule blocks port 22" is wrong; the firewall blocks it.
   - "The Makefile compiles the project" is wrong; `make` does. "The Rake task compiles the project" is correct: a Rake task is code that runs.
   - A Dockerfile depends on the step: a `RUN` step is a script, so it installs what it runs; a `FROM` line installs nothing, because Docker pulls an image.
10. The same holds for acts that follow from a file further down the line, and for setting another system's state, with or without "to" or "at" after "sets": "the crontab emails you the backup's output", "the DNS record sends mail", "the `.editorconfig` sets indentation to two spaces", and "the settings file sets the font size to 14" are wrong. "Your editor config sets tabs to four spaces" is correct: it is your editor's own configuration.

## Rules, laws, and other instruments

11. A rule, law, or other instrument may be the subject of what its own content makes true, when no program carries it out: "the zoning code bans factories on Main Street", "the contract defines a business day as Monday to Friday", "the schema allows a null birthday", "the will names her sister as executor", "the treaty gives the island to Spain", "the policy determines who gets a parking space", "the checklist requires a signature at step 5", "the ballot limits each voter to one choice", and "the invoice assigns the cost to marketing" are correct. It may not carry out what its content requires: "the law arrests anyone who drives drunk" and "the checklist signs the form" are wrong.
12. "Sets a limit" or "sets a deadline" fits only an instrument in force that creates it: "the law sets a speed limit of 65", "the league's rulebook sets a salary cap", "the contract sets a deadline of May 1", and "the config file sets a limit of two connections" are correct. It doesn't fit a statement of a decision made elsewhere ("the policy sets a limit of two bags", "the company handbook sets a dress code"), a record of a choice ("the settings file sets a limit of two connections"), or a program that only enforces it ("the booking system sets a limit of two bags"); use "has": "the ticket kiosk has a limit of four tickets". "Sets X at Y" adjusts a value, so "the lease sets the rent at $1,200" and "the menu sets the price of coffee at $3" are wrong.
13. Records that only hold values give, set, and name nothing: "the timetable gives 11:40 as the last train" and "the address book names her sister as the emergency contact" are wrong.

## Tense and reference

14. "Set" is an event and "own" is a state. "The airline set a limit of two bags last Tuesday" and "the company owns three trucks" are correct; "the airline sets a limit of two bags" is wrong, because an event in the present tense reads as a habit. For an instrument in force, "sets" describes a standing state, which is why rule 12's examples are correct.
15. Use "the" only for something the reader already knows. Otherwise a sentence about "the lockfile" reads as a claim about every lockfile: "the lockfile pins Rails at 8.1" is wrong, while "`Gemfile.lock` pins Rails at 8.1" and "a lockfile can pin Rails at 8.1" are correct. "A batch makes thirty cookies" is correct and "the batch makes thirty cookies" is wrong.
16. An event takes the past tense and a text the present: "the trial found that the drug works" is correct, "the trial finds" is wrong, and "the study finds" is correct.

## The object

17. Check the object as well as the subject:
   - "House" needs something that can be sheltered: "the barn houses forty cows" and "the museum houses a collection of clocks" are correct; "the building houses three shops" and "the mall houses a pharmacy" are wrong.
   - "Carry" needs the carrier to move the thing, or a force outside the thing to move it through the carrier: "the ferry carries forty cars", "the conveyor belt carries boxes", "the pipe carries water to the garden", "the sled carries the child down the hill", and "the river carries the boat downstream" are correct. "The bridge carries four lanes" (part of it), "the road carries twenty thousand cars a day" (they move themselves), and "the shelf carries forty books" (held still) are wrong. "The bike carries its rider up the hill" is correct for an e-bike and wrong for a bike the rider pedals.
   - "Contain" needs a container and something containable: "the envelope contains a check" and "the email from MegaCorp Inc contained a coupon code" are correct; "the letter contains a check", "Dad's letter contained an apology", and "the jar holds a smell of vinegar" are wrong. "Hold" means physical holding: "the email holds a threat" is wrong.

## Messages

18. A message isn't its speaker. "Mary's text message sounded angry" is correct and "the bank's text message sounded angry" is wrong: a company's message has no mood. An impression of the reader fits any message: "the bank's text message looked like a scam" is correct.

## Causes

19. An event or force may take a verb of effect, such as stop, end, delay, interrupt, cost, kill, wake, knock out, shut down, and ground (keep on the ground): "the storm knocked out the power", "the rain stopped the game", "the storm delayed the flight", "the recession cost him his job", "the earthquake woke the whole town", "the good reviews sold the book", and "the deadline forced us to cut the feature" are correct.
20. A verb whose meaning includes a decision belongs to people: "the scandal fired the CEO", "the drought rationed the water", "the power outage canceled the meeting", and "the fire closed the highway" are wrong. With a natural event as the subject, such a verb is a close call ("the snowstorm canceled the flight"); "the snowstorm caused the flight to be canceled" is correct. "The strike shut down the factory" is correct, because a strike is people acting.
21. A state named by an adjective and a noun is a reason, not an actor: "the empty tank stopped the car" and "the locked gate kept the dog in" are wrong, and "the gate kept the dog in" is correct. A condition that only allows something doesn't act: "the open door let the cat out" is wrong.
22. Choosing a cause assigns blame or excuses it. Writing "the wet floor made her slip" hides whoever wet it, and writing "the drought raised food prices" takes a side on whether sellers chose to charge more. Pick the cause on purpose.

## Want, need, require, make

23. A form, page, or device can want the input it takes from you: "the web form wants your name", "the login page wants your password", "the card reader wants your PIN" are correct. "Wants a" for a requirement is wrong; use "needs": "the vending machine needs exact change", "the build needs Ruby 4.0". A wish about the quality of your input is its authors' wish: "the survey wants your honest opinion" is wrong.
24. A system can want you to do something you may refuse: "the streaming service wants you to upgrade to Premium" is correct. Test every "wants you to": if the reader can't go on without doing it, it's a condition, not a want, whatever the reason for it, and "wants" is wrong. Typical conditions are a tutorial, an account or a login, terms, a confirmation, an ad, turning off an ad blocker, a required checkbox, and buying what you've run out of: "the game wants you to buy more coins" is correct, because coins are optional, and "the game wants you to buy more lives" is wrong, because you can't play without them. "The app wants you to install a security patch before you continue" is wrong when you can't continue without the patch. For a condition, write "you have to" or "makes you": "you have to finish the tutorial first", "the free app makes you watch an ad before it saves your file". "Before you log in" gives an order of steps, so "wants" fits; "before you can log in" makes it a gate, so it doesn't.
25. "Needs" is a real necessity, credited to whoever has it: "the bank needs you to verify your identity" is correct, "the bank's app wants you to verify your identity" is wrong, and "you need to watch a video to unlock the next level" is correct. "The app needs you to watch a video" is wrong: the need is yours.
26. "Requires you to" is a rule imposed on you: "the website requires you to use light mode" is correct, while "the website requires light mode", "needs light mode", and "wants light mode" are wrong.
27. Each of these verbs shows the reader how the writer feels about the actor. With "needs", the writer accepts a necessity; with "makes you", the writer resents a compulsion; with "wants", the writer suspects a motive. "Has", "lists", and "says" show no attitude.

## Screens and the programs behind them

28. A screen element is its system's message. It can't want anything: "the paywall wants you to subscribe", "the banner wants you to subscribe", "the error message wants you to try again later" are wrong. A screen that collects input can ask for it: "the login screen asks for your password" and "the pop-up asks for your email address" are correct. A request made on another program's behalf belongs to that program: "the browser asks for your location" is correct and "the permission dialog asks for your location" is wrong. "The confirmation dialog asks whether you're sure" reads correctly to readers who build interfaces.
29. A program that stands on its own can ask: "the chatbot asks for your order number", "the installer asks where to put the app", "the CAPTCHA asks you to pick the traffic lights" are correct.
30. "Says" reports content: "the tooltip says to save first" is correct, while "the tooltip tells you to save first" is wrong.

## What the writer knows

31. Learn the mechanism before you choose the actor. A writer who doesn't know how a thing works gives the agency to the file they edited, as with the MX record, and teaches the reader the same wrong model.
32. A writer who knows a field well hears its idioms as correct: "the style sheet hides the sidebar on phones" feels right to someone who writes CSS. Push back hardest there. Name what acts, and keep the idiom only on purpose, for readers in that field.

33. The verdict depends on the audience. The same sentence can be correct for readers who build the thing and wrong for readers who only use it: "the confirmation dialog asks whether you're sure" reads correctly to an interface developer, while a user hears the program asking. Write for the readers you have.

## Register

34. In speech and narrative, readers accept agency that technical writing can't have. "The low price convinced me to buy it" is common in speech, "the pandemic emptied the offices" works in a personal story, and "the printer wants paper" can be an indirect request to fetch some. In technical writing, use none of them.
35. False agency used on purpose is a jolt, as when someone angry says "The key *belongs* to the shed!" about a key that keeps leaving the shed. Readers feel accidental false agency as the same jolt. Never use it in technical writing.

## Verdicts that aren't yes or no

36. When the verdict depends on a fact the sentence doesn't give, such as which kind of tool, which era, or what the program does, it depends; state the fact, or ask.
37. When every fact is known and the line itself is blurred, it is a close call: "the open window cools the room". Prefer a sentence with a clear actor.
