"""
This module contains constant values used to draw each player's hand on the screen.
The list is different based on the number of players.
Each player has 5 values describing the postions of the cards:
 - [0]: The card's left position when in hand
 - [1]: The card's right position when in hand
 - [2]: The card's left position when played
 - [3]: The card's right position when in hand
 - [4]: The card's rotation
"""

from common.constants import SCREEN_WIDTH, HALF_WIDTH, SCREEN_HEIGHT, HALF_HEIGHT, scaler_func


HAND_START_X_LEFT = int(SCREEN_WIDTH * 0.15)
HAND_START_X_RIGHT = int(SCREEN_WIDTH * 0.85)

HAND_START_Y_BOT = int(SCREEN_HEIGHT * 0.85)
HAND_START_Y_TOP = int(SCREEN_HEIGHT * 0.15)

PLAYED_CARD_X_LEFT = HAND_START_X_LEFT + scaler_func(150)
PLAYED_CARD_X_RIGHT = HAND_START_X_RIGHT - scaler_func(150)

PLAYED_CARD_Y_BOT = HAND_START_Y_BOT - scaler_func(200)
PLAYED_CARD_Y_TOP = HAND_START_Y_TOP + scaler_func(150)

PLAYED_CARD_Y_LCORNER = HAND_START_Y_TOP + scaler_func(150)
PLAYED_CARD_Y_RCORNER = HAND_START_Y_BOT - scaler_func(150)


CARD_SPACING = scaler_func(50)  # Horizontal spacing between cards
HOVER_OFFSET = scaler_func(30) 


TWO_PLAYERS = [
    (HALF_WIDTH, HAND_START_Y_BOT, HALF_WIDTH, PLAYED_CARD_Y_BOT, 0),  # main player 
    (HALF_WIDTH, HAND_START_Y_TOP, HALF_WIDTH, PLAYED_CARD_Y_TOP, 0),  # top-middle player 
]

THREE_PLAYERS = [
    (HALF_WIDTH, HAND_START_Y_BOT, HALF_WIDTH, PLAYED_CARD_Y_BOT, 0),  # main player 
    (HAND_START_X_RIGHT,  HAND_START_Y_TOP, PLAYED_CARD_X_RIGHT, PLAYED_CARD_Y_LCORNER, 135),  # top-right player 
    (HAND_START_X_LEFT,  HAND_START_Y_TOP, PLAYED_CARD_X_LEFT, PLAYED_CARD_Y_LCORNER, 45),  # top-left player 
]

FOUR_PLAYERS = [
    (HALF_WIDTH, HAND_START_Y_BOT, HALF_WIDTH, PLAYED_CARD_Y_BOT, 0),  # main player 
    (HAND_START_X_RIGHT, HALF_HEIGHT, PLAYED_CARD_X_RIGHT - scaler_func(200), HALF_HEIGHT, 90),  # right player 
    (HALF_WIDTH, HAND_START_Y_TOP, HALF_WIDTH, PLAYED_CARD_Y_TOP, 0),  # top-middle player 
    (HAND_START_X_LEFT, HALF_HEIGHT, PLAYED_CARD_X_LEFT + scaler_func(200), HALF_HEIGHT, 90),  # left player 
]

FIVE_PLAYERS = [
    (HALF_WIDTH, HAND_START_Y_BOT, HALF_WIDTH, PLAYED_CARD_Y_BOT, 0),  # main player 
    (HAND_START_X_RIGHT, HALF_HEIGHT, PLAYED_CARD_X_RIGHT - scaler_func(200), HALF_HEIGHT, 90),  # right player 
    (HAND_START_X_RIGHT,  HAND_START_Y_TOP, PLAYED_CARD_X_RIGHT, PLAYED_CARD_Y_LCORNER, 135),  # top-right player 
    (HAND_START_X_LEFT,  HAND_START_Y_TOP, PLAYED_CARD_X_LEFT, PLAYED_CARD_Y_LCORNER, 45),  # top-left player
    (HAND_START_X_LEFT, HALF_HEIGHT, PLAYED_CARD_X_LEFT + scaler_func(200), HALF_HEIGHT, 90),  # left player 
]

