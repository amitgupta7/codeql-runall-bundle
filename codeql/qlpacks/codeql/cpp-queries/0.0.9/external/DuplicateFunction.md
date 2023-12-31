# Duplicate function
A function should never be duplicated verbatim in several places in the code. Of course the severity of this anti-pattern is higher for longer functions than for extremely short functions of one or two statements, but there are usually better ways of achieving the same effect.


## Recommendation
Code duplication in general is highly undesirable for a range of reasons: The artificially inflated amount of code hinders comprehension, and ranges of similar but subtly different lines can mask the real purpose or intention behind a function. There is also a risk of update anomalies, where only one of several copies of the code is updated to address a defect or add a feature.

In the case of function duplication, how to address the issue depends on the functions themselves and on the precise classes in which the duplication occurs. At its simplest, the duplication can be addressed by removing all but one of the duplicate function definitions and making callers of the removed functions refer to the (now canonical) single remaining definition instead.

This may not be possible for reasons of visibility or accessibility. A common example might be where two classes implement the same functionality but neither is a subtype of the other, so it is not possible to inherit a single function definition. In such cases, introducing a common superclass to share the duplicated code is a viable option. Alternatively, if the functions don't need access to private object state, they can be moved to a shared utility class that just provides the functionality itself.


## References
* Elmar Juergens, Florian Deissenboeck, Benjamin Hummel, and Stefan Wagner. 2009. Do code clones matter? In *Proceedings of the 31st International Conference on Software Engineering* (ICSE '09). IEEE Computer Society, Washington, DC, USA, 485-495.
