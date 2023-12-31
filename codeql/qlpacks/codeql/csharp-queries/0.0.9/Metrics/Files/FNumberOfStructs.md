# Number of structs
This metric measures the number of structs in each file. Files with a large number of structs in are more difficult to read and manage. The structure of the project is not reflected in the organization of files which can make structs more difficult to find. They can also cause problems with version control systems by increasing the likelihood that two developers work on the same file at once. That said there are sometimes advantages to grouping structs together into the same file so care should be taken when evaluating this metric.


## Recommendation
Consider whether the structs are logically related. If they are not then it makes sense to put them in separate files.


## References
* MSDN. [struct](http://msdn.microsoft.com/en-us/library/ah19swz4(v=vs.71).aspx).
