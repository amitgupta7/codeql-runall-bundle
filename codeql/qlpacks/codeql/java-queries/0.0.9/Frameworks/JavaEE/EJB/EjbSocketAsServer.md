# EJB uses server socket
The Enterprise JavaBeans 3.0 core specification, Section 21.1.2, states:

> An enterprise bean must not attempt to listen on a socket, accept connections on a socket, or use a socket for multicast.

The EJB architecture allows an enterprise bean instance to be a network socket client, but it does not allow it to be a network server. Allowing the instance to become a network server would conflict with the basic function of the enterprise bean&mdash;to serve the EJB clients.


## References
* [ JSR-220 Enterprise JavaBeans 3.0 Final Release](http://jcp.org/aboutJava/communityprocess/final/jsr220/index.html) (ejbcore), Section 21.1.2 Programming Restrictions
* Common Weakness Enumeration: [CWE-577](https://cwe.mitre.org/data/definitions/577.html).
