import random
import webbrowser
from modules.chatbot import data
from modules.chatbot import words
from modules.chatbot import classes
from modules.functions_chatbot import pred_class
from modules.functions_chatbot import get_response
from kivymd.app import MDApp
from kivy.lang import Builder


class MainApp(MDApp):

    def build(self):

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = self.generate_color()

        self.interface = Builder.load_file("stylesheets/interface.kv")
        return self.interface

    def generate_color(self):

        self.list_color = ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal',
                           'Green', 'LightGreen',
                           'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']
        self.color_choice = random.choice(self.list_color)
        return self.color_choice

    def open_browser(self):

        self.site = "https://github.com/jesuisroot123"
        webbrowser.open(self.site)

    def predict(self):

        self.message = self.root.ids.message.text
        self.label = self.root.ids.labele
        self.intents = pred_class(self.message, words, classes)
        self.resultat = get_response(self.intents, data)
        self.label.text = "Yoko: " + self.resultat

if __name__ == "__main__":
    MainApp().run()
