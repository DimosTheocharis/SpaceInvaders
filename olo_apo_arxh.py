import pygame
from pygame.locals import *
import time
import random


pygame.init()

display_width = 750
display_height = 750

GameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("Space Invaders")

# LOAD SPACESHIPS
RED_SPACE_SHIP = pygame.image.load("RedShip.png")
BLUE_SPACE_SHIP = pygame.image.load("BlueShip.png")
GREEN_SPACE_SHIP = pygame.image.load("GreenShip.png")
BOSS_SPACE_SHIP = pygame.image.load("FinalBoss.png")
ULTRA_BOSS_SPACE_SHIP = pygame.image.load('Boss2Pro.png')
TERA_BOSS_SPACE_SHIP = pygame.image.load('Boss3_Resized.png')

# PLAYER SPACESHIP
YELLOW_SPACE_SHIP = pygame.image.load("PlayerShip.png")
YELLOW_LASER = pygame.image.load("pixel_laser_yellow.png")

# LOAD LASERS
RED_LASER = pygame.image.load("pixel_laser_red.png")
BLUE_LASER = pygame.image.load("pixel_laser_blue.png")
GREEN_LASER = pygame.image.load("pixel_laser_green.png")
BOSS_LASER = pygame.image.load("Black_Yellow.png")
ULTRA_BOSS_LASER = pygame.image.load('BossLaser2.png')
TERA_BOSS_LASER = pygame.image.load('BossBoss.png')

# EIKONES
right_arrow = pygame.image.load("right_arrow.png")
left_arrow = pygame.image.load("left_arrow.png")
space_button = pygame.image.load("space_button.png")
pause_button = pygame.image.load("pause_button.png")
Coins_img = pygame.image.load("coins_final.png")
Button_D = pygame.image.load("ButtonDFinal.png")
Button_A = pygame.image.load("ButtonAFinal.png")
Button_S = pygame.image.load("ButtonSFinal.png")
Button_W = pygame.image.load("ButtonWFinal.png")
Button_E = pygame.image.load("ButtonEFinal.png")


# BACKROUND
GameBackround = pygame.image.load("GameBackround.png")
MainMenu = pygame.image.load("MainMenu2.png")
InstructionsBackround = pygame.image.load("InstructionsBackround.png")


# Grammatoseires
supersmallfont = pygame.font.SysFont("dejavusans", 15)
smallfont = pygame.font.SysFont("dejavusans", 20)
font = pygame.font.SysFont("dejavusans", 30)
bigfont = pygame.font.SysFont("dejavusans", 80)
middlefont = pygame.font.SysFont("dejavusans", 50)
mikrotera_grammata_freesans = pygame.font.SysFont('freesansbold.tff', 27)
mikrotera_dejavusans = pygame.font.SysFont('dejavusans', 15)
minimum_freesans = pygame.font.SysFont('freesansbold.tff', 15)
ligo_megalutera_freesans = pygame.font.SysFont('freesansbold.tff', 20)
comicsans_grammatoseira = pygame.font.SysFont('comicsans', 25)

prices = {
    'BOSS_LASER' : 1,
    'ULTRA_BOSS_LASER' : 2,
    'TERA_BOSS_LASER' : 5}

buy_status = {
    'BOSS_LASER' : False,
    'ULTRA_BOSS_LASER' : False,
    'TERA_BOSS_LASER' : False}

equip_status = {
    'BOSS_LASER' : False,
    'ULTRA_BOSS_LASER' : False,
    'TERA_BOSS_LASER' : False}

health_prices = {
    "First_Upgrade" : 1,
    "Second_Upgrade": 2,
    "Third_Upgrade" : 3,
    "Fourth_Upgrade": 4,
    "Fifth_Upgrade" : 5 }

health_stats = {
    "First_Upgrade" : False,
    "Second_Upgrade": False,
    "Third_Upgrade" : False,
    "Fourth_Upgrade": False,
    "Fifth_Upgrade" : False }

cooldown_prices = {
    "First_Upgrade" : 2,
    "Second_Upgrade": 4,
    "Third_Upgrade" : 6,
    "Fourth_Upgrade": 8,
    "Fifth_Upgrade" : 10}


cooldown_stats = {
    "First_Upgrade" : False,
    "Second_Upgrade": False,
    "Third_Upgrade" : False,
    "Fourth_Upgrade": False,
    "Fifth_Upgrade" : False}

speed_prices = {
    "First_Upgrade" : 3,
    "Second_Upgrade": 6,
    "Third_Upgrade" : 9,
    "Fourth_Upgrade": 12,
    "Fifth_Upgrade" : 15}

speed_stats = {
    "First_Upgrade" : False,
    "Second_Upgrade": False,
    "Third_Upgrade" : False,
    "Fourth_Upgrade": False,
    "Fifth_Upgrade" : False}

score = 0
boss_presence = True
level = 0
vari = True
kari = True
mari = True


current_health = 100
maximun_health = 150


current_cooldown = 30
maximun_cooldown = 30
phenomenal_cooldown = 20

current_speed = 5
maximun_speed = 10
phenomenal_speed = 20

# edw tha einai ta variables pou tha xrhsimopoihsw gia na kanw blit sthn othoni sto menu, gia to kostos tou kathe update
current_health_cost = health_prices["First_Upgrade"]
current_cooldown_cost = cooldown_prices["First_Upgrade"]
current_speed_cost = speed_prices["First_Upgrade"]

