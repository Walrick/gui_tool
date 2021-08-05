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
La couleur par défaut est "grey" si non renseigné.

````
self.manage.create_rectangle(x1, y1, x2, y2, fill="red")

or

self.manage.create_rectangle(x1, y1, x2, y2, fill="#FF0000")
````

##### fill_mouse

Fill_mouse permet de changer la couleur quand la souris passe dessus, son fonctionnement est le même que fill.
La couleur par défaut est la couleur de fill.

````
self.manage.create_rectangle(x1, y1, x2, y2, fill_mouse="red")

or

self.manage.create_rectangle(x1, y1, x2, y2, fill_mouse="#FF0000")
````

##### width

Width permet de choisir l'épaisseur de la bordure. Mettre à 0 pour désactiver
Par défaut, la valeur est 1.

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
Actuellement, la seule position est la position par défaut, le centre
````
self.manage.create_rectangle(x1, y1, x2, y2, text="test text", anchor="center")

````

##### text_fill

Text_fill permet de donner une couleur au texte, la couleur par défaut est noir.
La couleur fonctionne de la même manière que fill.

````
self.manage.create_rectangle(x1, y1, x2, y2, text="test text", fill_text="red")

or

self.manage.create_rectangle(x1, y1, x2, y2, text="test text", fill_text="#FF0000")
````

##### text_fill_mouse

Text_fill_mouse permet de changer la couleur du texte quand la souris passe sur le rectangle.
La couleur par défaut est text_fill.

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

La methode update permet de mettre a jour certain attribut de la classe qui sont initié à sa creation.
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


##### fill

Fill permet de remplir d'une couleur de l'ovale, la couleur prit en charge est la même que tkinter, on peut écrire "red" ou son format en hex "#FF0000".
La couleur par défaut est "grey" si non renseigné.

````
self.manage.create_round(x1, y1, x2, y2, fill="red")

or

self.manage.create_round(x1, y1, x2, y2, fill="#FF0000")
````

##### fill_mouse

Fill_mouse permet de changer la couleur quand la souris passe dessus, son fonctionnement est le même que fill.
La couleur par défaut est la couleur de fill.

````
self.manage.create_round(x1, y1, x2, y2, fill_mouse="red")

or

self.manage.create_round(x1, y1, x2, y2, fill_mouse="#FF0000")
````

##### width

Width permet de choisir l'épaisseur de la bordure. Mettre à 0 pour désactiver
Par défaut, la valeur est 1.

````
self.manage.create_round(x1, y1, x2, y2, width=0)

````

##### square_fill

Square_fill permet de remplir d'une couleur le rectangle obtenu avec les deux points de construction. La couleur prit en charge est la même que tkinter, on peut écrire "red" ou son format en hex "#FF0000".
La couleur par défaut est None si non renseigné et donc transparent.

````
self.manage.create_round(x1, y1, x2, y2, square_fill="red")

or

self.manage.create_round(x1, y1, x2, y2, square_fill="#FF0000")
````

##### square_fill_mouse

Square_fill_mouse permet de changer la couleur quand la souris passe dessus, son fonctionnement est le même que Square_fill.
La couleur par défaut est la couleur de Square_fill.

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

#### Methode update()

Comme avec la methode update du rectangle, la methode permet de mettre a jour certain attribut de la classe qui sont initié à sa creation.
Les arguments sont fill et fill_mouse pour le moment.

Dans l'init du template :
````
self.round_test = self.manage.create_round(x1, y1, x2, y2, fill="red")

````

Dans la methode update() du template :
````
self.round_test.update(fill="green")

````

### Text

Le texte se crée depuis le template. Il faut instancier la classe depuis le template en lui donnant plusieurs paramètres pour avoir l'effet voulu.
La classe retourne un objet.

````
self.text = self.manage.create_text(x1, y1, text="test")
```` 

On peut aussi appeler la methode update décrite plus bas.
		
#### Arguments obligatoires

La méthode pour appeler le text est la suivante : self.manage.create_text(x1, y1). Ceci est le code minimal pour créer un texte, même si rien ne sera ecrit dans ce cas là.

Les points x1 et y1 corresponde au point d'encrage, l'encre ou anchor ici, sera décrit plus bas.
````
:param x1: int 
:param y1: int
````

#### Arguments optionnels
Create_text peut prendre d'autre argument avec kwargs et ils sont tous optionnels. 

##### text

Text permet d'afficher le texte
````
self.text = self.manage.create_text(x1, y1, text="test")
```` 

##### Anchor

Anchor permet de modifier le debut d'affichage du texte.
Par défaut, vaut 'center' ce qui signifie que le texte est centré par rapport à la position (x,y)
````
self.text = self.manage.create_text(x1, y1, text="test", anchor="center")
```` 

##### Fill

Fill permet de remplir d'une couleur du texte, la couleur prit en charge est la même que tkinter, on peut écrire "red" ou son format en hex "#FF0000".
La couleur par défaut est "black" si non renseigné.

````
self.manage.create_text(x1, y1, text="test", fill="red")

or

self.manage.create_text(x1, y1, text="test", fill="#FF0000")
````

#### Methode update()

Comme avec la methode update du rectangle, la methode permet de mettre a jour certain attribut de la classe qui sont initier à sa creation.
Les arguments sont fill et text pour le moment.

Dans l'init du template :
````
self.text_test = self.manage.create_text(x1, y1, text="test", fill="red")

````

Dans la methode update() du template :
````
self.text_test.update(fill="green")

