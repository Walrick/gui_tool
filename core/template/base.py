#!/usr/bin/python3
# -*- coding: utf8 -*-

import tkinter as tk

# Instance
import core.manage_widget as manage_widget

# Heritage
from core.command_gui.mouse import Mouse
from core.command_gui.keyboard import Keyboard
from core.command_gui.command import CommandGUI
from core.tool.scroolbar import ScrollBar


class Base(Mouse, Keyboard, CommandGUI, ScrollBar):
    def __init__(self, window):

        # width screen
        self.width = window.winfo_screenwidth()
        # height screen
        self.height = window.winfo_screenheight()

        # Create the Canvas
        self.canvas = tk.Canvas(
            window,
            height=self.height,
            width=self.width,
            bg="grey",
            scrollregion=(0, 0, self.width, self.height),
        )

        # Instance
        self.window = window
        self.manage = manage_widget.ManageWidget(self.canvas)

        # Init ScrollBar Héritage
        ScrollBar.__init__(self)

        # Init Keyboard and Mouse Héritage
        Keyboard.__init__(self)
        Mouse.__init__(self)

        self.canvas.pack(fill=tk.BOTH, side=tk.LEFT, expand=tk.TRUE)

    def update(self):

        self.canvas.update_idletasks()
