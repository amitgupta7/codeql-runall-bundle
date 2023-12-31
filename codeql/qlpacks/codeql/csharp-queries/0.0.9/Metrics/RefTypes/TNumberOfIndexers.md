# Number of indexers
This metric counts the number of indexers each reference type has. While indexers can improve code readability when used properly, having multiple overloads for indexers can be confusing. Implicit type conversions can make it unclear which indexer is being called. It is occasionally useful to have multiple indexers. For example, consider a simple login system. It may make sense to index users based on both an ID number and a login name. Both are unique and hence appropriate for indexing and it should not be too confusing which one is being called.


## Recommendation
Consider whether it is obvious what the function of each indexer is. Consider if it is confusing which indexer will be called with any given set of parameters. If either of these causes concern then it may be best to convert some indexers into methods that perform lookups themselves. Since these methods can be named it can be made more obvious what they do.


## References
* MSDN. C\# Programming Guide. [Indexers](http://msdn.microsoft.com/en-us/library/vstudio/6x16t2tx.aspx).
