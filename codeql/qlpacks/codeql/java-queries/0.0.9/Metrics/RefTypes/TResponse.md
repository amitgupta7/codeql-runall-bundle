# Class response
*Response* is the number of unique methods (or constructors) that can be called by all the methods (or constructors) of a class. For example, if a class has two methods (X and Y), and one method calls methods A and B, and the other method calls methods A and C, the class's response is 3 (methods A, B, and C are called).

Classes that have a high response can be difficult to understand and test. This is because you have to read through all the methods that can possibly be called to fully understand the class.


## Recommendation
Generally, when a class has a high response, it is because it contains methods that individually make large numbers of calls or because it has high efferent coupling. The solution is therefore to fix these underlying problems, and the class's response decreases accordingly.


## References
* S. R. Chidamber and C. F. Kemerer, *A metrics suite for object-oriented design*. IEEE Transactions on Software Engineering, 20(6):476-493, 1994.
