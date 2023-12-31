# Mostly similar file
Two lines are defined as similar if they are either identical or contain only very minor differences. In cases where most of the lines in a file have corresponding "similar" lines in another file, the files themselves are highlighted as "mostly similar", instead of creating a large number of method-level or class-level warnings. The same caveats apply here, too.


## Recommendation
Code duplication in general is highly undesirable for a range of reasons: The artificially inflated amount of code hinders comprehension, and ranges of similar but subtly different lines can mask the real purpose or intention behind a method. There's also an omnipresent risk of update anomalies, where only one of several copies of the code is updated to address a defect or add a feature.

With files that are marked as mostly similar, special care should be taken. Why are they almost the same, and why are there differences? If the differences are accidental (for example from corrections that were only applied to one copy), then unifying the files and removing all but one is the best thing to do. If the files have genuinely different tasks, it is worth thinking about the reasons for the similarity. Can some of the shared code be extracted into methods (perhaps with additional parameters, to cover the differences in behavior)? Should it be moved into a utility class or file that is accessible to all current implementations, or should a new level of abstraction be introduced?


## References
* Elmar Juergens, Florian Deissenboeck, Benjamin Hummel, and Stefan Wagner. 2009. Do code clones matter? In *Proceedings of the 31st International Conference on Software Engineering* (ICSE '09). IEEE Computer Society, Washington, DC, USA, 485-495.
