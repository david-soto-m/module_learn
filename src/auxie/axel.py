''' # Here be the docstrings of death and resurection


## This is a heading, self reflecting

They continue here
'''


from . import worker as w
from inspect import getmembers, isfunction


def funny():
    '''They are inside the functions

    * Of
    * All
    * **places**
    '''
    pos_checks = dict(getmembers(w, isfunction))
    eval("worrier()", {}, pos_checks)
