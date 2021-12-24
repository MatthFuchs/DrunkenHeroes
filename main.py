import random
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.list import *
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


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
            font_size:'25sp'
            line_color_normal: 1, 1, 1, 1
            color_mode: 'custom'
            mode: "rectangle"
            rectangle_color_normal: 1, 1, 1, 1
            rectangle_color_focus: 1, 1, 1, 1
            line_color_focus: 1, 1, 1, 1
        Button:
            text: 'Heldenwahl'
            font_size:'50sp'
            on_release: root.Heldenwahl()
        Button:
            text: 'Heldenscreen'
            font_size:'50sp'
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = 'hero'
<Heroscreen>:
    GridLayout:
        rows:2
        cols:2
        Button:
            text: 'Team Lanzelot'
            font_size:'50sp'
            on_release:
                root.choose_lanzelot()
                root.manager.current='herohub'
        Button:
            text: 'Team Dunkler Lord'
            font_size:'50sp'
            on_release:
                root.choose_dunklerlord()
                root.manager.current='herohub'
        
        Button:
            text:'Zurück'
            size_hint_y: .5
            font_size:'50sp'
            on_release:
                root.manager.transition.direction = 'right' 
                root.manager.current='menu'
        Button:
            text:'Zur Stadt'
            size_hint_y:.5
            font_size:'50sp'
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
                root.manager.transition.direction = 'left'
                root.manager.current='zauberershop'
        Button:
            id:hexeshop
            background_normal: ""
            pos_hint:{'center_x': 0.259, 'center_y': 0.659}
            size_hint:0.15,0.2
            background_color: 0,0,0,0
            on_release:
                root.hexeshop()
                root.manager.transition.direction = 'left'
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
        
            id:hexmon1
            text:"Tollwutwolf"
            pos_hint:{'center_x':0.1,'center_y':0.9}
            size_hint:0.1,0.1
            on_release:
                root.monsterwahl(self)   
                
        Button:
            id:hexmon2
            text:"Hydra"
            pos_hint:{'center_x':0.2,'center_y':0.9}
            size_hint:0.1,0.1
            on_release:
                root.monsterwahl(self) 
        Button:
            id:hexmon3
            text:"Kojote"
            pos_hint:{'center_x':0.3,'center_y':0.9}
            size_hint:0.1,0.1
            on_release:
                root.monsterwahl(self) 
        Button:
            id:hexmon4
            text:"Vampir"
            pos_hint:{'center_x':0.1,'center_y':0.8}
            size_hint:0.1,0.1
            on_release:
                root.monsterwahl(self) 
        Button:
            id:hexmon5
            text:"Schlüsselwächter"
            pos_hint:{'center_x':0.2,'center_y':0.8}
            size_hint:0.1,0.1
            on_release:
                root.monsterwahl(self) 
        Button:
            id:hexmon6
            text:"Tiger"
            pos_hint:{'center_x':0.3,'center_y':0.8}
            size_hint:0.1,0.1
            on_release:
                root.monsterwahl(self)  
        Button:
            text:"Zurück"
            background_normal: ""
            pos_hint:{'center_x': 0.1, 'center_y': 0.1}
            size_hint:0.15,0.20
            background_color: 0,0,0,0.5
            on_release:
                root.manager.transition.direction = 'right'
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
            id:zaumon1
            text:"Tollwutschwein"
            pos_hint:{'center_x':0.1,'center_y':0.9}
            size_hint:0.1,0.1
            on_release:
                root.monsterwahl(self)   
                
        Button:
            id:zaumon2
            text:"Drache"
            pos_hint:{'center_x':0.2,'center_y':0.9}
            size_hint:0.1,0.1
            on_release:
                root.monsterwahl(self) 
        Button:
            id:zaumon3
            text:"Esel"
            pos_hint:{'center_x':0.3,'center_y':0.9}
            size_hint:0.1,0.1
            on_release:
                root.monsterwahl(self) 
        Button:
            id:zaumon4
            text:"Zombie"
            pos_hint:{'center_x':0.1,'center_y':0.8}
            size_hint:0.1,0.1
            on_release:
                root.monsterwahl(self) 
        Button:
            id:zaumon5
            text:"Verfluchte Kiste"
            pos_hint:{'center_x':0.2,'center_y':0.8}
            size_hint:0.1,0.1
            on_release:
                root.monsterwahl(self) 
        Button:
            id:zaumon6
            text:"Bär"
            pos_hint:{'center_x':0.3,'center_y':0.8}
            size_hint:0.1,0.1
            on_release:
                root.monsterwahl(self)          
        Button:
            text:"Zurück"
            background_normal: ""
            pos_hint:{'center_x': 0.1, 'center_y': 0.1}
            size_hint:0.15,0.20
            background_color: 0,0,0,0.5
            on_release:
                root.manager.transition.direction = 'right'
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
                root.manager.current='Monsterboese'       
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
    canvas:
        Rectangle:
            source: 'regal.png'
            pos: self.pos
            size: self.size
    FloatLayout:
        MDLabel:
            id:monsterlabel
            text:''
            font_size:'50sp'
            bg_color:0,0,0,0
            pos_hint:{'center_x': 0.5, 'center_y': 0.6}
            size_hint:.5,.5
        Button:
            text:'zurück'
            background_normal: ""
            pos_hint:{'center_x': 0.1, 'center_y': 0.1}
            size_hint:0.15,0.20
            background_color: 0,0,0,0.5
            on_release:
                root.printer()
                root.manager.transition.direction = 'up'
                root.manager.current='Wildnisgut'
        Button:
            id:mongutbesch
            text:'Beschwörem'
            background_normal: ""
            pos_hint:{'center_x': 0.5, 'center_y': 0.5}
            size_hint:0.15,0.20
            background_color: 0,0,0,0.5
            on_release:
                root.monsterbeschwoeren()
        
        Button:
            id:mongutmin
            pos_hint:{'center_x': 0.35, 'center_y': 0.4}
            text:'- 1'
            size_hint:0.1,0.1
            on_release:
                root.lebenmin(self)
            
        Button:
            id:mongutplu
            text:'+ 1'
            pos_hint:{'center_x': 0.55, 'center_y': 0.4}
            size_hint:0.1,0.1
            on_release:
                root.lebenplu(self)
        
        Button:
            id:mongutminmin
            text: '- 5'
            pos_hint:{'center_x': 0.45, 'center_y': 0.4}
            size_hint:0.1,0.1
            on_release:
                root.lebenmin(self)
        
        
        
        Button:
            text:"Gegnerangriff"
            pos_hint:{'center_x': 0.5, 'center_y': 0.75}
            size_hint:0.1,0.1
            on_release:
                root.angriff()

