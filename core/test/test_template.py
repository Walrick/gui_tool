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


class TestTemplate:

    def test_template_title(self, param_tkinter):
        self.template_manager = template_manager.Template(param_tkinter)
        assert self.template_manager.active_template.template_name is "Dashboard"

