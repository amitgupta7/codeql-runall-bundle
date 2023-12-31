# Assigned value is overwritten
A value is assigned to a local variable, but whenever the variable is subsequently read, there has been at least one other assignment to that variable. This means that the original assignment is suspect, because the state of the local variable that it creates is never used.


## Recommendation
Ensure that you check the control and data flow in the method carefully. If a value is really not needed, consider omitting the assignment. Be careful, though: if the right-hand side has a side-effect (like performing a method call), it is important to keep this to preserve the overall behavior.


## Example
In the following example, the value assigned to `result` on line 5 is always overwritten (line 6) before being read (line 7). This is a strong indicator that there is something wrong. By examining the code, we can see that the loop in lines 3-5 seems to be left over from an old way of storing the list of persons, and line 6 represents the new (and better-performing) way. Consequently, we can delete lines 3-5 while preserving behavior.


```java
Person find(String name) {
	Person result;
	for (Person p : people.values())
		if (p.getName().equals(name))
			result = p;  // Redundant assignment
	result = people.get(name);
	return result;
```