<Monsterboese>:
    canvas:
        Rectangle:
            source: 'regal.png'
            pos: self.pos
            size: self.size
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

        MDLabel:
            id:monsterlabelboese
            text:''
            font_size:'50sp'
            bg_color:0,0,0,0
            pos_hint:{'center_x': 0.5, 'center_y': 0.6}
            size_hint:.5,.5

        Button:
            id:monboebesch
            text:'Beschwörem'
            background_normal: ""
            pos_hint:{'center_x': 0.5, 'center_y': 0.5}
            size_hint:0.15,0.20
            background_color: 0,0,0,0.5
            on_release:
                root.monsterbeschwoeren()
        
        Button:
            id:monboemin
            pos_hint:{'center_x': 0.35, 'center_y': 0.4}
            text:'- 1'
            size_hint:0.1,0.1
            on_release:
                root.lebenmin(self)
            
        Button:
            id:monboeplu
            text:'+ 1'
            pos_hint:{'center_x': 0.55, 'center_y': 0.4}
            size_hint:0.1,0.1
            on_release:
                root.lebenplu(self)
        
        Button:
            id:monboeminmin
            text: '- 5'
            pos_hint:{'center_x': 0.45, 'center_y': 0.4}
            size_hint:0.1,0.1
            on_release:
                root.lebenmin(self)
              
        Button:
            text:"Gegnerangriff"
            pos_hint:{'center_x': 0.5, 'center_y': 0.75}
            size_hint:0.1,0.1
            on_release:
                root.angriff()


