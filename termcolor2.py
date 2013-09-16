from termcolor import colored

class _C(object):
    def __init__(self, string, color=None, on_color=None, attrs=None):
        self.string = string
        self.color = color
        self.on_color = on_color
        self.attrs = attrs

    def __getattr__(self, name):
        if name in ['red', 'green', 'yellow',
                    'blue', 'magenta', 'cyan', 'white']:
            self.color = name
        elif name in ['on_grey', 'on_red', 'on_green', 'on_yellow', 'on_blue',
                      'on_magenta', 'on_cyan', 'on_white']:
            self.on_color = name
        elif name in ['bold', 'dark', 'underline',
                      'blink', 'reverse', 'concealed']:
            if not self.attrs:
                self.attrs = []
            if name not in self.attrs:
                self.attrs.append(name)
        else:
            raise AttributeError("no such attr -> " + name)
        return self

    def __str__(self):
        return colored(self.string, color=self.color,
                       on_color=self.on_color, attrs=self.attrs)

    def __add__(self, other):
        return self.__str__() + other

    def __radd__(self, other):
        return other + self.__str__()
c = _C
