from gi.repository import Gtk, Adw

@Gtk.Template(resource_path='/github/io/habiter/window.ui')
class HabiterWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'HabiterWindow'

    leaflet = Gtk.Template.Child()
    start_button = Gtk.Template.Child()
    home_page = Gtk.Template.Child()
    dashboard_page = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Verify widgets were properly initialized
        if not self.start_button:
            print("Error: start_button not found in template!")
            return

        self.start_button.connect("clicked", self.on_start_button_clicked)

        # Make sure the leaflet can access its children by name
        if self.home_page:
            self.home_page.set_name("home_page")
        if self.dashboard_page:
            self.dashboard_page.set_name("dashboard_page")

    def on_start_button_clicked(self, button):
        if self.dashboard_page:
            # Alternative way to navigate - use object reference instead of name
            self.leaflet.set_visible_child(self.dashboard_page)
        else:
            print("Error: dashboard_page not found!")

