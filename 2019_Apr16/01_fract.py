"""
Implement a custom numeric Fraction class
that supports the features such that the
doctests listed below pass successfully.

    >>> from fract import Fraction

    >>> a = Fraction("1/2") # represents 1/2

    >>> b = Fraction(1, 4)  # represents 1/4

    >>> print(a + b)       # adds two fractions and returns a new fraction
    3/4

    >>> print(a - b)       # subtracts and returns a new fraction
    1/4

    >>> float(a)    # allow conversion to float
    0.5

    >>> repr(a)     # Official string representation
    'Fraction(1, 2)'

"""

if __name__ == '__main__':
    import doctest
    doctest.testmod()


