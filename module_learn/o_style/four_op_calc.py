class FourOpCalc():
    ''' A four op calculator class
    This class emulates a four op calculator that accumulates the answers in
    the left hand side
    '''

    def __init__(self, lhs: float = 0) -> None:
        ''' An constructor
        that sets the accumulated value for the first time

        # Defaults

        : self.lhs = 0

        # Parameters

        : lhs = Option(float)
        '''
        self.lhs = lhs
        '''The accumulated value up to the moment'''

    def add(self, rhs: float = 0) -> float:
        '''(the accumulated value) + rhs
        # Defaults
        : rhs = 0
        '''
        self.lhs += rhs
        return self.lhs

    def sub(self, rhs: float = 0) -> float:
        '''(the accumulated value) - rhs
        # Defaults
        : rhs = 0
        '''
        self.lhs -= rhs
        return self.lhs

    def mul(self, rhs: float = 1) -> float:
        '''(the accumulated value) * rhs
        # Defaults
        : rhs = 1
        '''
        self.lhs *= rhs
        return self.lhs

    def div(self, rhs: float = 1) -> float:
        '''(the accumulated value) / rhs
        # Defaults
        : rhs = 1
        '''
        self.lhs /= rhs
        return self.lhs

    def ans(self) -> float:
        '''return the accumulated value'''
        return self.lhs

    def clear(self, lhs: float = 0):
        '''Set the accumulated value, by default 0, else rhs
        # Defaults
        : lhs = 0
        '''
        self.lhs = lhs
