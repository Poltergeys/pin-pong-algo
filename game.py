import pygame
pygame.init()

window = pygame.display.set_mode((600,400))
window.fill((75,200,250))

clock = pygame.time.Clock()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_dir, width, height, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(image_dir), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.speed_x = self.speed
        self.speed_y = self.speed
        
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
        
    #Колизию
    def colision(self, obj):
        return self.rect.colliderect(obj.rect)
        
class Rocket(GameSprite):
    def move_up(self):
        if self.rect.y >= 0:
            self.rect.y -= self.speed
    def move_down(self):
        if self.rect.y <= 600:
            self.rect.y += self.speed
    def move_r_rocket(self):
        keyboard = pygame.key.get_pressed()
        if keyboard[pygame.K_UP]:
            self.move_up()
        if keyboard[pygame.K_DOWN]:
            self.move_down()
    def move_l_rocket(self):
        keyboard = pygame.key.get_pressed()
        if keyboard[pygame.K_w]:
            self.move_up()
        if keyboard[pygame.K_s]:
            self.move_down()
player1 = Rocket('rocket.png', 20, 100, 25, 200, 5)
player2 = Rocket('rocket.png', 20, 100, 555, 200, 5)

is_game = True
is_finished = False
ball = GameSprite('tenis_ball.png', 25, 25, 275, 175, 2)
font1 = pygame.font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font1.render('PLAYER 2 LOSE!', True, (180, 0, 0))
while is_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game = False
    if not is_finished:
        window.fill((75,200,250))
        player1.move_l_rocket()
        player2.move_r_rocket()
        ball.rect.x += ball.speed_x
        ball.rect.y += ball.speed_y
        if ball.rect.y >= window.get_height()-25 or ball.rect.y < 0:
            ball.speed_y *= -1
        if ball.colision(player1) or ball.colision(player2):
            ball.speed_x *= -1 
        if ball.rect.x < 0:
            is_finished = True
            window.blit(lose1,(200, 200))
        if ball.rect.x > 600:
            is_finished = True
            window.blit(lose2,(200, 200))
    player1.reset()
    player2.reset()
    ball.reset()
    clock.tick(60)
    pygame.display.update()