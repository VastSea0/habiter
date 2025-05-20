#window.py
from gi.repository import Gtk, Adw, GLib

@Gtk.Template(resource_path='/github/io/habiter/window.ui')
class HabiterWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'HabiterWindow'

    leaflet = Gtk.Template.Child()
    start_button = Gtk.Template.Child()
    back_button = Gtk.Template.Child()
    home_page = Gtk.Template.Child()
    dashboard_page = Gtk.Template.Child()
    habit_list = Gtk.Template.Child()
    add_button = Gtk.Template.Child()
    task_entry = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        if not self.start_button:
            print("Error: start_button not found in template!")
            return

        self.start_button.connect("clicked", self.on_start_button_clicked)
        self.back_button.connect("clicked", self.on_back_button_clicked)
        self.add_button.connect("clicked", self.on_add_button_clicked)
        text = self.task_entry.get_text()
        self.task_entry.set_text("Yeni görev")

        if self.home_page:
            self.home_page.set_name("home_page")
        if self.dashboard_page:
            self.dashboard_page.set_name("dashboard_page")

    def on_add_button_clicked(self, button):
        text = self.task_entry.get_text()
        if text.strip():
            new_check = Gtk.CheckButton(label=text)
            new_check.get_style_context().add_class("check-button-animated")
            self.habit_list.append(new_check)
            new_check.show()

            GLib.timeout_add(50, lambda: (new_check.get_style_context().add_class("appear"), False)[1])
            self.task_entry.set_text("")


    def on_start_button_clicked(self, button):
        if self.dashboard_page:
            self.leaflet.set_visible_child(self.dashboard_page)
        else:
            print("Error: dashboard_page not found!")

    def on_back_button_clicked(self, button):
        if self.home_page:
            self.leaflet.set_visible_child(self.home_page)
        else:
            print("Error: dashboard_page not found!")



