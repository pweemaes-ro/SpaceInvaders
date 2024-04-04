"""Game Over splash screen"""
import turtle


class GameOver(turtle.Turtle):
	"""The Game Over splash screen"""
	
	def __init__(self) -> None:
		
		super().__init__()
		
		self.hideturtle()
		self.color(1, 1, 1)
		self.write("GAME OVER", font=("Courier", 40, "bold"), align="center")
