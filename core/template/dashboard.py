#!/usr/bin/python3
# -*- coding: utf8 -*-


# Héritage
from core.template.base import Base


class Dashboard(Base):
    """
    Test template and example
    """

    def __init__(self, window):

        # Init Base Template Héritage
        Base.__init__(self, window)
        self.template_name = "Dashboard"

        # Create Canvas title
        self.title = self.canvas.create_text(50, 50, text="Dashboard", anchor="w")