Coins = 100
permanent_bought = False
buy_BOSS_LASER = False
buy_ULTRA_BOSS_LASER = False


# XRWMATA
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
red2 = (200,0,0)
red3 = (150,0,0)
green = (0,255,0)
green2 = (0,200,0)
blue = (0,0,255)
ble_skouro = (0,0, 102)
ble_anoixto = (153, 153, 255)
grey = (128, 128, 128)
grey2 = (64,64,64)
gold = (200,120,40)
orange = (204, 102, 0)
orange2 = (255, 128, 0)
# auta xreisimopoiountai gia to shop khriws
kafe_skouro = (51,25,0)
kafe_anoixto = (102, 51, 0)
mwb_skouro = (51,0,102)
mwb_anoixto = (102,0,204)
portokali_skouro = (153, 76, 0)
portokali_anoixto = (255,128,0)
# gia to boss
xryso = (212, 175, 55)


#####################################FUNCTIONS#################################
def ftiakse_rect(x,y,width,height,color):
    pygame.draw.rect(GameDisplay, color, [x,y,width,height])

def ftiakse_text(text, your_font, x, y, color):
    new_text = your_font.render(text, True, color)
    GameDisplay.blit(new_text, (x,y))


def arxh():
    arxiko_mhnyma = font.render("Welcome to SpaceInveders. Are you ready to play?", True, gold)
    GameDisplay.blit(arxiko_mhnyma, (display_width/2 - arxiko_mhnyma.get_width() / 2,100))


def back():
    global boss_presence, Coins, score
    Coins += score
    score = 0
    ksana = False
    boss_presence = True
    GameDisplay.blit(MainMenu, (0,0))
    Delta = False
    Kappa = False
    Gamma = True
    vari = True
    kari = True
    mari = True
    while not ksana:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
        button("Start", 150, 180, 110, 50, font, black, green, green2, "Start")
        button("Quit", 450, 180, 110, 50, font, black, red, red2, "Quit")
        button("Help", display_width - 90, display_height - 40, 90, 40, font, black, orange, orange2, "Help")
        button("Shop", display_width - 90, display_height - 40 - 40 , 90, 40, font, black,  orange, orange2, "Shop")
        arxh()
##        pygame.display.update()
    


