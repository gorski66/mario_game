import pygame, sys, player, event, display, hit_boxes,display_2,hit_boxes_2


from button import Button

SCREEN = pygame.display.set_mode((900, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

ev = event.Event()
play = player.Player()
play2 = player.Player()
bkgd = display.Canvas(play)
bkgd2 = display_2.Canvas_2(play)
coins = hit_boxes.HitBox()
coins2 = hit_boxes_2.HitBox_next()


def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

class Menu:

    def play_game():

        while True:

            bkgd.show(play)
            ev.check_event(play, bkgd, coins)
            play.collision(bkgd, coins)
            coins.show(bkgd)
            play.win(bkgd, coins)

            bkgd.time.tick(bkgd.fps)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def play_game_next():

        while True:
            bkgd2.show(play2)
            ev.check_event(play2, bkgd2, coins2)
            play2.collision(bkgd2, coins2)
            coins2.show(bkgd2)
            play.win2(bkgd2, coins2)

            bkgd2.time.tick(bkgd2.fps)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()



    def display_menu():

        while True:

            SCREEN.blit(BG, (0, 0))
            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = get_font(60).render("MAIN MENU", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(460, 100))

            PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(460, 350),
                                 text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
            QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(460, 550),
                                 text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

            SCREEN.blit(MENU_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        Menu.play_game()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()
            pygame.display.update()

    def display_end_menu():

        while True:

            SCREEN.blit(BG, (0, 0))
            MENU_MOUSE_POS = pygame.mouse.get_pos()


            NEXT_LEVEL_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(460, 350),
                                 text_input="NEXT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")


            QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(460, 550),
                                 text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")




            for button in [NEXT_LEVEL_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(SCREEN)

            for button in [QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if NEXT_LEVEL_BUTTON.checkForInput(MENU_MOUSE_POS):
                        Menu.play_game_next()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()
            pygame.display.update()









    def display_quit():

        while True:

            SCREEN.blit(BG, (0, 0))
            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = get_font(60).render("GOOD GAME!", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(460, 100))

            QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(460, 350),
                                 text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

            SCREEN.blit(MENU_TEXT, MENU_RECT)


            for button in [QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()
            pygame.display.update()

