"""
This module contains:
 - A player class to handle each player's hand, played card/s, lives, call etc...
 - A GameLogic class to handle each step of the game
"""

from common.button import handle_buttons
from common.constants import *
from card_handling.card_manager import CardManager
from game_logic.player_positions import player_pos
from common.text_handler import display_text

from game_logic.player import Player
from . import phases


class GameLogic:
    """Handles the game logic."""
    def __init__(self, len_players):
        
        """General use variables.""" 
        self.players = []  # List of the current players 
        self.len_players = len_players  # Total number of players
        self.PLAYER_POS = player_pos(len_players)  # Player positions used for placing cards on the screen and animations
        self.initialize_players() 
        
        self.turn = 1  # Turn counter
        self.player_index = 0  # Keep track of which player has to make a move
    
        self.last_player = None  # Keep track of the last player who has made a move
    
        self.card_manager = CardManager(self)  # Create a CardManager object to handle the graphics
        self.deck = self.card_manager.deck  # Take the deck from the CardManager object
        
        self.drawn = None  # Card to draw from self.deck
        self.anim_c = None  # Card to animate
        self.animating = False  # Keep track of the animation end
        self.ANIMATION_DURATION = 0.2
        
        """Game phases.""" 
        self.phase = "draw_phase"  # Phase tracker

        self.draw_phase = phases.DrawPhase(self)
        self.call_phase = phases.CallPhase(self)
        self.recall_phase = phases.RecallPhase(self, self.call_phase)
        self.single_call_phase = phases.SingleCallPhase(self)
        self.play_phase = phases.PlayPhase(self)
        self.jolly_phase = phases.JollyPhase(self)
        self.end_phase = phases.EndPhase(self)
         

    def initialize_players(self):
        """Initializes each player by adding them to self.players."""
        for i in range(0, self.len_players):
            hand = []
            self.players.append(Player(i, None, hand, self.PLAYER_POS))


    def cards_to_draw(self):
        """Calculates the numbers of cards to draw on each turn."""
        CARDS_NUM = [num for num in range(1, 6)]  # Possible card numbers in hand
        CARDS_NUM.reverse() 
        return CARDS_NUM[(self.turn % 5) - 1]


    def winner_found(self):
        if len(self.players) == 1:
            SCREEN.blit(TABLE_BACKGROUND, (0, 0))
            display_text(True, f"Player {self.players[0].pl_num} won!", MEDIUM_FONT, BLACK, (HALF_WIDTH, HALF_HEIGHT))   
            pygame.display.flip() 
            pygame.time.wait(2000)     
            
            SCREEN.blit(TABLE_BACKGROUND, (0, 0))  
            pygame.display.flip()
            
            return True
        return False


    def gameplay(self, events):
        SCREEN.blit(TABLE_BACKGROUND, (0, 0))  # Blits the background
        
        if self.phase != "draw_phase":
            self.card_manager.draw_deck(self.deck)  # Blits the deck
            
            for player in self.players:
                player.draw_player_info()

        to_draw = self.cards_to_draw()
        handle_buttons(self.card_manager.btns, events)

        if self.phase == "draw_phase":
            self.phase = self.draw_phase.execute(to_draw)
        elif self.phase == "call_phase":
            self.phase = self.call_phase.execute(to_draw, events)
        elif self.phase == "recall_phase":
            self.phase = self.recall_phase.execute(events)
        elif self.phase == "single_call_phase":
            self.phase = self.single_call_phase.execute(events)
        elif self.phase == "play_phase":
            self.phase = self.play_phase.execute(events)
        elif self.phase == "jolly_phase":
            self.phase = self.jolly_phase.execute(events)
        elif self.phase == "end_phase":
            self.phase = self.end_phase.execute()
            self.turn += 1

        if self.winner_found():
            return "menu"
        
        return "lan_game"
            