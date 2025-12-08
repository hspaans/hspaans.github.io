.. post:: 2025-12-07 08:00:00
    :tags: boolean logic
    :category: Language

The NAND, NOR, and XOR operators in Python
==========================================

The NAND, NOR, and XOR operators are logical operators that are not built into Python, but can be implemented using the built-in :py:obj:`not`, :py:obj:`and`, and :py:obj:`or` operators. The NAND operator returns `True` unless both of its operands are `True` (i.e., if at least one operand is `False`), and the NOR operator returns `True` if and only if both of its operands are `False`. The XOR operator returns `True` if and only if exactly one of its operands is `True`.

The NAND logic operator
-----------------------

As can be seen in the truth table below, the NAND operator returns `True` unless both of its operands are `True` (i.e., if at least one operand is `False`). This is the opposite of the `and` operator. That is because the `not` operator is applied to the result of the `and` operator which inverts the result.

The NAND operator can be implemented in Python as follows:

.. code-block:: python
    :caption: The NAND logic in a Python function

    def nand(a, b):
        """
        Returns the NAND of two boolean values a and b.
        
        Truth table:
        ======= ======= ========
        A       B       Result
        ======= ======= ========
        True    True    False
        True    False   True
        False   True    True
        False   False   True
        ======= ======= ========
        """
        return not (a and b)

If the `nand` function is called with `True` and `False` as its arguments, it will return `True` because the `and` operator returns `False` and the `not` operator inverts the result. This can also be directly implemented in a Python program as follows:

.. code-block:: python
    :caption: Using the NAND logic in a Python program

    def main():
        a = True
        b = False
        if not (a and b):
            print("The NAND of", a, "and", b, "is True")
        else:
            print("The NAND of", a, "and", b, "is False")


    if __name__ == "__main__":
        main()

The NOR logic operator
----------------------

Like the NAND operator, the NOR operator returns `True` if and only if both of its operands are `False`. This is the opposite of the `or` operator. That is because the `not` operator is applied to the result of the `or` operator which inverts the result.

The NOR operator can be implemented in Python as follows:

.. code-block:: python
    :caption: The NOR logic in a Python function

    def nor(a, b):
        """
        Returns the NOR of two boolean values a and b.
        
        Truth table:
        ======= ======= ========
        A       B       Result
        ======= ======= ========
        True    True    False
        True    False   False
        False   True    False
        False   False   True
        ======= ======= ========
        """
        return not (a or b)

If the `nor` function is called with `True` and `False` as its arguments, it will return `False` because the `or` operator returns `True` and the `not` operator inverts the result. This can also be directly implemented in a Python program as follows:

.. code-block:: python
    :caption: Using the NOR logic in a Python program

    def main():
        a = True
        b = False
        if not (a or b):
            print("The NOR of", a, "and", b, "is True")
        else:
            print("The NOR of", a, "and", b, "is False")


    if __name__ == "__main__":
        main()

The XOR logic operator
----------------------

Unlike the `and` and `or` operators, the XOR operator returns `True` if and only if exactly one of its operands is `True`. The truth table for the XOR operator is as follows and it can be implemented using the `and`, `or`, and `not` operators.

The XOR operator can be implemented in Python as follows:

.. code-block:: python
    :caption: The XOR logic in a Python function

    def xor(a, b):
        """
        Returns the XOR of two boolean values a and b.
        
        Truth table:
        ======= ======= ========
        A       B       Result
        ======= ======= ========
        True    True    False
        True    False   True
        False   True    True
        False   False   False
        ======= ======= ========
        """
        return (a and not b) or (not a and b)

.. note::

    The ``xor`` function can also be implemented using the ``^`` operator as follows:

    .. code-block:: python
        :caption: The XOR logic in a Python function using the ``^`` operator

        def xor(a, b):
            """
            Returns the XOR of two boolean values a and b.

            Truth table:
            ======= ======= ========
            A       B       Result
            ======= ======= ========
            True    True    False
            True    False   True
            False   True    True
            False   False   False
            ======= ======= ========
            """
            return a ^ b

    The ``^`` operator returns `True` if and only if exactly one of its operands is `True`.

If the `xor` function is called with `True` and `False` as its arguments, it will return `True` because the first part of the expression `(a and not b)` returns `True` and the second part of the expression `(not a and b)` returns `False`. The overall result is `True` due to the `or` operation. This can also be directly implemented in a Python program as follows:

.. code-block:: python
    :caption: Using the XOR logic in a Python program

    def main():
        a = True
        b = False
        if (a and not b) or (not a and b):
            print("The XOR of", a, "and", b, "is True")
        else:
            print("The XOR of", a, "and", b, "is False")
    

    if __name__ == "__main__":
        main()

.. note::

    The ``operator`` module in Python provides a function called `xor` that can be used to implement the XOR logic as follows:

    .. code-block:: python
        :caption: The XOR logic in a Python function using the `operator` module

        import operator

        def xor(a, b):
            return operator.xor(a, b)

The XNOR logic operator
-----------------------

The XNOR operator returns `True` if and only if both of its operands are `True` or both of its operands are `False`. This is the opposite of the XOR operator. The truth table for the XNOR operator is as follows and it can be implemented using the `and`, `or`, and `not` operators.

The XNOR operator can be implemented in Python as follows:

.. code-block:: python
    :caption: The XNOR logic in a Python function

    def xnor(a, b):
        """
        Returns the XNOR of two boolean values a and b.
        
        Truth table:
        ======= ======= ========
        A       B       Result
        ======= ======= ========
        True    True    True
        True    False   False
        False   True    False
        False   False   True
        ======= ======= ========
        """
        return (a and b) or (not a and not b)

If the `xnor` function is called with `True` and `False` as its arguments, it will return `False` because both parts of the expression—`(a and b)` and `(not a and not b)`—return `False`. The overall result is `False` because both parts of the `or` expression are `False`. This can also be directly implemented in a Python program as follows:

.. code-block:: python
    :caption: Using the XNOR logic in a Python program

    def main():
        a = True
        b = False
        if (a and b) or (not a and not b):
            print("The XNOR of", a, "and", b, "is True")
        else:
            print("The XNOR of", a, "and", b, "is False")
    

    if __name__ == "__main__":
        main()

.. note::
    
        The ``xnor`` function can also be implemented using the `==` operator as follows:
    
        .. code-block:: python
            :caption: The XNOR logic in a Python function using the `==` operator
    
            def xnor(a, b):
                return a == b
    
        The `==` operator returns `True` if and only if both of its operands are equal.

Considerations about logical operators
--------------------------------------

The logical operators in Python are used to perform logical operations on boolean values. The `and` operator returns `True` if and only if both of its operands are `True`, the `or` operator returns `True` if and only if at least one of its operands is `True`, and the `not` operator returns `True` if and only if its operand is `False`. The `and`, `or`, and `not` operators can be combined to implement the NAND, NOR, XOR, and XNOR operators.

Other built-in operators like the ``^`` operator can also be used to implement the XOR operator, and the ``==`` operator can be used to implement the XNOR operator. The :py:mod:`operator` module in Python provides a function called :py:func:`operator.xor` that can be used to implement the XOR operator. The logical operators in Python are used to perform logical operations on boolean values, and can be combined to implement the NAND, NOR, XOR, and XNOR operators.