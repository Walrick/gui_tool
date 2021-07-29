#!/usr/bin/python3
# -*- coding: utf8 -*-

from core.widget.rectangle import Rectangle


class ManageWidget:
    """
    ManageWidget manages widgets
    """

    def __init__(self, context):
        """
        :param context: Canvas instance
        """
        self.list_item = []
        self.context = context

        # Init attribute mouse
        self.x = 0
        self.y = 0
        self.action = None

    def create_rectangle(self, x1, y1, x2, y2, **kwargs):

        item = Rectangle(x1, y1, x2, y2, self.context, **kwargs)
        item.draw()
        self.list_item += [item]
        return item

    def motion(self, x, y):
        self.x = x
        self.y = y

        for item in self.list_item:
            item.motion(x, y)

    def command(self, x, y, action):
        self.action = action

        for item in self.list_item:
            item.commande(x, y, action)
