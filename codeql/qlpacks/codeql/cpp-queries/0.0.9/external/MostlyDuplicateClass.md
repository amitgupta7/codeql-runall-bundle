# Mostly duplicate class
In cases where several methods are duplicated between two (or more) classes, the classes themselves are highlighted as "mostly duplicate", rather than creating a large number of method-level warnings. The same caveats apply here, too.


## Recommendation
Code duplication in general is highly undesirable for a range of reasons: The artificially inflated amount of code hinders comprehension, and ranges of similar but subtly different lines can mask the real purpose or intention behind a method. There's also an omnipresent risk of update anomalies, where only one of several copies of the code is updated to address a defect or add a feature.

While completely duplicated classes are rare, they are usually a sign of a simple oversight (or deliberate copy/paste) on a developer's part. Usually the required remedy action is to remove all but one of them.

It is far more common to see duplication of many methods between two classes, leaving just a few that are actually different. Such situations warrant close inspection. Are the differences deliberate or a result of an inconsistent update to one of the clones? If the latter, then treating the classes as completely duplicate and eliminating all but one (while preserving any corrections or new features that may have been introduced) is the best course. If two classes serve genuinely different purposes but almost all of their methods are the same, that can be a sign that there is a missing level of abstraction. Introducing a common superclass to define the common methods and sharing the code is likely to prevent many problems in the long term.

Modern IDEs may provide refactoring support for this sort of transformation, usually under the names of "Pull up" or "Extract supertype".


## References
* Elmar Juergens, Florian Deissenboeck, Benjamin Hummel, and Stefan Wagner. 2009. Do code clones matter? In *Proceedings of the 31st International Conference on Software Engineering* (ICSE '09). IEEE Computer Society, Washington, DC, USA, 485-495.
