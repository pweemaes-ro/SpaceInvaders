"""The Cannon"""
import turtle


class Cannon(turtle.Turtle):
	"""Cannon class"""
	
	CANNON_STEP = 10
	
	def __init__(self) -> None:
		super().__init__()
		self.penup()
		self.color(1, 1, 1)  # RGB values
		self.shape("square")
		self.bottom = -self.screen.window_height() / 2

		self.floor_level = 0.9 * (-self.screen.window_height() / 2)
		self.setposition(0, self.floor_level)
		self.cannon_movement = 0
		self.screen_left = -self.screen.window_width() / 2
		self.screen_right = self.screen.window_width() / 2
		self.screen_gutter = 0.025 * self.screen.window_width()
		
	def move(self) -> None:
		"""Move the cannon"""
		
		x = self.xcor() + Cannon.CANNON_STEP * self.cannon_movement
		if (self.screen_left + self.screen_gutter
			<= x
			<= self.screen_right - self.screen_gutter):
			self.setx(x)
			self.draw()
			self.screen.update()
	
	def draw(self) -> None:
		"""(re)draw the cannon."""
		
		self.clear()
		self.turtlesize(1, 4)  # Base
		self.stamp()
		self.sety(self.floor_level + 10)
		self.turtlesize(1, 1.5)  # Next tier
		self.stamp()
		self.sety(self.floor_level + 20)
		self.turtlesize(0.8, 0.3)  # Tip of self
		self.stamp()
		self.sety(self.floor_level)
