#qpy:kivy

from kivy.app import App
from kivy.uix.label import Label


class OmcHubApp(App):

    def build(self):
        return Label(text='Hello world')


if __name__ == '__main__':
    OmcHubApp().run()
