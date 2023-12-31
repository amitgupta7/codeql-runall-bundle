# Result of multiplication cast to wider type
An integer multiplication that is assigned to a variable of type `long` or returned from a method with return type `long` may cause unexpected arithmetic overflow.


## Recommendation
Casting to type `long` before multiplying reduces the risk of arithmetic overflow.


## Example
In the following example, the multiplication expression assigned to `j` causes overflow and results in the value `-1651507200` instead of `4000000000000000000`.


```java
int i = 2000000000;
long j = i*i; // causes overflow
```
In the following example, the assignment to `k` correctly avoids overflow by casting one of the operands to type `long`.


```java
int i = 2000000000;
long k = i*(long)i; // avoids overflow
```

## References
* J. Bloch and N. Gafter, *Java Puzzlers: Traps, Pitfalls, and Corner Cases*, Puzzle 3. Addison-Wesley, 2005.
* Java Language Specification: [Multiplication Operator](https://docs.oracle.com/javase/specs/jls/se11/html/jls-15.html#jls-15.17.1).
* SEI CERT Oracle Coding Standard for Java: [NUM00-J. Detect or prevent integer overflow](https://wiki.sei.cmu.edu/confluence/display/java/NUM00-J.+Detect+or+prevent+integer+overflow).
* Common Weakness Enumeration: [CWE-190](https://cwe.mitre.org/data/definitions/190.html).
* Common Weakness Enumeration: [CWE-192](https://cwe.mitre.org/data/definitions/192.html).
* Common Weakness Enumeration: [CWE-197](https://cwe.mitre.org/data/definitions/197.html).
* Common Weakness Enumeration: [CWE-681](https://cwe.mitre.org/data/definitions/681.html).
