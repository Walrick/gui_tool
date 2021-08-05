# tk_gui_tools

--------------------------------------------------

## Description
tk_gui_tools est un package open source basé sur le canvas de Tkinter. Il propose des outils et widgets déjà formé et lié pour permettre de créer rapidement des interfaces.


## Utilisation - Tutoriel
Le paquetage a était développé avec l’idée qu’un objet graphique peux être écrit simplement dans un template et peut être mis a jour avec une seule méthode. 
Le package repose sur l’utilisation du canvas de Tkinter.
Les objets graphiques appelés ici « widgets » sont à la base calqué sur les widgets du canvas de tkinder. 
Mais ils ont été liés de base à l’action de l’utilisateur, par exemple : à la création d’un rectangle, on peut lui définir une couleur différente si le curseur passe dessus ou/et lui lier une action sur si on lui clique dessus.
Le paquetage tk_gui_tools gère la création de l’environnement de tkinter et la mainloop() mais il est nécessaire de préparer quelques fichiers.

Commencer par créer un fichier settings.py et y coller les variables suivantes :
Le dictionnaire screen permet de configurer la fenêtre voulue.

````
# Default settings screen
screen = {
    "screensize": "1920x1080",
    "fullscreen": False,
    "title": "Python Project",
    "resizable": {"height": True, "width": True},
}
````

La variable booléenne default_template permet de configurer le premier template à afficher.
Si vous voulait utiliser le template par default qui se nomme dashboard et qui sert de petit exemple mettre True à la place de False

````
# True is use default template in first
default_template = True
````

A variable refresh permet de fixer la méthode after() de tkinter, sa valeur s’exprime en ms

````
# set time refresh in ms
refresh = 200
````

Pour pouvoir intégrer la logique de votre application nous proposons cette façon de faire :

````
racine
├─app.py
├─README.md
├─.env
├─requirements.txt
└─ core
    ├─ __init__.py
    ├─ master.py
    ├─ settings.py
    ├─ gui
    │    ├─ __init__.py
    │    ├─ template_manager.py
    │    └─ template
    │          ├─ __init__.py
    │          └─ first_template.py	
    │    
    └─ logic_app
	    ├─ __init__.py
		├─ master_logic.py	
		etc...
````

Le fichier settings.py a était décrit plus haut, nous allons voir master.py

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
La classe Master hérite de la classe Main de tk_gui_tools qui permet d'initialiser Tkinter.
L'argument args transmis a l'init de Main sont les éventuelles commandes reçue au lancement par app.py et settings est le fichier de configuration établis plus haut.
Self.master_app permet de lancer la logique de votre application, ici on prend l'exemple de Master_logic est un classe. Un thread peut être utilisé pour lancer votre application, si c'est le cas, le thread de Tkinter doit être le premier, sinon votre application plantera.
Self.template permet d'initier la gui de votre programme, il est nécessaire de lui donner en argument self.window et self.default_template, le dernier dépendra de votre logique d'application.

Le prochain fichier est finalement optionnel si vous n’utilisez qu’un seul template et que vous souhaitez utiliser le template par défaut. Sinon il sera nécessaire de rajouter quelques lignes :

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

Cette classe permet de gérer les templates.
Self.active_template permet de d’afficher le template en cours
On pourra ajouter de nouveau template en ajoutant des méthodes et dans la méthode en précisant le nouveau template actif avec self.active_template

Le dernier fichier à ajouter est le template lui-même.
Dans notre exemple, first_template.py	
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

Notre template a besoin d'hériter de Base et de l’initialiser en lui donnant l’argument window, ensuite il ne reste plus cas utiliser les widgets pour afficher ce que l’on veut.
Les widgets de tk_gui_tools sont accessibles au travers de la classe manage qui s’initialise en héritant de Base. Notez aussi qu’il est possible d’utiliser les widgets de Tkinter comme dans l’exemple de self.title en utilisant self.canvas.create_text(… etc).
Les widgets de tk_gui_tools appelez avec self.manage.create_rectangle par exemple sont décrit dans la section Widget.
Il est possible de mettre a jour de le template grace a la méthode update(), le temps défini dans refresh sera utilisé pour appeler update(), si refresh est définis sur 200 ms, update() sera appelé toutes les 200 ms.


