# Self containedness of files
This metric measures the percentage of types on which the file depends for which the build process built from source. The availability of source code is one of the key factors that affects how easy a project will be to build for different versions of the .NET framework. Files with low self-containedness are also more affected by changes to their dependencies.


## Recommendation
Depending on your project, self-containedness may or may not be an issue for you. If you decide that it should be addressed then there are a few things you can do to easily increase self-containedness. One way of increasing self-containedness is by creating wrappers for any external classes. If the external class is changed then only your wrapper needs to be updated. You should also try to use libraries with source code available.


## References
* Wikipedia. [Software Portability](http://en.wikipedia.org/wiki/Software_portability).
