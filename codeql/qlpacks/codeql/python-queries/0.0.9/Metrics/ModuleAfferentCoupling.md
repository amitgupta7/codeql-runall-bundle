# Incoming module dependencies
This metric measures the number of incoming dependencies for each module, that is the number of other modules that depend on it.

Modules that are depended upon by many other modules typically require a lot of effort to change, because changing them will force their dependents to change as well. This is not necessarily a bad thing -- indeed, most systems will have some such modules (one example might be an I/O module). However, modules with a high number of incoming dependencies and a high number of outgoing dependencies are hard to maintain. A module with both high afferent coupling *and* high efferent coupling can be problematic because, on the one hand they are hard to change (high afferent coupling), yet on the other they have many reasons to change (high efferent coupling). This contradiction yields code that is very hard to maintain or test.

Conversely, some modules may only be depended on by very few other modules. Again, this is not necessarily a problem -- we would expect, for example, that the top-level modules of a system would meet this criterion. When lower-level modules have very few incoming dependencies, however, it can be an indication that a module is not pulling its weight. In extreme cases, modules may even have an afferent coupling of `0`, indicating that they are dead code.


## Recommendation
It is unwise to refactor a module based purely on its high or low number of incoming dependencies -- a module's afferent coupling value only makes sense in the context of its role in the system as a whole. However, when combined with other metrics such as efferent coupling, it is possible to make some general recommendations:

* Modules with high numbers of incoming *and* outgoing dependencies are prime candidates for refactoring (although this will not always be easy). The general strategy is to split the module into smaller modules that each have fewer responsibilities, and refactor the code that previously used that module accordingly.
* Modules that have an afferent coupling of `0` may be dead code -- in this situation, they can often be deleted.

## References
* M. Fowler. *Refactoring*. Addison-Wesley, 1999.
