"""Game Window."""
import time
import turtle

from alien import Alien
from cannon import Cannon
from gameover import GameOver
from laser import Laser
from score import Score


class GameWindow:
	"""The Game Window (todo LP: make singleton)"""

	TIME_PER_FRAME = 1/30  # Seconds
	
	def __init__(self) -> None:
		
		super().__init__()
		
		self.window = turtle.Screen()

		self.window.tracer(0)
		self.window.bgcolor(0.2, 0.2, 0.2)
		self.window.title("Space Invaders (simple clone)")

		self.window.onkeypress(self.set_cannon_direction_to_left, "Left")
		self.window.onkeypress(self.set_cannon_direction_to_right, "Right")
		self.window.onkeyrelease(self.stop_cannon_movement, "Left")
		self.window.onkeyrelease(self.stop_cannon_movement, "Right")
		self.window.onkeypress(self.game_over, "q")
		self.window.onkeypress(self.toggle_paused, "p")
		self.window.onkeypress(self.create_laser, "space")
		self.window.listen()

		setattr(self.window, "cannon", Cannon())
		setattr(self.window, "aliens", set())
		setattr(self.window, "lasers", set())
		self.score = Score()
		
		self.game_running = False
		self.game_paused = False
		
		self.window.update()
	
	def game_over(self) -> None:
		"""Aborts the game"""

		if self.game_running:
			self.game_running = False
		else:
			turtle.bye()

	def toggle_paused(self) -> None:
		"""Pause/unpause the game."""
		
		self.game_paused = not self.game_paused

	def set_cannon_direction_to_left(self) -> None:
		"""Function called when left arrow key is presssed.  Set direction of
		cannon movement to the left."""
		
		getattr(self.window, "cannon").cannon_movement = -1

	def set_cannon_direction_to_right(self) -> None:
		"""Function called when right arrow key is presssed. Set direction of
		cannon movement to the right."""
		
		getattr(self.window, "cannon").cannon_movement = 1

	def stop_cannon_movement(self) -> None:
		"""Function called when right or left arrow key is released. Set
		direction of cannon movement to 'no movement'."""
		
		getattr(self.window, "cannon").cannon_movement = 0

	def create_laser(self) -> None:
		"""Function called when space key is presssed. Create new laser and add
		it to the list of active lasers."""
		
		getattr(self.window, "lasers").add(Laser())
	
	def play(self) -> None:
		"""Play the game"""
		
		alien_timer = 0.0
		cannon = getattr(self.window, "cannon")
		score = 0
		self.game_running = True

		game_timer = time.time()

		# Game loop
		while self.game_running:
			frame_start_time = time.time()

			if not self.game_paused:

				self.score.update(time.time() - game_timer, score)
	
				cannon.move()
	
				aliens = getattr(self.window, "aliens")
				lasers = getattr(self.window, "lasers")
	
				# Move all lasers
				for laser in lasers.copy():
	
					# move laser, if move failed it went off screen and was removed.
					if not laser.move():
						break
					
					# Check for collision with aliens
					for alien in aliens.copy():
						if laser.distance(alien) < 20:
							# Remove alien and laser
							laser.remove()
							alien.remove()
							score += 1
							break
			
				if time.time() - alien_timer > Alien.ALIEN_SPAWN_INTERVAL:
					aliens.add(Alien())
					alien_timer = time.time()
				
				# Move all aliens
				for alien in aliens:
					# if move fails, alien got through, game over.
					if not alien.move():
						self.game_running = False
						break
			
			# Frame done before the reserved time for frame is over? Sleep!
			if (sleep_time := self.TIME_PER_FRAME -
			                  (time.time() - frame_start_time)) > 0:
				time.sleep(sleep_time)
			
			self.window.update()
			
		GameOver()


GameWindow().play()

turtle.done()
