#!/usr/bin/python3
# -*- coding: utf8 -*-

import tkinter as tk

import core.manage_widget as manage_widget


class Base:
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

        self.canvas.pack(fill=tk.BOTH, side=tk.LEFT, expand=tk.TRUE)

    def update(self):

        self.canvas.update_idletasks()
