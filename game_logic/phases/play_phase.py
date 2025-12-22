"""
This module handles the play phase using a PlayPhase class: 
- Players play one card
- Calls "assign_point" to modify each player's point count
"""

from common.constants import *
from card_handling.card_manager import AnimatedCard
from common.text_handler import display_text


class PlayPhase:
    def __init__(self, gameplay):
        self.gameplay = gameplay

        self.card_to_play = None  # Keep track of the card selected by the player


    def check_highest_card(self, played_cards):
        suits = ["hearts", "diamonds", "clubs", "spades"]
        values = ["ace", "3", "king", "queen", "jack", "7", "6", "5", "4", "2"]
        played_index = []

        for card in played_cards:
            value, suit = str(card).split(" of ")    
            if value.casefold() == "ace" and suit.casefold() == "hearts":
                pass
            else:
                played_index.append((suits.index(suit.casefold()), values.index(value.casefold())))

        played_index.sort()
        highest_suit, highest_value = played_index[0]
        highest_card = f"{values[highest_value]} of {suits[highest_suit]}"

        return highest_card


    def assign_point(self, played_cards):
        highest_card = self.check_highest_card(played_cards)

        winning_pl = None
        for player in self.gameplay.players:
            # Check for jolly
            if player.jolly_val == "low":
                pass
            elif player.jolly_val == "high":
                winning_pl = player
                winning_pl.jolly_val = None
                winning_pl.add_point()  # If high, assign the point immediately
            
            # If the jolly hasn't been played or the jolly is low
            if str(player.played_card).casefold() == highest_card.casefold() and winning_pl == None:
                winning_pl = player
                winning_pl.add_point()
            
            player.played_card = None

        self.gameplay.player_index = winning_pl.pl_num
        display_text(True, f"Player {winning_pl.pl_num} won 1 point!", MEDIUM_FONT, BLACK, (HALF_WIDTH, SCREEN_HEIGHT * 0.4))
        pygame.time.wait(1000)


    def everyone_played(self, current_player):
        """Checks if each player has played a card."""
        played_cards = []
        assign_end = False  # Check if the point has been assigned 
        
        for player in self.gameplay.players: 
            if player.played_card:
                played_cards.append(player.played_card)
            
            if len(played_cards) == len(self.gameplay.players):
                self.assign_point(played_cards)
                assign_end = True
        
        if not assign_end:
            display_text(True, f"Player {current_player.pl_num} is choosing...", MEDIUM_FONT, BLACK, (HALF_WIDTH, SCREEN_HEIGHT * 0.4))
        
        return assign_end


    def move_to_end_phase(self):
        empty_hands = 0
        for player in self.gameplay.players:
            if len(player.hand) == 0:
                empty_hands += 1
            if empty_hands == len(self.gameplay.players):
                return True
        
        return False


    def is_jolly(self, current_player):
        """Check if the jolly has been played."""
        
        if str(self.card_to_play).casefold() == "ace of hearts":
            self.gameplay.last_player = current_player
            self.card_to_play = None
            return True
            
        return False


    def execute(self, events): 
        current_player = self.gameplay.players[(self.gameplay.player_index) % len(self.gameplay.players)] 
       
        self.gameplay.card_manager.draw_player_hands(self.gameplay.players, current_player.pl_num, self.gameplay.PLAYER_POS)
        
        if self.card_to_play == None:
            self.card_to_play = self.gameplay.card_manager.handle_input(current_player.hand, self.gameplay.PLAYER_POS,events)  # Play a card from the hand
        
        if not self.gameplay.animating and self.card_to_play:
            self.gameplay.anim_c = AnimatedCard(
                self.card_to_play, 
                (self.gameplay.PLAYER_POS[current_player.pl_num][0], self.gameplay.PLAYER_POS[current_player.pl_num][1]), 
                (self.gameplay.PLAYER_POS[current_player.pl_num][2], self.gameplay.PLAYER_POS[current_player.pl_num][3]), 
                self.gameplay.ANIMATION_DURATION,
                current_player.pl_num, 
                len(self.gameplay.players), 
                True
            )  # Create an animated card object
            self.gameplay.animating = True

        # Animate the card 
        if self.gameplay.animating: 
            self.gameplay.animating = self.gameplay.card_manager.animation(self.gameplay.anim_c, self.gameplay.PLAYER_POS[current_player.pl_num][4])     

            if not self.gameplay.animating:
                if sfx_on[0]:
                    CARD_SOUND.play()
                current_player.played_card = self.card_to_play
                
                # Check for jolly
                if self.is_jolly(current_player):     
                    return "jolly_phase"   
                
                self.card_to_play = None
                
                # Reset the show_cards variable, so that the current player doesn't see the next player's hand
                self.gameplay.card_manager.show_cards = False

                # If the animation is finished and there's no jolly, move to the next player
                self.gameplay.player_index += 1
        
        self.gameplay.card_manager.draw_played_cards(self.gameplay.players, self.gameplay.PLAYER_POS)
        
        # Check when to move to the next phase
        if self.everyone_played(current_player): 
           if self.move_to_end_phase():
                return "end_phase"
        
        return "play_phase"
    