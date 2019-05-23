import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions
from pygame.sprite import Group


def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption(game_settings.game_caption)
    ship = Ship(game_settings, screen)
    aliens = Group()
    bullets = Group()
    game_functions.create_fleet(game_settings, screen, ship, aliens)
    while True:
        game_functions.check_events(game_settings, screen, ship, bullets)
        ship.update()
        game_functions.update_bullets(bullets)
        game_functions.update_screen(
            game_settings, screen, ship, aliens, bullets)


run_game()
