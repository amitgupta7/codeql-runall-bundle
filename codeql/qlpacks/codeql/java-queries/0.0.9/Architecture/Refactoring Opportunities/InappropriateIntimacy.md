# Inappropriate Intimacy
*Inappropriate intimacy* is an anti-pattern that describes a pair of otherwise unrelated classes that are too tightly coupled: each class uses a significant number of methods and fields of the other. This makes both classes difficult to maintain, change and understand. Inappropriate intimacy is the same as the "feature envy" anti-pattern but in both directions: each class is "envious" of some functionality or data defined in the other class.


## Recommendation
The solution might be as simple as moving some misplaced methods to their rightful place, or perhaps some tangled bits of code need to be extracted to their own methods first before being moved.

Sometimes the entangled parts (both fields and methods) indicate a missing object or level of abstraction. It might make sense to combine them into a new type that can be used in both classes. You may need to introduce delegation to hide some implementation details.

It may be necessary to convert the bidirectional association into a unidirectional relationship, possibly by using dependency inversion.

Modern IDEs provide refactoring support for this sort of issue, usually with the names "Move method", "Extract method" or "Extract class".


## References
* E. Gamma, R. Helm, R. Johnson, J. Vlissides, *Design patterns: elements of reusable object-oriented software*. Addison-Wesley Longman Publishing Co., Inc., Boston, MA, 1995.
* W. C. Wake, *Refactoring Workbook*, pp. 95&ndash;96. Addison-Wesley Professional, 2004.
