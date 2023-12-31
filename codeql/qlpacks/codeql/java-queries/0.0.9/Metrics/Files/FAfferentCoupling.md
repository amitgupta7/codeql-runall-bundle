# Incoming file dependencies
This metric measures the number of incoming dependencies for each compilation unit, i.e. the number of other compilation units that depend on it. (A compilation unit is a `.java` or `.class` file.)

Compilation units that are depended on by many other units are typically time-consuming to change, because changing them forces all of the units that depend on them to be recompiled. Most systems have some units like this at the lowest level, and it is not necessarily a problem as long as the unit is only changed infrequently -- for instance, a compilation unit containing a string class might be depended upon by everything, but would be unlikely to change on a regular basis.

What is problematic is if a compilation unit that is heavily depended upon also depends on a lot of other compilation units that have reasons to change frequently, because it is then likely to need recompiling on a regular basis, triggering a ripple effect of recompilation throughout the code: such units are known as hubs, and can be responsible for greatly increasing the time needed for incremental recompilation.


## Recommendation
Aside from the advice given for classes that have high afferent coupling, which still applies when a compilation unit contains a single class, it is important to look at the number of classes that are in a particular compilation unit when dealing with high afferent coupling at the unit level. Having multiple classes in the same file can cause far more units to depend on a particular unit than would otherwise be the case: the solution is to move each class to its own compilation unit. This is a good idea in any case, as it makes the code more understandable and easier to maintain.


## References
* M. Fowler. *Refactoring*. Addison-Wesley, 1999.
