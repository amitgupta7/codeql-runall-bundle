# Inheritance depth per class
This metric measures the inheritance depth of a class.

Whilst inheritance provides an avenue for code reuse, overly-deep class hierarchies can become a maintenance headache. Classes that inherit from many other classes can be brittle and hard to understand, because they depend on all of the classes further up the hierarchy. Conversely, changes to classes nearer the root of the hierarchy become harder and harder to make without breaking the descendants. In extreme cases, where the design of the hierarchy is seriously inappropriate, the class at the top of the hierarchy can become a 'blob' class: a storage point for anything that might be needed by one of its descendants. This is a key indicator that some serious refactoring is needed.


## Recommendation
As with many metrics, a high inheritance depth should be seen as an indicator that something is amiss, but further investigation will be needed to clarify the cause of the problem. Here are two possibilities:

* A class and its superclass represent fundamentally the same abstraction. In this case, they should generally be merged together (see the 'Collapse Hierarchy' refactoring on pp.279-80 of \[Fowler\]).
* The class hierarchy is trying to represent variation in more than one dimension using single inheritance. This can lead to an unnecessarily deep class hierarchy with lots of code duplication.
In languages that support it (such as C++), this situation can be modeled somewhat more effectively using multiple inheritance, but an altogether better approach is to use a component-based architecture (i.e. composition).


## References
* M. Fowler. *Refactoring*. Addison-Wesley, 1999.
* [Wikipedia: Code refactoring](https://en.wikipedia.org/wiki/Code_refactoring)
