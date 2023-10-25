# Functional vs. Object-Oriented: Extensibility in Blackjack

### Overview

We implemented Blackjack in two ways: functional programming (FP) and object-oriented programming (OOP). Let's dive into which is easier to extend.

### Code Changes

**Functional**:
- Used standalone functions.
- For PRNGs, added new generator functions and tweaked the shuffling.

**Object-Oriented**:
- Encapsulated game logic in a `Blackjack` class.
- For PRNGs, made a subclass and tweaked shuffling.

### Adding a Third PRNG

**Functional**:
- Add a new generator function and adjust where PRNGs are chosen.

**Object-Oriented**:
- Just tweak the `shuffled_deck` method in the subclass.

### Running PRNGs in Parallel

**Functional**:
- Adjust the main game function to initialize multiple PRNGs.

**Object-Oriented**:
- Make multiple `BlackjackWithPRNG` instances and run them.

### The Verdict

OOP is more structured. Make a subclass or a new method. FP might need changes across multiple functions. For big projects, OOP's structure can be a lifesaver.

### What's Abstraction?

**Abstraction** is hiding the messy details and showing only what's needed. It's like a car's dashboard vs. its engine. You don't need to know how the engine works to drive.

### Why Care?

Abstraction lets us manage and grow complex software without losing our minds. It's about keeping things clean and organized.

### Conclusion

For our Blackjack game, OOP wins in extensibility. It's more organized, especially when things get complex. But hey, both have their moments!
