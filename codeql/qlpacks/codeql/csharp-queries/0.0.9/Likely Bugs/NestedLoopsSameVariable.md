# Nested loops with same variable
Inner loops should not write to the iteration variables of the enclosing loop. If an inner loop changes the iteration variable of the enclosing loop this is normally because the programmer mistyped the iteration variable of the inner loop. If this is the intended behavior, then this is an example of bad practice. Loops should be designed so that each loop controls its own iteration. Nested loops where iteration is shared between loops are more difficult to understand and maintain.


## Recommendation
If there is a mistake in the code then correct it. If the behavior is intended then consider redesigning the way that iteration of the loops is controlled. This will make the code easier for other programmers to understand and maintain.


## Example
This example will run forever because the inner loop increments i instead of j.


```csharp
class NestedLoopsSameVariable
{
    static void Main(string[] args)
    {
        for (int i = 0; i < 2; i++)
        {
            for (int j = 0; j < 2; i++)
            {
                Console.WriteLine(i + " " + j);
            }
        }
    }
}

```

## References
* MSDN: [for](http://msdn.microsoft.com/en-us/library/ch45axte.aspx).
