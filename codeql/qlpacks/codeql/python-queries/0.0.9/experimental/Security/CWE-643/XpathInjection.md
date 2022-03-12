# XPath query built from user-controlled sources
Using user-supplied information to construct an XPath query for XML data can result in an XPath injection flaw. By sending intentionally malformed information, an attacker can access data that he may not normally have access to. He/She may even be able to elevate his privileges on the web site if the XML data is being used for authentication (such as an XML based user file).


## Recommendation
XPath injection can be prevented using parameterized XPath interface or escaping the user input to make it safe to include in a dynamically constructed query. If you are using quotes to terminate untrusted input in a dynamically constructed XPath query, then you need to escape that quote in the untrusted input to ensure the untrusted data can’t try to break out of that quoted context.

Another better mitigation option is to use a precompiled XPath query. Precompiled XPath queries are already preset before the program executes, rather than created on the fly after the user’s input has been added to the string. This is a better route because you don’t have to worry about missing a character that should have been escaped.


## Example
In the example below, the xpath query is controlled by the user and hence leads to a vulnerability.


```python
from lxml import etree
from io import StringIO

from django.urls import path
from django.http import HttpResponse
from django.template import Template, Context, Engine, engines


def a(request):
    value = request.GET['xpath']
    f = StringIO('<foo><bar></bar></foo>')
    tree = etree.parse(f)
    r = tree.xpath("/tag[@id='%s']" % value)


urlpatterns = [
    path('a', a)
]

```
This can be fixed by using a parameterized query as shown below.


```python
from lxml import etree
from io import StringIO

from django.urls import path
from django.http import HttpResponse
from django.template import Template, Context, Engine, engines


def a(request):
    value = request.GET['xpath']
    f = StringIO('<foo><bar></bar></foo>')
    tree = etree.parse(f)
    r = tree.xpath("/tag[@id=$tagid]", tagid=value)


urlpatterns = [
    path('a', a)
]

```

## References
* OWASP XPath injection : [](https://owasp.org/www-community/attacks/XPATH_Injection)/&gt;&gt;
* Common Weakness Enumeration: [CWE-643](https://cwe.mitre.org/data/definitions/643.html).
