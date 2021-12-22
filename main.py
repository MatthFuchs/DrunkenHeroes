import random

from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.uix.screenmanager import ScreenManager, NoTransition, SlideTransition
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.list import *
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
__version__ = "2.0.0"


Builder.load_string("""
<Startbildschirm>:
    users: username.text
    BoxLayout:
        orientation:'vertical'
        TextInput
            id: username
            color_mode: 'custom'
            color: 1, 1, 1, 1
            hint_text: "Spieleranzahl"
            line_color_normal: 1, 1, 1, 1
            color_mode: 'custom'
            mode: "rectangle"
            rectangle_color_normal: 1, 1, 1, 1
            rectangle_color_focus: 1, 1, 1, 1
            line_color_focus: 1, 1, 1, 1
        Button:
            text: 'Heldenwahl'
            on_release: root.Heldenwahl()
        Button:
            text: 'Heldenscreen'
            on_press:
                root.manager.current = 'hero'
<Heroscreen>:
    GridLayout:
        rows:5
        cols:2
        Button:
            text: 'Lanzelot'
            on_release:
                root.choose_lanzelot()
                root.manager.current='herohub'
        Button:
            text: 'Dunkler Lord'
            on_release:
                root.choose_dunklerlord()
                root.manager.current='herohub'
        Button:
            text:'Ritter'
            on_release:
                root.choose_ritter()
                root.manager.current='herohub'
        Button:
            text:'Hirnloser'
            on_release:
                root.choose_hirnloser()
                root.manager.current='herohub'
        Button:
            text:'Prinzessin'
            on_release:
                root.choose_prinzessin()
                root.manager.current='herohub'
        Button:
            text:'Braumeister'
            on_release:
                root.choose_braumeister()
                root.manager.current='herohub'
        Button:
            text:'Zurück'
            on_release:
                root.manager.transition.direction = 'right' 
                root.manager.current='menu'
        Button:
            text:'Zur Stadt'
            on_release:
                root.manager.transition.direction = 'left'
                root.manager.current='Stadt'
<Heldenhub>:
    on_pre_enter:
        root.pre()
    GridLayout:
        rows:4
        cols:1
        Button:
            id:heldenname
            color:1,1,1,1
            size_hint_y:0.15
            text:''
            font_size:'50sp'
            on_release:
                root.heldeninfo()
        MDLabel:
            id:heldbild
            text:'Hier ist ein schönes Bild'
            font_size:'30sp'
            size_hint_y:0.35
        GridLayout:
            size_hint_y:0.25
            rows:1
            cols:2
            MDLabel:
                id:heldleben
                text:'Leben: 30'
                font_size:'30sp'
                color:1,1,1,1
            GridLayout:
                rows:1
                cols:2
                Button:
                    text:'+'
                    on_release:
                        root.lebenplus()
                Button:
                    text:'-'
                    on_release:
                        root.lebenminus()
        GridLayout:
            size_hint_y: 0.25
            rows:1
            cols:2
            Button:
                id:skill1
                text: 'Skill 1'
                font_size:'30sp'
                on_release:
                    root.skillwahl()
                    root.manager.current='menu'
            Button:
                id:skill2
                text: 'Skill 2'
                font_size:'30sp'
                on_release:
                    root.skillwahl()
<Stadt>:
    canvas:
        Rectangle:
            source: 'hintergrund.png'
            pos: self.pos
            size: self.size
    FloatLayout:

        Button:
            text: '<--'
            font_size: '50sp'
            pos_hint:{'center_x':0.05, 'center_y': 0.35}
            size_hint: .1,.1
            background_color:0,0,0,.3
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current='Wildnisgut'

        Button:
            text: '-->'
            font_size: '50sp'
            pos_hint:{'center_x':0.95, 'center_y': 0.35}
            size_hint: .1,.1
            background_color:0,0,0,.3
            on_release:
                root.manager.transition.direction = 'left'
                root.manager.current='Wildnisböse'

        Button:
            text:"Zurück"
            background_normal: ""
            pos_hint:{'center_x': 0.1, 'center_y': 0.1}
            size_hint:0.15,0.20
            background_color: 0,0,0,0.5
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current='hero' 
        Button:
            id:magiershop
            background_normal: ""
            pos_hint:{'center_x': 0.4, 'center_y': 0.28}
            size_hint:0.157,0.25
            background_color: 0,0,0,0
            on_release:
                root.magiershop()
                root.manager.current='zauberershop'
        Button:
            id:hexeshop
            background_normal: ""
            pos_hint:{'center_x': 0.259, 'center_y': 0.659}
            size_hint:0.15,0.2
            background_color: 0,0,0,0
            on_release:
                root.hexeshop()
                root.manager.current='hexeshop'
<Hexeshop>:
    canvas:
        Rectangle:
            source: 'regal.png'
            pos: self.pos
            size: self.size
    FloatLayout:

        MDLabel:
            text: "Hexenshop"
            pos_hint:{'center_x': 0.23, 'center_y': 0.9}
            size_hint: 0.4,0.2
            font_size:'50sp'
            text_color: 1,1,1,1
        Button:
            id:hexbut1
            text: 'Verkauft'
            pos_hint:{'center_x':0.35,'center_y':0.7}
            size_hint:0.15,0.15
            text_color: 1,1,1,1
            on_release:
                root.buttonpress(self)
        Button:
            id:hexbut2
            text: 'Verkauft'
            pos_hint:{'center_x':0.525,'center_y':0.7}
            size_hint:0.15,0.15
            text_color: 1,1,1,1
            on_release:
                root.buttonpress(self)
        Button:
            id:hexbut3
            text: 'Verkauft'
            pos_hint:{'center_x':0.7,'center_y':0.7}
            size_hint:0.15,0.15
            text_color: 1,1,1,1
            on_release:
                root.buttonpress(self)
        Button:
            id:hexbut4
            text: 'Verkauft'
            pos_hint:{'center_x':0.35,'center_y':0.35}
            size_hint:0.15,0.15
            text_color: 1,1,1,1
            on_release:
                root.buttonpress(self)
        Button:
            id:hexbut5
            text: 'Verkauft'
            pos_hint:{'center_x':0.525,'center_y':0.35}
            size_hint:0.15,0.15
            text_color: 1,1,1,1
            on_release:
                root.buttonpress(self)
        Button:
            id:hexbut6
            text: 'Verkauft'
            pos_hint:{'center_x':0.7,'center_y':0.35}
            size_hint:0.15,0.15
            text_color: 1,1,1,1
            on_release:
                root.buttonpress(self)
        Button:
            text:"Zurück"
            background_normal: ""
            pos_hint:{'center_x': 0.1, 'center_y': 0.1}
            size_hint:0.15,0.20
            background_color: 0,0,0,0.5
            on_release:
                root.manager.current='Stadt' 


<Zauberershop>:
    canvas:
        Rectangle:
            source: 'regal.png'
            pos: self.pos
            size: self.size
    FloatLayout:
        MDLabel:
            text: "Zauberershop"
            pos_hint:{'center_x': 0.23, 'center_y': 0.9}
            size_hint: 0.4,0.2
            font_size:'50sp'
            text_color: 1,1,1,1
        Button:
            id:zaubut1
            text: 'Verkauft'
            pos_hint:{'center_x':0.35,'center_y':0.7}
            size_hint:0.15,0.15
            text_color: 1,1,1,1
            on_release:
                root.buttonpress(self)
        Button:
            id:zaubut2
            text: 'Verkauft'
            pos_hint:{'center_x':0.525,'center_y':0.7}
            size_hint:0.15,0.15
            text_color: 1,1,1,1
            on_release:
                root.buttonpress(self)
        Button:
            id:zaubut3
            text: 'Verkauft'
            pos_hint:{'center_x':0.7,'center_y':0.7}
            size_hint:0.15,0.15
            text_color: 1,1,1,1
            on_release:
                root.buttonpress(self)
        Button:
            id:zaubut4
            text: 'Verkauft'
            pos_hint:{'center_x':0.35,'center_y':0.35}
            size_hint:0.15,0.15
            text_color: 1,1,1,1
            on_release:
                root.buttonpress(self)
        Button:
            id:zaubut5
            text: 'Verkauft'
            pos_hint:{'center_x':0.525,'center_y':0.35}
            size_hint:0.15,0.15
            text_color: 1,1,1,1
            on_release:
                root.buttonpress(self)
        Button:
            id:zaubut6
            text: 'Verkauft'
            pos_hint:{'center_x':0.7,'center_y':0.35}
            size_hint:0.15,0.15
            text_color: 1,1,1,1
            on_release:
                root.buttonpress(self)              
        Button:
            text:"Zurück"
            background_normal: ""
            pos_hint:{'center_x': 0.1, 'center_y': 0.1}
            size_hint:0.15,0.20
            background_color: 0,0,0,0.5
            on_release:
                root.manager.current='Stadt'   


<Wildnisgut>:
    canvas:
        Rectangle:
            source: 'hinterliebpng.png'
            pos: self.pos
            size: self.size
    FloatLayout:  
        Button:
            text:'uuh böses Monster'
            pos_hint:{'center_x': 0.5, 'center_y': 0.5}
            font_size:'50sp' 
            size_hint:0.3,0.30 
            on_release:
                root.manager.transition.direction = 'down'
                root.manager.current='Monstergut'
        Button:
            text:"Zurück"
            background_normal: ""
            pos_hint:{'center_x': 0.9, 'center_y': 0.1}
            size_hint:0.15,0.20
            background_color: 0,0,0,0.5
            on_release:
                root.manager.transition.direction = 'left'
                root.manager.current='Stadt'

<Wildnisböse>:   
    canvas:
        Rectangle:
            source: 'hinterböse.png'
            pos: self.pos
            size: self.size      
    FloatLayout:   
        Button:
            text:'uuh böses Monster'
            pos_hint:{'center_x': 0.5, 'center_y': 0.5}
            font_size:'50sp' 
            size_hint:0.3,0.30 
            on_release:
                root.manager.transition.direction = 'up'
                root.manager.current='Monsterböse'       
        Button:
            text:"Zurück"
            background_normal: ""
            pos_hint:{'center_x': 0.1, 'center_y': 0.1}
            size_hint:0.15,0.20
            background_color: 0,0,0,0.5
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current='Stadt'

<Monstergut>:
    
    FloatLayout:
        Button:
            text:'zurück'
            background_normal: ""
            pos_hint:{'center_x': 0.1, 'center_y': 0.1}
            size_hint:0.15,0.20
            background_color: 0,0,0,0.5
            on_release:
                root.manager.transition.direction = 'up'
                root.manager.current='Wildnisgut'
                
<Monsterböse>:
    FloatLayout:
        Button:
            text:'zurück'
            background_normal: ""
            pos_hint:{'center_x': 0.1, 'center_y': 0.1}
            size_hint:0.15,0.20
            background_color: 0,0,0,0.5
            on_release:
                root.manager.transition.direction = 'down'
                root.manager.current='Wildnisböse'
            

""")


