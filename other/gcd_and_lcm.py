def get_gcd(a, b):
    """
    :type a: int
    :type b: int
    :rtype: int

    >>> get_gcd(10, 2)
    2
    >>> get_gcd(500, 375)
    125
    """
    while b:
        a, b = b, a % b
    return a


def get_lcm(a, b):
    """
    :type a: int
    :type b: int
    :rtype: int

    >>> get_lcm(10, 2)
    10
    >>> get_lcm(500, 375)
    1500
    """
    return (a * b) // get_gcd(a, b)