""")


class Startbildschirm(Screen):
    namen="Lucy Lukas Ella Konstantin Amy Ben Emely Jonas Finja Elias Amelie Niklas Luise David Frieda Oskar Katharina Philipp Romy Leon Juna Noah Theresa Luis Eva Paul Julia Finn Anna Felix Carla Julian Paulina Maximilian Elisabeth Henry Rosa Tim Mia Karl Maya Friedrich Selma Peter Edda Quirin Flora Liam Berenike Linus Simone Quentin Elena Paul Meike Johannes Susanne Alexander Annika Anton Augusta Aras Alba Asis Wilma Adrian Annegret Arthur Aglaia Adam Aaliyah Arian Annabelle Amos Alma Arik Alicia Ake Anette Altfried Astrid Ari Anisha Andreas Antke Allessandro Abigail Achim Aideen Ben Aini Bela Aida Baldur Aamenah Benedikt Ariane Beat Adriana Bernd Alexandra Bertram Ava Blue Arielle Badi Allissa Batiste Aamu Bastian Arzu Caleb Anouk Caspar Andrea Calvin Bianca Cadmus Blanka Christoph Benita Cedrik Bettina Camern Bamika Carsten Bente Cainan Barbara Cem Berit Carl Bentje Cyranus Birte Curt Brigitte Daniel Christiane Dominik Charlotte Darius Catherina Dario Caroline Dag Caren Diminic Caecilia Damian Celine Diego Coco Dieter Chaya Demian Dalia Dewis Deenah Dirk Daphne Donald Delia Enzo Dari Emil Doerte Erik Djamila Edwin Dominique Eliah Doerte Ethan Dorothee Erwin Emira Eliot Emily Enes Elif Emilio Ellen Ebbo Enna Eberhard Ebba Edgar Eleni Fabrizius Freya Finn Fiona Fabian Franziska Fabio Luzia Finjas Fabienne Franz Fiona Falko Felina Fatih Felicitas Fynn Fabia Flavio Fabiola Fady Fabrizia Fritz Filomae Falko Floris Gabriel Fae Gustav Fanny Guiseppe Fritzi Günter Greta Gerhard Gabrielle Georg Grit Gel Gwen Gerald Gabi Geoffrey Gila Gismund Giorgina Giulio Gisele Godo Heike Henri Hanna Hannes Helena Henry Haima Henrik Heike Hendrik Helen Heiko Isabell Haku Ida Hanno Ilona Hugo Ingrid Henryk Iris Hardy Ira Hagar Iara Hafiz Ivette Haile Irma Hakan Jardis Hasso Juni Harry Juna Hauke Josephine Harun Jella Hayo Jill Idil Jennifer Ian Jakobine Izzy Jessika Ibrahim Julie Igor Jasmin Jack Joana Jules Jaqueline Julian Jonna Jan Jean Jakob Janis Jaap Jodi Jonathan Jen Jannik Justyna Jona Jutta Jannis Kathleen Joel Kayra Jonte Klara Jarin Kiara Jörn Kathrin Jari Catrin Jannik Kiki Jukka Judith Samo Celia Jaakov Kaaria Jeremy Kerstin Jarne Kim Kilian Kader Kai Kaisa Kylan Liv Kristian Livia Kasper Louisa Kadmos Lucy Klaus Lina Kaarle Lena Kevin Leonie Kadir Lea Konrad Leni Lukas Lotta Leon Laura Leopold Lara Luca Lia Linas Lisa Roland Luna Leo Linda Lennard Laureen Luke Liv Lenny Liz Lasse Mona Lion Mareen Luca Mathilda Lutz Marlene Levi Marianne Matthias Mara Moritz Mina Meteo Magdalena Mats Miriam Matthis Marianne Mattes Martje Milo Maeve Mika Mae Maxim Nadja Marlon Nadine Mark Nele Matti Nora Martin Nina Morris Nada Miran Nadeshda Miro Nancy Niklas Nova Nika Nika Niko Nike Nabil Oda Noel Odilie Nils Okka Nick Olea Neo Odett Nadeem Olivia Namo Odilia Nepomuk Oana Oscar Pia Ole Paula Oliver Phlomena Olivier Paloma Onur Paris Owen Paola Obbo Poppy Idil Panja Otto Pardis Oswald Quirine Paul Quinta Phil Qara Patrick Ria Paavo Rita Pamir Raina Pascal Rabea Peter Radost Quinn Rabi Quazim Ronina Kasimir Rae René Radia Riko Svea Robin Smila Raphael Sofia Rudi Sonja Remigius Sophie Richard Stella Radi Sarah Rainer Silvie Rasmus Silke Ruben Sila Samuel Siri Stefan Sarah Sascha Saara Serkan Svenja Marco Sabine Manuel Sandra Tom Tiffanie Tim Thea Theo Tilda Theodor Tardis Thilo Tamina Till Tamy Timo Trudi Tino Tea Tiny Tima Taylor Tabia Titus Tassja Tristan Tilla Tizian Tabita Todd Tahua Thomas Uli Taavi Ulrike Tillmann Ute Uwe Uda Udo Ulla Ugor Ulrika Ulrich Ulva Uli Ulvi Ulas Uma Ulf Violeta Volker Victoria Vinzent Vanessa Valentin Valentine Vitus Valeska Volker Wandy Valentin Waris Vidu Walli Valerio Waltraud Wilhelm Wanda William Xenia Will Xani Walter Xanthe Wanja Yvonne Wadi Yu Walid Yla Xaver Zoe Yannis Zilla Yannik Zuri Yoshi Zamira Yunus"
    global namenliste
    namenliste=namen.split(" ")
    Helden = ["Lanzelot", "Dunkler Lord", "Prinzessin "+random.choice(namenliste), "Ritter "+random.choice(namenliste), "Hrinloser "+random.choice(namenliste)]
    global Heldena
    Heldena = []
    users = StringProperty()
    heldeninit = True

    def Heldenwahl(self):
        if self.heldeninit == True:
            Startbildschirm.Heldenliste(self)
            self.heldeninit = False
            global heldenlistefertig
            heldenlistefertig = Startbildschirm.Heldena[::]
        try:
            Heldenwahl = random.choice(Startbildschirm.Heldena)
            self.popupheld = MDDialog(title="[b][size=30sp][color=ffffff]Held[/color][/size][/b]",
                                      text="[size=25sp]" + Heldenwahl + "[/size]", auto_dismiss=False, buttons=[
                    MDFlatButton(text='Okay!', on_release=lambda _: self.popupheld.dismiss(), font_size=30)])
            self.popupheld.open()
            #print(Heldenwahl)
            Startbildschirm.Heldena.remove(Heldenwahl)
        except:
            self.popupheld = MDDialog(title="[b][size=30sp][color=ffffff]Held[/color][/size][/b]",
                                      text="[size=25sp] Keine Helden mehr! [/size]", auto_dismiss=False, buttons=[
                    MDFlatButton(text='Okay!', on_release=lambda _: self.popupheld.dismiss(), font_size=30)])
            self.popupheld.open()
            print("Keine Helden mehr")

    def Heldenliste(self):
        try:
            global playercount
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
            Startbildschirm.Heldena.append("Prinzessin "+random.choice(namenliste))
        Startbildschirm.lencheck(self)

    def lencheck(self):
        playercount = int(self.users)
        while playercount > int(len(self.Heldena) + 1):
            Startbildschirm.Heldena.append("Ritter "+random.choice(namenliste))
            Startbildschirm.Heldena.append("Hirnloser "+ random.choice(namenliste))




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
        #print("Held: " + self.held)

    def pre(self):
        #print(Heldenhub.held)
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
    monsterpool = ["Tollwutwolf", "Hydra", "Kojote", "Vampir", "Schlüsselwächter", "Tiger"]
    buttonmonster=["hexmon1","hexmon2","hexmon3","hexmon4","hexmon5","hexmon6"]
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

    kopfgeldverkauft = bool

    def monsterwahl(self, instance):
        for buttons in self.buttonmonster:
            if Hexeshop.kopfgeldverkauft != True:
                if instance.text == self.monsterpool[0]:
                    instance.text = "Verkauft!"
                    Hexeshop.kopfgeldverkauft = True
                    Monsterboese.monsterchoose(self, self.monsterpool[0])
                    break
                elif instance.text == self.monsterpool[1]:
                    instance.text = "Verkauft!"
                    Hexeshop.kopfgeldverkauft = True
                    Monsterboese.monsterchoose(self, self.monsterpool[1])
                    break
                elif instance.text == self.monsterpool[2]:
                    instance.text = "Verkauft!"
                    Hexeshop.kopfgeldverkauft = True
                    Monsterboese.monsterchoose(self, self.monsterpool[2])
                    break
                elif instance.text == self.monsterpool[3]:
                    instance.text = "Verkauft!"
                    Hexeshop.kopfgeldverkauft = True
                    Monsterboese.monsterchoose(self, self.monsterpool[3])
                    break
                elif instance.text == self.monsterpool[4]:
                    instance.text = "Verkauft!"
                    Hexeshop.kopfgeldverkauft = True
                    Monsterboese.monsterchoose(self, self.monsterpool[4])
                    break
                elif instance.text == self.monsterpool[5]:
                    instance.text = "Verkauft!"
                    Hexeshop.kopfgeldverkauft = True
                    Monsterboese.monsterchoose(self, self.monsterpool[5])
                    break
                else:
                    print("nicht nochmal auf verkauft drücken du penner")
            else:
                print("Es ist bereits ein Kopfgeld aktiv")


class Zauberershop(Screen):

    monsterpool=["Tollwutschwein","Drache","Esel","Zombie","Verfluchte Kiste","Bär"]
    buttonmonster=["zaumon1","zaumon2","zaumon3","zaumon4","zaumon5","zaumon6"]
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
                        pass

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
    kopfgeldverkauft=bool
    def monsterwahl(self,instance):
        for buttons in self.buttonmonster:
            if Zauberershop.kopfgeldverkauft!=True:
                if instance.text==self.monsterpool[0]:
                    instance.text="Verkauft!"
                    Zauberershop.kopfgeldverkauft=True
                    Monstergut.monsterchoose(self,self.monsterpool[0])
                    break
                elif instance.text==self.monsterpool[1]:
                    instance.text = "Verkauft!"
                    Zauberershop.kopfgeldverkauft = True
                    Monstergut.monsterchoose(self,self.monsterpool[1])
                    break
                elif instance.text==self.monsterpool[2]:
                    instance.text = "Verkauft!"
                    Zauberershop.kopfgeldverkauft = True
                    Monstergut.monsterchoose(self,self.monsterpool[2])
                    break
                elif instance.text==self.monsterpool[3]:
                    instance.text = "Verkauft!"
                    Zauberershop.kopfgeldverkauft = True
                    Monstergut.monsterchoose(self,self.monsterpool[3])
                    break
                elif instance.text==self.monsterpool[4]:
                    instance.text = "Verkauft!"
                    Zauberershop.kopfgeldverkauft = True
                    Monstergut.monsterchoose(self,self.monsterpool[4])
                    break
                elif instance.text==self.monsterpool[5]:
                    instance.text = "Verkauft!"
                    Zauberershop.kopfgeldverkauft = True
                    Monstergut.monsterchoose(self,self.monsterpool[5])
                    break
                else:
                    print("nicht nochmal auf verkauft drücken du penner")
            else:
                print("Es ist bereits ein Kopfgeld aktiv")

class Wildnisgut(Screen):
    pass


class Wildnisböse(Screen):
    pass


class Monstergut(Screen):

    Monstername="Nichts"
    Monsterleben=int
    goldwert=int
    Monsterschaden=int
    Monsteraktiv=bool
    Monsterschaden=int


    def monsterchoose(self,monster):
        if monster=="Tollwutschwein":
            print(monster)
            Monstergut.Monstername=monster
            Monstergut.Monsterleben=100
            Monstergut.Monsterschaden = 2
            Monstergut.goldwert=10
        elif monster=="Drache":
            print(monster)
            Monstergut.Monsterleben=500
            Monstergut.Monsterschaden = 6
            Monstergut.goldwert = 50
            Monstergut.Monstername = monster
        elif monster == "Esel":
            print(monster)
            Monstergut.Monstername = monster
            Monstergut.Monsterleben=50
            Monstergut.Monsterschaden=1
            Monstergut.goldwert = 5
        elif monster == "Zombie":
            print(monster)
            Monstergut.Monsterleben=150
            Monstergut.Monstername = monster
            Monstergut.Monsterschaden = 3
            Monstergut.goldwert = 15
        elif monster == "Verfluchte Kiste":
            print(monster)
            Monstergut.Monstername = monster
            Monstergut.Monsterleben=300
            Monstergut.Monsterschaden = 5
            Monstergut.goldwert = 30
        elif monster == "Bär":
            print(monster)
            Monstergut.Monsterleben=200
            Monstergut.Monsterschaden = 4
            Monstergut.goldwert = 20
            Monstergut.Monstername = monster
        else:
            print("Falsches Monster: "+monster)

    def looten(self):
        self.lootpop = MDDialog(
            title="[b][size=30sp][color=ffffff]" + Monstergut.Monstername + " ist besiegt! [/color][/size][/b]",
            text="[size=25sp]Ihr bekommt " + str(Monstergut.goldwert) + " Gold [/size]", auto_dismiss=False,
            buttons=[
                MDFlatButton(text='Okay!', on_release=lambda _: self.lootpop.dismiss(), font_size=30)])
        self.lootpop.open()

    def angriff(self):
        if Monstergut.Monsteraktiv==True:
            self.popupangriff = MDDialog(title="[b][size=30sp][color=ffffff]"+Monstergut.Monstername+" greift an! [/color][/size][/b]",
                                      text="[size=25sp]Alle trinken "+str(Monstergut.Monsterschaden)+" Schluck[/size]", auto_dismiss=False, buttons=[
                    MDFlatButton(text='Okay!', on_release=lambda _: self.popupangriff.dismiss(), font_size=30)])
            self.popupangriff.open()


    def lebenmin(self,instance):
        if Monstergut.Monsteraktiv==True:
            if instance.text=="- 5":
                #print(Monstergut.Monsterleben)
                Monstergut.Monsterleben=Monstergut.Monsterleben - 5
                self.ids["monsterlabel"].text = Monstergut.Monstername + "\nLeben: " + str(Monstergut.Monsterleben)
            else:
                #print(Monstergut.Monsterleben)
                Monstergut.Monsterleben = Monstergut.Monsterleben - 1
                self.ids["monsterlabel"].text = Monstergut.Monstername + "\nLeben: " + str(Monstergut.Monsterleben)
        if Monstergut.Monsterleben<=0 and Monstergut.Monsteraktiv == True:
            Zauberershop.kopfgeldverkauft=False
            Monstergut.Monsteraktiv=False
            self.ids['mongutbesch'].background_color=[0,0,0,1]
            self.ids['mongutbesch'].text="Beschwören"
            self.ids["monsterlabel"].color=[0,0,0,0]
            self.ids["monsterlabel"].text=" "
            Monstergut.looten(self)



    def lebenplu(self,instance):
        if Monstergut.Monsteraktiv == True:
            #print(Monstergut.Monsterleben)
            Monstergut.Monsterleben = Monstergut.Monsterleben + 1
            self.ids["monsterlabel"].text = Monstergut.Monstername + "\nLeben: " + str(Monstergut.Monsterleben)

    def monsterbeschwoeren(self):
        if Zauberershop.kopfgeldverkauft==True:
            Monstergut.Monsteraktiv=True
            self.ids['mongutbesch'].background_color=[0,0,0,0]
            self.ids['mongutbesch'].text=" "
            self.ids["monsterlabel"].color=[0,0,0,1]
            self.ids["monsterlabel"].text=Monstergut.Monstername+"\nLeben: "+str(Monstergut.Monsterleben)

    def on_pre_enter(self, *args):
        if Monstergut.Monsteraktiv==True:
            self.ids['mongutbesch'].background_color = [0, 0, 0, 0]
            self.ids['mongutbesch'].text = " "
            self.ids["monsterlabel"].color = [0, 0, 0, 1]
            self.ids["monsterlabel"].text = Monstergut.Monstername + "\nLeben: " + str(Monstergut.Monsterleben)
        spieler = len(heldenlistefertig)

        ############Monster sollen vom Magier oder der Hexe gekauft werden können und machen dann dementsprechend Damage########---> Haben höheres Leben je nach stufe und sind dann auch mehr Loot wert!
        print("Spieler: "+str(spieler))

    def printer(self):
        print("testttettrjfnfkeabf")
        for i in heldenlistefertig:
            print(i)


class Monsterboese(Screen):

    Monstername="Nichts"
    Monsterleben=int
    goldwert=int
    Monsterschaden=int
    Monsteraktiv=bool
    Monsterschaden=int


    def monsterchoose(self,monster):
        if monster=="Tollwutwolf":
            print(monster)
            Monsterboese.Monstername=monster
            Monsterboese.Monsterleben=100
            Monsterboese.Monsterschaden = 2
            Monsterboese.goldwert=10
        elif monster=="Hydra":
            print(monster)
            Monsterboese.Monsterleben=500
            Monsterboese.Monsterschaden = 6
            Monsterboese.goldwert = 50
            Monsterboese.Monstername = monster
        elif monster == "Kojote":
            print(monster)
            Monsterboese.Monstername = monster
            Monsterboese.Monsterleben=50
            Monsterboese.Monsterschaden=1
            Monsterboese.goldwert = 5
        elif monster == "Vampir":
            print(monster)
            Monsterboese.Monsterleben=150
            Monsterboese.Monstername = monster
            Monsterboese.Monsterschaden = 3
            Monsterboese.goldwert = 15
        elif monster == "Schlüsselwächter":
            print(monster)
            Monsterboese.Monstername = monster
            Monsterboese.Monsterleben=300
            Monsterboese.Monsterschaden = 5
            Monsterboese.goldwert = 30
        elif monster == "Tiger":
            print(monster)
            Monsterboese.Monsterleben=200
            Monsterboese.Monsterschaden = 4
            Monsterboese.goldwert = 20
            Monsterboese.Monstername = monster
        else:
            print("Falsches Monster: "+monster)

    def looten(self):
        self.lootpop = MDDialog(
            title="[b][size=30sp][color=ffffff]" + Monsterboese.Monstername + " ist besiegt! [/color][/size][/b]",
            text="[size=25sp]Ihr bekommt " + str(Monsterboese.goldwert) + " Gold [/size]", auto_dismiss=False,
            buttons=[
                MDFlatButton(text='Okay!', on_release=lambda _: self.lootpop.dismiss(), font_size=30)])
        self.lootpop.open()

    def angriff(self):
        if Monsterboese.Monsteraktiv==True:
            self.popupangriff = MDDialog(title="[b][size=30sp][color=ffffff]"+Monsterboese.Monstername+" greift an! [/color][/size][/b]",
                                      text="[size=25sp]Alle trinken "+str(Monsterboese.Monsterschaden)+" Schluck[/size]", auto_dismiss=False, buttons=[
                    MDFlatButton(text='Okay!', on_release=lambda _: self.popupangriff.dismiss(), font_size=30)])
            self.popupangriff.open()


    def lebenmin(self,instance):
        if Monsterboese.Monsteraktiv==True:
            if instance.text=="- 5":
                #print(Monsterboese.Monsterleben)
                Monsterboese.Monsterleben=Monsterboese.Monsterleben - 5
                self.ids["monsterlabelboese"].text = Monsterboese.Monstername + "\nLeben: " + str(Monsterboese.Monsterleben)
            else:
                #print(Monsterboese.Monsterleben)
                Monsterboese.Monsterleben = Monsterboese.Monsterleben - 1
                self.ids["monsterlabelboese"].text = Monsterboese.Monstername + "\nLeben: " + str(Monsterboese.Monsterleben)
        if Monsterboese.Monsterleben <=0 and Monsterboese.Monsteraktiv == True:
            Hexeshop.kopfgeldverkauft=False
            Monsterboese.Monsteraktiv=False
            self.ids['monboebesch'].background_color=[0,0,0,1]
            self.ids['monboebesch'].text="Beschwören"
            self.ids["monsterlabelboese"].color=[0,0,0,0]
            self.ids["monsterlabelboese"].text=" "
            Monsterboese.looten(self)



    def lebenplu(self,instance):
        if Monsterboese.Monsteraktiv == True:
            #print(Monsterboese.Monsterleben)
            Monsterboese.Monsterleben = Monsterboese.Monsterleben + 1
            self.ids["monsterlabelboese"].text = Monsterboese.Monstername + "\nLeben: " + str(Monsterboese.Monsterleben)

    def monsterbeschwoeren(self):
        if Hexeshop.kopfgeldverkauft==True:
            Monsterboese.Monsteraktiv=True
            self.ids['monboebesch'].background_color=[0,0,0,0]
            self.ids['monboebesch'].text=" "
            self.ids["monsterlabelboese"].color=[0,0,0,1]
            self.ids["monsterlabelboese"].text=Monsterboese.Monstername+"\nLeben: "+str(Monsterboese.Monsterleben)

    def on_pre_enter(self, *args):
        if Monsterboese.Monsteraktiv==True:
            self.ids['monboebesch'].background_color = [0, 0, 0, 0]
            self.ids['monboebesch'].text = " "
            self.ids["monsterlabelboese"].color = [0, 0, 0, 1]
            self.ids["monsterlabelboese"].text = Monsterboese.Monstername + "\nLeben: " + str(Monsterboese.Monsterleben)
        spieler = len(heldenlistefertig)

        ############Monster sollen vom Magier oder der Hexe gekauft werden können und machen dann dementsprechend Damage########---> Haben höheres Leben je nach stufe und sind dann auch mehr Loot wert!
        print("Spieler: "+str(spieler))

    def printer(self):
        print("testttettrjfnfkeabf")
        for i in heldenlistefertig:
            print(i)



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
        sm.add_widget(Monsterboese(name='Monsterboese'))
        return sm


if __name__ == '__main__':
    DrunkenHeroes().run()


    """
    Spieler bekommen Chars zugewisen. Mit denen entscheidet sich dann das Team und der name mit dem se angesprochen werden
    
    WAFFENSCHMIED MUSS NOCH GEMACHT WERDEN
    
    TEAMCAMP MACHEN wo dann Team Lanzelot oder Team Dunkler Lord hocken. Da kann ma dann Leben, Gold und so anzeigen lassen
    
    Teamleiter muss dann am anfang enscheiden was er kauft: Fluch, billige challenge, waffe oder besseres kopfgeld.
    
    Dann macht ma Monster kaputt vom Kopfgeld, krigt geld und kann mehr sachen kaufen. Man kann jedes Monster unendlich oft machen --> so lange status verkauft bis gekloppt
    
    Man gewinnt wenn man x gold hat oder das gegnerteam durch die challenges kaputt ist (20 Leben, große challenge zieht 3 leben ab, kleine 1)
    
    Erklärungsseite machen wo kleines Tutorial steht
    
    STÄRKERE WAFFEN SIND DANN DIE BESSEREN WÜRFEL ____ ALTER IS DES A GEILE IDEE
    
    Boss darf angreifen, wenn der Spieler an 1er würfelt oder beim 6er würfel an 1 oder 2 er usw ______>>>>>>> GEILE IDEEEEEEEEEEEEEEEEEEE
    
    Auf einem Hanfy wird gespielt, auf dem anderen Finanzen verwaltet!
    
    
    ABLAGE:
    
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
    
    
    """