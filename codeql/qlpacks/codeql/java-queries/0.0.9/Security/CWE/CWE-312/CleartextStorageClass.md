# Cleartext storage of sensitive information using storable class
Sensitive information that is stored unencrypted is accessible to an attacker who gains access to the storage.


## Recommendation
Ensure that sensitive information is always encrypted before being stored. It may be wise to encrypt information before it is put into a heap data structure (such as `Java.util.Properties`) that may be written to disk later. Objects that are serializable or marshallable should also always contain encrypted information unless you are certain that they are not ever going to be serialized.

In general, decrypt sensitive information only at the point where it is necessary for it to be used in cleartext.


## Example
The following example shows two ways of storing user credentials in a cookie. In the 'BAD' case, the credentials are simply stored in cleartext. In the 'GOOD' case, the credentials are hashed before storing them.


```java
public static void main(String[] args) {
	{
		String data;
		PasswordAuthentication credentials =
				new PasswordAuthentication("user", "BP@ssw0rd".toCharArray());
		data = credentials.getUserName() + ":" + new String(credentials.getPassword());
	
		// BAD: store data in a cookie in cleartext form
		response.addCookie(new Cookie("auth", data));
	}
	
	{
		String data;
		PasswordAuthentication credentials =
				new PasswordAuthentication("user", "GP@ssw0rd".toCharArray());
		String salt = "ThisIsMySalt";
		MessageDigest messageDigest = MessageDigest.getInstance("SHA-512");
		messageDigest.reset();
		String credentialsToHash =
				credentials.getUserName() + ":" + credentials.getPassword();
		byte[] hashedCredsAsBytes =
				messageDigest.digest((salt+credentialsToHash).getBytes("UTF-8"));
		data = bytesToString(hashedCredsAsBytes);
		
		// GOOD: store data in a cookie in encrypted form
		response.addCookie(new Cookie("auth", data));
	}
}

```

## References
* SEI CERT Oracle Coding Standard for Java: [SER03-J. Do not serialize unencrypted, sensitive data](https://wiki.sei.cmu.edu/confluence/display/java/SER03-J.+Do+not+serialize+unencrypted+sensitive+data).
* M. Dowd, J. McDonald and J. Schuhm, *The Art of Software Security Assessment*, 1st Edition, Chapter 2 - 'Common Vulnerabilities of Encryption', p. 43. Addison Wesley, 2006.
* M. Howard and D. LeBlanc, *Writing Secure Code*, 2nd Edition, Chapter 9 - 'Protecting Secret Data', p. 299. Microsoft, 2002.
* Common Weakness Enumeration: [CWE-499](https://cwe.mitre.org/data/definitions/499.html).
* Common Weakness Enumeration: [CWE-312](https://cwe.mitre.org/data/definitions/312.html).
