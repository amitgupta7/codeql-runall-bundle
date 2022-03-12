# Insecure LDAP authentication
When using the Java LDAP API to perform LDAPv3-style extended operations and controls, a context with connection properties including user credentials is started. Transmission of LDAP credentials in cleartext allows remote attackers to obtain sensitive information by sniffing the network.


## Recommendation
Use LDAPS to send credentials through SSL or use SASL authentication.


## Example
The following example shows two ways of using LDAP authentication. In the 'BAD' case, the credentials are transmitted in cleartext. In the 'GOOD' case, the credentials are transmitted over SSL.


```java
public class InsecureLdapAuth {
	/** LDAP authentication */	
	public DirContext ldapAuth(String ldapUserName, String password) {
		{
			// BAD: LDAP authentication in cleartext
			String ldapUrl = "ldap://ad.your-server.com:389";
		}

		{
			// GOOD: LDAPS authentication over SSL
			String ldapUrl = "ldaps://ad.your-server.com:636";
		}

		Hashtable<String, String> environment = new Hashtable<String, String>();
		environment.put(Context.INITIAL_CONTEXT_FACTORY, "com.sun.jndi.ldap.LdapCtxFactory");
		environment.put(Context.PROVIDER_URL, ldapUrl);
		environment.put(Context.REFERRAL, "follow");
		environment.put(Context.SECURITY_AUTHENTICATION, "simple");
		environment.put(Context.SECURITY_PRINCIPAL, ldapUserName);
		environment.put(Context.SECURITY_CREDENTIALS, password);
		DirContext dirContext = new InitialDirContext(environment);
		return dirContext;
	}
}

```

## References
* Oracle: [LDAP and LDAPS URLs](https://docs.oracle.com/javase/jndi/tutorial/ldap/misc/url.html)
* Oracle: [Simple authentication](https://docs.oracle.com/javase/tutorial/jndi/ldap/simple.html)
* Common Weakness Enumeration: [CWE-522](https://cwe.mitre.org/data/definitions/522.html).
* Common Weakness Enumeration: [CWE-319](https://cwe.mitre.org/data/definitions/319.html).
