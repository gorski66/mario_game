import pygame
from menu import Menu

if __name__ == "__main__":
    pygame.font.init()
    pygame.init()
    pygame.mixer.Sound('audio\level_music.wav').play()
    Menu.display_menu()