def Shop():
    exit = True
    global current_health
    GameDisplay.fill(kafe_anoixto)
    while exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        shop_label = bigfont.render("Shop", True, white)
        coins_label = middlefont.render(f'{Coins}', True, white)
        boss_laser_label = smallfont.render('The Mega Boss Laser', True, gold)
        ultra_boss_laser_label = smallfont.render('The Ultra Boss Laser', True, gold)
        tera_boss_laser_label = smallfont.render('The Tera Boss Laser', True, gold)
        health_label = font.render("Health", True, gold)
        cooldown_label = font.render("Cooldown", True, gold)
        speed_label = font.render("Speed", True, gold)
        health_description_label_1 = supersmallfont.render("Each upgrade gives you 10", True, white)
        health_description_label_2 = supersmallfont.render("additional health.", True, white)
        cooldown_description_label_1 = supersmallfont.render("Each upgrade decreases", True, white)
        cooldown_description_label_2 = supersmallfont.render("the cooldown by 2 sec.", True, white)
        speed_description_label_1 = supersmallfont.render("Each upgrade increases your", True, white)
        speed_description_label_2 = supersmallfont.render("speed by 0.5 px/frame.", True, white)
        health_cost_label = supersmallfont.render(f"The next upgrade costs: {current_health_cost}", True, white)
        cooldown_cost_label = supersmallfont.render(f"The next upgrade costs: {current_cooldown_cost}", True, white)
        speed_cost_label = supersmallfont.render(f"The next upgrade costs: {current_speed_cost}", True, white)
        GameDisplay.blit(shop_label, (display_width / 2 - shop_label.get_width() / 2, 75))
        # ftiaxnei diafora orthogonia gia to skhniko tou katasthmatos
        pygame.draw.rect(GameDisplay, kafe_skouro, [display_width - 100, 0, 100, 40])
        GameDisplay.blit(Coins_img, (635, -8))
        pygame.draw.rect(GameDisplay, kafe_skouro, [0,150,display_width, 30])
        pygame.draw.rect(GameDisplay, kafe_skouro, [50, 220, 150, 300])
        pygame.draw.rect(GameDisplay, kafe_skouro, [300, 220, 150, 300])
        pygame.draw.rect(GameDisplay, kafe_skouro, [550, 220, 150, 300])
        pygame.draw.rect(GameDisplay, kafe_skouro, [0, 550, display_width, 30])
        pygame.draw.rect(GameDisplay, kafe_skouro, [50, 620, 150, 110])
        pygame.draw.rect(GameDisplay, kafe_skouro, [300, 620, 150, 110])
        pygame.draw.rect(GameDisplay, kafe_skouro, [550, 620, 150, 110])
        pygame.draw.rect(GameDisplay, red3, [50 + 1, 680, int(maximun_health * 0.9), 15])
        pygame.draw.rect(GameDisplay, red, [50 + 1, 680, int(current_health * 0.9), 15])
        pygame.draw.rect(GameDisplay, mwb_skouro, [300 + 1, 680, int(maximun_cooldown * 4.5), 15])  # edw ebala prwta to maximun me 30 CD gt
        pygame.draw.rect(GameDisplay, mwb_anoixto, [300 + 1, 680, int(phenomenal_cooldown * 4.5), 15]) # paei antitheta,( apo 30 katebainei sto
        pygame.draw.rect(GameDisplay, portokali_skouro, [550 + 1, 680, int(maximun_speed * 13.5), 15])
        pygame.draw.rect(GameDisplay, portokali_anoixto, [550 + 1, 680, int(phenomenal_speed * 4.5), 15])
        thesi1 = 51                                                                                  #20) . kai to phenomenal to xrhsimopoiw
        for x in range(15):                                                                        # mono gia na auksanetai to mhkos tou rect
            pygame.draw.line(GameDisplay, black, (thesi1, 680), (thesi1, 695), 2)                  # otan pataw + sto cooldown
            thesi1 += 9                                                               # epishs xrhsimopoiw phenomenal_speed epeidh tairiazei
        thesi2 = 301                                                            # kalytera san arithmos sto na kanw th bara gia to speed                
        for x in range(15):
            pygame.draw.line(GameDisplay, black, (thesi2, 680), (thesi2, 695), 2)
            thesi2 += 9
        thesi3 = 551
        for x in range(15):
            pygame.draw.line(GameDisplay, black, (thesi3, 680), (thesi3, 695), 2)
            thesi3 += 9

        # perigrafes gia ta items
            # BOSS_LASER
        description_boss_laser1 = smallfont.render("This bullet belongs to", True, white)
        description_boss_laser2 = smallfont.render("the Mega Boss and ", True, white)
        description_boss_laser3 = smallfont.render("does 20 damage to the ", True, white)
        description_boss_laser4 = smallfont.render("enemy bosses.", True, white)
        description_boss_laser5 = smallfont.render(f"It costs {prices['BOSS_LASER']} coins.", True, white)
        GameDisplay.blit(description_boss_laser1, (55, 350))
        GameDisplay.blit(description_boss_laser2, (55, 370))
        GameDisplay.blit(description_boss_laser3, (55, 390))
        GameDisplay.blit(description_boss_laser4, (55, 410))
        GameDisplay.blit(description_boss_laser5, (55, 430))
            # ULTRA_BOSS_LASER
        description_ultra_boss_laser1 = smallfont.render("This bullet belongs to", True, white)
        description_ultra_boss_laser2 = smallfont.render("the Ultra Boss", True, white)
        description_ultra_boss_laser3 = smallfont.render("and does 30 damage to  ", True, white)
        description_ultra_boss_laser4 = smallfont.render("the enemy bosses.", True, white)
        description_ultra_boss_laser5 = smallfont.render(f"It costs {prices['ULTRA_BOSS_LASER']} coins.", True, white)
        GameDisplay.blit(description_ultra_boss_laser1, (305, 350))
        GameDisplay.blit(description_ultra_boss_laser2, (305, 370))
        GameDisplay.blit(description_ultra_boss_laser3, (305, 390))
        GameDisplay.blit(description_ultra_boss_laser4, (305, 410))
        GameDisplay.blit(description_ultra_boss_laser5, (305, 430))
            # TERA_BOSS_LASER
        description_tera_boss_laser1 = smallfont.render("This bullet belongs to", True, white)
        description_tera_boss_laser2 = smallfont.render("the Tera Boss  ", True, white)
        description_tera_boss_laser3 = smallfont.render("and does 40 damage to  ", True, white)
        description_tera_boss_laser4 = smallfont.render("the enemy bosses.", True, white)
        description_tera_boss_laser5 = smallfont.render(f"It costs {prices['TERA_BOSS_LASER']} coins.", True, white)
        GameDisplay.blit(description_tera_boss_laser1, (555, 350))
        GameDisplay.blit(description_tera_boss_laser2, (555, 370))
        GameDisplay.blit(description_tera_boss_laser3, (555, 390))
        GameDisplay.blit(description_tera_boss_laser4, (555, 410))
        GameDisplay.blit(description_tera_boss_laser5, (555, 430))
        
        # Edw kanw blit tous titlous sto katasthma
        GameDisplay.blit(boss_laser_label, (60, 230))
        GameDisplay.blit(ultra_boss_laser_label, (310, 230))
        GameDisplay.blit(tera_boss_laser_label, (560, 230))
        GameDisplay.blit(health_label, (50 + 45,620 + 5))
        GameDisplay.blit(cooldown_label, (300 + 35, 620 + 5))
        GameDisplay.blit(speed_label, (550 + 45, 620 + 5))
        GameDisplay.blit(health_description_label_1, (50, 650))
        GameDisplay.blit(health_description_label_2, (50, 665))
        GameDisplay.blit(cooldown_description_label_1, (300, 650))
        GameDisplay.blit(cooldown_description_label_2, (300, 665))
        GameDisplay.blit(speed_description_label_1, (550, 650))
        GameDisplay.blit(speed_description_label_2, (550, 665))
        GameDisplay.blit(health_cost_label, (50, 720))
        GameDisplay.blit(cooldown_cost_label, (300, 720))
        GameDisplay.blit(speed_cost_label, (550, 720))
        # Edw kanw blit ta images sto katasthma
        GameDisplay.blit(BOSS_LASER, (100, 250))
        GameDisplay.blit(ULTRA_BOSS_LASER, (350, 250))
        GameDisplay.blit(TERA_BOSS_LASER, (600, 250))
        GameDisplay.blit(coins_label, (700, 2))
        Buy("ULTRA_BOSS_LASER", 350, 470, 50, 40, font, white, green2, red)
        Buy('BOSS_LASER', 100, 470, 50, 40, font, white, green2, red)
        Buy('TERA_BOSS_LASER', 600,470, 50, 40, font, white, green2, red)
        plus(50 + 138, 680, 13,15, font, black, white, "health")
        plus(300 + 138, 680, 13, 15, font, black, white, "cooldown")
        plus(550 + 138, 680, 13, 15, font, black, white, "speed")
        button("<-Back", 0, 0, 90, 40, font, black, grey, grey2, 'Back')
        keys = pygame.key.get_pressed()
        pygame.display.update()
        
