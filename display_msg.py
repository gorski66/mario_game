import pygame

def text_objects(text, font):
    color = (130,210,180)
    text_block = font.render(text, True, color)
    return text_block, text_block.get_rect()


def message_display(text, bkgd):
    x, y = (bkgd.width/2),(bkgd.height/2)
    font_size = 55
    font_style = 'timesnewroman'
    text_obj = pygame.font.SysFont(font_style, font_size)
    text_surf, text_pos = text_objects(text, text_obj)
    text_pos.center = (x, y)

    bkgd.display.blit(text_surf, text_pos)
    pygame.display.update()

def message_display_coins(text, bkgd):
    x, y = (bkgd.width/8),(bkgd.height/20)
    font_size = 55
    font_style = 'timesnewroman'
    text_obj = pygame.font.SysFont(font_style, font_size)
    text_surf, text_pos = text_objects("Coins: "+text, text_obj)
    text_pos.center = (x, y)

    bkgd.display.blit(text_surf, text_pos)
    pygame.display.update()