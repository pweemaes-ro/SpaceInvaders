"""Class representing a laser."""
import turtle


class Laser(turtle.Turtle):
	"""Laser class"""
	
	LASER_LENGTH = 20
	LASER_SPEED = 20
	
	def __init__(self) -> None:
		
		super().__init__()
		
		self.penup()
		self.color(1, 0, 0)
		self.hideturtle()
		cannon = getattr(self.screen, "cannon")
		self.setposition(cannon.xcor(), cannon.ycor())
		self.setheading(90)
		# Move laser to just above cannon tip
		self.forward(20)
		# Prepare to draw the laser
		self.pendown()
		self.pensize(5)

	def move(self) -> bool:
		"""Move laser. Return True if laser moved, False if laser went off
		screen (and therefore removed)."""
		
		if self.ycor() > self.screen.window_height() / 2:
			self.remove()
			return False
		else:
			self.clear()
			self.forward(self.LASER_SPEED)
			# Draw the laser
			self.forward(self.LASER_LENGTH)
			self.forward(-self.LASER_LENGTH)
			return True
		
	def remove(self) -> None:
		"""Remove current laser from the system."""
		
		lasers = getattr(self.screen, "lasers")
		self.clear()
		self.hideturtle()
		self.screen.update()
		lasers.remove(self)
		turtle.turtles().remove(self)
