# Number of re-commits for each file
This metric measures the number of file re-commits that have occurred below this location in the tree. A re-commit is taken to mean a commit to a file that was touched less than five days ago.

In a system that is being developed using a controlled change process (where changes are not committed until they are in some sense 'complete'), re-commits can be (but are not always) an indication that an initial change was not successful and had to be revisited within a short time period. The intuition is that the original change may have been difficult to get right, and hence the code in the file may be more than usually defect-prone. The concept is somewhat similar to that of 'change bursts', as described in \[Nagappan\].


## Recommendation
High numbers of re-commits can be addressed on two levels: preventative and corrective.

* On the preventative side, a high number of re-commits may be an indication that your code review process needs an overhaul.
* On the corrective side, code that has experienced a high number of re-commits should be vigorously code reviewed and tested.

## References
* N. Nagappan et al. *Change Bursts as Defect Predictors*. In Proceedings of the 21st IEEE International Symposium on Software Reliability Engineering, 2010.
