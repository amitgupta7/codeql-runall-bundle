# Class response
This metric counts the number of method calls in a class. Multiple method calls to the same method are only counted once. Calling a large number of different methods from a class makes it difficult to understand the class. For a full understanding of the class you must also understand every method called by the class. This makes the class difficult to test and debug


## Recommendation
Generally speaking, when a type has a high response metric, it is because it contains methods that individually make large numbers of calls or because it has high efferent coupling. The solution is therefore to fix these underlying problems, and the class's response will decrease accordingly.


## References
* Shyam Chidamber, Chris Kemerer. Towards a metrics suite for object oriented design. pp 12-13.
