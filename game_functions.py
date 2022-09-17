import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, game_settings, screen, ship, bullets):
    """Reakcja na naciśnięcie klawisza."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(game_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
    """Reakcja na zwolnienie klawisza."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
def check_events(game_settings, screen, ship, bullets):
    """Reakcja na zdarzenia generowane przez klawiaturę i mysz."""
    # Oczekiwanie na naciśnięcie klawisza lub przycisku myszy.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def fire_bullet(game_settings, screen, ship, bullets):
    """Wystrzelenie pocisku, jeśli nie przekroczono ustalonego limitu."""
    # Utworzenie nowego pocisku i dodanie go do grupy pocisków.
    if len(bullets) < game_settings.bullets_allowed:
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)

def update_screen(game_settings, screen, ship, bullets):
    """Uaktualnienie obrazów na ekranie i przejście do nowego ekranu."""
    # Odświeżenie ekranu w trakcie każdej iteracji pętli.
    screen.fill(game_settings.bg_color)

# Tu był błąd: kiedy linię 41 miałem pod 48, nie wyświetlały się pociski.

    # Ponowne wyświetlenie wszystkich pocisków pod warstwami statku kosmicznego
    # i obcych.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # Wyświetlenie ostatnio zmodyfikowanego ekranu.
    pygame.display.flip()

def update_bullets(bullets):
    """Uaktualnienie położenia pocisków i usunięcie tych niewidocznych na ekranie."""
    bullets.update()

    # Usunięcie pocisków, które znajdują się poza ekranem.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)