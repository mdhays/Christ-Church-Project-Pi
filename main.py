import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class mylayout(GridLayout):
	"""Initialize the layout
	You can use **kwargs to let your functions take an
	 arbitrary number of keyword arguments
	 ("kwargs" means "keyword arguments")"""
	def __init__(self, **kwargs):
		super(mylayout, self).__init__(**kwargs)
		
		self.cols = 2

		btnLeftProjOn = Button(text = "Left Projector On")
		btnLeftProjOn.bind(on_press=self.clkLeftProjOn)

		btnLeftProjOff = Button(text = "Left Projector Off")
		btnLeftProjOff.bind(on_press=self.clkLeftProjOff)

		btnRightProjOn = Button(text = "Right Projector On")
		btnRightProjOn.bind(on_press=self.clkRightProjOn)

		btnRightProjOff = Button(text = "Right Projector Off")
		btnRightProjOff.bind(on_press=self.clkRightProjOff)

		self.add_widget(btnLeftProjOn)
		self.add_widget(btnRightProjOn)
		self.add_widget(btnLeftProjOff)
		self.add_widget(btnRightProjOff)

	def clkLeftProjOn(self, obj):
		print("Left Projector On!")

	def clkLeftProjOff(self, obj):
		print("Left Projector Off")

	def clkRightProjOn(self, obj):
		print("Right Projector On!")

	def clkRightProjOff(self, obj):
		print("Right Projector Off")


class ChristChurchApp(App):
    def build(self):
    	mL = mylayout()
    	return mL


if __name__ == '__main__':
    ChristChurchApp().run()