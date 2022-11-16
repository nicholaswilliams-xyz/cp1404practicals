"""
Convert miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Nicholas Williams'

MILES_TO_KM_SCALE = 1.609


class MilesKilometreApp(App):
    """MilesKilometreApp is a Kivy App for converting miles to kilometres"""

    def build(self):
        """Build the Kivy app from the kv file"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def increment(self, value):
        """ Increment by "value" """
        miles = self.root.ids.input_number.text
        try:
            miles = float(miles) + value
            if miles < 0:
                # Disable negative distances
                miles = 0
            self.root.ids.input_number.text = str(miles)
        except ValueError:
            pass

    def convert(self):
        """Handle the conversion of miles to kilometres"""
        miles = self.root.ids.input_number.text
        try:
            kilometres = float(miles) * MILES_TO_KM_SCALE
            self.root.ids.kilometres_value.text = str(round(kilometres, 3))
        except ValueError:
            self.root.ids.input_number.text = str('')
            self.root.ids.kilometres_value.text = str(0.0)
            pass


MilesKilometreApp().run()
