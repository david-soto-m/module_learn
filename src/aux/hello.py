''' Documenting clases in other modules

This is as much as me finding a correct tool for
documentation as it is about me learning how modules and importing wok

'''


class Saluter:
    '''A class to say hi to your best friends'''
    name: str

    def __init__(self, name: str):
        '''Create a saluting class
        '''
        self.name = name

    def salute(self):
        '''Say hello
        '''
        print(f'Hello {self.name}')

    def __secret_salute__(self):
        ''' YOU SHOULD NEVER INVOKE THIS METHOD!!!!

        I am very angry about you reading this
        '''
        print('Hi Ami')
