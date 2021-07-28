#!/usr/bin/python3
# -*- coding: utf8 -*-

import tkinter as tk

import core.setting as setting
import core.template_manager as template_manager


class Main(tk.Tk):

    REFRESH = 200

    def __init__(self, *args):

        # launch command
        self.command(*args)

        # Init Tkinter
        tk.Tk.__init__(self)
        self.title(setting.screen["title"])
        self.geometry(setting.screen["screensize"])
        self.attributes("-fullscreen", setting.screen["fullscreen"])
        self.resizable(
            height=setting.screen["resizable"]["height"],
            width=setting.screen["resizable"]["width"],
        )

        # Init template manager
        self.template = template_manager.Template(self)

    def run(self):
        self.after(self.REFRESH, self.update_gui)
        self.mainloop()

    def update_gui(self):
        self.template.active_template.update()
        self.after(self.REFRESH, self.update_gui)

    def command(self, *args):
        """
        Manage command
        :param args:
        :return:
        """

        pass
