# Inner class could be static
Nested classes allow logical grouping of related concerns, increasing encapsulation and readability. However, there is a potential disadvantage when using them that you should be aware of.

Any non-static nested class implicitly holds onto its "enclosing instance". This means that:

* The nested class has an implicitly defined field. The field holds a reference to the instance of the enclosing class that constructed the nested class.
* The nested class's constructors have an implicit parameter. The parameter is used for passing in the instance of the enclosing class. A reference to the instance is then stored in the field mentioned above.
Often, this is useful and necessary, because non-static nested class instances have access to instance state on their enclosing classes. However, if this instance state is not needed by the nested class, this makes nested class instances larger than necessary, and hidden references to the enclosing classes are often the source of subtle memory leaks.


## Recommendation
When a nested class does not need the enclosing instance, it is better to declare the nested class `static`, avoiding the implicit field. As a result, instances of the nested class become smaller, and hidden references to the enclosing class are made explicit.

If a reference to the enclosing class instance is required during construction of the nested class instance (but not subsequently), the constructor of the nested class should be refactored so that it is explicitly given a reference to the enclosing instance.

If the nested class refers to a type variable of an enclosing class instance, consider parameterizing the nested class by that type variable.


## References
* J. Bloch, *Effective Java (second edition)*, Item 22. Addison-Wesley, 2008.
* Java Language Specification: [8.1.3. Inner Classes and Enclosing Instances](https://docs.oracle.com/javase/specs/jls/se11/html/jls-8.html#jls-8.1.3).
* The Java Tutorials: [Nested Classes](https://docs.oracle.com/javase/tutorial/java/javaOO/nested.html).
