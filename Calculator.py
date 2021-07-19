# list1 = [1,2,3]
# list2 = [1,2,3]
# # is And == tafavot
# print(list1 is list1)



import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

from kivy.uix.button import Button

 
class CalcGridLayout(GridLayout):
    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"


class CalculatorApp(App):
    def build(self):
        return CalcGridLayout()
 
calcApp = CalculatorApp()
calcApp.run()






# from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.textinput import TextInput

# class TestApp(App):
#     def build(self):
#         return TextInput(text='Hello World')

# TestApp().run()