class Startbildschirm(Screen):
    Helden = ["Lanzelot", "Dunkler Lord", "Prinzessin", "Ritter", "Hrinloser"]
    Heldena = []
    users = StringProperty()
    heldeninit = True

    def Heldenwahl(self):
        if self.heldeninit == True:
            Startbildschirm.Heldenliste(self)
            self.heldeninit = False
        try:
            Heldenwahl = random.choice(Startbildschirm.Heldena)
            self.popupheld = MDDialog(title="[b][size=30sp][color=ffffff]Held[/color][/size][/b]",
                                      text="[size=25sp]" + Heldenwahl + "[/size]", auto_dismiss=False, buttons=[
                    MDFlatButton(text='Okay!', on_release=lambda _: self.popupheld.dismiss(), font_size=30)])
            self.popupheld.open()
            print(Heldenwahl)
            Startbildschirm.Heldena.remove(Heldenwahl)
        except:
            self.popupheld = MDDialog(title="[b][size=30sp][color=ffffff]Held[/color][/size][/b]",
                                      text="[size=25sp] Keine Helden mehr! [/size]", auto_dismiss=False, buttons=[
                    MDFlatButton(text='Okay!', on_release=lambda _: self.popupheld.dismiss(), font_size=30)])
            self.popupheld.open()
            print("Keine Helden mehr")

    def Heldenliste(self):
        try:
            playercount = int(self.users)
        except:
            playercount = 1
        Startbildschirm.Heldena = [self.Helden[0], self.Helden[1], self.Helden[3], self.Helden[4]]
        if playercount == 1:
            Startbildschirm.Heldena = ["Matze"]
        elif playercount == 2:
            Startbildschirm.Heldena = self.Helden[0:2]
        elif playercount == 3:
            Startbildschirm.Heldena = self.Helden[0:3]
        elif playercount == 4:
            Startbildschirm.Heldena = [self.Helden[0], self.Helden[1], self.Helden[3], self.Helden[4]]
        elif playercount == 5:
            Startbildschirm.Heldena = self.Helden
        elif playercount in (7, 9, 11, 13, 15, 17):
            Startbildschirm.Heldena = [self.Helden[0], self.Helden[1], self.Helden[3], self.Helden[4]]
            Startbildschirm.Heldena.append("Prinzessin")
        Startbildschirm.lencheck(self)

    def lencheck(self):
        playercount = int(self.users)
        while playercount > int(len(self.Heldena) + 1):
            Startbildschirm.Heldena.append("Ritter")
            Startbildschirm.Heldena.append("Hirnloser")


