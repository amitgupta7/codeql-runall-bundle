# Number of co-committed files
This metric measures the average number of co-committed files for the files below this location in the tree.

A co-committed file is one that is committed at the same time as a given file. For instance, if you commit files A, B and C together, then B and C would be the co-committed files of A for that commit. The value of the metric for an individual file is the average number of such co-committed files over all commits. The value of the metric for a directory is the aggregation of these averages - for instance, if we are using `max` as our aggregation function, the value would be the maximum of the average number of co-commits over all files in the directory.

An unusually high value for this metric may indicate that the file in question is too tightly-coupled to other files, and it is difficult to change it in isolation. Alternatively, it may just be an indication that you commit lots of unrelated changes at the same time.


## Recommendation
Examine the file in question to see what the problem is.

* If the file is too tightly coupled, it will have high values for its afferent and/or efferent coupling metrics, and you should apply the advice given there.
* If the file is not tightly coupled, but you find that you are committing lots of unrelated changes at the same time, then you may want to revisit your commit practices.
