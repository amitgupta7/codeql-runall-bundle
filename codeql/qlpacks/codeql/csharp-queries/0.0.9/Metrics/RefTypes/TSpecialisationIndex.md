# Specialization index
This metric measures how much a class overrides its ancestors. The metric is computed by determining the ratio of methods that are overridden and multiplying it by the depth of the class in the inheritance hierarchy inheritance hierarchy. A high specialization index indicates a poorly designed inheritance hierarchy.


## Recommendation
A high specialization index may indicate that lots of classes are specializing a base class in the same way. If this is the case for all subclasses of the base class then the base class should be modified with the same change being applied to all children. If only some of the subclasses have the modification then consider inserting another level in the inheritance hierarchy to contain the modification.

It is also possible that the inheritance hierarchy could be badly designed and really the heavily specialized classes should not be inheriting from their parent class at all.


## References
* Oege de Moor et al. Keynote Address: .QL for Source Code Analysis. Proceedings of the 7th IEEE International Working Conference on Source Code Analysis and Manipulation. 2007.