def plus(X,Y,WIDTH, HEIGHT, FONT, COLOR_FONT, COLOR, ELEMENT):
    global current_health, upgrade, Coins, current_cooldown, phenomenal_cooldown, current_speed, current_health_cost, current_cooldown_cost, current_speed_cost,phenomenal_speed
    running = True
    if ELEMENT == "health":
        element_stats = health_stats
        element_prices = health_prices
    elif ELEMENT == "cooldown":
        element_stats = cooldown_stats
        element_prices = cooldown_prices
    elif ELEMENT == "speed":
        element_stats = speed_stats
        element_prices = speed_prices
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pygame.draw.rect(GameDisplay, COLOR, [X,Y,WIDTH,HEIGHT])
    plus_text = FONT.render('+', True, COLOR_FONT)
    GameDisplay.blit(plus_text, (X,Y - 5))
    if X <= mouse[0] <= X + WIDTH and Y <= mouse[1] <= Y + HEIGHT:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if element_stats["First_Upgrade"] == False and Coins >= element_prices["First_Upgrade"]:
                            Coins -= element_prices["First_Upgrade"]
                            element_stats["First_Upgrade"] = True
                            if ELEMENT == "health":
                                current_health += 10
                                current_health_cost = health_prices["Second_Upgrade"]
                            elif ELEMENT == "cooldown":
                                current_cooldown -= 2
                                phenomenal_cooldown += 2
                                current_cooldown_cost = cooldown_prices["Second_Upgrade"]
                            elif ELEMENT == "speed":
                                current_speed += 1
                                phenomenal_speed += 2
                                current_speed_cost = speed_prices["Second_Upgrade"]
                        elif element_stats["Second_Upgrade"] == False and Coins >= element_prices["Second_Upgrade"]:
                            Coins -= element_prices["Second_Upgrade"]
                            element_stats["Second_Upgrade"] = True
                            if ELEMENT == "health":
                                current_health += 10
                                current_health_cost = health_prices["Third_Upgrade"]
                            elif ELEMENT == "cooldown":
                                current_cooldown -= 2
                                phenomenal_cooldown += 2
                                current_cooldown_cost = cooldown_prices["Third_Upgrade"]
                            elif ELEMENT == "speed":
                                current_speed += 1
                                phenomenal_speed += 2
                                current_speed_cost = speed_prices["Third_Upgrade"]
                        elif element_stats["Third_Upgrade"] == False and Coins >= element_prices["Third_Upgrade"]:
                            Coins -= element_prices["Third_Upgrade"]
                            element_stats["Third_Upgrade"] = True
                            if ELEMENT == "health":
                                current_health += 10
                                current_health_cost = health_prices["Fourth_Upgrade"]
                            elif ELEMENT == "cooldown":
                                current_cooldown -= 2
                                phenomenal_cooldown += 2
                                current_cooldown_cost = cooldown_prices["Fourth_Upgrade"]
                            elif ELEMENT == "speed":
                                current_speed += 1
                                phenomenal_speed += 2
                                current_speed_cost = speed_prices["Fourth_Upgrade"]
                        elif element_stats["Fourth_Upgrade"] == False and Coins >= element_prices["Fourth_Upgrade"]:
                            Coins -= element_prices["Fourth_Upgrade"]
                            element_stats["Fourth_Upgrade"] = True
                            if ELEMENT == "health":
                                current_health += 10
                                current_health_cost = health_prices["Fifth_Upgrade"]
                            elif ELEMENT == "cooldown":
                                current_cooldown -= 2
                                phenomenal_cooldown += 2
                                current_cooldown_cost =  cooldown_prices["Fifth_Upgrade"]
                            elif ELEMENT == "speed":
                                current_speed += 1
                                phenomenal_speed += 2
                                current_speed_cost = speed_prices["Fifth_Upgrade"]
                        elif element_stats["Fifth_Upgrade"] == False and Coins >= element_prices["Fifth_Upgrade"]:
                            Coins -= element_prices["Fifth_Upgrade"]
                            element_stats["Fifth_Upgrade"] = True
                            if ELEMENT == "health":
                                current_health += 10
                            elif ELEMENT == "cooldown":
                                current_cooldown -= 2
                                phenomenal_cooldown += 2
                            elif ELEMENT  == "speed":
                                current_speed += 1
                                phenomenal_speed += 2
 
