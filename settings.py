import sublime
import sys

PY3 = sys.version >= '3'

if PY3:
    from .request import *
else:
    from request import *


class settings(object):
    loaded_settings = sublime.load_settings('githubNotif.sublime-settings')

    get = loaded_settings.get
    set = loaded_settings.set

    def __init__(self):
        self.loaded_settings.add_on_change('reload', lambda:self.load(self))
        self.load()

    def load(self):
        pass

