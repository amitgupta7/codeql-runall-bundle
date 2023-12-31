# Recent changes
This metric measures the number of recent commits to files that have occurred below this location in the tree. A recent commits is taken to mean a commits that has occurred in the last `180` days.

All code that has changed a great deal may be more than usually prone to defects, but this is particularly true of code that has been changing dramatically in the recent past, because it has not yet had a chance to be properly field-tested in order to iron out the bugs.


## Recommendation
There is more than one reason why a file may have been changing a lot recently:

* The file may be part of a new subsystem that is being written. New code is always going to change a lot in a short period of time, but it is important to ensure that it is properly code reviewed and unit tested before integrating it into a working product.
* The file may be being heavily refactored. Large refactorings are sometimes essential, but they are also quite risky. You should write proper regression tests before starting on a major refactoring, and check that they still pass once you're done.
* The same bit of code may be being changed repeatedly because it is difficult to get right. Aside from vigorous code reviewing and testing, it may be a good idea to rethink the system design - if something is that hard to get right (and it's not an inherently difficult concept), you might be making life unnecessarily hard for yourself and risking introducing insidious defects.

## References
* N. Nagappan et al. *Change Bursts as Defect Predictors*. In Proceedings of the 21st IEEE International Symposium on Software Reliability Engineering, 2010.