##            if health_stats["First_Upgrade"] == False and Coins >= health_prices["First_Upgrade"]:
##                Coins -= health_prices["First_Upgrade"]
##                health_stats["First_Upgrade"] = True
##                current_health += 10
##            elif health_stats["Second_Upgrade"] == False and Coins >= health_prices["Second_Upgrade"]:
##                    Coins -= health_prices["Second_Upgrade"]
##                    health_stats["Second_Upgrade"] = True
##                    current_health += 1
##            elif health_stats["Third_Upgrade"] == False and Coins >= health_prices["Third_Upgrade"]:
##                    Coins -= health_prices["Third_Upgrade"]
##                    health_stats["Third_Upgrade"] = True
##                    curent_health += 10
##            elif health_stats["Fourth_Upgrade"] == False and Coins >= health_prices["Fourth_Upgrade"]:
##                    Coins -= health_prices["Fourth_Upgrade"]
##                    health_stats["Fourth_Upgrade"] = True
##                    current_health += 10
##            elif health_stats["Fifth_Upgrade"] == False and Coins >= health_prices["Fifth_Upgrade"]:
##                    Coins -= health_prices["Fifth_Upgrade"]
##                    health_stats["Fifth_Upgrade"] = True
##                    current_health += 10
##
##                

            

def Buy(ITEM, X, Y, WIDTH, HEIGHT, FONT,COLOR, AC, IC):
    global Coins, permanent_bought, buy_BOSS_LASER, buy_ULTRA_BOSS_LASER
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()
    Equip(ITEM, X, Y, WIDTH, HEIGHT, FONT, COLOR, AC)
    if buy_status[ITEM] == False :
        ftiakse_rect(X,Y,WIDTH,HEIGHT,AC)
        mhnyma = FONT.render('Buy', True, COLOR)
        mhnymaRect = mhnyma.get_rect(center = ((X + (WIDTH / 2)), (Y + (HEIGHT / 2))   ))
        GameDisplay.blit(mhnyma, mhnymaRect)
        
    if X + WIDTH >= mouse[0] >= X and Y + HEIGHT >= mouse[1] >= Y:
        if buy_status[ITEM] == True:
            if keys[pygame.K_e]:
                for key in equip_status:
                    equip_status[key] = False
                equip_status[ITEM] = True
                    
        elif not buy_status[ITEM]:
            if click[0] == 1 and Coins >= prices[ITEM]:
                Coins -= prices[ITEM]
                buy_status[ITEM] = True
                buy_BOSS_LASER = True

   
def Equip(ITEM, X, Y, WIDTH, HEIGHT, FONT,COLOR, AC):
    if buy_status[ITEM] == True:
        if equip_status[ITEM] == False:
            WIDTH += 20
            mess = FONT.render('Equip', True, COLOR)
            messRect = mess.get_rect(center = ((X + (WIDTH / 2)), (Y + (HEIGHT / 2))   ))
            pygame.draw.rect(GameDisplay, kafe_anoixto, [X,Y,WIDTH,HEIGHT])
            GameDisplay.blit(mess, messRect)
        elif equip_status[ITEM] == True:
            mess2 = FONT.render('Equiped', True, COLOR)
            mess2Rect = mess2.get_rect(center = ((X + (WIDTH / 2)), (Y + (HEIGHT / 2))   ))
            GameDisplay.blit(mess2, mess2Rect)

    
            
        

def button(text,x,y,width,height,your_font,color, ac,ic, action = None, item = None):
    global permanent_bought
    not_bought = True
    message = your_font.render(text, True, color)
    messageRect = message.get_rect(center = ((x + (width/2)), (y + (height/2))     ))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+width > mouse[0] > x and  y+height > mouse[1] > y and action == 'Buy':
        if click[0] == 1:
          Buy(item, x, y, width, height, your_font, color, ac, ic)
    elif  x+width > mouse[0] > x and  y+height > mouse[1] > y and action != None:
        pygame.draw.rect(GameDisplay, ac, [x,y,width,height])
        if click[0] == 1:
            if action == "Start":
                main()
            elif action == "Quit":
                pygame.quit()
                quit()
            elif action == "Pause":
                pause()
            elif action == "Back":
                back()
            elif action == "Help":
                help()
            elif action == "Shop":
                Shop()

             
    else:
        pygame.draw.rect(GameDisplay, ic, [x,y,width,height])
    GameDisplay.blit(message, messageRect)
    pygame.display.update()

def pause():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit() 
    button("Resume", 250, 105, 135, 47, font, black, ble_anoixto, ble_skouro)
    button("MainMenu", 250, 175, 135, 47, font, black, ble_anoixto, ble_skouro)
    button("Instructions", 250, 245, 135, 47, font, black, ble_anoixto, ble_skouro)
    button("Quit", 250, 315, 135, 47, font, black, ble_anoixto, ble_skouro)




def Production():
    GameDisplay.fill(black)
    ftiakse_text("SPACEINVADERS", bigfont, 150, 100, white)
    ftiakse_text("By T&D production...", font, 300, 170, white)
    pygame.display.update()
    time.sleep(3)
    

