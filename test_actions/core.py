"""
Non-empty
"""


class Klass:
    def __init__(self, x):
        self.x = x


    def method(self):
        """non-empty"""
        return 42 + self.x

    def method0(self):
        """non-empty"""
        return 32 + self.x
