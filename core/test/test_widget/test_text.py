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


class TestRound:
    def test_text_init(self, param_tkinter):
        self.template_manager = template_manager.Template(param_tkinter)
        text_test = self.template_manager.active_template.manage.create_text(10, 10)
        assert text_test.x1 == 10

    def test_text_text(self, param_tkinter):
        self.template_manager = template_manager.Template(param_tkinter)
        text_test = self.template_manager.active_template.manage.create_text(
            10, 10, text="test"
        )
        assert text_test.text == "test"

    def test_text_draw(self, param_tkinter):
        self.template_manager = template_manager.Template(param_tkinter)
        text_test = self.template_manager.active_template.manage.create_text(
            10, 10, text="test", fill="red"
        )
        assert text_test.fill == "red"
        text_test.update(fill="green")
        assert text_test.fill == "green"