def help():
    boitheia = False
    while not boitheia:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("<-Back", 0, 0, 90, 40, font, black, grey, grey2, "Back")
        ftiakse_text("Instructions", middlefont, 200, 50, black)
        GameDisplay.blit(InstructionsBackround, (0, 0))

        goal = middlefont.render('ALIENS ARE ATTACKING OUR PLANET', True, white)
        goal_2 = font.render('YOU HAVE TO PROTECT THE HUMANITY', True, white)
        real_goal = mikrotera_grammata_freesans.render('You have to kill the aliens with your rockets.', True, white)
        real_goal_2 = mikrotera_grammata_freesans.render("You start the game with 5 lives to endure their attacks and 100hp.", True,
                                                         white)
        real_goal_3 = mikrotera_grammata_freesans.render('Each time an enemy reaches earth, you lose 1 life...', True, white)
        real_goal_4 = mikrotera_grammata_freesans.render('Also, their attacks damage you for 10hp.', True, white)
        real_goal_5 = mikrotera_grammata_freesans.render("At levels 5, 10, 15, strong bosses will be spawned.", True, white)
        real_goal_6 = mikrotera_grammata_freesans.render("Each boss will have more hp and cause more damage than the previous one.", True, white)
        real_goal_7 = mikrotera_grammata_freesans.render("However, you can unlock their bullets at shop by collecting coins.", True, white)
        real_goal_8 = mikrotera_grammata_freesans.render("Each time you die, your score will be converted into coins so as to buy items.", True, white)
        real_goal_9 = mikrotera_grammata_freesans.render("For each level, 3 more aliens will be spawned.", True, white)
        real_goal_10 = mikrotera_grammata_freesans.render("However, fortunately for you, you gain 10hp for each new level", True, white)
        real_goal_11 = mikrotera_grammata_freesans.render("and gain full of your hp by killing each boss.", True, white)
        equip = mikrotera_grammata_freesans.render('Equip items, by moving the cursor in the equip button, with:', True, white)
        throw_rockets = mikrotera_grammata_freesans.render('Launch rockets with:', True, white)
        left_and_right = mikrotera_grammata_freesans.render('Move left or right with:', True, white)
        up_and_down = mikrotera_grammata_freesans.render('Move up  or down with:', True, white)
        message_or = bigfont.render('or', True, white)

        GameDisplay.blit(goal, (display_width / 2 - goal.get_width() / 2, 40))
        GameDisplay.blit(goal_2, (126, 80))
        GameDisplay.blit(real_goal, (50, 140))
        GameDisplay.blit(real_goal_2, (50, 180))
        GameDisplay.blit(real_goal_3, (50, 220))
        GameDisplay.blit(real_goal_4, (50, 260))
        GameDisplay.blit(real_goal_5, (50, 300))
        GameDisplay.blit(real_goal_6, (50, 340))
        GameDisplay.blit(real_goal_7, (50, 380))
        GameDisplay.blit(real_goal_8, (50,420))
        GameDisplay.blit(real_goal_9, (50, 460))
        GameDisplay.blit(real_goal_10, (50, 500))
        GameDisplay.blit(real_goal_11, (50, 530))
        GameDisplay.blit(equip, (50, 560))
        GameDisplay.blit(Button_E, (50  + equip.get_width() , 537))
        GameDisplay.blit(throw_rockets, (50, 600))
        GameDisplay.blit(space_button, (50 + 20 + throw_rockets.get_width(), 600))
        GameDisplay.blit(left_and_right, (50, 650))
        GameDisplay.blit(Button_A, (50 + 20 + left_and_right.get_width(), 630))
        GameDisplay.blit(Button_D, (50 + 20 + left_and_right.get_width() + 70 + 5, 630))
        GameDisplay.blit(up_and_down, (50, 720))
        GameDisplay.blit(Button_W, (50 + 20 + up_and_down.get_width(), 690))
        GameDisplay.blit(Button_S, (50 + 20 + up_and_down.get_width() + 70, 690))

##############################################################################
Delta = False
Kappa = False
Gamma = True
Sigma = False

class Laser():
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)


    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return not self.y + self.img.get_height() >= 0 and self.y <= height

    def collision(self, obj):
        return collide(self, obj)

class Ship():
    COOLDOWN = current_cooldown
    def __init__(self, x, y, health = 100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0


    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)
        pygame.display.update()



    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(display_height):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)
                if obj.health == 0:
                    mhnyma = font.render("Your ship exploded...You lost!", True, white)
                    global GameDisplay
                    global display_width
                    GameDisplay.blit(mhnyma, (display_width / 2 - mhnyma.get_width() / 2, 350))
                    pygame.display.update()
                    time.sleep(2)
                    back()


    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x + 17, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def cooldown(self):
        if self.cool_down_counter == self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1
            


    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()


