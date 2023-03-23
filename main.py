from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDTopAppBar
from kivy.uix.image import Image
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFillRoundFlatButton



class Number_ConverterApp(MDApp):
    def flip(self):
        if self.state == 0:
            self.state = 1
            self.toolbar.title = "Decimal to Binary"
            self.input.hint_text = "Enter a Decimal Number"
            self.convertor.text = ""
            self.label.text = ""

        else:
            self.state = 0
            self.toolbar.title = "Binary to Decimal"
            self.input.hint_text = "Enter a Binary Number"
            self.convertor.text = ""
            self.label.text = ""

    def convert(self, args):
        try:
            if "." not in self.input.text:
                if self.state == 0:
                    val = int(self.input.text, 2)
                    self.convertor.text = str(val)
                    self.label.text = "Decimal Number"
                else:
                    val = bin(int(self.input.text))[2:]

                    self.label.text = "Binary Number"
                    self.convertor.text = val
            else:
                whole, fract = self.input.text.split(".")

                if self.state == 0:
                    whole = int(whole, 2)
                    floating = 0
                    for idx, digit in enumerate(fract):
                        floating += int(digit) * 2 ** (-(idx + 1))
                    self.label.text = "Decimal Number"
                    self.convertor.text = str(whole + floating)


                else:
                    decimal_places = 10
                    whole = bin(int(whole))[2:]
                    fract = float("0." + fract)
                    floating = []
                    for i in range(decimal_places):
                        if fract * 2 < 1:
                            floating.append("0")
                            fract *= 2

                        elif fract * 2 > 1:
                            floating.append("1")
                            fract = fract * 2 - 1
                        elif fract * 2 == 1.0:
                            floating.append("1")
                            break
                    self.label.text = "Binary Number"
                    self.convertor.text = whole + "." + "".join(floating)

        except ValueError:
            self.convertor.text=""
            if self.state == 0:
                self.label.text="Please enter a valid binary number"
            else:
                self.label.text = "Please enter a valid Decimal number"



    def build(self):
        self.state = 0
        self.theme_cls.primary_palette = "BlueGray"
        self.icon = "mainlogo.jpg"

        screen = MDScreen()

        self.toolbar = MDTopAppBar(title="Binary to Decimal",
                                   pos_hint = {"top": 1},
                                   right_action_items = [["rotate-3d-variant", lambda x: self.flip()]]
                                   )

        screen.add_widget(self.toolbar)


        screen.add_widget(Image(source="logo.png", pos_hint={'center_x': 0.53, 'center_y': 0.8}))

        self.input = MDTextField(hint_text="Enter a Binary Number",
                                 halign='center',
                                 size_hint=(0.8, 1),
                                 pos_hint={'center_x': 0.5, 'center_y': 0.6},
                                 icon_right="android",
                                 font_size=88)

        screen.add_widget(self.input)

        self.label = MDLabel(
            halign='center',
            pos_hint={'center_x': 0.5, 'center_y': 0.45},
            theme_text_color="Secondary",font_style="H6"
        )

        self.convertor = MDLabel(
            halign='center',
            pos_hint={'center_x': 0.5, 'center_y': 0.38},
            theme_text_color="Primary",
            font_style="H4"
        )

        self.footer = MDLabel(text='Made by Niranjan Patil',
            halign='center',
            pos_hint={'center_x': 0.5, 'center_y': 0.05},
            theme_text_color="Secondary", font_style="Subtitle1"
        )

        screen.add_widget(self.label)
        screen.add_widget(self.convertor)
        screen.add_widget(self.footer)

        screen.add_widget(MDFillRoundFlatButton(
            text="CONVERT",
            font_size=65,
            pos_hint={'center_x': 0.5, 'center_y': 0.25},
            on_press=self.convert
        ))



        return screen


if __name__ == '__main__':
    Number_ConverterApp().run()
