# Mostly duplicate file
In cases where most of a file's lines have been duplicated in one or more other files, the files themselves are highlighted as "mostly duplicate", rather than creating a large number of method-level or class-level warnings. The same caveats apply here, too.


## Recommendation
Code duplication in general is highly undesirable for a range of reasons: The artificially inflated amount of code hinders comprehension, and ranges of similar but subtly different lines can mask the real purpose or intention behind a method. There's also an omnipresent risk of update anomalies, where only one of several copies of the code is updated to address a defect or add a feature.

While completely duplicated files are rare, they are usually a sign of a simple oversight (or deliberate copy/paste) on a developer's part. Usually the required remedy action is to remove all but one of them. A common exception may arise from generated code that simply occurs in several places in the source tree; the check can be adapted to exclude such results.

It is far more common to see duplication of many lines between two files, leaving just a few that are actually different. Such situations warrant close inspection. Are the differences deliberate or a result of an inconsistent update to one of the clones? If the latter, then treating the files as completely duplicate and eliminating all but one (while preserving any corrections or new features that may have been introduced) is the best course. If two files serve genuinely different purposes but almost all of their lines are the same, that can be a sign that there is a missing level of abstraction. Look for ways to share the functionality, either by extracting a utility class for parts of it or by encapsulating the common parts into a new super class of any classes involved.


## References
* Elmar Juergens, Florian Deissenboeck, Benjamin Hummel, and Stefan Wagner. 2009. Do code clones matter? In *Proceedings of the 31st International Conference on Software Engineering* (ICSE '09). IEEE Computer Society, Washington, DC, USA, 485-495.
