# Number of calls
If the number of calls that is made by a function (or method) to other functions is high, the function can be difficult to understand, because you have to read through all the functions that it calls to fully understand what it does. There are various reasons why a function may make a high number of calls, including:

* The function is simply too large in general.
* The function has too many responsibilities (see \[Martin\]).
* The function spends all of its time delegating rather than doing any work itself.

## Recommendation
The appropriate action depends on the reason why the function makes a high number of calls:

* If the function is too large, you should refactor it into multiple smaller functions, using the 'Extract Method' refactoring from \[Fowler\], for example.
* If the function is taking on too many responsibilities, a new layer of functions can be introduced below the top-level function, each of which can do some of the original work. The top-level function then only needs to delegate to a much smaller number of functions, which themselves delegate to the functions lower down.
* If the function spends all of its time delegating, some of the work that is done by the subsidiary functions can be moved into the top-level function, and the subsidiary functions can be removed. This is the refactoring called 'Inline Method' in \[Fowler\].

## References
* M. Fowler, *Refactoring*. Addison-Wesley, 1999.
* Wikipedia: [The Single Responsibility Principle](https://en.wikipedia.org/wiki/Single_responsibility_principle).
