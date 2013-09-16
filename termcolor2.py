from termcolor import colored

class C(object):
    def __init__(self, string, color=None, on_color=None, attrs=[]):
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
            self.attrs.append(name)
        else:
            raise AttributeError("no such attr -> " + name)
        return self

    def __str__(self):
        return colored(self.string, color=self.color,
                       on_color=self.on_color, attrs=self.attrs)
c = C
