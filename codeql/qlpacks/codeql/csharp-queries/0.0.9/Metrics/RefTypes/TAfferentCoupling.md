# Incoming dependencies
This metric calculates the number of incoming dependencies of a type (the number of other types that depend on it).

Types that have a large number of incoming type dependencies are very hard to change because any changes may require changes to their dependents. This is not necessarily a problem and it is expected that some types will have a lot of incoming dependencies in most projects. Types with a high number of incoming and outgoing dependencies are problematic because they are both hard to change and have a lot of reasons to need to change.

Types with very few incoming type dependencies (especially lower level types) might not be doing very much. Types with no incoming dependencies at all (and no static entry points) are dead code.


## Recommendation
This metric alone should not be used to decide whether a type needs to be refactored. Types with a large number of incoming and outgoing type dependencies should be considered for refactoring. Generally this means splitting up the type into multiple other types.

Types with very few incoming dependencies that are not at the top level of the program might not be pulling their weight and should possibly have their functionality merged with other classes.

Types with no incoming dependencies may be dead code that can be removed.


## References
* Robert Cecil Martin. *Agile Software Development: Principles, Patterns and Practices*. Pearson Education. 2002.
