# Mostly duplicate class
If two classes share a lot of code then there is a lot of unnecessary code duplication. This makes it difficult to make changes in future and makes the classes less easy to read.


## Recommendation
While completely duplicated classes are rare, they are usually a sign of a simple oversight. Usually the required action is to remove all but one of them. A common exception to this rule may arise from generated code that simply occurs in several places in the source tree; the check can be adapted to exclude such results.

It is far more common to see duplication of many methods between two classes, leaving just a few that are actually different. Consider such situations carefully. Are the differences deliberate or a result of an inconsistent update to one of the clones? If the latter, then treating the classes as completely duplicate and eliminating one (while preserving any corrections or new features that may have been introduced) is the best course. If the two classes serve different purposes then it is possible there is a missing level of abstraction. Consider creating a common superclass of the duplicate classes.


## References
* E. Juergens, F. Deissenboeck, B. Hummel and S. Wagner, *Do Code Clones Matter?*, 2009. ([available online](https://wwwbroy.in.tum.de/~juergens/publications/ICSE2009_RP_0110_juergens.pdf)).
