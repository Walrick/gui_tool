#!/usr/bin/python3
# -*- coding: utf8 -*-

import sys

import tk_gui_tools.main as main

import tk_gui_tools.settings as settings


class App:
    """
    GUI tool project
    """
    def __init__(self):

        # get the launch options
        arg = sys.argv

        setting = settings

        self.main = main.Main(arg, settings=setting)

    def run(self):

        self.main.run()


if __name__ == "__main__":

    app = App()
    app.run()