class Player(Ship):
    def __init__(self, x, y, health = 100):
        super().__init__(x, y, health)
        self.health = current_health
        self.ship_img = YELLOW_SPACE_SHIP
        self.damage = 10
        self.max_health = 100
        # to variable pou xrhsimopoieitai gia na bazei to healthbar sthn mesh ths eikonas tou ship tou player
        self.difference = 10
        if current_health == 110:
            self.difference = 15
            self.max_health = 110
        elif current_health == 120:
            self.difference = 20
            self.max_health = 120
        elif current_health == 130:
            self.difference = 25
            self.max_health = 130
        elif current_health == 140:
            self.difference = 30
            self.max_health = 140
        elif current_health == 150:
            self.difference = 35
            self.max_health = 150
        if equip_status['BOSS_LASER'] == True:
            self.laser_img = BOSS_LASER
            self.damage = 20
        elif equip_status['ULTRA_BOSS_LASER'] == True:
            self.laser_img = ULTRA_BOSS_LASER
            self.damage = 30
        elif equip_status['TERA_BOSS_LASER'] == True:
            self.laser_img = TERA_BOSS_LASER
            self.damage = 40
        else:
            self.laser_img = YELLOW_LASER
            self.damage = 10

        self.mask = pygame.mask.from_surface(self.ship_img)
        self.score = 0

    
    def cooldown(self, cooldown_number):
        if self.cool_down_counter == cooldown_number:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def move_lasers(self, vel, objs, bigobj1, bigobj2, bigobj3, number):
        self.cooldown(number)
        dentro = True
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(display_height):
                self.lasers.remove(laser)
            elif laser.collision(bigobj1):
                if bigobj1.health > 0:
                    bigobj1.health -= self.damage
                    self.lasers.remove(laser)
            elif laser.collision(bigobj2):
                if bigobj2.health > 0:
                    bigobj2.health -= self.damage
                    self.lasers.remove(laser)
            elif laser.collision(bigobj3):
                if bigobj3.health > 0:
                    bigobj3.health -= self.damage
                    self.lasers.remove(laser)
                
                    
            else:
                for obj in objs:
                    if laser.collision(obj):
                        self.lasers.remove(laser)
                        objs.remove(obj)
                        global score
                        score += 1

    def healthbar(self, window):
        pygame.draw.rect(window, red, (self.x - self.difference, self.y + self.get_height(), self.max_health, 10))
        pygame.draw.rect(window, green, (self.x - self.difference, self.y + self.get_height(), self.health, 10))


    def draw(self,window):
        super().draw(window)
        self.healthbar(GameDisplay)
                       
                        


    def shoot2(self):
        if self.cool_down_counter == 0:
            if self.laser_img == TERA_BOSS_LASER:
                laser = Laser(self.x, self.y, self.laser_img)
                self.lasers.append(laser)
                self.cool_down_counter = 1

            else:    
                laser = Laser(self.x - 14, self.y, self.laser_img)
                self.lasers.append(laser)
                self.cool_down_counter = 1



class Enemy(Ship):
    colors_on_pairs = {"red" : [RED_SPACE_SHIP, RED_LASER],
                       "blue" : [BLUE_SPACE_SHIP, BLUE_LASER],
                       "green" : [GREEN_SPACE_SHIP, GREEN_LASER]}


    def __init__(self, x, y, color):
        super().__init__(x, y)
        self.color = color
        self.ship_img, self.laser_img = self.colors_on_pairs[color]
        self.mask = pygame.mask.from_surface(self.ship_img)


    def move(self, vel):
        self.y += vel



class Boss(Ship):
    bosses = {
        1: [BOSS_SPACE_SHIP, BOSS_LASER],
        2: [ULTRA_BOSS_SPACE_SHIP, ULTRA_BOSS_LASER],
        3: [TERA_BOSS_SPACE_SHIP, TERA_BOSS_LASER] }
    def __init__(self, x, y,number):
        super().__init__(x, y)
        self.ship_img, self.laser_img = self.bosses[number]
        self.mask = pygame.mask.from_surface(self.ship_img)
        if number == 1:
            self.health = 150
            self.max_health = 150
        elif number == 2:
            self.health = 200
            self.max_health = 200
        elif number == 3:
            self.health = 250
            self.max_health = 250


    def healthbar(self, window):
        pygame.draw.rect(window, red, (self.x , self.y + self.get_height() , self.get_width(), 10))
        pygame.draw.rect(window, green, (self.x, self.y + self.get_height(), self.get_width() * (self.health / self.max_health), 10)) 

    def draw(self, window):
        super().draw(window)
        self.healthbar(GameDisplay)
        

    def moveBoss(self, vel):
       global Delta
       global Kappa
       global Gamma
       global Sigma
       if Sigma:
           Delta = False
           Kappa = False
           Gamma = True
           Sigma = False
       if Gamma:
           self.y += vel
           if self.y == 100:
               Delta = True
               Gamma = False
               
       elif Delta:
           if self.x == 20:
               Kappa = True
               Delta = False
           else:
               self.x -= vel
       elif Kappa:
           self.x += vel
           if self.x + self.ship_img.get_width() == display_width - 19 or self.x + self.ship_img.get_width() == 748:
               Delta = True
               Kappa = False



    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(display_height):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                if self.ship_img == BOSS_SPACE_SHIP:
                    obj.health -= 20
                elif self.ship_img == ULTRA_BOSS_SPACE_SHIP:
                    obj.health -= 30
                elif self.ship_img == TERA_BOSS_SPACE_SHIP:
                    obj.health -= 40
            
               
                self.lasers.remove(laser)
                if obj.health <= 0:
                    mhnyma = middlefont.render("The Great Boss killed you...", True, white)
                    GameDisplay.blit(mhnyma, (display_width / 2 - mhnyma.get_width() /2, 350))
                    pygame.display.update()
                    time.sleep(1)
                    back()


    def shoot(self):
        if self.cool_down_counter == 0:
            if self.ship_img == TERA_BOSS_SPACE_SHIP:
                laser = Laser(self.x + 100, self.y, self.laser_img)
                self.lasers.append(laser)
                self.cool_down_counter = 1
            else:
                laser = Laser(self.x + 20, self.y, self.laser_img)
                self.lasers.append(laser)
                self.cool_down_counter = 1

    
           
 

