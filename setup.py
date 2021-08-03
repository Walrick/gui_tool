from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='gui_tool',
    version='0.1',
    packages=['core', 'core.test', 'core.test.test_widget', 'core.tool', 'core.widget', 'core.template',
              'core.command_gui'],
    url='https://github.com/Walrick/gui_tool',
    license='MIT License',
    author='Jeremy COMBES',
    author_email='jeremy.combes0902@gmail.com',
    description=' Quickly create a user interface based on tkinter\'s canvas',
    long_description=long_description,
    long_description_content_type="text/markdown",
)
