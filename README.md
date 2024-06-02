# Messy To Cleaner Code: Car Simulator
Understanding how to write clean code has always eluded me. It is not something that is taught in any of my uni modules. While I am modulating and fucusing on the single-responsibility principle, I find myself lingering on whether I have found an acceptable outcome to my search for a template to follow.

## Messy Code Car Simulator
This is a novice project that was actually an assigment from year 0 (Foundaton) of my degree. This was the first challenge that I completed that was not in a Leetcode-style where test cases were available to check against. I was expected to create my own test cases. I competed this assignment with 7 months of Python classes and tutorials and 7 months of self-taught online learning through 3 certificates from edx website. Looking back, I can see that even after 14 months of learning to program, I still barely reached a beginner understanding of programming.

## Clean Code Car Simulator
This is the same project, but refactored after another 2 years of programming. I must point out that during this time, I did not programming in Python as C++ was our prinicle language. Using the concepts learned, I rewrote the project to reflect my ability as a student in their final year of study. 

## Changes made.
There were so many changes made, including simplification of conditioanls, fixing code that repeats itself, minimising comments. Here is a more indepth look:

### Removing multiple if statements
I returned to this assessment a year or so after submission and the first things that frustated me was the amount of "if" statements in the run-simulator method. At the time I did not know how to improve this, however, the following year I was able to improve this by using a dictionary with a tuple as its value. The tuple contained the method and its argument to be passed. the dictionary key was the command, for example "ACCELERATE" or "BRAKE".

![ifStatements](https://github.com/WillowSaysWhat/messyToCleanCarSim/assets/126318401/9b92d32d-da03-4eeb-a283-cdcf422236f3)

### Minimising comments.
In my eagerness, I commented every line in my original assessment. I improved this by only commenting where necessary. This can be seen in the image above. I have learned over the years that over-commenting can make the code competely unreadable. This is, i believe is the case with my original submission.

