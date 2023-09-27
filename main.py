# Import library Kivy
import kivy
from kivy.app import App
from kivy.uix.button import Button

# # Inisialisasi Kivy (opsional)
# kivy.require('1.11.1')

# Aplikasi Kivy yang sederhana
class SimpleKivyApp(App):
    
    # Fungsi yang akan dipanggil saat aplikasi dimulai
    def build(self):
        # Membuat tombol
        button = Button(text='Klik Saya!', size_hint=(.5, .5), pos=(200, 200))
        # Menambahkan fungsi yang akan dipanggil saat tombol diklik
        button.bind(on_press=self.on_button_click)
        # Mengembalikan tampilan utama
        return button

    # Fungsi yang akan dipanggil saat tombol diklik
    def on_button_click(self, instance):
        print("Tombol diklik!")

# Jalankan aplikasi Kivy
if __name__ == '__main__':
    SimpleKivyApp().run()
