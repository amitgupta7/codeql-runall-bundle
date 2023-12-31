# Mostly similar file
When most of the lines in one file have corresponding "similar" lines in one or more other files, the files themselves are regarded as *mostly similar*. Two lines are defined as similar if they are either identical or contain only very minor differences.

Code duplication in general is highly undesirable for a range of reasons. The artificially inflated amount of code is more difficult to understand, and sequences of similar but subtly different lines can mask the real purpose or intention behind them. Also, there is always a risk that only one of several copies of the code is updated to address a defect or add a feature.


## Recommendation
Consider whether the differences are deliberate or a result of an inconsistent update to one of the clones. If the latter, then treating the files as completely duplicate and eliminating all but one (while preserving any corrections or new features that may have been introduced) is the best course. If two files serve genuinely different purposes but almost all of their lines are the same, that can be a sign that there is a missing level of abstraction. Can some of the shared code be extracted into methods (perhaps with additional parameters, to cover the differences in behavior)? Should it be moved into a utility class or file that is accessible to all current implementations, or should a new level of abstraction be introduced?


## References
* E. Juergens, F. Deissenboeck, B. Hummel, S. Wagner. *Do code clones matter?* Proceedings of the 31st International Conference on Software Engineering, 485-495, 2009.
