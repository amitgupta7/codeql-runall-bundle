# Frequency counts for external APIs that are used with untrusted data
Using unsanitized untrusted data in an external API can cause a variety of security issues. This query reports all external APIs that are used with untrusted data, along with how frequently the API is used, and how many unique sources of untrusted data flow to this API. This query is designed primarily to help identify which APIs may be relevant for security analysis of this application.

An external API is defined as a call to a callable (method/property accessor/operator/...) that is not defined in the source code, not overridden in the source code, and is not modeled as a taint step in the default taint library. External APIs may be from the .NET standard library, third-party dependencies or from internal dependencies. The query will report the signature with a fully qualified name, along with either `[param x]`, where `x` indicates the position of the parameter receiving the untrusted data or `[qualifier]` indicating the untrusted data is used as the qualifier to the call.


## Recommendation
For each result:

* If the result highlights a known sink, no action is required.
* If the result highlights an unknown sink for a problem, then add modeling for the sink to the relevant query.
* If the result represents a call to an external API which transfers taint, add the appropriate modeling, and re-run the query to determine what new results have appeared due to this additional modeling.
Otherwise, the result is likely uninteresting. Custom versions of this query can extend the `SafeExternalAPICallable` class to exclude known safe external APIs from future analysis.


## Example
If the query were to return the API `System.Web.HttpResponse.Write(string) [param 0]` then we should first consider whether this a security relevant sink. In this case, this is writing to a HTTP response, so we should consider whether this is an XSS sink. If it is, we should confirm that it is handled by the XSS query.


## References
* Common Weakness Enumeration: [CWE-20](https://cwe.mitre.org/data/definitions/20.html).
