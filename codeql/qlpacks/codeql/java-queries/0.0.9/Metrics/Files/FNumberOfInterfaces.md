# Number of interfaces
This metric measures the number of interfaces below this location in the tree. At a file level, this would just be the number of interfaces in the file.

In general, it is not a good idea to put multiple interfaces in the same file. Interfaces are intended in some sense to be publicly visible, and changes to them are expected to have a higher impact than changes to internal classes. Making a change to an interface forces everybody who depends on that interface to recompile their code, which is already hugely disruptive. If multiple interfaces are in the same file, not only do the people who depend on the changing interface need to recompile, but so does everyone who depends on any of the interfaces in the file (since they have a physical dependency on the file, not just a logical dependency on one of the interfaces in it). For this reason, a strict rule of one interface per file should be rigorously enforced.

Note that this should be compared to the advice for classes - whilst it is advisable to use a single file for each class, it is acceptable to put classes in the same file when they are logically related (if only then). It is far less acceptable in the case of interfaces due to their public-facing nature.


## Recommendation
Any interfaces that currently share a source file with another interface (or indeed a class) should be given their own file.


## References
* Java Language Specification. [9 Interfaces](https://docs.oracle.com/javase/specs/jls/se11/html/jls-9.html).
