# Indirect source includes per file
This metric measures the number of files that are directly or indirectly included using `#include`, excluding header files which are outside the main source tree (for example, system headers).

The value of this metric is usually correlated to the file's build time: the more included files, the longer the compilation time. Since we don't count system headers, however, it is also a measure of the amount of the current code base that the present file relies on.

Often, files with a large number of includes do not require most of the included definitions, so they are contributing to unnecessarily long build times and creating artificial build dependencies.


## Recommendation
* Remove redundant `#include` directives
* Use the specific header file required, if possible, rather than a high-level header that includes many other header files as well
* Split header files that contain lots of unrelated definitions or include large unrelated header files

## References
* [Header files](http://www.learncpp.com/cpp-tutorial/19-header-files/)
* [Decoupling C Header Files](http://www.drdobbs.com/cpp/decoupling-c-header-files/212701130)
* [C++ Best Practice - Designing Header Files](https://accu.org/journals/overload/14/72/griffiths_1995/)