SIX_PLAYERS = [
    (HALF_WIDTH, HAND_START_Y_BOT, HALF_WIDTH, PLAYED_CARD_Y_BOT, 0),  # main player 
    (HAND_START_X_RIGHT, HALF_HEIGHT, PLAYED_CARD_X_RIGHT - scaler_func(200), HALF_HEIGHT, 90),  # right player 
    (HAND_START_X_RIGHT,  HAND_START_Y_TOP, PLAYED_CARD_X_RIGHT, PLAYED_CARD_Y_LCORNER, 135),  # top-right player 
    (HALF_WIDTH, HAND_START_Y_TOP, HALF_WIDTH, PLAYED_CARD_Y_TOP, 0),  # top-middle player 
    (HAND_START_X_LEFT,  HAND_START_Y_TOP, PLAYED_CARD_X_LEFT, PLAYED_CARD_Y_LCORNER, 45),  # top-left player
    (HAND_START_X_LEFT, HALF_HEIGHT, PLAYED_CARD_X_LEFT + scaler_func(200), HALF_HEIGHT, 90),  # left player 
]

SEVEN_PLAYERS = [
    (HALF_WIDTH, HAND_START_Y_BOT, HALF_WIDTH, PLAYED_CARD_Y_BOT, 0),  # main player 
    (HAND_START_X_RIGHT,  HAND_START_Y_BOT, PLAYED_CARD_X_RIGHT, PLAYED_CARD_Y_RCORNER, 45),  # bot-right player 
    (HAND_START_X_RIGHT, HALF_HEIGHT, PLAYED_CARD_X_RIGHT - scaler_func(200), HALF_HEIGHT, 90),  # right player 
    (HAND_START_X_RIGHT,  HAND_START_Y_TOP, PLAYED_CARD_X_RIGHT, PLAYED_CARD_Y_LCORNER, 135),  # top-right player
    (HAND_START_X_LEFT,  HAND_START_Y_TOP, PLAYED_CARD_X_LEFT, PLAYED_CARD_Y_LCORNER, 45),  # top-left player 
    (HAND_START_X_LEFT, HALF_HEIGHT, PLAYED_CARD_X_LEFT + scaler_func(200), HALF_HEIGHT, 90),  # left player 
    (HAND_START_X_LEFT,  HAND_START_Y_BOT, PLAYED_CARD_X_LEFT, PLAYED_CARD_Y_RCORNER, 135),  # bot-left player 
]

EIGHT_PLAYERS = [
    (HALF_WIDTH, HAND_START_Y_BOT, HALF_WIDTH, PLAYED_CARD_Y_BOT, 0),  # main player 
    (HAND_START_X_RIGHT,  HAND_START_Y_BOT, PLAYED_CARD_X_RIGHT, PLAYED_CARD_Y_RCORNER, 45),  # bot-right player 
    (HAND_START_X_RIGHT, HALF_HEIGHT, PLAYED_CARD_X_RIGHT - scaler_func(200), HALF_HEIGHT, 90),  # right player
    (HAND_START_X_RIGHT,  HAND_START_Y_TOP, PLAYED_CARD_X_RIGHT, PLAYED_CARD_Y_LCORNER, 135),  # top-right player 
    (HALF_WIDTH, HAND_START_Y_TOP, HALF_WIDTH, PLAYED_CARD_Y_TOP, 0),  # top-middle player 
    (HAND_START_X_LEFT,  HAND_START_Y_TOP, PLAYED_CARD_X_LEFT, PLAYED_CARD_Y_LCORNER, 45),  # top-left player 
    (HAND_START_X_LEFT, HALF_HEIGHT, PLAYED_CARD_X_LEFT + scaler_func(200), HALF_HEIGHT, 90),  # left player 
    (HAND_START_X_LEFT,  HAND_START_Y_BOT, PLAYED_CARD_X_LEFT, PLAYED_CARD_Y_RCORNER, 135)  # bot-left player 
]


def player_pos(num_of_players):
    if num_of_players == 2:
        return TWO_PLAYERS
    elif num_of_players == 3:
        return THREE_PLAYERS
    elif num_of_players == 4:
        return FOUR_PLAYERS
    elif num_of_players == 5:
        return FIVE_PLAYERS
    elif num_of_players == 6:
        return SIX_PLAYERS
    elif num_of_players == 7:
        return SEVEN_PLAYERS
    elif num_of_players == 8:
        return EIGHT_PLAYERS