#!/usr/bin/python3
# -*- coding: utf8 -*-


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

    def motion(self, x, y):
        self.x = x
        self.y = y

        for item in self.list_item:
            pass

    def command(self, x, y, action):
        self.action = action

        for item in self.list_item:
            pass
