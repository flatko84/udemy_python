import random

class Password:

    input_universe = {
        'letters': list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'),
        'numbers': list('0123456789'),
        'punctuation': list('?!.:;,')
    }
    default_lengths = {
            'low': 8,
            'mid': 12,
            'high': 16
        }

    def __init__(self, strength = 'mid', length = None):
        if strength not in self.default_lengths.keys():
            strength = 'mid'
        self.strength = strength
        self.length = length or self.default_lengths[strength]
        self.password = self._generate()


    def _generate(self):
        pool = self.input_universe['letters'].copy()
        if self.strength == 'mid' or self.strength == 'high':
            pool += self.input_universe['numbers']
        if self.strength == 'high':
            pool += self.input_universe['punctuation']
        password = [random.choice(pool) for char in range(self.length)]
        return ''.join(password)


    @classmethod
    def show_input_universe(cls):
        return cls.input_universe