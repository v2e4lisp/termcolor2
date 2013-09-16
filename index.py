from termcolor2 import *

# termcolor
print colored("hello", "red", "on_white", ["blink", "underline", "dark"])

# termcolor2
print c("hello").red.on_white.blink.underline.dark
