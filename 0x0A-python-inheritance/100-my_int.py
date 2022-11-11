#!/usr/bin/python3
"""Define rebel class MyInt"""


class MyInt(int):
    """Rebel class"""

    def __eq__(self, value):
        """Defining equality for class MyInt

        Args:
            value (int): term for comparison
        """
        return super().__ne__(value)

    def __ne__(self, value):
        """Defining inequality for class MyInt

        Args:
            value (int): term for comparison
        """
        return super().__eq__(value)
