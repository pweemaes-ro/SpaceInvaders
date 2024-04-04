"""Score"""
import turtle


class Score(turtle.Turtle):
	"""Score and time"""
	
	def __init__(self) -> None:
		
		super().__init__()
		
		self.penup()
		self.hideturtle()
		self.setposition(-self.screen.window_width() * 0.4,
		                 self.screen.window_height() * 0.4)
		self.color(1, 1, 1)

	def update(self, time_elapsed: float, score: int):
		"""Update the score fields."""
		
		self.clear()
		self.write(f"Time: {time_elapsed:5.1f}s\nScore: {score: 5}",
		                 font=("Courier", 20, "bold"), )
