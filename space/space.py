import pygame
import time 
import os
import random 

#setting up font 
pygame.font.init()

#display screen 
WIDTH, HEIGHT= 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space invader")

#load images 
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets","pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets","pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets","pixel_ship_blue_small.png"))

#player player 
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets","pixel_ship_yellow.png"))

#lasers 
RED_LASER= pygame.image.load(os.path.join("assets","pixel_laser_red.png"))
GREEN_LASER= pygame.image.load(os.path.join("assets","pixel_laser_green.png"))
BLUE_LASER= pygame.image.load(os.path.join("assets","pixel_laser_blue.png"))
YELLOW_LASER= pygame.image.load(os.path.join("assets","pixel_laser_yellow.png"))

#background
BG= pygame.transform.scale(pygame.image.load(os.path.join("assets","background-black.png")),(WIDTH,HEIGHT))


#abstract player class to call in different time  
class Ship:
	def __init__(self,x,y, health=100):
		self.x = x 
		self.y = y
		self.health = health
		self.player_img= None
		self.laser_img = None
		self.lasers = []
		self.cool_down_counter = 0

	def draw(self, window):
		window.blit(self.player_img, (self.x,self.y))
		# pygame.draw.rect(window, (255,0,0),(self.x,self.y,50,50),2)  #2 is to create unfilled

	def get_width(self):
		return self.player_img.get_width()

	def get_height(self):
		return self.player_img.get_height()


class Player(Ship):
	def __init__(self,x,y,health=100):
		super().__init__(x,y,health)
		self.player_img = YELLOW_SPACE_SHIP
		self.laser_img = YELLOW_LASER
		self.mask = pygame.mask.from_surface(self.player_img)
		self.max_health = health

class Enemy(Ship):
	COLOR_MAP = {
				"red":(RED_SPACE_SHIP,RED_LASER),
				"green":(GREEN_SPACE_SHIP,GREEN_LASER),
				"blue":(BLUE_SPACE_SHIP,BLUE_LASER)
			}
	def __init__(self,x,y,color,health=100):
		super().__init__(x,y,health)
		self.ship_img,self.laser_img = self.COLOR_MAP[color]
		self.mask = pygame.mask.from_surface(self.ship_img)

	def move(self,vel):
		self.y += vel


#main loop 
def main():
	run = True
	FPS = 60 #game speed
	level = 1
	lives = 5 
	main_font= pygame.font.SysFont("comicsans",50)

	enemies= []
	wave_length = 5
	enemy_vel=1


	player_vel = 10 
	player = Player(300,650)
	clock= pygame.time.Clock()

	def redraw_window():      #redraw windwo and renders assets
		WIN.blit(BG, (0,0))

		#draw text
		lives_label=main_font.render(f"Lives :{lives}",1,(255,0,0))
		level_label= main_font.render(f"Level:{level}",1,(255,255,255))

		WIN.blit(lives_label, (10,10))
		WIN.blit(level_label,(WIDTH - level_label.get_width()-10, 10))

		for enemy in enemies:
			enemy.draw(WIN)

		player.draw(WIN)

		pygame.display.update()


	while run:
		clock.tick(FPS)

		if len(enemies) == 0:
			level += 1
			wave_length += 5
			for i in range(wave_length):
				enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500 , -100),random.choice(["red","blue","green"]))
				enemies.append(enemy)


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		keys = pygame.key.get_pressed()
		if keys[pygame.K_a] and player.x - player_vel > 0: #left
			player.x -= player_vel
		if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH: #right
			player.x += player_vel
		if keys[pygame.K_w] and player.y-player_vel  > 0: #up
			player.y -= player_vel
		if keys[pygame.K_s] and player.y + player_vel + player.get_height() < HEIGHT: #down
			player.y += player_vel

		for enemy in enemies:
			enemy.move(enemy_vel)
			
		redraw_window()
main()

