# Local variable is never read
A local variable is assigned a value, but the variable is never read. This suggests that the local variable is either useless and should be removed, or that the value was intended to be used somewhere.


## Recommendation
Ensure that you check the control and data flow in the method carefully. If a value is really not needed, consider removing the variable. Be careful, though: if the right-hand side has a side-effect (like performing a method call), it is important to keep this to preserve the overall behavior.

