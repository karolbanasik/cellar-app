import remi.gui as front_provider
from remi import start, App

class Presentation(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self):
        container = front_provider.VBox(width=120, height=100)
        self.lbl = front_provider.Label('Hello world!')
        self.bt = front_provider.Button('Press me!')

        self.bt.onclick.do(self.on_button_pressed)

        container.append(self.lbl)
        container.append(self.bt)

        # return of the root widget
        return container

    def on_button_pressed(self, widget):
        self.lbl.set_text('Button pressed!')
        self.bt.set_text('Hi!')


start(Presentation, address='127.0.0.1', port=8081, multiple_instance=False, enable_file_cache=True, update_interval=0.1, start_browser=True)
