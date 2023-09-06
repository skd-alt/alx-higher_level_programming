#!/usr/bin/python3
"""Create a locked class."""


class LockedClass:
    """
    Prevents the user from instantiating new attributes
    only for attributes called 'first_name'.
    """
    __slots__ = ["first_name"]
