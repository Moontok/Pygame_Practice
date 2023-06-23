class GameManager:
    """
    Manages general settings and states of the game.
    """

    def __init__(self, clock):
        self.window_width = 800
        self.window_height = self.window_width
        self.game_speed = 10 
        self.segment_size = self.window_width / 20      

        self.game_running = True
        self.in_main_menu = True
        self.playing_game = False
        self.game_over_screen = False

        self.clock = clock

    def tick(self):
        """
        Tick the clock.
        """

        self.clock.tick(self.game_speed)

    def center(self):
        """
        Get the center of the screen.
        """

        return (self.window_width / 2, self.window_height / 2)
    
    def get_dimensions(self):
        """
        Get the dimensions of the screen.
        """

        return (self.window_width, self.window_height)

