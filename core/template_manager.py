#!/usr/bin/python3
# -*- coding: utf8 -*-

import core.template.dashboard as dashboard


class Template:
    def __init__(self, window):

        self.window = window

        self.active_template = dashboard.Dashboard(self.window)

    def draw_dashboard(self):

        self.active_template = dashboard.Dashboard(self.window)
