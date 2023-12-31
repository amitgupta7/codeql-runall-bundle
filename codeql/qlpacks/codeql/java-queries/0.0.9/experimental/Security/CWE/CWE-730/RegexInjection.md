# Regular expression injection
Constructing a regular expression with unsanitized user input is dangerous as a malicious user may be able to modify the meaning of the expression. In particular, such a user may be able to provide a regular expression fragment that takes exponential time in the worst case, and use that to perform a Denial of Service attack.


## Recommendation
Before embedding user input into a regular expression, use a sanitization function to escape meta-characters that have special meaning.


## Example
The following example shows a HTTP request parameter that is used to construct a regular expression:


```java
package com.example.demo;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class DemoApplication {

    @GetMapping("/string1")
    public String string1(@RequestParam(value = "input", defaultValue = "test") String input,
                          @RequestParam(value = "pattern", defaultValue = ".*") String pattern) {
        // BAD: Unsanitized user input is used to construct a regular expression
        if (input.matches("^" + pattern + "=.*$"))
            return "match!";

        return "doesn't match!";
    }

    @GetMapping("/string2")
    public String string2(@RequestParam(value = "input", defaultValue = "test") String input,
                          @RequestParam(value = "pattern", defaultValue = ".*") String pattern) {
        // GOOD: User input is sanitized before constructing the regex
        if (input.matches("^" + escapeSpecialRegexChars(pattern) + "=.*$"))
            return "match!";

        return "doesn't match!";
    }

    Pattern SPECIAL_REGEX_CHARS = Pattern.compile("[{}()\\[\\]><-=!.+*?^$\\\\|]");

    String escapeSpecialRegexChars(String str) {
        return SPECIAL_REGEX_CHARS.matcher(str).replaceAll("\\\\$0");
    }
}
```
In the first case the user-provided regex is not escaped. If a malicious user provides a regex that has exponential worst case performance, then this could lead to a Denial of Service.

In the second case, the user input is escaped using `escapeSpecialRegexChars` before being included in the regular expression. This ensures that the user cannot insert characters which have a special meaning in regular expressions.


## References
* OWASP: [Regular expression Denial of Service - ReDoS](https://www.owasp.org/index.php/Regular_expression_Denial_of_Service_-_ReDoS).
* Wikipedia: [ReDoS](https://en.wikipedia.org/wiki/ReDoS).
* Common Weakness Enumeration: [CWE-730](https://cwe.mitre.org/data/definitions/730.html).
* Common Weakness Enumeration: [CWE-400](https://cwe.mitre.org/data/definitions/400.html).
