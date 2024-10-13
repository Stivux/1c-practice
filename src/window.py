# window.py
#
# Copyright 2024 User
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from gi.repository import Adw
from gi.repository import Gtk
from .calories_item import CaloriesItem 


@Gtk.Template(resource_path='/sp/nazarov/Calories/ui/window.ui')
class CaloriesWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'CaloriesWindow'
    new_item: Gtk.Button = Gtk.Template.Child()
    list_box = Gtk.Template.Child()
    entry: Gtk.Entry = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.new_item.connect("clicked", self.new_dialog)

    def new_dialog(self, button):
        dialog = Adw.AlertDialog(
        heading="New Dish",
        close_response="cancel",
    )

        dialog.add_response("cancel", "Cancel")
        dialog.add_response("new", "New")

        dialog.set_response_appearance("new", Adw.ResponseAppearance.SUGGESTED)
        self.entry = Gtk.Entry(name="dish_title")
        dialog.set_extra_child(self.entry)
        dialog.connect("response", self.new_dish)
        dialog.choose(self)

    def new_dish(self, response, select):
        if select == "new":
            item = CaloriesItem(title=self.entry.get_text())
            item.set_expanded(True)
            self.list_box.append(item)