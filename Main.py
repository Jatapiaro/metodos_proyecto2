# coding=utf-8
from Algoritmos.MM1 import mm1
from Algoritmos.MMS import mms
from Algoritmos.MMSK import mmsk
from Algoritmos.MG1 import mg1
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.app import App


Builder.load_file('Kivy_Files/InitialScreen.kv')
Builder.load_file('Kivy_Files/ErrorPopup.kv')

class ErrorPopup(Popup):
    errores = []
    def on_open(self):
        for e in self.errores:
            self.ids['errord'].add_widget(Label(text=e))

class InitialScreen(Screen):

    #def centros(self):
    #    screen_manager.transition.duration = 1.5
    #    screen_manager.transition.direction = "left"
        #screen_manager.current = 'centros_screen'

    def close_app(self):
        App.get_running_app().stop()


screen_manager = ScreenManager()
screen_manager.add_widget(InitialScreen(name="initial_screen"))

class App(App):
    def build(self):
        return screen_manager

sample = App()
sample.run()