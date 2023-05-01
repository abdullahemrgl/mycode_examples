import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

class ComboWithEntry():
    def __init__(self):
        self.b = Gtk.Builder()
        self.b.add_from_file("app.ui")
        self.b.connect_signals(self)

        self.win = self.g_o("win")
        self.cmb = self.g_o("cmb")
        self.lbl = self.g_o("lbl")

    
    def g_o(self, id):
        return self.b.get_object(id)
    

    def on_win_destroy(self, widget):
        Gtk.main_quit()

    
    def on_txt_changed(self, widget):
        
        self.cmb.set_active_id(widget.get_text())

        msg = ""
        
        if self.cmb.get_active() == -1:
            widget.set_icon_from_icon_name(Gtk.EntryIconPosition.SECONDARY, "gtk-cancel")
            msg = ""
        else:
            widget.set_icon_from_icon_name(Gtk.EntryIconPosition.SECONDARY, "gtk-apply")
            msg = self.cmb.get_active_id()
        
        self.lbl.set_markup(f"Selected in ComboBox: <b>{msg}</b>")
    

if __name__ == "__main__":
    ComboWithEntry().win.show_all()
    Gtk.main()