# Use of `Kernel.open` or `IO.read`
If `Kernel.open` is given a file name that starts with a `|` character, it will execute the remaining string as a shell command. If a malicious user can control the file name, they can execute arbitrary code. The same vulnerability applies to `IO.read`.


## Recommendation
Use `File.open` instead of `Kernel.open`, as the former does not have this vulnerability. Similarly, use `File.read` instead of `IO.read`.


## Example
The following example shows code that calls `Kernel.open` on a user-supplied file path.


```ruby
class UsersController < ActionController::Base
  def create
    filename = params[:filename]
    open(filename) # BAD
  end
end  
```
Instead, `File.open` should be used, as in the following example.


```ruby
class UsersController < ActionController::Base
    def create
      filename = params[:filename]
      File.open(filename)
    end
  end  
```

## References
* OWASP: [Command Injection](https://www.owasp.org/index.php/Command_Injection).
* Example CVE: [Command Injection in RDoc](https://www.ruby-lang.org/en/news/2021/05/02/os-command-injection-in-rdoc/).
* Common Weakness Enumeration: [CWE-78](https://cwe.mitre.org/data/definitions/78.html).
* Common Weakness Enumeration: [CWE-88](https://cwe.mitre.org/data/definitions/88.html).
* Common Weakness Enumeration: [CWE-73](https://cwe.mitre.org/data/definitions/73.html).
