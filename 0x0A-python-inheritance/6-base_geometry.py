#!/usr/bin/python3
"""Defines an empty BaseGeometry class"""


class BaseGeometry:
    """Represent base geometry."""
    
    def area(self):
        """when not implemented"""
        raise Exception("area() is not implemented")
