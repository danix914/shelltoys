import unittest


class IWasTheOne:
    def __init__(self):
        pass


class Foo:
    def __init__(self):
        self.one = IWasTheOne()


class Bar:
    def __init__(self):
        self.one = IWasTheOne()


class TestSingletonPattern(unittest.TestCase):
    def test_ids_are_different(self):
        foo = Foo()
        bar = Bar()
        self.assertIsNot(foo, bar)
        self.assertIs(foo.one, bar.one)


if __name__ == '__main__':
    unittest.main()
