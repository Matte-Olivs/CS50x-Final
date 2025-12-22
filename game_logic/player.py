"""This module handles each player's hand, lives count and points using a Player class"""

from common.constants import SCREEN, ICONS, SMALL_FONT, BLACK
from game_logic.player_positions import *
from common.text_handler import display_text


class Player:
    """Handles each player's hand, lives count and points"""
    def __init__(self, pl_num, pl_name, hand, PLAYER_POS):
        self.pl_num = pl_num  # Keeps track of which player: pl_num = 0, pl_num = 1, ...
        self.pl_name = pl_name
        self.hand = hand  # Player's cards in hand
        
        self.is_ready = False
        self.is_turn = False

        self.pl_pos = PLAYER_POS[self.pl_num]  # The player's position on the screen
        
        self.played_card = None 
        self.angle = 0  # Card angle rotation

        self.lives = 3  # Total lives before losing 

        self.call = None  # Declared points
        self.prev_call = None  # Previous call of the player
        self.single_card_call = None  # When a single card is drawn, players choose between win or loss
        self.points = 0  # Actual won points

        self.jolly_val = None  # Keep track of the jolly's value (ace of hearts)
        
        self.rect_created = False
        self.rects = {}


    def add_point(self):
        self.points += 1


    def life_lost(self):
        self.lives -= 1


    def reset_variables(self):
        self.call = None
        self.single_card_call = None
        self.prev_call = None
        self.points = 0
        self.single_card_call = None
        self.jolly_val = None


    def draw_player_info(self):
        """
        Draws each player's stats on the screen.
         - lives(a heart)
         - cards in hand(a magnifying glass)
         - call(a speech bubble)
         - points(a star)
        """
        if self.lives > 0:
            x_lives_calls = 0
            x_cards_points = 0
            y_lives_cards = -40
            y_calls_points = 40

            if self.pl_pos[0] < HALF_WIDTH:
                x_lives_calls = scaler_func(150)
                x_cards_points = scaler_func(200)
            elif self.pl_num == 0:
                x_lives_calls = scaler_func(200)
                x_cards_points = scaler_func(250)
            else:
                x_lives_calls = scaler_func(-200)
                x_cards_points = scaler_func(-150) 

            if self.pl_pos[1] < HALF_HEIGHT:
                y_lives_cards = scaler_func(10)
                y_calls_points = scaler_func(50)
            else:
                y_lives_cards = scaler_func(-50)
                y_calls_points = scaler_func(-10)

            if not self.rect_created:
                self.rect_created = True
                
                lives_rect = ICONS["lives"].get_rect(center = (self.pl_pos[0] + x_lives_calls, self.pl_pos[1] + y_lives_cards))
                cards_rect = ICONS["cards"].get_rect(center = (self.pl_pos[0] + x_cards_points, self.pl_pos[1] + y_lives_cards)) 
                call_rect = ICONS["call"].get_rect(center = (self.pl_pos[0] + x_lives_calls, self.pl_pos[1] + y_calls_points + 4))
                points_rect = ICONS["points"].get_rect(center = (self.pl_pos[0] + x_cards_points, self.pl_pos[1] + y_calls_points))

                self.rects["lives"] = lives_rect
                self.rects["cards"] = cards_rect
                self.rects["call"] = call_rect
                self.rects["points"] = points_rect

            SCREEN.blit(ICONS["lives"], self.rects["lives"])     
            display_text(False, self.lives, SMALL_FONT, BLACK, (self.pl_pos[0] + x_lives_calls, self.pl_pos[1] + y_lives_cards))

            SCREEN.blit(ICONS["cards"], self.rects["cards"])     
            if len(self.hand) > -1:
                display_text(False, len(self.hand), SMALL_FONT, BLACK, (self.pl_pos[0] + x_cards_points + 4, self.pl_pos[1] + y_lives_cards))

            SCREEN.blit(ICONS["call"], self.rects["call"])     
            if self.call != None:
                display_text(False, self.call, SMALL_FONT, BLACK, (self.pl_pos[0] + x_lives_calls, self.pl_pos[1] + y_calls_points))

            SCREEN.blit(ICONS["points"], self.rects["points"])     
            if self.points > -1:
                display_text(False, self.points, SMALL_FONT, BLACK, (self.pl_pos[0] + x_cards_points, self.pl_pos[1] + y_calls_points))
          
