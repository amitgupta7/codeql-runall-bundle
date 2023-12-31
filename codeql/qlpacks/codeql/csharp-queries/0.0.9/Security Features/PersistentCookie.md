# Cookie security: persistent cookie
This rule finds cookies that are made to expire in more than 5 minutes from now. Cookies are usually non-persistent, in which case they reside in the browser's memory only. However, by setting an expiration date in the future, cookies can be made persistent and are then written to disk to survive the browser restarts. If a persistent cookie is set to expire in a fairly distant future, it is easier for an attacker to steal its data.


## Recommendation
Do not put sensitive information in persistent cookies.


## References
* Common Weakness Enumeration: [CWE-539](https://cwe.mitre.org/data/definitions/539.html).
