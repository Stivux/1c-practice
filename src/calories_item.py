from gi.repository import Adw
from gi.repository import Gtk
import re

@Gtk.Template(resource_path='/sp/nazarov/Calories/ui/item.ui')
class CaloriesItem(Adw.ExpanderRow):
    __gtype_name__ = 'CaloriesItem'

    calories: Adw.EntryRow = Gtk.Template.Child()
    proteins: Adw.EntryRow = Gtk.Template.Child()
    fats: Adw.EntryRow = Gtk.Template.Child()
    carbohydrates: Adw.EntryRow = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.calories.connect("apply", self.on_insert_text)
        self.proteins.connect("apply", self.on_insert_text)
        self.fats.connect("apply", self.on_insert_text)
        self.carbohydrates.connect("apply", self.on_insert_text)

    def on_insert_text(self, entry):
        text = entry.get_text()
        if not self.is_number(text):
            entry.set_text("")
        else:
            pass
        entry.set_show_apply_button(False)
        entry.set_show_apply_button(True)

    def is_number(self, text):
        return re.match(r'^-?\d+(\.\d+)?$', text) is not None

    