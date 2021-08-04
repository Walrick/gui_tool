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
Les widgets de tk_gui_tools sont accessibles au travers de la classe manage qui s’initialise en héritant de Base. Notez aussi qu’il est possible d’utiliser les widgets de Tkinter comme dans l’exemple de self.title en utilisant self.canvas.create_text(… etc)
Les widgets de tk_gui_tools appelez avec self.manage.create_rectangle par exemple sont décrit dans la section Widget
Il est possible de mettre a jour de le template grace a la méthode update(), le temps défini dans refresh sera utilisé pour appeler update(), si refresh est définis sur 200 ms, update() sera appelé toutes les 200 ms.


## Widget

### Rectangle

### Round

### Text

### Button

### Menu

## Commande

### Clavier

### Souris

### Commande personnalisée



