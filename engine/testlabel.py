import re
import unittest

from engine.label import startLabel, scopeLabel, getterLabel, setterLabel


class MyTestCase(unittest.TestCase):
    def test_startLabel(self):
        p = re.compile(startLabel)
        m = p.match("{{start aa,bb,cc }}")
        vs = m.groups()
        print(vs)

    def test_scopeLabel(self):
        p = re.compile(scopeLabel)
        m = p.match("{{start aa,bb,cc }} class name {{end}}")
        vs = m.groups()
        print(vs)

    def test_getterLabel(self):
        p = re.compile(getterLabel)
        m = p.match("{{ obj.name }}")
        vs = m.groups()
        print(vs)

    def test_setterLabel(self):
        class Test:
            def __init__(self):
                self.Name = "Test"

        obj = Test()
        p = re.compile(setterLabel)
        m = p.match("{{ obj.Name = 5 }}")
        vs = m.groups()
        code = str(vs[0])
        exec(code)
        print(obj.Name)


if __name__ == '__main__':
    unittest.main()