## Widget
Les widgets de tk_gui_tools sont des widgets qui sont basé sur ceux de tkinter.
Actuellement, le rectangle, le rond et le texte sont implémentés. Button et Menu sont des assemblages graphiques des trois premiers widgets 

### Rectangle

Les rectangles se crée depuis le template. Il faut instancier la classe depuis le template en lui donnant plusieurs paramètres pour avoir l'effet voulu.
La classe retourne un objet.

````
self.rectange = self.manage.create_rectangle(x1, y1, x2, y2)
```` 

On peut par la suite avoir accès a sont attribut self.rectange.active_focus si la souris passe sur lui.
On peut aussi appeler la methode update décrite plus bas.
		
#### Arguments obligatoires

La méthode pour appeler le rectangle est la suivante : self.manage.create_rectangle(x1, y1, x2, y2). Ceci est le code minimal pour créer un rectangle.

Les points x1 et y1 corresponde au debut du rectangle en haut a gauche et x2 et y2 correspond au point en bas a gauche
````
:param x1: int 
:param y1: int
:param x2: int
:param y2: int
````

#### Arguments optionnels
Create_rectangle peut prendre d'autre argument avec kwargs et ils sont tous optionnels. 

##### fill

Fill permet de remplir d'une couleur le rectangle, la couleur prit en charge est la même que tkinter, on peut écrire "red" ou son format en hex "#FF0000".
La couleur par default est "grey" si non renseigné.

````
self.manage.create_rectangle(x1, y1, x2, y2, fill="red")

or

self.manage.create_rectangle(x1, y1, x2, y2, fill="#FF0000")
````

##### fill_mouse

Fill_mouse permet de changer la couleur quand la souris passe dessus, son fonctionnement est le même que fill.
La couleur par default est la couleur de fill.

````
self.manage.create_rectangle(x1, y1, x2, y2, fill_mouse="red")

or

self.manage.create_rectangle(x1, y1, x2, y2, fill_mouse="#FF0000")
````

##### width

Width permet de choisir l'épaisseur de la bordure. Mettre à 0 pour désactiver
Par default, la valeur est 1.

````
self.manage.create_rectangle(x1, y1, x2, y2, width=0)

````

##### text

Text permet d'afficher du texte dans le rectangle.

````
self.manage.create_rectangle(x1, y1, x2, y2, text="test text")

````

##### anchor

Anchor permet de positionner le texte dans le rectangle.
Actuellement, la seule position est la position par default, le centre
````
self.manage.create_rectangle(x1, y1, x2, y2, text="test text", anchor="center")

````

##### text_fill

Text_fill permet de donner une couleur au texte, la couleur par default est noir.
La couleur fonctionne de la même manière que fill.

````
self.manage.create_rectangle(x1, y1, x2, y2, text="test text", fill_text="red")

or

self.manage.create_rectangle(x1, y1, x2, y2, text="test text", fill_text="#FF0000")
````

##### text_fill_mouse

Text_fill_mouse permet de changer la couleur du texte quand la souris passe sur le rectangle.
La couleur par default est text_fill.

````
self.manage.create_rectangle(x1, y1, x2, y2, text="test text", text_fill_mouse="red")

or

self.manage.create_rectangle(x1, y1, x2, y2, text="test text", text_fill_mouse="#FF0000")
````

##### command

Command permet de donner une action quand on clique sur le rectangle.
````
self.manage.create_rectangle(x1, y1, x2, y2, command=("<Button-1>", self.quit_gui))

````
Dans l'exemple ci-dessus, le premier argument du tuple est l'action à faire sur le rectangle, ici un clique gauche de souris activera self.quit_gui. La syntaxe et la même que tkinter et pour plus d'information se reporter au chapitre des commandes.
Command peut prendre plusieurs actions, pour se faire, rajouter dans le tuple les deux autres arguments, action - commande à la suite. 
Exemple :

````
self.manage.create_rectangle(x1, y1, x2, y2, command=("<Button-1>", self.quit_gui, "<Double-Button-1>", self.quit_gui))

````
Ici comme au premier exemple, le clique gauche activera la commande self.quit_gui mais également, le double clique gauche.

##### relief

Relief permet d'afficher un relief. Elle fait apparaitre une ligne noire sous le rectangle et à droite du rectangle
````
self.manage.create_rectangle(x1, y1, x2, y2, relief=True)

