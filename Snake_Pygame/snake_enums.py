class AudioFile:
    """Sound class to hold all audio files."""

    eat: str = "audio/gulp.wav"
    music: str = "audio/music.ogg"


class Color:
    """Color class to store RGB values for a color."""

    bg: tuple = (0, 0, 0)
    food: tuple = (255, 0, 0)
    snake: tuple = (0, 255, 255)
    text: tuple = (255, 255, 255)


class Direction:
    """Directions used for snake."""

    up: tuple = (0, -1)
    down: tuple = (0, 1)
    right: tuple = (1, 0)
    left: tuple = (-1, 0)


class ImageFile:
    """Image class to hold all image files."""

    body: str = "images/snake_body.png"
    tail: str = "images/snake_tail.png"
    head: str = "images/snake_head.png"
    food: str = "images/food.png"
    game_bg: str = "images/background.png"
    menu_bg: str = "images/main_menu.png"
    game_over_bg: str = "images/game_over.png"


class State:
    """State class to represent the games states."""

    menu: int = 0
    in_game: int = 1
    game_over: int = 2
    end_game: int = 3

    def next_state(state: int) -> int:
        """Get the next state."""

        state = (state + 1) % 3
        return state