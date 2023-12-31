# Mostly duplicate function
A "mostly duplicate function" is a function for which there is at least one almost exact duplicate somewhere else in the code, but for which there are no exact duplicates. There will be minor typographical differences between this function and any "mostly duplicate function" to which it corresponds (for example, comments and small code changes), preventing an exact match. Pairs of such functions are sometimes referred to as "similar".

This class of problem can often be more insidious than mere duplication, because the two implementations have diverged. This may be on purpose (when a function is copy-and-pasted and adapted to a new context) or accidentally (when a correction is only introduced in one of several identical pieces of code), and to address the problem one needs to understand which of the two situations applies.


## Recommendation
Code duplication in general is highly undesirable for a range of reasons: The artificially inflated amount of code hinders comprehension, and ranges of similar but subtly different lines can mask the real purpose or intention behind a function. There's also a risk of update anomalies, where only one of several copies of the code is updated to address a defect or add a feature.

In the case of function similarity, how to address the issue depends on the functions themselves and on the precise classes in which they occur. At its simplest, if the differences are accidental, the problem can be addressed by unifying the functions to behave identically. Then, we can remove all but one of the duplicate function definitions and make callers of the removed functions refer to the (now canonical) single remaining definition instead.

In more complex cases, look for ways of encapsulating the commonality and sharing it while retaining the differences in functionality. Perhaps the function can be moved to a single place and given an additional parameter, allowing it to cover all use cases? Alternatively, there may be a common preprocessing or postprocessing step which can be extracted to its own (shared) function, leaving only the specific parts in the existing functions.

Modern IDEs may provide refactoring support for this sort of transformation. Relevant refactorings might be "Extract function", "Change function signature", "Pull up" or "Extract supertype".


## References
* Elmar Juergens, Florian Deissenboeck, Benjamin Hummel, and Stefan Wagner. 2009. Do code clones matter? In *Proceedings of the 31st International Conference on Software Engineering* (ICSE '09). IEEE Computer Society, Washington, DC, USA, 485-495.
