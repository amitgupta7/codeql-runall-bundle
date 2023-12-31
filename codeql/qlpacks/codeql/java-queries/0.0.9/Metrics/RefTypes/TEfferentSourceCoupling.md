# Outgoing dependencies to source types
This metric measures the number of outgoing source dependencies for each reference type, i.e. the number of other source types on which each reference type depends. Dependencies into libraries are not counted.

Types that depend on many other types are quite brittle, because if any of their dependencies change then they may have to as well. Furthermore, the reason for the high number of dependencies is often that different bits of the class depend on different sets of other types, so it is not uncommon to find that classes with high efferent coupling also lack cohesion.


## Recommendation
Efferent coupling can be reduced by splitting a class into pieces along its dependency fault lines. For example, consider the following very simple class:

```java

class X {
    public void iUseY(Y y) {
        y.doStuff();
    }

    public Y soDoY() {
        return new Y();
    }

    public Z iUseZ(Z z1, Z z2) {
        return z1.combine(z2);
    }
}

```
In this class, `X` depends on both `Y` and `Z`, but the functions that are using `Y` are not also using `Z`, and vice-versa. We could thus split the class into two, one of which depends only on `Y` and the other only on `Z`:

```java

class YX {
    public void iUseY(Y y) {
        y.doStuff();
    }

    public Y soDoY() {
        return new Y();
    }
}

class ZX {
    public Z iUseZ(Z z1, Z z2) {
        return z1.combine(z2);
    }
}

```
Whilst this is a somewhat contrived example, this sort of situation does tend to crop up even (or especially) in more complicated classes, so the general technique is quite widely applicable.


## References
* A. Glover. [Code quality for software architects](https://web.archive.org/web/20190919093358/http://7thgen.info/wiki/Code_Quality_For_Software_Architects). Published online, 2006.
* R. Martin. *Agile Software Development: Principles, Patterns and Practices*. Pearson, 2011.
