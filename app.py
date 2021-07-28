#!/usr/bin/python3
# -*- coding: utf8 -*-

import sys

import core.main as main


class App:
    """
    Alpha branch
    """
    def __init__(self):

        # get the launch options
        arg = sys.argv

        self.main = main.Main(arg)

    def run(self):

        self.main.run()


if __name__ == "__main__":

    app = App()
    app.run()
