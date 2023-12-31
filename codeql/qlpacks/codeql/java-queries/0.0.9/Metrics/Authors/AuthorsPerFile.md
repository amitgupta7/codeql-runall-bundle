# Number of authors (Javadoc)
A file's Javadoc comment can include a tag that lists the authors who have worked on the file.

A file that has been changed by a large number of different authors is the product of many minds. New authors working on the file may be less familiar with the design and implementation of the code than the original authors, which can be a potential source of defects. Furthermore, if the code is not carefully maintained, it often results in a lack of conceptual integrity.


## Recommendation
There is clearly no way to reduce the number of authors that have worked on a file - it is impossible to rewrite history. However, you should pay special attention in a code review to a file that has been worked on by a large number of authors. The file may be need to be refactored or rewritten by an individual, experienced programmer.


## References
* F. P. Brooks Jr, *The Mythical Man-Month*, Chapter 4. Addison-Wesley, 1974.
