# Cleartext storage of sensitive information using `SharedPreferences` on Android
`SharedPreferences` is an Android API that stores application preferences using simple sets of data values. It allows you to easily save, alter, and retrieve the values stored in a user's profile. However, sensitive information should not be saved in cleartext. Otherwise it can be accessed by any process or user in rooted devices, or can be disclosed through chained vulnerabilities, like unexpected access to the private storage through exposed components.


## Recommendation
Use the `EncryptedSharedPreferences` API or other encryption algorithms for storing sensitive information.


## Example
In the first example, sensitive user information is stored in cleartext.

In the second and third examples, the code encrypts sensitive information before saving it to the device.


```java
public void testSetSharedPrefs(Context context, String name, String password)
{
	{
		// BAD - sensitive information saved in cleartext.
		SharedPreferences sharedPrefs = context.getSharedPreferences("user_prefs", Context.MODE_PRIVATE);
		Editor editor = sharedPrefs.edit();
		editor.putString("name", name);
		editor.putString("password", password);
		editor.commit();
	}

	{
		// GOOD - save sensitive information encrypted with a custom method.
		SharedPreferences sharedPrefs = context.getSharedPreferences("user_prefs", Context.MODE_PRIVATE);
		Editor editor = sharedPrefs.edit();
		editor.putString("name", encrypt(name));
		editor.putString("password", encrypt(password));
		editor.commit();
	}

	{
		// GOOD - sensitive information saved using the built-in `EncryptedSharedPreferences` class in androidx.
		MasterKey masterKey = new MasterKey.Builder(context, MasterKey.DEFAULT_MASTER_KEY_ALIAS)
			.setKeyScheme(MasterKey.KeyScheme.AES256_GCM)
			.build();

		SharedPreferences sharedPreferences = EncryptedSharedPreferences.create(
			context,
			"secret_shared_prefs",
			masterKey,
			EncryptedSharedPreferences.PrefKeyEncryptionScheme.AES256_SIV,
			EncryptedSharedPreferences.PrefValueEncryptionScheme.AES256_GCM);

		SharedPreferences.Editor editor = sharedPreferences.edit();
		editor.putString("name", name);
		editor.putString("password", password);
		editor.commit();
	}
}

private static String encrypt(String cleartext) throws Exception {
	// Use an encryption or hashing algorithm in real world. The demo below just returns its
	// hash.
	MessageDigest digest = MessageDigest.getInstance("SHA-256");
	byte[] hash = digest.digest(cleartext.getBytes(StandardCharsets.UTF_8));
	String encoded = Base64.getEncoder().encodeToString(hash);
	return encoded;
}

```

## References
* Android Developers: [Work with data more securely](https://developer.android.com/topic/security/data)
* ProAndroidDev: [Encrypted Preferences in Android](https://proandroiddev.com/encrypted-preferences-in-android-af57a89af7c8)
* Common Weakness Enumeration: [CWE-312](https://cwe.mitre.org/data/definitions/312.html).
