class Settings():
    """Klasa przeznaczona do przechowywania wszystkich ustawień gry."""

    def __init__(self):
        """Inicjalizacja ustawień gry."""
        # Ustawienia ekranu.
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ustawienia dotyczące statku.
        self.ship_speed_factor = 2
