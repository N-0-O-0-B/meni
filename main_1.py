import pygame, sys
from pygame import *
from random import randint
 
# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500),0,32)
 
font = pygame.font.SysFont(None, 20)
 
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False
 
def main_menu():
    while True:
 
        screen.fill((0,0,0))
        draw_text('main menu', font, (255, 255, 255), screen, 20, 20)
 
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
 
def game():
    # running = True
    # while running:
    #     screen.fill((0,0,0))
        
    #     draw_text('game', font, (255, 255, 255), screen, 20, 20)
    #     for event in pygame.event.get():
    #         if event.type == QUIT:
    #             pygame.quit()
    #             sys.exit()
    #         if event.type == KEYDOWN:
    #             if event.key == K_ESCAPE:
    #                 running = False
        
    #     pygame.display.update()
    #     mainClock.tick(60)
    font_UI = font.SysFont(None, 36)
    font_IU = font.SysFont(None, 200)
    font.init()
    font_win_lose = font.Font(None, 70)

    a = 1
    b = 5
    c = 1
    d = 5
    score_1 = 0
    score_2 = 0
    speed_y = randint(1,6)
    speed_x = randint(1,6)

    background = transform.scale(image.load('hon.jpg'),(700,500))

    mixer.init()
    mixer.music.load('gg.ogg')
    mixer.music.play()
    clock = time.Clock()
    FPS = 60
    speed = 3
    finish = False

    # UI

    while True:
 
        screen.fill((0,0,0))
        draw_text('main menu', font, (255, 255, 255), screen, 20, 20)
 
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)


    class GS(sprite.Sprite):
        def __init__(self, player_image, player_x, player_y, player_speed, width, height):
            super().__init__()
            self.image = transform.scale(image.load(player_image), (width, height))
            self.speed = player_speed
            self.rect = self.image.get_rect()
            self.rect.x = player_x
            self.rect.y = player_y
        def reset(self):
            window.blit(self.image, (self.rect.x, self.rect.y))

    win_width = 400
    win_height = 500       
    font.init()
    font = font.Font(None, 70)

    window = display.set_mode((700,500))
    display.set_caption("ПеЛьМеНь На СвЕрХзВуКоВоЙ сКоРоСтИ")

    class Player(GS):
        def update(self):
            keys_pressed = key.get_pressed()
            if keys_pressed[K_UP] and self.rect.y > 5:
                self.rect.y-=self.speed
            if keys_pressed[K_DOWN] and self.rect.y < win_height - 80:
                self.rect.y+=self.speed

    class Player_2(GS):
        def update(self):
            keys_pressed = key.get_pressed()
            if keys_pressed[K_w] and self.rect.y > 5:
                self.rect.y-=self.speed
            if keys_pressed[K_s] and self.rect.y < win_height - 80:
                self.rect.y+=self.speed

    player_1 = Player('vilka.png', 15, 100, 15,50,70)
    player_2 = Player_2('logka.png', 555, 100, 15,50,70)
    ball = GS('mic.png',350, 250, 15, 40, 50)
    hon_2 = GS('Шлёпа.png', 285, 333, 0,150,180)

    game = True
    clock = time.Clock()
    FPS = 2000
    finish = False
    while game: 
        text_2 = font_UI.render("счёт 2:  "+str(score_2), True, (41, 24, 96))
        text_1 = font_UI.render("счёт 1:  "+str(score_1), True, (34, 61, 24))
        window.blit(background,(0,0))
        window.blit(text_1,(10,10))
        window.blit(text_2,(10,50))
        for e in event.get():
            if e.type == QUIT:
                game = False

        if finish != True:
            ball.rect.x += speed_x
            ball.rect.y += speed_y

        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(player_1, ball) or sprite.collide_rect(player_2, ball):
            speed_x *= -1

        if ball.rect.x < -50 :
            ball.rect.x = 350
            ball.rect.y = 250
            speed_y = randint(a,b)
            speed_x = randint(c,d)
            score_2 += 1
            a += 1
            b += 1
            c += 1
            d += 1

        elif ball.rect.x > 750:
            ball.rect.x = 350
            ball.rect.y = 250
            speed_y = randint(a,b)
            speed_x = randint(c,d)
            score_1 += 1
            a += 1
            b += 1
            c += 1
            d += 1

        player_1.update()
        player_1.reset()

        player_2.update()
        player_2.reset()

        ball.update()
        ball.reset()

        hon_2.update()
        hon_2.reset()

        display.update()
        clock.tick(FPS)
 
def options():
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('options', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)
 
main_menu()