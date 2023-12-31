# Mostly similar module
This rule identifies two files that have a lot of the same lines but with different variable and method names. This makes it difficult to make changes in future and makes the code less easy to read.


## Recommendation
It is important to determine why there are small differences in the files. Sometimes the files might have been duplicates but an update was only applied to one copy. If this is the case it should be simple to merge the files, preserving any changes.

If the files are intentionally different then it could be a good idea to consider extracting some of the shared code into its own module and import that module into the original.


## References
* E. Juergens, F. Deissenboeck, B. Hummel and S. Wagner, *Do Code Clones Matter?*, 2009. ([available online](https://wwwbroy.in.tum.de/~juergens/publications/ICSE2009_RP_0110_juergens.pdf)).