````

#### Methode update()

La methode update permet de mettre a jour certain attribut de la classe qui sont initier à sa creation.
Les arguments sont fill et fill_mouse pour le moment.

Dans l'init du template :
````
self.rectangle = self.manage.create_rectangle(x1, y1, x2, y2, fill="red")

````

Dans la methode update() du template :
````
self.rectangle.update(fill="green")

````

### Round

Pour créer des ovales, comme pour les rectangles, il faut instancier la classe depuis le template en lui donnant plusieurs paramètres pour avoir l'effet voulu.
La classe retourne un objet.

````
self.round = self.manage.create_round(x1, y1, x2, y2)
```` 

On peut par la suite avoir accès a sont attribut self.round.active_focus si la souris passe sur lui.
On peut aussi appeler la methode update décrite plus bas.

#### Arguments obligatoires

La méthode pour appeler l'ovale est la suivante : self.manage.create_round(x1, y1, x2, y2). Ceci est le code minimal pour créer un ovale.

La methode pour créer un ovale est la même qu'avec tkinter, on place un rectange ou un ovale va venir se créer.
Les points x1 et y1 corresponde au debut de l'ovale en haut a gauche et x2 et y2 correspond au point en bas a gauche
````
:param x1: int 
:param y1: int
:param x2: int
:param y2: int
````

#### Arguments optionnels
Create_round peut prendre d'autre argument avec kwargs et ils sont tous optionnels. 


        "command": couple of command action and effect (action, effet) or
        (action, effet, action, effet, etc..) ex:
        ("<Button-1>", "self.quit_gui")
        }
        """

##### fill

Fill permet de remplir d'une couleur de l'ovale, la couleur prit en charge est la même que tkinter, on peut écrire "red" ou son format en hex "#FF0000".
La couleur par default est "grey" si non renseigné.

````
self.manage.create_round(x1, y1, x2, y2, fill="red")

or

self.manage.create_round(x1, y1, x2, y2, fill="#FF0000")
````

##### fill_mouse

Fill_mouse permet de changer la couleur quand la souris passe dessus, son fonctionnement est le même que fill.
La couleur par default est la couleur de fill.

````
self.manage.create_round(x1, y1, x2, y2, fill_mouse="red")

or

self.manage.create_round(x1, y1, x2, y2, fill_mouse="#FF0000")
````

##### width

Width permet de choisir l'épaisseur de la bordure. Mettre à 0 pour désactiver
Par default, la valeur est 1.

````
self.manage.create_round(x1, y1, x2, y2, width=0)

````

##### square_fill

Square_fill permet de remplir d'une couleur le rectangle obtenu avec les deux points de construction. La couleur prit en charge est la même que tkinter, on peut écrire "red" ou son format en hex "#FF0000".
La couleur par default est None si non renseigné et donc transparent.

````
self.manage.create_round(x1, y1, x2, y2, square_fill="red")

or

self.manage.create_round(x1, y1, x2, y2, square_fill="#FF0000")
````

##### square_fill_mouse

Square_fill_mouse permet de changer la couleur quand la souris passe dessus, son fonctionnement est le même que Square_fill.
La couleur par default est la couleur de Square_fill.

````
self.manage.create_round(x1, y1, x2, y2, fill_mouse="red")

or

self.manage.create_round(x1, y1, x2, y2, fill_mouse="#FF0000")
````

##### command

Command permet de donner une action quand on clique sur le rectangle.
````
self.manage.create_round(x1, y1, x2, y2, command=("<Button-1>", self.quit_gui))

````
Dans l'exemple ci-dessus, le premier argument du tuple est l'action à faire sur le rectangle, ici un clique gauche de souris activera self.quit_gui. La syntaxe et la même que tkinter et pour plus d'information se reporter au chapitre des commandes.
Command peut prendre plusieurs actions, pour se faire, rajouter dans le tuple les deux autres arguments, action - commande à la suite. 
Exemple :

````
self.manage.create_round(x1, y1, x2, y2, command=("<Button-1>", self.quit_gui, "<Double-Button-1>", self.quit_gui))

````
Ici comme au premier exemple, le clique gauche activera la commande self.quit_gui mais également, le double clique gauche.

### Text

### Button

### Menu

## Commande

### Clavier

### Souris

### Commande personnalisée



