# main.py

import sys
import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Gio, Adw
from .window import HabiterWindow


class HabiterApplication(Adw.Application):
    """The main application singleton class."""

    def __init__(self):
        super().__init__(application_id='github.io.habiter',
                         flags=Gio.ApplicationFlags.DEFAULT_FLAGS,
                         resource_base_path='/github/io/habiter')
        self.create_action('quit', lambda *_: self.quit(), ['<primary>q'])
        self.create_action('about', self.on_about_action)
        self.create_action('preferences', self.on_preferences_action)

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = HabiterWindow(application=self)
        win.present()

    def on_about_action(self, *args):
        about = Adw.AboutDialog(application_name='Habiter',
                                application_icon='github.io.habiter',
                                developer_name='Egehan KAHRAMAN',
                                version='0.1.0',
                                developers=['Egehan'],
                                copyright='© 2025 Egehan')
        about.set_translator_credits(_('translator-credits'))
        about.present(self.props.active_window)

    def on_preferences_action(self, widget, _):
        print('app.preferences action activated')

    def create_action(self, name, callback, shortcuts=None):
        action = Gio.SimpleAction.new(name, None)
        action.connect("activate", callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f"app.{name}", shortcuts)

def main(version):
    app = HabiterApplication()
    return app.run(sys.argv)
