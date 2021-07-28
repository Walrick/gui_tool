#!/usr/bin/python3
# -*- coding: utf8 -*-


class CommandGUI:
    """
    Manage command events
    """
    def quit_gui(self):

        self.window.destroy()

    def fullscreen(self, event=None):

        fullscreen_var = self.window.wm_attributes("-fullscreen")
        if fullscreen_var == 1:
            self.window.attributes("-fullscreen", False)
        else:
            self.window.attributes("-fullscreen", True)

    def draw_dashboard(self):

        self.window.template.active_template.canvas.destroy()
        self.window.template.draw_dashboard()
