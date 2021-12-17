
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
            text:'Bauer'
            on_release:
                root.choose_bauer()
                root.manager.current='herohub'
    
      
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
                root.manager.current='hero'
        MDLabel:
            id:heldbild
            text:'Hier ist ein schönes Bild'
            size_hint_y:0.35
            
        GridLayout:
            size_hint_y:0.25
            rows:1
            cols:2
            MDLabel:
                text:'Leben: 30'
            GridLayout:
                rows:1
                cols:2
                Button:
                    text:'+'
                Button:
                    text:'-'
        GridLayout:
            size_hint_y: 0.25
            rows:1
            cols:2
            Button:
                text: 'Skill 1'
            Button:
                text: 'Skill 2'
            
""")

# Declare both screens



class Startbildschirm(Screen):
    Helden=["Lanzelot","Dunkler Lord","Prinzessin","Ritter","Hrinloser","Hexe","Zauberer","Braumeister"]
    Heldena = []
    users = StringProperty()
    heldeninit=True

    def Heldenwahl(self):
        if self.heldeninit == True:
            Startbildschirm.Heldenliste(self)
            self.heldeninit = False
        try:
            Heldenwahl = random.choice(Startbildschirm.Heldena)
            self.popupheld = MDDialog(title="[b][size=30sp][color=ffffff]Held[/color][/size][/b]",
                                   text="[size=25sp]"+Heldenwahl+"[/size]", auto_dismiss=False, buttons=[
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
            playercount=int(self.users)
        except:
            playercount=1
        if playercount == 1:
            Startbildschirm.Heldena=["Matze"]
        elif playercount == 2:
            Startbildschirm.Heldena=self.Helden[0:2]
        elif playercount == 3:
            Startbildschirm.Heldena= self.Helden[0:3]
        elif playercount == 4:
            Startbildschirm.Heldena = [self.Helden[0],self.Helden[1],self.Helden[3],self.Helden[4]]
        elif playercount == 5:
            Startbildschirm.Heldena = self.Helden[0:5]
        elif playercount == 6:
            Startbildschirm.Heldena=Startbildschirm.Helden
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
    charakter=''
    def choose_bauer(self):
        self.charakter="Bauer"
        Heldenhub.choosehelden(self,self.charakter)
    def choose_lanzelot(self):
        self.charakter='Lanzelot'
        Heldenhub.choosehelden(self,self.charakter)
    def choose_dunklerlord(self):
        self.charakter='Dunkler Lord'
        Heldenhub.choosehelden(self,self.charakter)
    def choose_ritter(self):
        self.charakter='Ritter'
        Heldenhub.choosehelden(self,self.charakter)
    def choose_hirnloser(self):
        self.charakter='Hirnloser'
        Heldenhub.choosehelden(self,self.charakter)
    def choose_prinzessin(self):
        self.charakter='Prinzessin'
        Heldenhub.choosehelden(self,self.charakter)
    def choose_hexe(self):
        self.charakter='Hexe'
        Heldenhub.choosehelden(self,self.charakter)
    def choose_zauberer(self):
        self.charakter='Zauberer'
        Heldenhub.choosehelden(self,self.charakter)
    def choose_braumeister(self):
        self.charakter='Braumeister'
        Heldenhub.choosehelden(self,self.charakter)

class Heldenhub(Screen):
    held=''
    def choosehelden(self,auswahl):
        self.held=auswahl
        Heldenhub.held=auswahl
        print("Held: "+self.held)
        #Heldenhub.add_widget(self,Label(text="Arsch"))
    def pre(self):
        print(Heldenhub.held)
        self.ids['heldenname'].text=Heldenhub.held



class TestApp(MDApp):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(Startbildschirm(name='menu'))
        sm.add_widget(Heroscreen(name='hero'))
        sm.add_widget(Heldenhub(name='herohub'))

        return sm

if __name__ == '__main__':
    TestApp().run()