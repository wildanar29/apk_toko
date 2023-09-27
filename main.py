from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import StringProperty
# import paho.mqtt.client as paho
from datetime import datetime

# broker = "broker.hivemq.com"
# port = 1883
pesan = ""
date = datetime.now()
current_date = date.strftime("%D")
# def on_message(client, userdata, message):
#     msg = str(message.payload.decode("utf-8"))
#     t = str(message.topic)
#     if (t == "toko_solusa"):
#         global pesan
#         pesan = str(msg)
#         print(pesan)

class MyApp(App):
    text_to_change = StringProperty("Initial Text")

    def change_text(self):
        self.text_to_change = pesan

    def build(self):
        # Create the root widget, which will be a BoxLayout
        root = BoxLayout(orientation='vertical')

        # Create the label widget
        label = Label(text=f'Omset {current_date}',
                      font_size='24sp',  # Set the font size to 24
                      color=(0, 1, 0, 1))  # Set the text color to green (RGBA format)

        # Add the label widget to the root widget
        root.add_widget(label)

        # Create the text label with the StringProperty value
        self.text_label = Label(text=self.text_to_change,
                                font_size='20sp',
                                halign='center')  # Center-align the text
        root.add_widget(self.text_label)

        # Create a button to change the text dynamically
        button = Button(text="Update",
                        size_hint=(None, None),
                        size=(150, 50),
                        pos_hint={'center_x': 0.5})
        button.bind(on_press=lambda instance: self.change_text())
        root.add_widget(button)

        return root

    def on_text_to_change(self, instance, value):
        self.text_label.text = value

if __name__ == '__main__':
    # client= paho.Client("GUI")
    # client.on_message=on_message
    # client.connect(broker,port)#connect
    # client.loop_start()
    # client.subscribe('toko_solusa')
    MyApp().run()
