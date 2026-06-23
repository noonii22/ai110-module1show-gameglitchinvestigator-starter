# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

*  Hitting Enter to apply my numberNumber is taken as input guess Nothing happens  
* The higher lower guessing markers are incorrect.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 43 | Hint tells me to go higher | Hint told me to go lower | ? |
| New Game button clicked | New game is started and allows me to start guessing again | Does not allow me to make guesses | ? |
| -5 | Number is not taken as input guess since its lower than 1 | Allows the guess | Should give error saying input cannot be < 1 |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude Code on this project and an example of and AI suggestion that was correct was fixing the high/low bug that was causing the user to be mislead after each guess. I was able to also have Claude correctly point out to me what might be causing the game to not restart properly when we want to start a new game. It was nice to have it pinpoint me quickly and allow me to start reading and when I got confused I had it clarify some of that confusion

One example where it was misleading was when I had to make the test file. I did not read my directory correctly so it instead created a new test directory and made the test file in there. When I tried running the test I would get an error saying that the directory naming convention is incorrect which is when I realized that the agent made a new directory with a seperate new name for it. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I would run it and also had the agent generate some simple tests for it. For the frontend related things I just tested it myself by visually seeing if it worked. 

I had a pytest for seeing if the high/low hints worked properly after each guess which showed me the logic still worked well after the refactoring we did.

AI helped me more so pin point bugs and be able to identify why it might be a cause. As for designing it was pretty straightforward testing we did this time around so nothing complex.



---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

This personally was my first time using streamlit but how I understood it was that for every change I made it would reset on every run so it explains some other untended bugs like the history feature. 
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

I like the habit of having the specific details in my prompt questions and making sure that I'm thorough in how I explain my changes. It makes the whole process a lot easier instead of having to reprompt if after it assumes things, 

As for what I would do differently I think I want to direct it more on what I want. This time around I let it suggest test cases to make but next time I want to have an idea of test cases I want specifically and have it generate those for me.

This helped in how I interact with AI in my prompts and how I can strategically be detailed in my prompts. I think also discovering that it can write up commit messages and do a lot more than I thought was something that changed the way I think about the use cases for a tool like this.
