# Static field written by instance method
Static fields represent the shared state of all instances of a class. It is therefore bad practice to modify this state from any particular instance. Because static fields are shared between all instances of a class existing in all threads of a program, one instance trying to read the field while another tries to write it can lead to race conditions and hence mean the class is not thread safe. It also decreases readability as most developers expect instance methods to only affect the instance state and static methods to only affect the static state.


## Recommendation
It is important to evaluate the situation carefully before implementing a fix for an alert of this rule. Perhaps the field is erroneously declared static, and should in fact be an instance field; if so, then remove the static modifier from the field. If the field genuinely has to be static, evaluate the assumptions behind the code. Does it really have to be modified directly in an instance method? It could be helpful to wrap the accesses to the field in static methods, so that any concerns about synchronization can be addressed while avoiding code duplication.


## Example
In this example the field called "name" has been mistakenly declared static. Attempting to rename a person will actually modify the static name field and affect all people.


```csharp
public class Customer
{
    private static String name;
    public void rename(String newname)
    {
        name = newname; // BAD
    }
}

```

## References
* MSDN, C\# Reference, [static](http://msdn.microsoft.com/en-us/library/98f28cdx(v=vs.71).aspx).