class Heroscreen(Screen):
    global charakter
    charakter = ''

    def choose_bauer(self):
        self.charakter = "Bauer"
        Heldenhub.choosehelden(self, self.charakter)

    def choose_lanzelot(self):
        self.charakter = 'Lanzelot'
        Heldenhub.choosehelden(self, self.charakter)

    def choose_dunklerlord(self):
        self.charakter = 'Dunkler Lord'
        Heldenhub.choosehelden(self, self.charakter)

    def choose_ritter(self):
        self.charakter = 'Ritter'
        Heldenhub.choosehelden(self, self.charakter)

    def choose_hirnloser(self):
        self.charakter = 'Hirnloser'
        Heldenhub.choosehelden(self, self.charakter)

    def choose_prinzessin(self):
        self.charakter = 'Prinzessin'
        Heldenhub.choosehelden(self, self.charakter)

    def choose_hexe(self):
        self.charakter = 'Hexe'
        Heldenhub.choosehelden(self, self.charakter)

    def choose_zauberer(self):
        self.charakter = 'Zauberer'
        Heldenhub.choosehelden(self, self.charakter)

    def choose_braumeister(self):
        self.charakter = 'Braumeister'
        Heldenhub.choosehelden(self, self.charakter)


class Heldenhub(Screen):
    held = ''

    def choosehelden(self, auswahl):
        self.held = auswahl
        Heldenhub.held = auswahl
        print("Held: " + self.held)

    def pre(self):
        print(Heldenhub.held)
        self.ids['heldenname'].text = Heldenhub.held

    def heldeninfo(self):
        if self.ids['heldenname'].text == 'Lanzelot':
            self.beschreibung = "Lanzelot ist ein tollkühner Held, mit breitem grinsen und aufrechter Statur tritt er dem Dunklen Lord entgegen. \nZiel für Lanzelot ist es, den Dunklen Lord zu besiegen und nebenbei noch die Prinzessin zu klären."
        elif self.ids['heldenname'].text == 'Ritter':
            self.beschreibung = "Der Ritter ist ein treuer Mitstreiter von Lanzelot und unterstützt diesen bei seinen Abenteuern. Ziel ist es, auf Lanzelot aufzupassen, damit sich dieser nicht tollkühn ins Unheil manövriert"
        elif self.ids['heldenname'].text == 'Dunkler Lord':
            self.beschreibung = "Der Dunkle Lord ist ein dreckiger Schuft, dessen Ziel es ist, Lanzelots Abenteuer zu vermiesen, um Ihm den Tag zu versauen. Nebenbei würde der Dunkle Lord auch gern die Prinzessin verführen."
        elif self.ids['heldenname'].text == 'Hirnloser':
            self.beschreibung = "Der Hirnlose wurde vom Dunklen Lord verhext, um diesem zu dienen und ihn in seinem Vorhaben zu unterstützen, Lanzelot zu besiegen"
        elif self.ids['heldenname'].text == 'Prinzessin':
            self.beschreibung = "Die Prinzessin ist die schärfste Schnitte im ganzen Dorf und kann sich nicht recht entscheiden, ob sie den Dunklen Lord oder Lanzelot als angetrauten möchte. \n Ziel ist es, den beiden Wiedersachern sowohl Hinderniss als auch Unterstützung zu sein."
        elif self.ids['heldenname'].text == 'Hexe':
            self.beschreibung = "Die Hexe war die Frau des Zauberers. Nach einer unschönen Trennung (an der alleine der Zauberer Schuld trug), hat sie nun ein konkurrierendes Geschäft zum Zauberlädchen eröffnet: Das Hexenlädchen! \n Ziel ist es, den Abenteuerern ihre Waren anzudrehen und vor allem dem Zauberer die Kundschaft zu stehlen indem sie billigere Preise anbietet."
        elif self.ids['heldenname'].text == 'Zauberer':
            self.beschreibung = "Der Zauberer hat ein Zauberlädchen, welches bereits seit Generationen im Familienbesitz ist. Leider laufen die Geschäfte nicht mehr so gut wie früher, weil seine Exfrau (die Hexe) auf der gegenüberliegenden Straßenseite einen Laden eröffnet hat, nachdem sie die Trennung nicht verkraften konnte (an welcher alleine sie Schuld war).\n Ziel ist es, die eigenen Waren zu verkaufen indem man die Hexe unterbietet."
        elif self.ids['heldenname'].text == 'Braumeister':
            self.beschreibung = "Der Braumeister kümmert sich schon seit Lebzeiten um die flüssigen Bedurfnisse der Abenteuerer in seinem Dorf. Vorausgesetzt er ist gut gelaunt...\n Ziel ist es, den Abenteuerern Getränke zu verkaufen welche verschiedenste Effekte haben können."
        elif self.ids['heldenname'].text == 'Bauer':
            self.beschreibung = "Der Bauer hatte eigentlich nicht so richtig Lust auf ein Abenteuer zu gehen, aber dafür dass er die Bäuerin für ein paar Stunden nicht sehen muss, macht er fast alles mit."
        else:
            print("Fehler")
        self.popupheldinfo = MDDialog(title="[b][size=30sp][color=ffffff]Heldeninfo[/color][/size][/b]",
                                      text="[size=25sp]" + self.beschreibung + "[/size]", auto_dismiss=False, buttons=[
                MDFlatButton(text='Okay!', on_release=lambda _: self.popupheldinfo.dismiss(), font_size=30)])
        self.popupheldinfo.open()

    """
    hier muss ma jetz unterscheiden wer was machen kann z.B. Zauberer und Hexe haben andere Skills als Ritter und dann muss ma halt schauen wie ma des machen
    """

    def skillwahl(self):
        if self.ids['skill1'].text == "Skill 1":
            pass
        elif self.ids['skill1'].text == "Skill 2":
            pass
        else:
            Heldenhub.skilluse(self)

    def skilluse(self):
        pass

    def lebenplus(self):
        Leben = self.ids['heldleben'].text
        Lebenneu = Leben.lstrip("Leben: ")
        self.ids['heldleben'].text = "Leben: " + str(int(Lebenneu) + 1)

    def lebenminus(self):
        Leben = self.ids['heldleben'].text
        Lebenneu = Leben.lstrip("Leben: ")
        self.ids['heldleben'].text = "Leben: " + str(int(Lebenneu) - 1)


