# Guitool

![](https://img.shields.io/badge/Coverage-97%25-green)
![](https://img.shields.io/badge/Version-v0.1.3-blue)
![](https://img.shields.io/badge/Licence-MIT-red)

--------------------------------------------------
-------------------------------------------------

## Installation
To install it, just use pip :
````
pip install guitool
````

----------------------------------------------------

## Description
Guitool is an open source package based on the Tkinter canvas. It offers tools and widgets already formed and linked to allow to quickly create interfaces.

-----------------------------------------------------

## Link
GitHub : https://github.com/Walrick/gui_tool

-----------------------------------------------------

## Use - Tutorial
The package was developed with the idea that a graphical object can be written simply in a template and can be updated with a single method.
The package is based on the use of Tkinter's canvas.
The graphic objects called here widgets are basically modeled on the widgets of the tkinter canvas.
But they were linked from the base to the action of the user, for example: when creating a rectangle, we can define a different color for it if the cursor passes over it or / and link an action to it if we have it click on it.
The tk_gui_tools package handles the creation of the tkinter environment and the mainloop () but it is necessary to prepare some files.

Start by creating a settings.py file and pasting the following variables into it:
The screen dictionary is used to configure the desired window.

````
# Default settings screen
screen = {
    "screensize": "1920x1080",
    "fullscreen": False,
    "title": "Python Project",
    "resizable": {"height": True, "width": True},
}
````

The Boolean variable default_template is used to configure the first template to display.
If you wanted to use the default template which is called dashboard and which serves as a small example, put True instead of False.

````
# True is use default template in first
default_template = True
````

A variable refresh allows you to set the after () method of tkinter, its value is expressed in ms

````
# set time refresh in ms
refresh = 200
````

To be able to integrate the logic of your application, we propose this way of doing things:

````
racine
|-app.py
|-README.md
|-.env
|-requirements.txt
|- core
    |- __init__.py
    |- master.py
    |- settings.py
    |- gui
    |    |- __init__.py
    |    |- template_manager.py
    |    |- template
    |          |- __init__.py
    |          |- first_template.py	
    |    
    |- logic_app
	    |- __init__.py
		|- master_logic.py	
		etc...
````

The settings.py file was described above, we will see master.py

master.py
````
from tk_gui_tools.main import Main

import core.gui.template_manager as template_manager
import core.settings as settings
import core.logic_app.master_logic as master_logic

class Master(Main):

    def __init__(self, *args):

        Main.__init__(self, args, settings=settings)

        self.master_app = master_logic.MasterLogic()
		
        self.template = template_manager.TemplateGUI(self.window, self.default_template, self.master_app)

````
The Master class inherits from the Main class of tk_gui_tools which allows Tkinter to be initialized.
The argument args passed to the init of Main are any commands received at launch by app.py and settings is the configuration file established above.
Self.master_app allows you to launch the logic of your application, here we take the example of Master_logic is a class.
A thread can be used to launch your application, if so, Tkinter's thread must be the first, otherwise your application will crash.
Self.template allows you to initiate the gui of your program, it is necessary to give it as arguments "self.window" and self.default_template, the latter will depend on your application logic.

The next file is ultimately optional if you are only using a single template and want to use the default template. Otherwise, it will be necessary to add a few lines:

template_manager.py
````
from tk_gui_tools.template_manager import Template

import core.gui.template.first_template as first_template


class TemplateGUI(Template):

    def __init__(self, window, default_template, master_app):
        Template.__init__(self, window, default_template)
        self.master_app = master_app
        self.active_template = first_template.FirstTemplate(self.window, self.master_app)

    def draw_first_template(self):
        self.active_template = first_template.FirstTemplate(self.window, self.master_app)

````

This class is used to manage templates.
Self.active_template allows you to display the current template.
We can add new template by adding methods and in the method by specifying the new active template with self.active_template

The last file to add is the template itself.
In our example, first_template.py	
````
# Héritage
from tk_gui_tools.template.base import Base


class FirstTemplate(Base):

    def __init__(self, window, master_app):
        # Init Base Template Héritage
        Base.__init__(self, window)
		
        self.template_name = "First Template"
        self.master_app = master_app

        # Create Canvas title
        self.title = self.canvas.create_text(50, 50, text="First Template", anchor="w")

        # Create button quit
        self.button_quit = self.manage.create_rectangle(
            50,
            100,
            100,
            150,
            text="quit",
            fill="white",
            fill_mouse="red",
            command=("<Button-1>", self.quit_gui),
        )

        # Create round
        self.round_test = self.manage.create_round(
            200, 200, 250, 250, fill="red", fill_mouse="green"
        )

        # Create text
        self.text_test = self.manage.create_text(500, 500, text="test", fill="black")
	
    def update(self):
        """
        Update the template
        """

        self.canvas.update_idletasks()
		
        if self.round_test.active_focus:
            self.text_test.update(text="test ok", fill="red")
        else:
            self.text_test.update(text="test", fill="black")
		
````

Our template needs to inherit from Base and to initialize by giving it the window argument, then we don't have to use widgets to display what we want.
The guitool widgets are accessible through the manage class which is initialized by inheriting from Base.
Note also that it is possible to use Tkinter widgets as in the example of self.title using self.canvas.create_text (... etc).
The widgets of tk_gui_tools called with self.manage.create_rectangle, for example, are described in the Widget section.
It is possible to update the template thanks to the update () method, the time defined in refresh will be used to call update (), if refresh is set to 200 ms, update () will be called every 200 ms.

---------------------------------
## Widget
The widgets of tk_gui_tools are widgets which are based on those of tkinter.
Currently, rectangle, oval, and text are implemented. Button and Menu are graphic assemblies of the first three widgets.

### Rectangle
The rectangles are created from the template. You have to instantiate the class from the template by giving it several parameters to have the desired effect.
The class returns an object.

````
self.rectange = self.manage.create_rectangle(x1, y1, x2, y2)
```` 

We can then have access to its attribute self.rectange.active_focus if the mouse passes over it.
You can also call the update method described below.
		
#### Mandatory arguments

The method to call the rectangle is as follows: self.manage.create_rectangle (x1, y1, x2, y2). This is the minimum code to create a rectangle.

The points x1 and y1 correspond to the beginning of the rectangle at the top left and x2 and y2 correspond to the point at the bottom left
````
:param x1: int 
:param y1: int
:param x2: int
:param y2: int
````

#### Optional arguments

Create_rectangle can take other arguments with kwargs, and they are all optional.

##### fill

Fill allows you to fill the rectangle with a color, the color supported is the same as tkinter, you can write "red" or its hex format "# FF0000".
The default color is "gray" if not specified.
````
self.manage.create_rectangle(x1, y1, x2, y2, fill="red")

or

self.manage.create_rectangle(x1, y1, x2, y2, fill="#FF0000")
````

##### fill_mouse

Fill_mouse allows to change the color when the mouse passes over it, its operation is the same as fill.
The default color is the fill color.

````
self.manage.create_rectangle(x1, y1, x2, y2, fill_mouse="red")

or

self.manage.create_rectangle(x1, y1, x2, y2, fill_mouse="#FF0000")
````

##### width

Width allows you to choose the thickness of the border. Set to 0 to deactivate
By default, the value is 1.

````
self.manage.create_rectangle(x1, y1, x2, y2, width=0)

````

##### text

Text displays text in the rectangle.

````
self.manage.create_rectangle(x1, y1, x2, y2, text="test text")

````

##### anchor

Anchor allows you to position the text in the rectangle.
Currently, the only position is the default position, the center.
````
self.manage.create_rectangle(x1, y1, x2, y2, text="test text", anchor="center")

````

##### text_fill

Text_fill allows you to give a color to the text, the default color is black.
Color works the same as fill.

````
self.manage.create_rectangle(x1, y1, x2, y2, text="test text", fill_text="red")

or

self.manage.create_rectangle(x1, y1, x2, y2, text="test text", fill_text="#FF0000")
````

##### text_fill_mouse

Text_fill_mouse allows to change the color of the text when the mouse passes over the rectangle.
The default color is text_fill.

````
self.manage.create_rectangle(x1, y1, x2, y2, text="test text", text_fill_mouse="red")

or

self.manage.create_rectangle(x1, y1, x2, y2, text="test text", text_fill_mouse="#FF0000")
````

##### command

Command allows you to give an action when you click on the rectangle.
````
self.manage.create_rectangle(x1, y1, x2, y2, command=("<Button-1>", self.quit_gui))

````
In the example above, the first argument of the tuple is the action to be done on the rectangle, here a left mouse click will activate self.quit_gui.
The syntax is the same as tkinter and for more information refer to the commands chapter.
Command can take several actions, to do so, add the other two arguments to the tuple, action - command following. 
Example :

````
self.manage.create_rectangle(x1, y1, x2, y2, command=("<Button-1>", self.quit_gui, "<Double-Button-1>", self.quit_gui))

````
Here as in the first example, the left click will activate the self.quit_gui command but also, the double left click.

##### relief

Relief is used to display a relief. It makes a black line appear under the rectangle and to the right of the rectangle.
````
self.manage.create_rectangle(x1, y1, x2, y2, relief=True)

````

#### Methode update()

The update method allows you to update certain attributes of the class which are initiated when it is created.
The arguments are fill and fill_mouse at the moment.

In the init of the template:
````
self.rectangle = self.manage.create_rectangle(x1, y1, x2, y2, fill="red")

````

In the update () method of the template:
````
self.rectangle.update(fill="green")

````

### Round

To create ovals, as for rectangles, you have to instantiate the class from the template by giving it several parameters to have the desired effect.
The class returns an object.

````
self.round = self.manage.create_round(x1, y1, x2, y2)
```` 

We can then have access to its attribute self.round.active_focus if the mouse passes over it.
You can also call the update method described below.

#### Mandatory arguments

The method to call the oval is: self.manage.create_round (x1, y1, x2, y2). This is the minimal code to create an oval.

The method to create an oval is the same as with tkinter, we place a rectangle, or an oval will be created.
The points x1 and y1 correspond to the beginning of the oval at the top left and x2 and y2 correspond to the point at the bottom left.
````
:param x1: int 
:param y1: int
:param x2: int
:param y2: int
````

#### Optional arguments
Create_round can take other arguments with kwargs, and they are all optional.


##### fill

Fill allows to fill with a color of the oval, the supported color is the same as tkinter, we can write "red" or its format in hex "# FF0000".
The default color is "gray" if not specified.

````
self.manage.create_round(x1, y1, x2, y2, fill="red")

or

self.manage.create_round(x1, y1, x2, y2, fill="#FF0000")
````

##### fill_mouse

Fill_mouse allows to change the color when the mouse passes over it, its operation is the same as fill.
The default color is the fill color.

````
self.manage.create_round(x1, y1, x2, y2, fill_mouse="red")

or

self.manage.create_round(x1, y1, x2, y2, fill_mouse="#FF0000")
````

##### width

Width allows you to choose the thickness of the border. Set to 0 to deactivate
By default, the value is 1.

````
self.manage.create_round(x1, y1, x2, y2, width=0)

````

##### square_fill


Square_fill allows you to fill the rectangle obtained with the two construction points with a color. The supported color is the same as tkinter, you can write "red" or its hex format "# FF0000".
The default color is None if not specified and therefore transparent.

````
self.manage.create_round(x1, y1, x2, y2, square_fill="red")

or

self.manage.create_round(x1, y1, x2, y2, square_fill="#FF0000")
````

##### square_fill_mouse

Square_fill_mouse allows to change the color when the mouse passes over it, its operation is the same as Square_fill.
The default color is the color of Square_fill.

````
self.manage.create_round(x1, y1, x2, y2, fill_mouse="red")

or

self.manage.create_round(x1, y1, x2, y2, fill_mouse="#FF0000")
````

##### command

Command allows you to give an action when you click on the rectangle.
````
self.manage.create_round(x1, y1, x2, y2, command=("<Button-1>", self.quit_gui))

````
In the example above, the first argument of the tuple is the action to be done on the rectangle, here a left mouse click will activate self.quit_gui.
The syntax is the same as tkinter and for more information refer to the commands chapter.
Command can take several actions, to do so, add the other two arguments to the tuple, action - command following. 
Example :

````
self.manage.create_round(x1, y1, x2, y2, command=("<Button-1>", self.quit_gui, "<Double-Button-1>", self.quit_gui))

````
Here as in the first example, the left click will activate the self.quit_gui command but also, the double left click.

#### Methode update()

As with the update method of the rectangle, the method allows you to update certain attributes of the class which are initiated when it is created.
The arguments are fill and fill_mouse at the moment.

In the init of the template:
````
self.round_test = self.manage.create_round(x1, y1, x2, y2, fill="red")

````

In the update () method of the template:
````
self.round_test.update(fill="green")

````

### Text

The text is created from the template. You have to instantiate the class from the template by giving it several parameters to have the desired effect.
The class returns an object.
````
self.text = self.manage.create_text(x1, y1, text="test")
```` 

You can also call the update method described below.
		
#### Mandatory arguments

The method to call the text is: self.manage.create_text (x1, y1). This is the minimal code to create a text, although nothing will be written in this case.

The points x1 and y1 correspond to the point of inking, the ink or anchor here, will be described below.
````
:param x1: int 
:param y1: int
````

#### Optional arguments
Create_text can take other arguments with kwargs and they are all optional.

##### text

Text displays the text.
````
self.text = self.manage.create_text(x1, y1, text="test")
```` 

##### Anchor

Anchor allows you to modify the start of text display.
By default, is 'center' which means that the text is centered in relation to the position (x, y).
````
self.text = self.manage.create_text(x1, y1, text="test", anchor="center")
```` 

##### Fill

Fill allows to fill with a color of the text, the supported color is the same as tkinter, one can write "red" or its format in hex "# FF0000".
The default color is "black" if not specified.

````
self.manage.create_text(x1, y1, text="test", fill="red")

or

self.manage.create_text(x1, y1, text="test", fill="#FF0000")
````

#### Methode update()

As with the update method of the rectangle, the method allows to update certain attributes of the class which are initiated at its creation.
The arguments are fill and text at the moment.

In the init of the template:
````
self.text_test = self.manage.create_text(x1, y1, text="test", fill="red")

````

In the update () method of the template:
````
self.text_test.update(fill="green")

````

### Button

The button is a graphic object which is not integrated into the tkinter canvas, this button is in two states, active or not.
The body of the button is made up of a rectangle in the center superimposed with a circle that moves from side to side of the rectangle to visually show if the button is active.
````
self.button = self.manage.create_button(x1, y1)
````
Trick :
To create a simple button, rectangular or round widgets allow you to do this by linking an action when clicked.

#### Mandatory arguments

The method to call the button is: self.manage.create_button (x1, y1). This is the minimal code to create a button.

Points x1 and y1 correspond to the center of the button.
````
:param x1: int 
:param y1: int
````

#### Optional arguments

Create_button can take other arguments with kwargs, and they are all optional.

##### Active

Active allows to choose if the button is activated at the beginning.
By default, the button will be disabled.
````
self.button = self.manage.create_button(x1, y1, active=True)
````

##### Fill_round

Fill_round allows you to choose the color of the round part of the button
By default, the color is "red"
````
self.button = self.manage.create_button(x1, y1, fill_round="black")
````

##### Fill_body

Fill_body allows you to choose the color of the rectangle part of the button
By default, the color is "blue"
````
self.button = self.manage.create_button(x1, y1, fill_body="red")
````

##### Scale

Scale allows you to adjust the size of the button.
By default, the size is 1

````
self.button = self.manage.create_button(x1, y1, scale=2)
````

### Menu

Menu is also like button a graphic object created.
Menu allows you to create a menu by adding cascading labels, its operation is similar to Menu () of tkinter but adapted to the canvas.

````
self.menu = self.manage.create_menu(x1, y1, x2, y2, text="test")
````

#### Mandatory arguments

The method to call the menu is as follows: self.manage.create_menu (x1, y1, x2, y2). This is the minimal code to create a menu.

As with the rectangle, x1 and y1 represent the points of the rectangle at the top left and x2 and y2 represent the points at the bottom right.
````
:param x1: int 
:param y1: int
:param x2: int 
:param y2: int
````

#### Optional arguments
Create_menu takes all the points of the rectangle, except the command that will be used has deployed the label drop-down list.

#### Add_label () method

The add_label method allows you to add labels to the drop-down list when the menu is activated.
For the used, after with initiated a menu.
````
self.menu = self.manage.create_menu(x1, y1, x2, y2, text="test")
````

Added:
````
self.label_menu = self.menu.add_label("label_test")
````
A command can be given as an argument, as before, you must give a tuple (action, command)

#### Add_cascade () method

The add_cascade method allows you to add a drop-down list to a label, the list will be opened on the right of the label window.
To use it, after having initiated the menu and the label.
````
self.menu = self.manage.create_menu(x1, y1, x2, y2, text="test")

label_menu = self.menu.add_label("label_test")
````

Added:
````
self.menu.add_cascade("cascade_test", label_menu)
````

An order can be linked by adding:
````
self.menu.add_cascade("cascade_test", label_menu, command=("<Button-1>", self.quit_gui))
````


## Order

Guitool has a few commands, but you can add your own.
The commands are separated into three classes, keyboard, mouse, and custom commands.

### Keyboard

To add keyboard commands, nothing could be simpler.
Create a class where you group your commands linked to the keyboard.
````
class KeyBoard:
    """
    Manage keyboard events
    """

    def __init__(self):

        # key press alt + enter
        self.window.bind("<Alt-Return>", self.fullscreen)

````

The use of the bind method of tkinter which allows to manage the events.
self.fullscreen points to a custom command that we will see below.

To have access to this command, all you have to do is to inherit this class from your template.
Please note that the Keyboard name for the class name is already used.

### Mouse

If you want to add actions with the mouse by clicking on your widgets, it will also defraud creating a new class.
Basically, mouse capture, left single click and left double click are supported.
You can add more with:
````
class Mous:
    """
    Manage mouse events
    """

    def __init__(self):
        """
        Init mouse event
        """
		
        self.window.bind("<Button-3>", self.click_button_3)


    def self.click_button_3(self, event):

        self.adjust_mousse(event.x, event.y)
        self.manage.command(self.x, self.y, "<Button-3>")
		
````

This example allows you to add the right click to the manage event loop and therefore to your widgets.
The call of the method self.adjust_mousse (event.x, event.y) allows to adjust the movement of the mouse with the real position of the window on you used scroolbar.
As for keyboard commands, all that remains is to inherit the class from your template.
Please note that the Mouse name for the class is already used

### Custom order

You can create your commands which are given to your widgets.

For that you need a new class:
````
class CommandGui:
    """
    Manage command events
    """
	
	def draw_dashboard(self):
		"""
		destroy the old page and load the new one
		"""

		self.window.template.active_template.canvas.destroy()
		self.window.template.draw_dashboard()
	
	def quit_gui(self):
		"""
		Destroy window and close app
		"""

		self.window.destroy()
		self.window.template = None
		
````

All that remains is to inherit your class from your template.
It is here for example where you can put the command to load a new template with the example draw_dashboard





