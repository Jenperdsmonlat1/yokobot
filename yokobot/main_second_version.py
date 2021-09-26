import random
import webbrowser
from modules.chatbot import data
from modules.chatbot import words
from modules.chatbot import classes
from modules.functions_chatbot import pred_class
from modules.functions_chatbot import get_response
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFloatingActionButton


class MainApp(MDApp):

    def build(self):

        self.screen = MDScreen()

        self.list_color = ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen',
        'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']

        self.color_choice = random.choice(self.list_color)
        self.theme_cls.primary_palette = self.color_choice

        self.toolbar = MDToolbar(title="YokoBot")
        self.toolbar.pos_hint = {'top': 1}
        self.toolbar.right_action_items = [
            ['github', lambda x: self.open_browser()]]
        self.screen.add_widget(self.toolbar)

        self.textfield = MDTextField(
            halign="center",
            size_hint=(0.8, 0.1),
            pos_hint={"center_x": 0.42, "center_y": 0.05},
            font_size=14,
            mode="fill",
            hint_text="Votre message à Yoko"
        )

        self.label = MDLabel(
            text="Discutez avec notre intelligence artificielle.",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            theme_text_color="Secondary"
        )

        self.bouton_valider = MDFloatingActionButton(
            text='Valider',
            icon='send',
            pos_hint={"center_x": 0.92, "center_y": 0.055},
            elevation=10
        )
        self.bouton_valider.bind(on_press=self.predict)

        self.screen.add_widget(self.label)
        self.screen.add_widget(self.textfield)
        self.screen.add_widget(self.bouton_valider)

        return self.screen

    def open_browser(self):

        self.site = "https://github.com/jesuisroot123"
        webbrowser.open(self.site)

    def predict(self, instance):
        self.message = self.textfield.text
        self.intents = pred_class(self.message, words, classes)
        self.resultat = get_response(self.intents, data)
        self.label.theme_text_color = "Primary"
        self.label.text = "Yoko: " + self.resultat


if __name__ == "__main__":
    MainApp().run()