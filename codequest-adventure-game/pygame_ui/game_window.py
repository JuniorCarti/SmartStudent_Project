"""
PyGame Game Window - Main graphical interface
"""

import pygame
from engine.game_engine import GameEngine
from pygame_ui.ui_elements import Button, TextBox, InventoryPanel, ActionPanel

class GameWindow:
    def __init__(self):
        # Initialize pygame
        pygame.init()
        self.screen = pygame.display.set_mode((1024, 768))
        pygame.display.set_caption("CodeQuest Adventure")
        self.clock = pygame.time.Clock()
        
        # Load game engine
        self.game = GameEngine()
        self.game.initialize_game()
        
        # UI elements
        self.font = pygame.font.SysFont("Arial", 18)
        self.title_font = pygame.font.SysFont("Arial", 24, bold=True)
        self.create_ui()
        
        # Game state
        self.show_inventory = False
        self.current_message = "Welcome to CodeQuest Adventure!"
        self.messages = ["Game started!"]
        
    def create_ui(self):
        # Create direction buttons
        self.direction_buttons = {
            "north": Button(462, 100, 100, 40, "North", lambda: self.handle_direction("north")),
            "south": Button(462, 600, 100, 40, "South", lambda: self.handle_direction("south")),
            "east": Button(762, 350, 100, 40, "East", lambda: self.handle_direction("east")),
            "west": Button(162, 350, 100, 40, "West", lambda: self.handle_direction("west")),
        }
        
        # Action panel
        self.action_panel = ActionPanel(800, 100, 200, 300)
        
        # Room description area
        self.room_text = TextBox(162, 200, 600, 150, "")
        
        # Message log
        self.message_log = TextBox(162, 400, 600, 150, "")
        
        # Inventory panel
        self.inventory_panel = InventoryPanel(200, 150, 600, 400)
        
        # Status display
        self.status_text = TextBox(162, 570, 600, 30, "")
        
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(pygame.mouse.get_pos())
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_i:
                        self.toggle_inventory()
                    elif event.key == pygame.K_ESCAPE:
                        if self.show_inventory:
                            self.show_inventory = False
            
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)
            
        pygame.quit()
        
    def handle_click(self, pos):
        # Handle inventory clicks first
        if self.show_inventory:
            if self.inventory_panel.handle_click(pos, self.game.player, self):
                return
            # Click outside inventory panel closes it
            if not self.inventory_panel.rect.collidepoint(pos):
                self.show_inventory = False
            return
            
        # Check direction buttons
        for button in self.direction_buttons.values():
            if button.rect.collidepoint(pos):
                button.callback()
                return
                
        # Check action panel buttons
        self.action_panel.handle_click(pos, self)
    
    def handle_direction(self, direction):
        result = self.game.parser.parse(f"go {direction}", self.game.player, 
                                     self.game.current_room, self.game.world)
        if result:
            self.game.current_room = result
            self.add_message(f"You go {direction}.")
        else:
            self.add_message(f"You can't go {direction}.")
    
    def handle_look(self):
        self.add_message("You look around...")
        self.update_room_display()
    
    def toggle_inventory(self):
        self.show_inventory = not self.show_inventory
        if self.show_inventory:
            self.inventory_panel.update_items(self.game.player.inventory)
    
    def handle_use_item(self):
        self.add_message("Open inventory (I) and click an item to use it.")
        self.show_inventory = True
        self.inventory_panel.update_items(self.game.player.inventory)
    
    def handle_attack(self):
        creatures = self.game.current_room.creatures
        if creatures:
            # Attack the first creature in the room
            target = creatures[0]
            self.game.parser.parse(f"attack {target.name.lower()}", self.game.player,
                                 self.game.current_room, self.game.world)
        else:
            self.add_message("There's nothing to attack here.")
    
    def update(self):
        # Update room display
        self.update_room_display()
        
        # Update status
        self.status_text.text = f"Health: {self.game.player.health}/{self.game.player.max_health} | Score: {self.game.player.score}"
        
        # Update inventory if open
        if self.show_inventory:
            self.inventory_panel.update_items(self.game.player.inventory)
    
    def update_room_display(self):
        room = self.game.current_room
        room_desc = f"{room.name}\n\n{room.description}"
        
        # Add items and creatures to description
        if room.items:
            room_desc += f"\n\nItems here: {', '.join([item.name for item in room.items])}"
        if room.creatures:
            room_desc += f"\n\nCreatures here: {', '.join([creature.name for creature in room.creatures])}"
            
        self.room_text.text = room_desc
    
    def add_message(self, message):
        self.messages.append(message)
        if len(self.messages) > 5:  # Keep last 5 messages
            self.messages.pop(0)
        self.message_log.text = "\n".join(self.messages)
    
    def draw(self):
        # Clear screen with dark background
        self.screen.fill((30, 30, 40))
        
        # Draw room area background
        pygame.draw.rect(self.screen, (50, 50, 60), (150, 190, 624, 154))
        
        # Draw UI elements
        for button in self.direction_buttons.values():
            button.draw(self.screen)
        
        # Draw action panel
        self.action_panel.draw(self.screen)
        
        # Draw text areas
        self.room_text.draw(self.screen, self.font)
        self.message_log.draw(self.screen, self.font)
        self.status_text.draw(self.screen, self.font)
        
        # Draw inventory if open
        if self.show_inventory:
            self.inventory_panel.draw(self.screen, self.font)
            
        # Draw mini-map or room indicators
        self.draw_room_indicators()
    
    def draw_room_indicators(self):
        # Simple room connection indicators
        exits = self.game.current_room.exits
        colors = {"north": (100, 200, 100), "south": (100, 200, 100), 
                 "east": (100, 200, 100), "west": (100, 200, 100)}
        
        for direction in exits:
            if direction == "north":
                pygame.draw.polygon(self.screen, colors[direction], 
                                  [(512, 80), (502, 100), (522, 100)])
            elif direction == "south":
                pygame.draw.polygon(self.screen, colors[direction], 
                                  [(512, 620), (502, 600), (522, 600)])
            elif direction == "east":
                pygame.draw.polygon(self.screen, colors[direction], 
                                  [(812, 384), (792, 374), (792, 394)])
            elif direction == "west":
                pygame.draw.polygon(self.screen, colors[direction], 
                                  [(212, 384), (232, 374), (232, 394)])