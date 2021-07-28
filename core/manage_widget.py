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
        self.list_item = {}
        self.context = context

        # Init attribute mouse
        self.x = 0
        self.y = 0
