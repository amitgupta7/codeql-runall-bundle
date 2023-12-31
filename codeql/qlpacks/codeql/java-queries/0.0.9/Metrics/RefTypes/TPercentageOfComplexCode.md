# Percentage of complex code in types
This metric measures the percentage of the code within each type that is part of a complex method (defined to be a method that has a high cyclomatic complexity, i.e. there are a high number of linearly-independent execution paths through the method).

Methods with high cyclomatic complexity are typically difficult to understand and test. Types whose code is primarily contained within such tricky methods are often strong candidates for refactoring.


## Recommendation
Each of the individual methods whose cyclomatic complexity is too high should be simplified, e.g. by tidying up complex logic and/or by splitting the method into multiple smaller methods using the 'Extract Method' refactoring from \[Fowler\]. If splitting the methods up results in a class with too many methods, the refactoring should be followed up with another one to resolve the new problem (as per the advice given for that situation).


## References
* M. Fowler. *Refactoring*. Addison-Wesley, 1999.
