import sublime
import sys
import sublime_plugin
import webbrowser

PY3 = sys.version > '3'

if PY3:
    from .request import *
else:
    from request import *


class OpenGithubNotificationsCommand(sublime_plugin.WindowCommand):
    def run(self):
        webbrowser.open_new_tab("https://github.com/notifications")


class GithubNotifStatusBar(sublime_plugin.EventListener):

    _template = None
    _activated = False
    _status = None

    def on_activated_async(self, view):
        self._run(view)

    def _run(self, view):
        self._view = view

        if not self._activated:
            settings = sublime.load_settings('githubNotif.sublime-settings')
            self._updateInterval = settings.get('update_interval', 60)
            self._template = settings.get('template', None)

            self._startTimer()

            self._activated = True

        self._showStatus()

    def _startTimer(self):
        self._updateData()
        self._showStatus()

        sublime.set_timeout_async(lambda: self._startTimer(), self._updateInterval * 1e3)

    def _updateData(self):
        print("[GithubNotifStatusBar]: updateData")
        notifications = api_request('https://api.github.com/notifications')
        if notifications is not None:
            not_count = len(notifications)
            not_str = str(not_count)
            if not_count >= 50:
                not_str += "+"
            self._status = self._template.format(notif=not_str)
            return True
        else:
            return False

    def _showStatus(self):
        if self._status is not None:
            self._view.set_status('GithubNotif', self._status)
