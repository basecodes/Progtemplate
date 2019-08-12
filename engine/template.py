import re

from engine.label import scopeLabel, getterLabel, setterLabel


def align(code):
    space = re.match(r"\n(\s+)", code)
    if space is None:
        return "", code
    splitlines = code.splitlines(True)
    spaces = str(space.groups()[0])
    for i in range(len(splitlines)):
        new_value = splitlines[i].replace(spaces, "", 1)
        splitlines[i] = new_value
    lines = "".join(splitlines)
    return spaces, lines


class Template:
    def __init__(self):
        self.obj = None

        self.getter = re.compile(getterLabel)
        self.setter = re.compile(setterLabel, re.DOTALL)
        self.scope = re.compile(scopeLabel, re.DOTALL)
        self.body = ""
        self.suffix = ""

    def parse_objects(self, obj):
        self.obj = obj

    def handle_body(self, objs):
        def repl(obj):
            code = obj.groups()[0]
            try:
                v = eval(code, {}, {self.obj: objs})
            except AttributeError:
                print("Error: 没有字段(%s)!" % code)
                exit()
            return v

        getter = self.getter.sub(repl, self.body)

        def exerepl(obj):
            code = obj.groups()[0]
            txt = ""

            spaces, fmt_code = align(code)

            def showln(msg):
                nonlocal txt
                txt += "\n" + spaces + msg

            def show(msg):
                nonlocal txt
                txt += msg

            try:
                exec(fmt_code, {}, {"write": show, "writeln": showln, self.obj: objs})
            except BaseException as ex:
                print(str(ex) + "\n" + str(code))
                exit()
            return txt

        spaces, fmt_code = align(getter)
        setter = self.setter.sub(exerepl, fmt_code)
        return setter

    def parse_body(self, txt):
        m = self.scope.findall(txt)
        for item in m:
            self.parse_objects(item[0])
            self.body = item[1]
            self.suffix = item[2]
