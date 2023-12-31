# Mostly duplicate file
When most of the lines in one file are duplicated in one or more other files, the files themselves are regarded as *mostly duplicate*.

Code duplication in general is highly undesirable for a range of reasons. The artificially inflated amount of code is more difficult to understand, and sequences of similar but subtly different lines can mask the real purpose or intention behind them. Also, there is always a risk that only one of several copies of the code is updated to address a defect or add a feature.


## Recommendation
Although completely duplicated files are rare, they are usually a sign of a simple oversight (or deliberate copy/paste) by a developer. Usually the required solution is to remove all but one of them. A common exception is generated code that simply occurs in several places in the source tree.

It is more common to see duplication of many lines between two files, leaving just a few that are actually different. Decide whether the differences are intended or the result of an inconsistent update to one of the copies:

* If the two files serve different purposes but many of their lines are duplicated, this indicates that there is a missing level of abstraction. Look for ways to share the functionality, either by extracting a utility class for parts of it or by encapsulating the common parts into a new super class of any classes involved.
* If the two files serve the same purpose and are different only as a result of inconsistent updates then treat the files as completely duplicate. Determine the most up-to-date and correct version of the code and eliminate all near duplicates.

## References
* E. Juergens, F. Deissenboeck, B. Hummel, S. Wagner. *Do code clones matter?* Proceedings of the 31st International Conference on Software Engineering, 485-495, 2009.