````

### Button

Le bouton est un objet graphique qui n'est pas intégré au canvas de tkinter, ce bouton là est en deux états, actif ou non.
Le corps du bouton est composé d'un rectangle au centre superposé d'un rond qui se déplace d'un côté et de l'autre du rectangle pour montrer visuellement si le bouton est actif.
````
self.button = self.manage.create_button(x1, y1)
````
Astuce :
Pour créer un bouton simple, les widgets rectangles ou rounds permettent de faire cela en liant une action quand on clique dessus.

#### Arguments obligatoires

La méthode pour appeler le bouton est la suivante : self.manage.create_button(x1, y1). Ceci est le code minimal pour créer un bouton.

Les points x1 et y1 corresponde au centre du bouton
````
:param x1: int 
:param y1: int
````

#### Arguments optionnels

Create_button peut prendre d'autre argument avec kwargs et ils sont tous optionnels. 

##### Active

Active permet de choisir si le bouton est activé au debut.
Par défaut, le bouton sera désactivé.
````
self.button = self.manage.create_button(x1, y1, active=True)
````

##### Fill_round

Fill_round permet de choisir la couleur de la partie ronde du bouton
Par défaut, la couleur est "red"
````
self.button = self.manage.create_button(x1, y1, fill_round="black")
````

##### Fill_body

Fill_body permet de choisir la couleur de la partie rectangle du bouton
Par défaut, la couleur est "blue"
````
self.button = self.manage.create_button(x1, y1, fill_body="red")
````

##### Scale

Scale permet de réger la taille du bouton.
Par défaut, la taille est sur 1

````
self.button = self.manage.create_button(x1, y1, scale=2)
````

### Menu

Menu est aussi comme button un objet graphique créer.
Menu permet de créer un menu en ajoutant des labels cascades, sont fonctionnement resemble a Menu() de tkinter mais adapté au canvas.

````
self.menu = self.manage.create_menu(x1, y1, x2, y2, text="test")
````

#### Arguments obligatoires

La méthode pour appeler le menu est la suivante : self.manage.create_menu(x1, y1, x2, y2). Ceci est le code minimal pour créer un menu.

Comme avec le rectangle, x1 et y1 représente le points du rectangle en haut à gauche et x2 et y2 représente les points en bas a droite.
````
:param x1: int 
:param y1: int
:param x2: int 
:param y2: int
````

#### Arguments optionnels
Create_menu reprend tous les points du rectangle, sauf la commande qui sera utilisé a déployé la liste déroulante de label.

#### Méthode add_label()

La méthode add_label permet d'ajouter des labels à la liste déroulante quand le menu sera activé.
Pour l'utilisé, apres avec initié un menu.
````
self.menu = self.manage.create_menu(x1, y1, x2, y2, text="test")
````

Ajouté :
````
self.label_menu = self.menu.add_label("label_test")
````
Une commande peut être donnée en argument, comme précédemment, il faut donner un tuple (action, commande)

#### Méthode add_cascade()

La méthode add_cascade permet d'ajouter un liste déroulante à un label, la liste sera ouverte à droite de la fenêtre du label.
Pour l'utiliser, apres avoir initié le menu et le label.
````
self.menu = self.manage.create_menu(x1, y1, x2, y2, text="test")

label_menu = self.menu.add_label("label_test")
````

Ajouté :
````
self.menu.add_cascade("cascade_test", label_menu)
````

Une commande peut être liée en ajoutant :

````
self.menu.add_cascade("cascade_test", label_menu, command=("<Button-1>", self.quit_gui))
````


## Commande

tk_gui_tools possède quelques commande mais vous pouvez en ajouter les vôtres.
Les commandes sont séparées en trois classes, clavier, souris et les commandes personnalisées.

### Clavier

Pour ajouter des commandes claviers, rien de plus simple.
Créer une classe ou vous regroupez vos commande lié au clavier.
````
class KeyBoard:
    """
    Manage keyboard events
    """

    def __init__(self):

        # key press alt + enter
        self.window.bind("<Alt-Return>", self.fullscreen)

````

L'utilisation de la methode bind de tkinter qui permet de gérer les events.
self.fullscreen pointe vers une commande personnalisée que nous verront plus bas.

Pour avoir accès a cette commande, il ne reste plus qu'à faire hériter cette classe à votre template.
Attention le nom Keyboard pour le nom de la classe est deja utilisé.

### Souris

Si vous souhaitez ajouter des actions avec la souris en cliquant sur vos widgets, il fraudera là aussi créer une nouvelle classe.
De base, la capture de la souris, le simple clique gauche et le double clique gauche sont gérés.
Vous pouvez en rajouter avec :
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

Cette exemple permet d'ajouter le clique droit à la boucle d'évenement de manage et donc sur vos widgets.
L'appel de la méthode self.adjust_mousse(event.x, event.y) permet d'ajuster le déplacement de la souris avec la position véritable de la fenêtre sur vous utilisé scroolbar.
Comme pour les commande clavier, il ne reste plus qu'à hériter la classe à vote template. 
Attention le nom Mouse pour la classe est deja utilisé

### Commande personnalisée

Vous pouvez créer vos commandes qui sont données à vos widgets.

Pour cela il vous faut une nouvelle classe :
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

Il ne reste plus qu'à faire hériter votre classe à votre template.
C'est ici par exemple ou vous pouvez mettre la commande pour charger un nouveau template avec l'exemple draw_dashboard





