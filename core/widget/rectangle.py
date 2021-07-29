#!/usr/bin/python3
# -*- coding: utf8 -*-


class Rectangle:
    def __init__(self, x1: int, y1: int, x2: int, y2: int, context, **kwargs):

        self.context = context
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        self.fill = kwargs.get("fill", "grey")
        self.fill_mouse = kwargs.get("fill_mouse", self.fill)
        self.text = kwargs.get("text", None)
        self.width = kwargs.get("width", None)

        if self.text is not None:
            self.text_fill = kwargs.get("text_fill", "black")
            self.text_fill_mouse = kwargs.get("text_fill_mouse", "black")
            self.anchor = kwargs.get("anchor", "center")
            if self.anchor == "center":
                self.text_x = (self.x2 - self.x1) / 2 + self.x1
                self.text_y = (self.y2 - self.y1) / 2 + self.y1

        command = kwargs.get("command", None)
        self.command = {}
        if command is not None:
            index = 0
            count = int(len(command) / 2)
            if count == 1:
                c = command[index + 1]
                self.command[command[index]] = c
            else:
                for i in range(count):
                    a = command[index + 1]
                    self.command[command[index]] = a
                    index += 2

        self.relief = kwargs.get("relief", False)
        if self.relief:
            self.ligne_1 = [self.x1, self.y2, self.x2, self.y2]
            self.ligne_2 = [self.x2, self.y1, self.x2, self.y2]

        self.active_focus = False
        self.item_tk = []

    def draw(self):
        if len(self.item_tk) > 0:
            for item in self.item_tk:
                self.context.delete(item)
            self.item_tk = []

        item = self.context.create_rectangle(
            self.x1, self.y1, self.x2, self.y2, fill=self.fill, width=self.width
        )
        self.item_tk.append(item)
        if self.text is not None:
            item = self.context.create_text(
                self.text_x,
                self.text_y,
                text=self.text,
                fill=self.text_fill,
                anchor=self.anchor,
            )
            self.item_tk.append(item)
        if self.relief:
            item = self.context.create_line(
                self.ligne_1[0],
                self.ligne_1[1],
                self.ligne_1[2],
                self.ligne_1[3],
                width=1,
            )
            self.item_tk.append(item)
            item = self.context.create_line(
                self.ligne_2[0],
                self.ligne_2[1],
                self.ligne_2[2],
                self.ligne_2[3],
                width=1,
            )
            self.item_tk.append(item)

    def draw_focus(self):
        if len(self.item_tk) > 0:
            for item in self.item_tk:
                self.context.delete(item)
            self.item_tk = []

        item = self.context.create_rectangle(
            self.x1, self.y1, self.x2, self.y2, fill=self.fill_mouse, width=self.width
        )
        self.item_tk.append(item)
        if self.text is not None:
            item = self.context.create_text(
                self.text_x,
                self.text_y,
                text=self.text,
                fill=self.text_fill_mouse,
                anchor=self.anchor,
            )
            self.item_tk.append(item)
        if self.relief:
            item = self.context.create_line(
                self.ligne_1[0],
                self.ligne_1[1],
                self.ligne_1[2],
                self.ligne_1[3],
                width=2,
            )
            self.item_tk.append(item)
            item = self.context.create_line(
                self.ligne_2[0],
                self.ligne_2[1],
                self.ligne_2[2],
                self.ligne_2[3],
                width=2,
            )
            self.item_tk.append(item)

    def motion(self, x, y):

        if self.x1 < x < self.x2 and self.y1 < y < self.y2:
            if not self.active_focus:
                self.draw_focus()
                self.active_focus = True

        else:
            if self.active_focus:
                self.draw()
                self.active_focus = False

    def commande(self, x, y, action):

        if action in self.command:
            if self.x1 < x < self.x2 and self.y1 < y < self.y2:
                self.command[action]()
