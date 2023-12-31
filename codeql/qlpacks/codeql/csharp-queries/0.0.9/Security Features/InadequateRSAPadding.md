# Weak encryption: inadequate RSA padding
This query finds uses of RSA encryption without secure padding. Using PKCS\#1 v1.5 padding can open up your application to several different attacks resulting in the exposure of the encryption key or the ability to determine plaintext from encrypted messages.


## Recommendation
Use the more secure PKCS\#1 v2 (OAEP) padding.


## References
* Wikipedia. [RSA. Padding Schemes](http://en.wikipedia.org/wiki/RSA_(algorithm)#Padding_schemes).
* Common Weakness Enumeration: [CWE-327](https://cwe.mitre.org/data/definitions/327.html).
* Common Weakness Enumeration: [CWE-780](https://cwe.mitre.org/data/definitions/780.html).
