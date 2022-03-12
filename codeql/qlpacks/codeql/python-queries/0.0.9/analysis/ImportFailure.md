# Unresolved import
Tracing which module is imported by an import statement is very important in ensuring that the whole program is available for analysis. Failure to determine which module is imported by an import reduces the extent and accuracy of Semmle's analysis.

Missing imports will degrade the effectiveness of code analysis and may result in errors going undetected.


## Recommendation
Ensure that all required modules and packages can be found when running the extractor.


## References
* Semmle Tutorial: [Creating a CodeQL database](https://help.semmle.com/codeql/codeql-cli/procedures/create-codeql-database.html).
