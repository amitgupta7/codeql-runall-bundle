# Incoming dependencies per class
This metric measures the number of incoming dependencies for each class, i.e. the number of other classes that depend on it.

Classes that are depended upon by many other classes typically require a lot of effort to change, because changing them will force their dependents to change as well. This is not necessarily a bad thing -- indeed, most systems will have some such classes (one example might be a string class). However, classes with a high number of incoming dependencies and a high number of outgoing dependencies are hard to maintain. They are hard to change (high afferent coupling) and yet there are many reasons to change them (high efferent coupling). This contradiction yields code that is very hard to maintain or test.

Conversely, some classes may only be depended on by very few other classes. Again, this is not necessarily a problem -- we would expect, for example, that the top-level classes of a system would meet this criterion. When lower-level classes have very few incoming dependencies, however, it can be an indication that a class is not pulling its weight. In extreme cases, classes may even have an afferent coupling of `0`, indicating that they are dead code.


## Recommendation
It is unwise to refactor a class based purely on its high or low number of incoming dependencies -- a class's afferent coupling value only makes sense in the context of its role in the system as a whole. However, when combined with other metrics such as efferent coupling, it is possible to make some general recommendations:

* Classes with high numbers of incoming *and* outgoing dependencies are prime candidates for refactoring (although this will not always be easy). The general strategy is to split the class into smaller classes, each of which has fewer responsibilities, and refactor the code that used the original class accordingly.
* Classes that have very few incoming dependencies and are not at the top level of a system may not be pulling their weight and should be refactored.
* Classes that have an afferent coupling of `0` may be dead code -- in this situation, they can often be deleted.

## References
* M. Fowler. *Refactoring*. Addison-Wesley, 1999.
* [Wikipedia: Code refactoring](https://en.wikipedia.org/wiki/Code_refactoring)
* [Refactoring as Meta Programming?](http://www.jot.fm/issues/issue_2005_01/column1/)
