#!/usr/bin/python3
# -*- coding: utf8 -*-

import pytest
import tkinter as tk

import core.template_manager as template_manager


@pytest.fixture
def param_tkinter():
    # Init Tkinter
    root = tk.Tk()
    root.title("Python Project")
    root.geometry("1920x1080")
    root.attributes("-fullscreen", False)
    root.resizable(height=False, width=False)
    return root


class TestCommand:
    def test_command_mouse(self, param_tkinter):
        self.template_manager = template_manager.Template(param_tkinter)
        self.template_manager.active_template.adjust_mousse(10, 15)
        assert self.template_manager.active_template.x == 10
        assert self.template_manager.active_template.y == 15
