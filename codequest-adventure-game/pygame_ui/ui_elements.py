"""
UI Elements for PyGame interface
"""

import pygame

class Button:
    def __init__(self, x, y, width, height, text, callback):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.callback = callback
        self.color = (70, 70, 90)
        self.hover_color = (90, 90, 110)
        self.text_color = (255, 255, 255)
        self.border_color = (100, 100, 120)
        
    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color
        
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, self.border_color, self.rect, 2)
        
        font = pygame.font.SysFont("Arial", 16)
        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

class TextBox:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.bg_color = (40, 40, 50)
        self.text_color = (255, 255, 255)
        self.border_color = (80, 80, 100)
        
    def draw(self, screen, font):
        pygame.draw.rect(screen, self.bg_color, self.rect)
        pygame.draw.rect(screen, self.border_color, self.rect, 2)
        
        # Render wrapped text
        y_offset = 5
        for line in self._wrap_text(font):
            text_surface = font.render(line, True, self.text_color)
            screen.blit(text_surface, (self.rect.x + 10, self.rect.y + y_offset))
            y_offset += font.get_height() + 2
            
    def _wrap_text(self, font):
        if not self.text:
            return []
            
        words = self.text.split(' ')
        lines = []
        current_line = []
        
        for word in words:
            test_line = ' '.join(current_line + [word])
            test_width = font.size(test_line)[0]
            
            if test_width <= self.rect.width - 20:
                current_line.append(word)
            else:
                lines.append(' '.join(current_line))
                current_line = [word]
                
        if current_line:
            lines.append(' '.join(current_line))
            
        return lines

class InventoryPanel:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.items = []
        self.item_buttons = []
        self.bg_color = (40, 40, 50)
        self.border_color = (80, 80, 100)
        
    def update_items(self, inventory):
        self.items = inventory
        self.item_buttons = []
        
        for i, item in enumerate(inventory):
            btn_y = self.rect.y + 50 + i * 40
            self.item_buttons.append({
                'rect': pygame.Rect(self.rect.x + 20, btn_y, self.rect.width - 40, 30),
                'item': item
            })
            
    def handle_click(self, pos, player, game_window):
        for item_btn in self.item_buttons:
            if item_btn['rect'].collidepoint(pos):
                # Try to use the item
                result = player.use_item(item_btn['item'].name)
                if result:
                    game_window.add_message(f"You used {item_btn['item'].name}.")
                else:
                    game_window.add_message(f"Cannot use {item_btn['item'].name} here.")
                return True
        return False
        
    def draw(self, screen, font):
        # Draw background with semi-transparency
        s = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        s.fill((40, 40, 50, 240))  # Semi-transparent
        screen.blit(s, (self.rect.x, self.rect.y))
        
        pygame.draw.rect(screen, self.border_color, self.rect, 2)
        
        # Draw title
        title_font = pygame.font.SysFont("Arial", 20, bold=True)
        title = title_font.render("Inventory", True, (255, 255, 255))
        screen.blit(title, (self.rect.x + 20, self.rect.y + 15))
        
        # Draw close button
        close_btn = pygame.Rect(self.rect.right - 30, self.rect.y + 10, 20, 20)
        pygame.draw.rect(screen, (200, 50, 50), close_btn)
        pygame.draw.line(screen, (255, 255, 255), (close_btn.x+5, close_btn.y+5), 
                       (close_btn.right-5, close_btn.bottom-5), 2)
        pygame.draw.line(screen, (255, 255, 255), (close_btn.x+5, close_btn.bottom-5), 
                       (close_btn.right-5, close_btn.y+5), 2)
        
        # Draw items
        for i, item_btn in enumerate(self.item_buttons):
            # Draw item button
            mouse_pos = pygame.mouse.get_pos()
            color = (60, 60, 80) if item_btn['rect'].collidepoint(mouse_pos) else (50, 50, 70)
            pygame.draw.rect(screen, color, item_btn['rect'])
            pygame.draw.rect(screen, (70, 70, 90), item_btn['rect'], 1)
            
            # Draw item name
            item_text = font.render(item_btn['item'].name, True, (255, 255, 255))
            screen.blit(item_text, (item_btn['rect'].x + 10, item_btn['rect'].y + 5))

class ActionPanel:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.buttons = [
            Button(x, y, width, 40, "Look", None),
            Button(x, y + 50, width, 40, "Inventory (I)", None),
            Button(x, y + 100, width, 40, "Use Item", None),
            Button(x, y + 150, width, 40, "Attack", None),
            Button(x, y + 200, width, 40, "Save Game", None)
        ]
        
    def handle_click(self, pos, game_window):
        for i, button in enumerate(self.buttons):
            if button.rect.collidepoint(pos):
                if i == 0:  # Look
                    game_window.handle_look()
                elif i == 1:  # Inventory
                    game_window.toggle_inventory()
                elif i == 2:  # Use Item
                    game_window.handle_use_item()
                elif i == 3:  # Attack
                    game_window.handle_attack()
                elif i == 4:  # Save
                    game_window.add_message("Save feature coming soon!")
                return True
        return False
        
    def draw(self, screen):
        # Draw panel background
        pygame.draw.rect(screen, (50, 50, 60), self.rect)
        pygame.draw.rect(screen, (70, 70, 90), self.rect, 2)
        
        # Draw buttons
        for button in self.buttons:
            button.draw(screen)