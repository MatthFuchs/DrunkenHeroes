import random

from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.uix.screenmanager import ScreenManager, NoTransition, SlideTransition
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.list import *
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout

Window.size = (800, 500)

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
            on_press: root.manager.current = 'hero'

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
            text:'Zauberer'
            on_release:
                root.choose_zauberer()
                root.manager.current='herohub'
        Button:
            text:'Hexe'
            on_release:
                root.choose_hexe()
                root.manager.current='herohub'
        Button:
            text:'Braumeister'
            on_release:
                root.choose_braumeister()
                root.manager.current='herohub'
        Button:
            text:'Zurück'
            on_release:
                root.manager.current='menu'
        Button:
            text:'Zur Stadt'
            on_release:
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
            id:magiershop
            background_normal: ""
            pos_hint:{'center_x': 0.4, 'center_y': 0.28}
            size_hint:0.157,0.25
            background_color: 0,0,0,0.2
            on_release:
                root.magiershop()
        
        Button:
            id:hexeshop
            background_normal: ""
            pos_hint:{'center_x': 0.259, 'center_y': 0.659}
            size_hint:0.15,0.2
            background_color: 0,0,0,0.2
            on_release:
                root.hexeshop()
    
      

""")


# Declare both screens


class Startbildschirm(Screen):
    Helden = ["Lanzelot", "Dunkler Lord", "Prinzessin", "Ritter", "Hrinloser", "Hexe", "Zauberer", "Braumeister"]
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
        if playercount == 1:
            Startbildschirm.Heldena = ["Matze"]
        elif playercount == 2:
            Startbildschirm.Heldena = self.Helden[0:2]
        elif playercount == 3:
            Startbildschirm.Heldena = self.Helden[0:3]
        elif playercount == 4:
            Startbildschirm.Heldena = [self.Helden[0], self.Helden[1], self.Helden[3], self.Helden[4]]
        elif playercount == 5:
            Startbildschirm.Heldena = self.Helden[0:5]
        elif playercount == 6:
            Startbildschirm.Heldena = Startbildschirm.Helden
            Startbildschirm.Heldena.remove("Prinzessin")
            Startbildschirm.Heldena.remove("Braumeister")
        elif playercount == 7:
            Startbildschirm.Heldena.remove("Braumeister")
        elif playercount == 8:
            Startbildschirm.Heldena = self.Helden
        else:
            while playercount > len(self.Helden):
                Startbildschirm.Heldena.append("Bauer")


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
        # Heldenhub.add_widget(self,Label(text="Arsch"))

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

    # wenn der held unterschiedliche leben haben soll dann musse ma da no was einfallen lassen, weil ichs hier lock
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

class TestApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        sm = ScreenManager()
        sm.add_widget(Startbildschirm(name='menu'))
        sm.add_widget(Heroscreen(name='hero'))
        sm.add_widget(Heldenhub(name='herohub'))
        sm.add_widget(Stadt(name='Stadt'))

        return sm


if __name__ == '__main__':
    TestApp().run()