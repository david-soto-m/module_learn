''' An object oriented approach to a four function calculator

It can perform:
- addition
- subtraction
- multiplication
- division

# Examples:

Create, and add:

```python
a = FourOpCalc(5)
a.add(5)
a.add(4)
assert(a == 14)
```

'''

from .four_op_calc import FourOpCalc

__all__ = [
    'FourOpCalc'
]
