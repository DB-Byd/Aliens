import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions
def run_game():
    # Inicjalizacja gry i utworzenie obiektu ekranu.
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Inwazja obcych")

    # Utworzenie statku kosmicznego.
    ship = Ship(game_settings, screen)

    # Utworzenie grupy przeznaczonej do przechowywania pocisków.
    bullets = Group()

    # Rozpoczęcie pętli głównej gry.
    while True:
        game_functions.check_events(game_settings, screen, ship, bullets)
        ship.update()
        game_functions.update_bullets(bullets)
        game_functions.update_screen(game_settings, screen, ship, bullets)

run_game()