class Stadt(Screen):
    def magiershop(self):
        pass

    def hexeshop(self):
        pass


class Hexeshop(Screen):
    itempool = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    challengepool = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    buttonitem = ["hexbut1", "hexbut2", "hexbut3"]
    buttonchallenge = ["hexbut4", "hexbut5", "hexbut6"]

    def on_pre_enter(self, *args):
        Hexeshop.pre(self)

    def buttonpress(self, instance):

        if instance.text != "Verkauft":
            instance.text = "Verkauft"
        else:
            print("SCHEISSE!!!!!!11!!")

    def pre(self):

        for button in self.buttonitem:
            if self.ids[button].text == "Verkauft":
                try:
                    auswahl = random.choice(Hexeshop.itempool)
                    self.ids[button].text = auswahl
                    Hexeshop.itempool.remove(auswahl)
                except:
                    if self.ids[button].text == "Verkauft":
                        print("Arsch")

        for button in self.buttonchallenge:
            if self.ids[button].text == "Verkauft":
                try:
                    auswahl = random.choice(Hexeshop.challengepool)
                    self.ids[button].text = auswahl
                    Hexeshop.challengepool.remove(auswahl)
                except:
                    if self.ids[button].text == "Verkauft":
                        pass


class Zauberershop(Screen):
    itempool = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    challengepool = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    buttonitem = ["zaubut1", "zaubut2", "zaubut3"]
    buttonchallenge = ["zaubut4", "zaubut5", "zaubut6"]

    def on_pre_enter(self, *args):
        Zauberershop.pre(self)

    def pre(self):

        for button in self.buttonitem:
            if self.ids[button].text == "Verkauft":
                try:
                    auswahl = random.choice(Zauberershop.itempool)
                    self.ids[button].text = auswahl
                    Zauberershop.itempool.remove(auswahl)
                except:
                    if self.ids[button].text == "Verkauft":
                        print("Arsch")

        for button in self.buttonchallenge:
            if self.ids[button].text == "Verkauft":
                try:
                    auswahl = random.choice(Zauberershop.challengepool)
                    self.ids[button].text = auswahl
                    Zauberershop.challengepool.remove(auswahl)
                except:
                    if self.ids[button].text == "Verkauft":
                        pass

    def buttonpress(self, instance):

        if instance.text != "Verkauft":
            instance.text = "Verkauft"
        else:
            print("SCHEISSE!!!!!!11!!")


class Wildnisgut(Screen):
    pass


class Wildnisböse(Screen):
    pass

class Monstergut(Screen):
    pass

class Monsterböse(Screen):
    pass
class DrunkenHeroes(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        sm = ScreenManager()
        sm.add_widget(Startbildschirm(name='menu'))
        sm.add_widget(Heroscreen(name='hero'))
        sm.add_widget(Heldenhub(name='herohub'))
        sm.add_widget(Stadt(name='Stadt'))
        sm.add_widget(Hexeshop(name='hexeshop'))
        sm.add_widget(Zauberershop(name='zauberershop'))
        sm.add_widget(Wildnisböse(name='Wildnisböse'))
        sm.add_widget(Wildnisgut(name='Wildnisgut'))
        sm.add_widget(Monstergut(name='Monstergut'))
        sm.add_widget(Monsterböse(name='Monsterböse'))
        return sm


if __name__ == '__main__':
    DrunkenHeroes().run()