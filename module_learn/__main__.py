from o_style import FourOpCalc
from func_style import (op,
                        add,
                        sub,
                        div,
                        mul)

if __name__ == '__main__':
    four = FourOpCalc()
    four.add(5)
    four.mul(5)
    four.add(1)
    four.div(2)
    four.sub(1)
    print(four.add(-5.5))
    assert(four.ans() == 6.5)
    four.clear()
    assert(four.ans() == 0)
    assert(op(4, 5, add if mul(4, add(div(36, 6), 5)) > 40 else sub) == 9)
