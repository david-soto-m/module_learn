'''All must be documented,
for only that which is documented is known
'''


def op(lhs: float, rhs: float, oper) -> float:
    '''An abstract operation over lhs, and rhs

    # Example

    ~~~python
    a = add(1, 2)
    op(4, 5, add if a > 2 else sub)

    ~~~

    '''
    return oper(lhs, rhs)
