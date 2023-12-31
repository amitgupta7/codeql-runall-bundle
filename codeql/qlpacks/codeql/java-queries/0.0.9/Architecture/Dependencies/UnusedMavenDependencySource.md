# Unused Maven dependency (source)
For projects that build with Maven, unnecessary dependencies add a variety of maintenance burdens. Most immediately, unnecessary dependencies increase build time, because Maven rebuilds an artifact whenever its declared dependencies are modified. This rule identifies Maven dependencies that are declared in a POM file but are not used by the underlying source code.

If the dependency's source code is part of the code base being analyzed, then the result is reported by one version of the rule. Otherwise, the dependency is reported by a separate version of the rule. This allows the two types of unused Maven dependencies to be reported separately.


## Recommendation
Try removing the dependency from the POM file. Then run all build and test targets that are relevant for the modified POM file. If all of the relevant build and test targets still succeed, then leave the dependency out permanently. Doing so will make future maintenance of the relevant source code easier.

In some cases, there may be a true dependency on the code that is not detected by the analysis. If any of the build and test targets fail after the dependency is removed, then the result is a false positive, and the dependency should be restored.


## References
* Apache Maven Project: [Maven POM Reference: Dependencies](http://maven.apache.org/pom.html#Dependencies).
