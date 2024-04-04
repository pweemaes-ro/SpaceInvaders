"""A class representing invading aliens."""
import random
import turtle


class Alien(turtle.Turtle):
	"""Alien class."""
	
	ALIEN_SPAWN_INTERVAL = 2  # Seconds
	ALIEN_SPEED = 3.5
	COLORS = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
	
	def __init__(self) -> None:
		
		super().__init__()
		
		self.penup()
		self.turtlesize(1.5)
		self.top = self.screen.window_height() / 2
		self.gutter = 0.025 * self.screen.window_width()
		self.setposition(
			random.randint(int(-self.screen.window_width() / 2 + self.gutter),
			               int(self.screen.window_width() / 2 - self.gutter)),
			self.top)
		self.shape("turtle")
		self.setheading(-90)
		self.color(*self.COLORS[random.randint(0, len(self.COLORS) - 1)])

	def move(self) -> bool:
		"""Move the alien. Return False if alien went off screen, else True."""
		
		self.forward(self.ALIEN_SPEED)
	
		cannon = getattr(self.screen, "cannon")
		return not self.ycor() < cannon.floor_level
	
	def remove(self) -> None:
		"""Remove current alien from the system."""
		
		aliens = getattr(self.screen, "aliens")
		self.clear()
		self.hideturtle()
		aliens.remove(self)
		self.screen.update()
		turtle.turtles().remove(self)
	