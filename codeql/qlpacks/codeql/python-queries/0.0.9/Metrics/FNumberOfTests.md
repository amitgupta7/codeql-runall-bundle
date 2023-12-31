# Number of tests
This metric measures the number of tests below this location in the tree. At a file level, this would just be the number of tests in the file.

A function or method is considered to be a "test" if one of the major testing frameworks would invoke it as part of a test run. Recognized frameworks include unittest, pytest, doctest and nose.

In general, having many test cases is a good thing rather than a bad thing. However, at the file level, tests should typically be grouped by the functionality they relate to, which makes a file with an exceptionally high number of tests a strong candidate for splitting up. At a higher level, this metric makes it possible to compare the number of tests in different components, potentially flagging functionality that is comparatively under-tested.


## Recommendation
Since it is typically not a problem to have too many tests, this metric is usually included for the purposes of collecting information, rather than finding problematic areas in the code. With that in mind, it is usually a good idea to avoid an excessive number of tests in a single file, and to maintain a broadly comparable level of testing across components.

When assessing the thoroughness of a code base's test suite, the number of tests provides only part of the story. Test coverage statistics allow a more detailed examination of which parts of the code deserve improvements in this area.


## References
* Python Standard Library: [unitest](https://docs.python.org/library/unittest.html).
* Python Standard Library: [doctest](https://docs.python.org/2/library/doctest.html).
* [http://pytest.org](http://pytest.org/latest/).
* Read the docs: [http://nose.readthedocs.org/en/latest](http://nose.readthedocs.org/en/latest/).
