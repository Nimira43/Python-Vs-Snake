WINDOW_SIZE = (800, 600)
FIELDS = (20, 15)
START_POS = (5, int(FIELDS[1] / 2))
DIRECTIONS = {'left': [-1, 0], 'right': [1, 0], 'up': [0, -1], 'down': [0, 1]}
REFRESH_SPEED = 250

LEFT_LIMIT = -1
TOP_LIMIT = 0
RIGHT_LIMIT = FIELDS[0]
BOTTOM_LIMIT = FIELDS[1]
SNAKE_BODY_COLOUR = '#ff4500'
SNAKE_HEAD_COLOUR = '#111111'
APPLE_COLOUR = '#00ff00'