# Weak encryption: Insufficient key size
This rule finds uses of encryption algorithms with too small a key size. Encryption algorithms are vulnerable to brute force attack when too small a key size is used.


## Recommendation
The key should be at least 2048 bits long when using RSA and DSA encryption, 256 bits long when using EC encryption, and 128 bits long when using symmetric encryption.


## References
* Wikipedia. [Key size](http://en.wikipedia.org/wiki/Key_size)
* SonarSource. [Cryptographic keys should be robust](https://rules.sonarsource.com/java/type/Vulnerability/RSPEC-4426)
* CWE. [CWE-326: Inadequate Encryption Strength](https://cwe.mitre.org/data/definitions/326.html)
* Common Weakness Enumeration: [CWE-326](https://cwe.mitre.org/data/definitions/326.html).
