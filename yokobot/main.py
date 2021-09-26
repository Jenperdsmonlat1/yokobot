from modules.chatbot import data
from modules.chatbot import words
from modules.chatbot import classes
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from modules.functions_chatbot import pred_class
from modules.functions_chatbot import get_response


class Main(App):

    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        self.label = Label(
            text="Écrivez quelque chose et le bot vous répondra",
            font_size=20,
            color="#FF7C7C",
        )

        self.entry = TextInput(
            multiline=False,
            background_color="white",
            padding_y=(20, 20),
            size_hint=(0.2, 0.5)
        )

        self.bouton_valider = Button(
            text="Envoyer",
            size_hint=(1, 0.5),
            bold=True,
            background_color="#FF7C7C",
            background_down="#FF9E7C"
        )

        self.bouton_valider.bind(on_press=self.predict)

        self.window.add_widget(self.label)
        self.window.add_widget(self.entry)
        self.window.add_widget(self.bouton_valider)

        return self.window

    def predict(self, instance):
        self.message = self.entry.text
        self.intents = pred_class(self.message, words, classes)
        self.result = get_response(self.intents, data)
        self.label.text = "Yoko: " + self.result


if __name__ == "__main__":
    Main().run()