def collide(obj1, obj2):
    distance_x = obj2.x - obj1.x
    distance_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (distance_x, distance_y))



def main():
    run = True
    global score
    global boss_presence
    global level
    global vari, kari, mari
    global Sigma, current_health
    boss_presence = True
    vari = True
    kari = True
    mari = True
    Sigma = True
    FPS = 25
    lives = 5
    level = 0
    player_vel2 = 5
    player_vel = current_speed
    player_cooldown = current_cooldown
    enemy_vel = 1
    laser_vel = 8
    boss_vel = 2
    score = 0
    clock = pygame.time.Clock()

    enemies = []
    wave = 0


    player = Player(300,300)
    

    boss1 = Boss(300, -200, 1)
    boss2 = Boss(300, -200, 2)
    boss3 = Boss(300, -200, 3)

    
    
    
    def redraw():
        global level, score
        global vari, kari, mari
        global Sigma, Gamma, Delta, Kappa

        GameDisplay.blit(GameBackround, (0,0))
        level_label = font.render(f"Level: {level}", True, white)
        lives_label = font.render(f"Lives: {lives}", True, white)
        score_label = font.render(f"Score: {score}", True, white)
        GameDisplay.blit(lives_label, (10, 10))
        GameDisplay.blit(level_label, (display_width - level_label.get_width() - 10, 10))
        GameDisplay.blit(score_label, (display_width - score_label.get_width() - 10, 35))
        player.draw(GameDisplay)
        if boss1.health <= 0:
            if vari:
                boss1.x = 2000
                player.health = player.max_health
                level += 1
                score += 10
                Sigma = True
                vari = False
                text = middlefont.render("Wow.. you defeated the great Boss!", True, white)
                GameDisplay.blit(text, (display_width / 2 - text.get_width() / 2, 350))
                pygame.display.update()
                time.sleep(1)

        if boss2.health <= 0:
            if kari:
                boss2.x = 2000
                player.health = player.max_health
                level += 1
                score += 20
                Sigma = True
                kari = False
                text2 = middlefont.render("Wow.. you defeated the Ultra Boss!", True, white)
                GameDisplay.blit(text2, (display_width / 2 - text2.get_width() / 2, 350))
                pygame.display.update()
                time.sleep(1)


        if boss3.health <= 0:
            if mari:
                boss3.x = 2000
                player.health = player.max_health
                level += 1
                score += 30
                Sigma = True
                Gamma = True
                mari = False
                text3 = middlefont.render("Wow.. you defeated the Tera Boss!", True, white)
                GameDisplay.blit(text3, (display_width / 2 - text3.get_width() / 2, 350))
                pygame.display.update()
                time.sleep(1)
                

                    

        if level >= 2 and boss1.health > 0:
            if boss_presence == True:
                boss1.draw(GameDisplay)
        elif level >= 3 and boss2.health > 0:
            if boss_presence == True:
                boss2.draw(GameDisplay)
        elif level >= 4 and boss3.health > 0:
            if boss_presence == True:
                boss3.draw(GameDisplay)

        for enemy in enemies:
            enemy.draw(GameDisplay)

        pygame.display.update()


    while run:
        clock.tick(FPS)
        redraw()
        button("<-Back", 0, display_width - 40, 90, 40, font, black, grey, grey2, "Back")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if len(enemies) == 0:
            level += 1
            wave += 3
            if level != 1 and player.health < 100:
                player.health += 10
            for x in range(wave):
                enemy = Enemy(random.randint(50,display_width - 100), random.randint(-500, -100), random.choice(["red", "blue", "green"]))
                enemies.append(enemy)
                        
        


        for enemy in enemies:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)
            if enemy.y + enemy.get_height() - 50 > display_height:
                enemies.remove(enemy)
                lives -= 1
            if random.randrange(0, 4 * 60) == 1:
                enemy.shoot()

        if lives == 0:
                mhnyma_lost = bigfont.render('You lost!', True, white)
                GameDisplay.blit(mhnyma_lost, (display_width / 2 - mhnyma_lost.get_width() / 2, 350))
                pygame.display.update()
                time.sleep(2)
                main()

        
        player.move_lasers(-laser_vel, enemies, boss1, boss2, boss3,player_cooldown)
        if level >= 2 and  boss1.health > 0:
            boss1.moveBoss(boss_vel)
            boss1.move_lasers(laser_vel, player)
            if random.randrange(0, 1 * 60) == 1:
                boss1.shoot()

        elif level >= 3 and boss2.health > 0:
            boss2.moveBoss(boss_vel)
            boss2.move_lasers(laser_vel, player)
            if random.randint(0, 1 * 60) == 1:
                boss2.shoot()

        elif level >= 4 and boss3.health > 0:
            boss3.moveBoss(boss_vel)
            boss3.move_lasers(laser_vel, player)
            if random.randint(0, 1* 60) == 1:
                boss3.shoot()
 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and player.x + player.ship_img.get_width() < display_width:
            player.x += player_vel
        if keys[pygame.K_a] and player. x > player_vel:
            player.x -= player_vel
        if keys[pygame.K_w] and player.y > player_vel:
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player.ship_img.get_height() + 15 < display_height:
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot2()


            
Production()
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    back()
    






















    
