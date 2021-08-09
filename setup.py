from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="guitool",
    version="0.1.2",
    packages=[
        "tk_gui_tools",
        "tk_gui_tools.test",
        "tk_gui_tools.test.test_widget",
        "tk_gui_tools.tool",
        "tk_gui_tools.widget",
        "tk_gui_tools.template",
        "tk_gui_tools.command_gui",
    ],
    url="https://github.com/Walrick/gui_tool",
    license="MIT License",
    author="Jeremy COMBES",
    author_email="jeremy.combes0902@gmail.com",
    description=" Quickly create a user interface based on tkinter's canvas",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
