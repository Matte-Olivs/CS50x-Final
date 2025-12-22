"""
This module contains a CardManager class to handle the behaviour of cards, such as
blitting the deck, player hands, animations etc...
"""

from common.button import Button
from common.constants import *
from card_handling.deck import *


class CardManager:
    """Handles the animation of cards and user input."""
    def __init__(self, gameplay):
        self.deck = Deck()
        self.gameplay = gameplay

        self.animated_cards = []
        self.hovered_card_index = None
 
        # Pre-rotate card backs for side players
        self.rotated_back_sides = pygame.transform.rotate(Deck.back_image, 90)
        self.rotated_back_main_diag = pygame.transform.rotate(Deck.back_image, 45)
        self.rotated_back_sec_diag = pygame.transform.rotate(Deck.back_image, 135)

        # Show cards button
        self.show_cards = False
        btn = Button(
            (SCREEN_WIDTH * 0.6), SCREEN_HEIGHT * 0.7, BUTTON_WIDTH * 0.6, BUTTON_HEIGHT * 0.8, 
            BUTTON_TEXT_SIZE, BUTTON_BACKGROUND, None, 
            text="Reveal", on_click_callback=self.see_hand
        )
        self.btns = []
        self.btns.append(btn)


    def see_hand(self):
        if self.show_cards == True:
            self.show_cards = False
        else:
            self.show_cards = True


    def handle_input(self, hand, player_pos, events): 
        """Handle click on a card in hand."""
        self.check_hover(hand, player_pos)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:              
                if self.hovered_card_index is not None and self.show_cards:
                    card_to_play = hand.pop(self.hovered_card_index) 
                    return card_to_play    

                
    def check_hover(self, hand, player_pos):
        """Checks if the mouse pos is hover a card in the hand of the main player."""
        self.hovered_card_index = None
        if hand:
            total_hand_width = (len(hand) - 1) * CARD_SPACING
            hand_start_x = player_pos[0][0] - total_hand_width // 2
            hand_start_y = player_pos[0][1]

            # Iterate right to left for checking the visible part of the cards
            for i in reversed(range(len(hand))):
                card = hand[i]
                card_rect = card.image.get_rect(center=(hand_start_x + i * CARD_SPACING, hand_start_y))
                
                mouse_x, mouse_y = pygame.mouse.get_pos()
                offset_x = mouse_x - card_rect.x
                offset_y = mouse_y - card_rect.y
                
                if offset_x >= 0 and offset_x < card.image.get_width() and offset_y >= 0 and offset_y < card.image.get_height():
                    if card.mask.get_at((offset_x, offset_y)):
                        self.hovered_card_index = i
                        break

   
    def draw_deck(self, deck, rotation=None):
        """Draws the deck at the center of the screen and rotates it during the draw phase."""
        if deck:
            if rotation:
                rotate = pygame.transform.rotate(Deck.back_image, rotation)
                deck_rect = rotate.get_rect(center=(HALF_WIDTH, HALF_HEIGHT))
                SCREEN.blit(rotate, deck_rect)
            else:
                deck_rect = Deck.back_image.get_rect(center=(HALF_WIDTH, HALF_HEIGHT))
                SCREEN.blit(Deck.back_image, deck_rect)


    def draw_player_hands(self, players, pl_num, player_pos):
        """Draws the current player's hand, other players are represented by a single rotated card."""

        for player in players:
            if player.pl_num == pl_num: 
                if player.hand and self.show_cards:       
                    total_hand_width = (len(player.hand) - 1) * CARD_SPACING
                    hand_start_x = player_pos[0][0] - total_hand_width // 2
                                
                    for i, card in enumerate(player.hand):
                        if card:
                            vertical_offset_hover = HOVER_OFFSET if i == self.hovered_card_index and self.gameplay.phase == "play_phase" else 0
                            card_rect = card.image.get_rect(center=(hand_start_x + i * CARD_SPACING, player_pos[0][1] - vertical_offset_hover))
                            SCREEN.blit(card.image, card_rect)   
          
            if player.hand and not self.show_cards: 
                rotate = pygame.transform.rotate(Deck.back_image, player_pos[player.pl_num][4])
                card_rect = rotate.get_rect(center = (player_pos[player.pl_num][0], player_pos[player.pl_num][1]))
                SCREEN.blit(rotate, card_rect)

            if player.hand and player.pl_num != 0:
                rotate = pygame.transform.rotate(Deck.back_image, player_pos[player.pl_num][4])
                card_rect = rotate.get_rect(center = (player_pos[player.pl_num][0], player_pos[player.pl_num][1]))
                SCREEN.blit(rotate, card_rect)
            
            
    def single_card_round(self, players, PLAYER_POS, current_player):
        """Handles the rounds that have a single card to draw."""
        for player in players:
            card = player.hand[0]
            card_rect = card.image.get_rect(center=(PLAYER_POS[player.pl_num][0], PLAYER_POS[player.pl_num][1]))
            card_rect_current_player = Deck.back_image.get_rect(center=(PLAYER_POS[current_player.pl_num][0], PLAYER_POS[current_player.pl_num][1]))
            SCREEN.blit(card.image, card_rect)
            SCREEN.blit(Deck.back_image, card_rect_current_player)
     
     
    def draw_played_cards(self, players, PLAYER_POS):
        """Draws the cards played by each player in front of them."""
        for player in players:
            if player.played_card:
                rotate = pygame.transform.rotate(player.played_card.image, PLAYER_POS[player.pl_num][4])
                played_rect = rotate.get_rect(center=(PLAYER_POS[player.pl_num][2], PLAYER_POS[player.pl_num][3]))
                SCREEN.blit(rotate, played_rect)


    def animation(self, anim_c, player_pos):
        """Animates a given card. It also rotates the card based on the player's position."""
        if anim_c.elapsed_time >= anim_c.duration:
            return False  # If the animation has finished, return False
        else:
            current_pos = anim_c.get_current_pos()
            
            if anim_c.is_face_up:
                card_surface = anim_c.card.image  # If the card is drawn, move it face down
            else:
                card_surface = Deck.back_image
            rotate = pygame.transform.rotate(card_surface, player_pos)
            card_rect = rotate.get_rect(center = current_pos)
            SCREEN.blit(rotate, card_rect)           
            return True
     