import pygame
import numpy as np
import time
import copy
import math
import random
import pytesseract
from PIL import Image, ImageDraw, ImageFont
import io
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# Initialize pygame
pygame.init()

# Light mode colors
LIGHT_WHITE = (255, 255, 255)
LIGHT_BLACK = (0, 0, 0)
LIGHT_GRAY = (200, 200, 200)
LIGHT_BLUE = (96, 216, 232)
LIGHT_RED = (255, 0, 0)
LIGHT_GREEN = (0, 255, 0)
LIGHT_BLUE = (0, 0, 255)
LIGHT_DARK_GRAY = (100, 100, 100)
LIGHT_LIGHT_RED = (255, 200, 200)
LIGHT_LIGHT_GREEN = (200, 255, 200)
LIGHT_DARK_BLUE = (0, 0, 150)
LIGHT_PURPLE = (128, 0, 128)
LIGHT_LIGHT_PURPLE = (200, 150, 255)
LIGHT_GOLD = (255, 215, 0)
LIGHT_LIGHT_GOLD = (255, 240, 200)
LIGHT_GRID_COLOR = (220, 220, 220)
LIGHT_SELECTION_COLOR = (200, 230, 255)
LIGHT_NOTE_COLOR = (150, 150, 150)
LIGHT_BACKGROUND_COLOR = (245, 245, 245)
LIGHT_TEXT_COLOR = (0, 0, 0)  # Black text for light mode
LIGHT_ORIGINAL_NUMBER_COLOR = (0, 0, 0)  # Black for original numbers in light mode
LIGHT_GENERATED_COLOR = (0, 0, 0)  # Black for generated numbers in light mode
LIGHT_HANDWRITTEN_COLOR = (0, 120, 215)  # Blue for handwritten numbers in light mode

# Dark mode colors
DARK_WHITE = (240, 240, 240)
DARK_BLACK = (30, 30, 30)
DARK_GRAY = (60, 60, 60)
DARK_BLUE = (0, 120, 215)
DARK_RED = (255, 50, 50)
DARK_GREEN = (50, 255, 50)
DARK_BLUE = (50, 150, 255)
DARK_DARK_GRAY = (80, 80, 80)
DARK_LIGHT_RED = (255, 100, 100)
DARK_LIGHT_GREEN = (100, 255, 100)
DARK_DARK_BLUE = (0, 0, 100)
DARK_PURPLE = (150, 50, 150)
DARK_LIGHT_PURPLE = (180, 100, 255)
DARK_GOLD = (255, 200, 0)
DARK_LIGHT_GOLD = (255, 220, 100)
DARK_GRID_COLOR = (50, 50, 50)
DARK_SELECTION_COLOR = (50, 70, 100)
DARK_NOTE_COLOR = (180, 180, 180)  # Brighter notes for better visibility
DARK_BACKGROUND_COLOR = (20, 20, 20)
DARK_TEXT_COLOR = (240, 240, 240)  # White text for dark mode
DARK_ORIGINAL_NUMBER_COLOR = (240, 240, 240)  # White for original numbers in dark mode
DARK_GENERATED_COLOR = (255, 255, 255)  # White for generated numbers in dark mode
DARK_HANDWRITTEN_COLOR = (255, 255, 255)  # White for handwritten numbers in dark mode

# Default to dark mode
WHITE = DARK_WHITE
BLACK = DARK_BLACK
GRAY = DARK_GRAY
BLUE = DARK_BLUE
RED = DARK_RED
GREEN = DARK_GREEN
DARK_GRAY = DARK_DARK_GRAY
LIGHT_RED = DARK_LIGHT_RED
LIGHT_GREEN = DARK_LIGHT_GREEN
DARK_BLUE = DARK_DARK_BLUE
PURPLE = DARK_PURPLE
LIGHT_PURPLE = DARK_LIGHT_PURPLE
GOLD = DARK_GOLD
LIGHT_GOLD = DARK_LIGHT_GOLD
GRID_COLOR = DARK_GRID_COLOR
SELECTION_COLOR = DARK_SELECTION_COLOR
NOTE_COLOR = DARK_NOTE_COLOR
BACKGROUND_COLOR = DARK_BACKGROUND_COLOR
TEXT_COLOR = DARK_TEXT_COLOR
ORIGINAL_NUMBER_COLOR = DARK_ORIGINAL_NUMBER_COLOR

# Global theme state
dark_mode = True

CONFETTI_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]

# Screen dimensions
WIDTH, HEIGHT = 540, 600
GRID_SIZE = 9
CELL_SIZE = WIDTH // GRID_SIZE

# Fonts
FONT = pygame.font.SysFont('Arial', 35)
BUTTON_FONT = pygame.font.SysFont('Arial', 20)
NOTES_FONT = pygame.font.SysFont('Arial', 12)
TITLE_FONT = pygame.font.SysFont('Arial', 50)
SUBTITLE_FONT = pygame.font.SysFont('Arial', 25)
WIN_FONT = pygame.font.SysFont('Arial', 60)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sudoku')

def set_theme(dark_mode):
    global WHITE, BLACK, GRAY, BLUE, RED, GREEN, DARK_GRAY, LIGHT_RED, LIGHT_GREEN
    global DARK_BLUE, PURPLE, LIGHT_PURPLE, GOLD, LIGHT_GOLD, GRID_COLOR
    global SELECTION_COLOR, NOTE_COLOR, BACKGROUND_COLOR, TEXT_COLOR, ORIGINAL_NUMBER_COLOR
    
    if dark_mode:
        WHITE = DARK_WHITE
        BLACK = DARK_BLACK
        GRAY = DARK_GRAY
        BLUE = DARK_BLUE
        RED = DARK_RED
        GREEN = DARK_GREEN
        DARK_GRAY = DARK_DARK_GRAY
        LIGHT_RED = DARK_LIGHT_RED
        LIGHT_GREEN = DARK_LIGHT_GREEN
        DARK_BLUE = DARK_DARK_BLUE
        PURPLE = DARK_PURPLE
        LIGHT_PURPLE = DARK_LIGHT_PURPLE
        GOLD = DARK_GOLD
        LIGHT_GOLD = DARK_LIGHT_GOLD
        GRID_COLOR = DARK_GRID_COLOR
        SELECTION_COLOR = DARK_SELECTION_COLOR
        NOTE_COLOR = DARK_NOTE_COLOR
        BACKGROUND_COLOR = DARK_BACKGROUND_COLOR
        TEXT_COLOR = DARK_TEXT_COLOR
        ORIGINAL_NUMBER_COLOR = DARK_ORIGINAL_NUMBER_COLOR
    else:
        WHITE = LIGHT_WHITE
        BLACK = LIGHT_BLACK
        GRAY = LIGHT_GRAY
        BLUE = LIGHT_BLUE
        RED = LIGHT_RED
        GREEN = LIGHT_GREEN
        DARK_GRAY = LIGHT_DARK_GRAY
        LIGHT_RED = LIGHT_LIGHT_RED
        LIGHT_GREEN = LIGHT_LIGHT_GREEN
        DARK_BLUE = LIGHT_DARK_BLUE
        PURPLE = LIGHT_PURPLE
        LIGHT_PURPLE = LIGHT_LIGHT_PURPLE
        GOLD = LIGHT_GOLD
        LIGHT_GOLD = LIGHT_LIGHT_GOLD
        GRID_COLOR = LIGHT_GRID_COLOR
        SELECTION_COLOR = LIGHT_SELECTION_COLOR
        NOTE_COLOR = LIGHT_NOTE_COLOR
        BACKGROUND_COLOR = LIGHT_BACKGROUND_COLOR
        TEXT_COLOR = LIGHT_TEXT_COLOR
        ORIGINAL_NUMBER_COLOR = LIGHT_ORIGINAL_NUMBER_COLOR

class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.size = random.randint(5, 10)
        self.speed_x = random.uniform(-5, 5)
        self.speed_y = random.uniform(-10, -5)
        self.gravity = 0.3
        self.life = 1.0
        self.decay = random.uniform(0.01, 0.03)
    
    def update(self):
        self.x += self.speed_x
        self.speed_y += self.gravity
        self.y += self.speed_y
        self.life -= self.decay
        return self.life > 0
    
    def draw(self, screen):
        alpha = int(255 * self.life)
        color = (*self.color, alpha)
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), self.size)

class WinAnimation:
    def __init__(self):
        self.particles = []
        self.duration = 3.0
        self.start_time = time.time()
        self.active = True
        self.text_alpha = 0
        self.text_scale = 0.5
    
    def update(self):
        if not self.active:
            return False
        
        current_time = time.time() - self.start_time
        if current_time > self.duration:
            self.active = False
            return False
        
        # Update text animation
        self.text_alpha = min(255, int(255 * (current_time / 0.5)))
        self.text_scale = min(1.0, 0.5 + (current_time / 0.5) * 0.5)
        
        # Add new particles
        if random.random() < 0.3:
            x = random.randint(0, WIDTH)
            y = HEIGHT
            color = random.choice(CONFETTI_COLORS)
            self.particles.append(Particle(x, y, color))
        
        # Update existing particles
        self.particles = [p for p in self.particles if p.update()]
        
        return True
    
    def draw(self, screen):
        # Draw particles
        for particle in self.particles:
            particle.draw(screen)
        
        # Draw win text
        text = WIN_FONT.render("You Win!", True, GREEN)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        
        # Scale and fade text
        scaled_text = pygame.transform.scale(text, 
            (int(text.get_width() * self.text_scale), 
             int(text.get_height() * self.text_scale)))
        scaled_rect = scaled_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        
        # Create a surface for the text with alpha
        text_surface = pygame.Surface((scaled_text.get_width(), scaled_text.get_height()), pygame.SRCALPHA)
        text_surface.blit(scaled_text, (0, 0))
        text_surface.set_alpha(self.text_alpha)
        
        screen.blit(text_surface, scaled_rect)

class GameState:
    def __init__(self, board, notes):
        self.board = copy.deepcopy(board)
        self.notes = copy.deepcopy(notes)

class Animation:
    def __init__(self, duration=0.3):
        self.start_time = time.time()
        self.duration = duration
        self.active = True
    
    def get_progress(self):
        if not self.active:
            return 1.0
        progress = (time.time() - self.start_time) / self.duration
        if progress >= 1.0:
            self.active = False
            return 1.0
        return progress
    
    def get_eased_progress(self):
        progress = self.get_progress()
        # Ease-out cubic
        return 1 - (1 - progress) ** 3

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, hotkey=None, tooltip=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.current_color = color
        self.hotkey = hotkey
        self.tooltip = tooltip
        self.is_hovered = False
        self.animation = None
        self.original_y = y
        self.tooltip_visible = False
        self.tooltip_timer = 0
        
    def draw(self, screen):
        # Draw button background with rounded corners
        radius = 10
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.current_color, rect, border_radius=radius)
        
        # Draw button text
        text_surface = BUTTON_FONT.render(self.text, True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(text_surface, text_rect)
        
        # Draw tooltip if hovered for more than 0.5 seconds
        if self.tooltip_visible and self.tooltip:
            tooltip_surface = BUTTON_FONT.render(self.tooltip, True, TEXT_COLOR)
            tooltip_rect = tooltip_surface.get_rect(midbottom=(self.x + self.width // 2, self.y - 5))
            
            # Draw tooltip background
            padding = 5
            bg_rect = pygame.Rect(
                tooltip_rect.x - padding,
                tooltip_rect.y - padding,
                tooltip_rect.width + 2 * padding,
                tooltip_rect.height + 2 * padding
            )
            pygame.draw.rect(screen, BACKGROUND_COLOR, bg_rect, border_radius=5)
            pygame.draw.rect(screen, TEXT_COLOR, bg_rect, 1, border_radius=5)
            
            screen.blit(tooltip_surface, tooltip_rect)
        
        # Handle animation
        if self.animation and self.animation.active:
            progress = self.animation.get_eased_progress()
            self.y = self.original_y + 5 * math.sin(progress * math.pi)
        
    def is_hover(self, pos):
        if self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height:
            if not self.is_hovered:
                self.current_color = self.hover_color
                self.is_hovered = True
                self.animation = Animation()
                self.tooltip_timer = time.time()
            self.tooltip_visible = time.time() - self.tooltip_timer > 0.5
            return True
        else:
            if self.is_hovered:
                self.current_color = self.color
                self.is_hovered = False
                self.animation = None
                self.y = self.original_y
                self.tooltip_visible = False
        return False

class StartScreen:
    def __init__(self):
        self.title = TITLE_FONT.render("SUDOKU", True, PURPLE)
        self.title_rect = self.title.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        
        self.subtitle = SUBTITLE_FONT.render("A Classic Puzzle Game", True, DARK_GRAY)
        self.subtitle_rect = self.subtitle.get_rect(center=(WIDTH // 2, HEIGHT // 3 + 50))
        
        button_width = 200
        button_height = 50
        button_x = (WIDTH - button_width) // 2
        
        self.start_button = Button(
            button_x, HEIGHT // 2, 
            button_width, button_height,
            "Start Game", LIGHT_PURPLE, PURPLE, "S", "Start a new game"
        )
        
        self.theme_button = Button(
            button_x, HEIGHT // 2 + 70, 
            button_width, button_height,
            "Theme: Dark", LIGHT_PURPLE, PURPLE, "T", "Toggle between light and dark mode"
        )
        
        self.quit_button = Button(
            button_x, HEIGHT // 2 + 140, 
            button_width, button_height,
            "Quit", LIGHT_RED, RED, "Q", "Exit the game"
        )
        
        # Animation for title
        self.title_animation = Animation(1.0)
        self.title_original_y = self.title_rect.y
        
    def draw(self, screen):
        screen.fill(BACKGROUND_COLOR)
        
        # Animate title
        if self.title_animation.active:
            progress = self.title_animation.get_eased_progress()
            self.title_rect.y = self.title_original_y - 20 * (1 - progress)
        
        # Draw title with shadow
        shadow_offset = 2
        shadow = TITLE_FONT.render("SUDOKU", True, GRAY)
        shadow_rect = shadow.get_rect(center=(WIDTH // 2 + shadow_offset, self.title_rect.y + shadow_offset))
        screen.blit(shadow, shadow_rect)
        screen.blit(self.title, self.title_rect)
        
        # Draw subtitle
        screen.blit(self.subtitle, self.subtitle_rect)
        
        # Draw buttons
        self.start_button.draw(screen)
        self.theme_button.draw(screen)
        self.quit_button.draw(screen)
        
        pygame.display.update()
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if self.start_button.is_hover(pos):
                    return "start"
                if self.theme_button.is_hover(pos):
                    self.toggle_theme()
                if self.quit_button.is_hover(pos):
                    return "quit"
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    return "start"
                elif event.key == pygame.K_t:
                    self.toggle_theme()
                elif event.key == pygame.K_q:
                    return "quit"
            
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                self.start_button.is_hover(pos)
                self.theme_button.is_hover(pos)
                self.quit_button.is_hover(pos)
        
        return None
    
    def toggle_theme(self):
        global dark_mode
        dark_mode = not dark_mode
        set_theme(dark_mode)
        self.theme_button.text = f"Theme: {'Dark' if dark_mode else 'Light'}"

class Stroke:
    def __init__(self):
        self.points = []
        self.start_time = time.time()
        self.directions = []
        self.cell = None  # Store which cell this stroke belongs to
    
    def add_point(self, pos):
        self.points.append(pos)
        if len(self.points) >= 2:
            dx = self.points[-1][0] - self.points[-2][0]
            dy = self.points[-1][1] - self.points[-2][1]
            self.directions.append((dx, dy))
    
    def get_direction(self):
        if len(self.points) < 2:
            return None
        dx = self.points[-1][0] - self.points[0][0]
        dy = self.points[-1][1] - self.points[0][1]
        return (dx, dy)
    
    def get_bounds(self):
        if not self.points:
            return None
        min_x = min(p[0] for p in self.points)
        max_x = max(p[0] for p in self.points)
        min_y = min(p[1] for p in self.points)
        max_y = max(p[1] for p in self.points)
        return (min_x, min_y, max_x, max_y)
    
    def get_curvature(self):
        if len(self.points) < 3:
            return 0
        
        total_angle = 0
        for i in range(1, len(self.points)-1):
            v1 = (self.points[i][0] - self.points[i-1][0],
                  self.points[i][1] - self.points[i-1][1])
            v2 = (self.points[i+1][0] - self.points[i][0],
                  self.points[i+1][1] - self.points[i][1])
            dot = v1[0] * v2[0] + v1[1] * v2[1]
            mag1 = math.sqrt(v1[0]**2 + v1[1]**2)
            mag2 = math.sqrt(v2[0]**2 + v2[1]**2)
            if mag1 > 0 and mag2 > 0:
                angle = math.acos(max(-1, min(1, dot / (mag1 * mag2))))
                total_angle += angle
        
        return total_angle
    
    def has_loop(self):
        bounds = self.get_bounds()
        if not bounds:
            return False
        min_x, min_y, max_x, max_y = bounds
        width = max_x - min_x
        height = max_y - min_y
        return width > height * 0.7 and height > width * 0.7

class SudokuGame:
    def __init__(self):
        self.board = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
        self.original_board = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
        self.notes = [[set() for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.selected = None
        self.notes_mode = False
        self.dark_mode = True
        
        # History for undo/redo
        self.history = []
        self.future = []
        self.history_limit = 50
        
        # Animations
        self.win_animation = None
        self.cell_animations = {}
        
        # Buttons
        button_width = 80
        button_height = 40
        button_margin = 10
        button_y = HEIGHT - 50
        
        self.solve_button = Button(button_margin, button_y, button_width, button_height, "Solve", LIGHT_BLUE, BLUE, "F", "Auto-solve the puzzle (F)")
        self.notes_button = Button(button_width + 2*button_margin, button_y, button_width, button_height, "Notes", LIGHT_PURPLE, PURPLE, "N", "Toggle notes mode (N)")
        self.undo_button = Button(2*button_width + 3*button_margin, button_y, button_width, button_height, "Undo", LIGHT_RED, RED, "Z", "Undo last move (Ctrl+Z)")
        self.redo_button = Button(3*button_width + 4*button_margin, button_y, button_width, button_height, "Redo", LIGHT_GREEN, GREEN, "Y", "Redo last move (Ctrl+Y)")
        self.new_game_button = Button(4*button_width + 5*button_margin, button_y, button_width, button_height, "New", LIGHT_GOLD, GOLD, "R", "Start new game (R)")
        self.theme_button = Button(5*button_width + 6*button_margin, button_y, button_width, button_height, "Theme", LIGHT_PURPLE, PURPLE, "T", "Toggle between light and dark mode (T)")
        
        # Add clear button for handwriting
        self.clear_button = Button(
            button_margin, button_y - 100, 
            button_width, button_height,
            "Clear", LIGHT_RED, RED, "C", "Clear handwriting in current cell (C)"
        )
        
        # Handwriting recognition
        self.current_stroke = None
        self.strokes = {}  # Dictionary to store strokes per cell
        self.recognition_mode = False
        self.recognition_button = Button(
            button_margin, button_y - 50, 
            button_width, button_height,
            "Handwrite", LIGHT_PURPLE, PURPLE, "H", "Toggle handwriting mode (H)"
        )
        self.last_written_cell = None
        self.stroke_start_time = None
        self.stroke_colors = {
            'dark': (255, 255, 255),  # White
            'light': (0, 120, 215)    # Bright blue
        }
        
        # Initialize Tesseract
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path
        
        self.generate_puzzle()
        self.save_state()
        
        # Animation for new game
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if self.original_board[i, j] != 0:
                    self.cell_animations[(i, j)] = Animation(0.5)
    
    def generate_puzzle(self):
        # Generate a solved board
        self.solve_empty_board()
        # Copy the solved board
        solved_board = self.board.copy()
        # Remove numbers to create a puzzle
        self.make_puzzle(solved_board)
        # Save original board state to check against
        self.original_board = self.board.copy()
    
    def is_valid(self, row, col, num):
        # Check row
        if num in self.board[row, :]:
            return False
        
        # Check column
        if num in self.board[:, col]:
            return False
        
        # Check 3x3 box
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for r in range(box_row, box_row + 3):
            for c in range(box_col, box_col + 3):
                if self.board[r, c] == num:
                    return False
                
        return True
    
    def solve_empty_board(self):
        # Fill the diagonal boxes first
        for i in range(0, 9, 3):
            self.fill_box(i, i)
            
        # Solve the rest
        self.solve_board()
        
    def fill_box(self, row, col):
        nums = list(range(1, 10))
        np.random.shuffle(nums)
        index = 0
        for i in range(3):
            for j in range(3):
                self.board[row + i, col + j] = nums[index]
                index += 1
    
    def solve_board(self):
        empty = self.find_empty()
        if not empty:
            return True
        
        row, col = empty
        
        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.board[row, col] = num
                
                if self.solve_board():
                    return True
                
                self.board[row, col] = 0
        
        return False
    
    def find_empty(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if self.board[i, j] == 0:
                    return (i, j)
        return None
    
    def make_puzzle(self, solved_board):
        # Start with a full board and remove numbers
        self.board = solved_board.copy()
        
        # Randomly remove numbers while ensuring uniqueness
        cells = [(i, j) for i in range(GRID_SIZE) for j in range(GRID_SIZE)]
        np.random.shuffle(cells)
        
        # Remove about 50-55 numbers (leave ~30 numbers)
        for i, j in cells[:55]:
            backup = self.board[i, j]
            self.board[i, j] = 0
            
            # If the board becomes unsolvable with a unique solution, restore the number
            if not self.has_unique_solution():
                self.board[i, j] = backup
    
    def has_unique_solution(self):
        # Simplified check - in a real game, you'd implement a more sophisticated solver
        # that counts solutions
        return True
    
    def draw(self):
        screen.fill(BACKGROUND_COLOR)
        
        # Draw grid with thicker lines for 3x3 boxes
        for i in range(GRID_SIZE + 1):
            line_width = 3 if i % 3 == 0 else 1
            pygame.draw.line(screen, GRID_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), line_width)
            pygame.draw.line(screen, GRID_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, WIDTH), line_width)
        
        # Draw numbers and notes
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                # Draw main numbers
                if self.board[i, j] != 0:
                    # Use different colors for generated vs handwritten numbers
                    if self.original_board[i, j] != 0:
                        # Generated number
                        color = DARK_GENERATED_COLOR if dark_mode else LIGHT_GENERATED_COLOR
                    else:
                        # Handwritten number
                        color = DARK_HANDWRITTEN_COLOR if dark_mode else LIGHT_HANDWRITTEN_COLOR
                    
                    # Handle animation for initial numbers
                    if (i, j) in self.cell_animations and self.cell_animations[(i, j)].active:
                        progress = self.cell_animations[(i, j)].get_eased_progress()
                        scale = 0.5 + 0.5 * progress
                        text = FONT.render(str(self.board[i, j]), True, color)
                        text_rect = text.get_rect(center=(j * CELL_SIZE + CELL_SIZE // 2, i * CELL_SIZE + CELL_SIZE // 2))
                        text = pygame.transform.scale(text, (int(text.get_width() * scale), int(text.get_height() * scale)))
                        text_rect = text.get_rect(center=(j * CELL_SIZE + CELL_SIZE // 2, i * CELL_SIZE + CELL_SIZE // 2))
                        screen.blit(text, text_rect)
                    else:
                        text = FONT.render(str(self.board[i, j]), True, color)
                        text_rect = text.get_rect(center=(j * CELL_SIZE + CELL_SIZE // 2, i * CELL_SIZE + CELL_SIZE // 2))
                        screen.blit(text, text_rect)
                
                # Draw notes
                elif len(self.notes[i][j]) > 0:
                    for num in range(1, 10):
                        if num in self.notes[i][j]:
                            note_size = CELL_SIZE // 3
                            note_x = j * CELL_SIZE + ((num-1) % 3) * note_size + 5
                            note_y = i * CELL_SIZE + ((num-1) // 3) * note_size + 5
                            note_text = NOTES_FONT.render(str(num), True, NOTE_COLOR)
                            screen.blit(note_text, (note_x, note_y))
        
        # Draw selection with animation
        if self.selected:
            row, col = self.selected
            selection_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, SELECTION_COLOR, selection_rect, 4, border_radius=5)
        
        # Draw buttons
        self.solve_button.draw(screen)
        self.new_game_button.draw(screen)
        self.notes_button.draw(screen)
        self.undo_button.draw(screen)
        self.redo_button.draw(screen)
        self.theme_button.draw(screen)
        self.recognition_button.draw(screen)
        self.clear_button.draw(screen)
        
        # Draw notes mode status
        notes_status = "Notes: ON" if self.notes_mode else "Notes: OFF"
        self.notes_button.text = notes_status
        
        # Draw theme status
        theme_status = "Dark" if self.dark_mode else "Light"
        self.theme_button.text = f"Theme: {theme_status}"
        
        # Draw undo/redo availability
        self.undo_button.current_color = LIGHT_RED if len(self.history) > 0 else GRAY
        self.redo_button.current_color = LIGHT_GREEN if len(self.future) > 0 else GRAY
        
        # Draw recognition mode status
        self.recognition_button.text = "Handwrite: ON" if self.recognition_mode else "Handwrite: OFF"
        
        # Draw win animation if active
        if self.win_animation:
            if not self.win_animation.update():
                self.win_animation = None
            else:
                self.win_animation.draw(screen)
        
        # Draw all strokes for the current cell
        if self.selected in self.strokes:
            stroke_color = self.stroke_colors['dark' if dark_mode else 'light']
            for stroke in self.strokes[self.selected]:
                if len(stroke.points) > 1:
                    pygame.draw.lines(screen, stroke_color, False, stroke.points, 3)
        
        # Draw current stroke
        if self.current_stroke and len(self.current_stroke.points) > 1:
            stroke_color = self.stroke_colors['dark' if dark_mode else 'light']
            pygame.draw.lines(screen, stroke_color, False, self.current_stroke.points, 3)
    
    def select(self, row, col):
        self.selected = (row, col)
    
    def save_state(self):
        # Save current state for undo/redo
        current_state = GameState(self.board, self.notes)
        self.history.append(current_state)
        
        # Clear redo history when a new move is made
        self.future = []
        
        # Limit history size
        if len(self.history) > self.history_limit:
            self.history.pop(0)
    
    def undo(self):
        if len(self.history) > 0:
            # Save current state to redo stack
            current_state = GameState(self.board, self.notes)
            self.future.append(current_state)
            
            # Restore previous state
            prev_state = self.history.pop()
            self.board = prev_state.board.copy()
            self.notes = copy.deepcopy(prev_state.notes)
    
    def redo(self):
        if len(self.future) > 0:
            # Save current state to history
            current_state = GameState(self.board, self.notes)
            self.history.append(current_state)
            
            # Restore next state
            next_state = self.future.pop()
            self.board = next_state.board.copy()
            self.notes = copy.deepcopy(next_state.notes)
    
    def clean_notes(self, value, row, col):
        # Remove value from notes in the same row
        for c in range(GRID_SIZE):
            if c != col and self.board[row, c] == 0 and value in self.notes[row][c]:
                self.notes[row][c].remove(value)
        
        # Remove value from notes in the same column
        for r in range(GRID_SIZE):
            if r != row and self.board[r, col] == 0 and value in self.notes[r][col]:
                self.notes[r][col].remove(value)
        
        # Remove value from notes in the same 3x3 box
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for r in range(box_row, box_row + 3):
            for c in range(box_col, box_col + 3):
                if (r != row or c != col) and self.board[r, c] == 0 and value in self.notes[r][c]:
                    self.notes[r][c].remove(value)
    
    def place_number(self, num):
        if not self.selected:
            return
            
        row, col = self.selected
        
        if self.original_board[row, col] != 0:
            return
        
        self.save_state()
            
        if self.notes_mode:
            if num in self.notes[row][col]:
                self.notes[row][col].remove(num)
            else:
                self.notes[row][col].add(num)
        else:
            if num != 0:
                self.notes[row][col].clear()
                self.board[row, col] = num
                self.clean_notes(num, row, col)
                
                # Add animation for new number
                self.cell_animations[(row, col)] = Animation(0.3)
            else:
                self.board[row, col] = 0
    
    def toggle_notes_mode(self):
        self.notes_mode = not self.notes_mode
    
    def auto_solve(self):
        self.save_state()
        current_board = self.board.copy()
        
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if self.original_board[i, j] == 0:
                    self.board[i, j] = 0
                    self.notes[i][j].clear()
        
        if not self.solve_board():
            self.board = current_board
            return False
        
        # Add animations for solved numbers
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if self.board[i, j] != current_board[i, j]:
                    self.cell_animations[(i, j)] = Animation(0.3)
        
        return True
    
    def check_win(self):
        # Check if board is full
        if 0 in self.board:
            return False
        
        # Check rows
        for i in range(GRID_SIZE):
            if len(set(self.board[i, :])) != GRID_SIZE:
                return False
        
        # Check columns
        for i in range(GRID_SIZE):
            if len(set(self.board[:, i])) != GRID_SIZE:
                return False
        
        # Check boxes
        for box_row in range(0, GRID_SIZE, 3):
            for box_col in range(0, GRID_SIZE, 3):
                box = [self.board[box_row + i, box_col + j] for i in range(3) for j in range(3)]
                if len(set(box)) != GRID_SIZE:
                    return False
        
        return True
    
    def toggle_theme(self):
        global dark_mode, WHITE, BLACK, GRAY, BLUE, RED, GREEN, DARK_GRAY, LIGHT_RED, LIGHT_GREEN, DARK_BLUE, PURPLE, LIGHT_PURPLE, GOLD, LIGHT_GOLD, GRID_COLOR, SELECTION_COLOR, NOTE_COLOR, BACKGROUND_COLOR, TEXT_COLOR, ORIGINAL_NUMBER_COLOR, GENERATED_COLOR, HANDWRITTEN_COLOR
        
        dark_mode = not dark_mode
        
        if dark_mode:
            WHITE = DARK_WHITE
            BLACK = DARK_BLACK
            GRAY = DARK_GRAY
            BLUE = DARK_BLUE
            RED = DARK_RED
            GREEN = DARK_GREEN
            DARK_GRAY = DARK_DARK_GRAY
            LIGHT_RED = DARK_LIGHT_RED
            LIGHT_GREEN = DARK_LIGHT_GREEN
            DARK_BLUE = DARK_DARK_BLUE
            PURPLE = DARK_PURPLE
            LIGHT_PURPLE = DARK_LIGHT_PURPLE
            GOLD = DARK_GOLD
            LIGHT_GOLD = DARK_LIGHT_GOLD
            GRID_COLOR = DARK_GRID_COLOR
            SELECTION_COLOR = DARK_SELECTION_COLOR
            NOTE_COLOR = DARK_NOTE_COLOR
            BACKGROUND_COLOR = DARK_BACKGROUND_COLOR
            TEXT_COLOR = DARK_TEXT_COLOR
            ORIGINAL_NUMBER_COLOR = DARK_ORIGINAL_NUMBER_COLOR
            GENERATED_COLOR = DARK_GENERATED_COLOR
            HANDWRITTEN_COLOR = DARK_HANDWRITTEN_COLOR
        else:
            WHITE = LIGHT_WHITE
            BLACK = LIGHT_BLACK
            GRAY = LIGHT_GRAY
            BLUE = LIGHT_BLUE
            RED = LIGHT_RED
            GREEN = LIGHT_GREEN
            DARK_GRAY = LIGHT_DARK_GRAY
            LIGHT_RED = LIGHT_LIGHT_RED
            LIGHT_GREEN = LIGHT_LIGHT_GREEN
            DARK_BLUE = LIGHT_DARK_BLUE
            PURPLE = LIGHT_PURPLE
            LIGHT_PURPLE = LIGHT_LIGHT_PURPLE
            GOLD = LIGHT_GOLD
            LIGHT_GOLD = LIGHT_LIGHT_GOLD
            GRID_COLOR = LIGHT_GRID_COLOR
            SELECTION_COLOR = LIGHT_SELECTION_COLOR
            NOTE_COLOR = LIGHT_NOTE_COLOR
            BACKGROUND_COLOR = LIGHT_BACKGROUND_COLOR
            TEXT_COLOR = LIGHT_TEXT_COLOR
            ORIGINAL_NUMBER_COLOR = LIGHT_ORIGINAL_NUMBER_COLOR
            GENERATED_COLOR = LIGHT_GENERATED_COLOR
            HANDWRITTEN_COLOR = LIGHT_HANDWRITTEN_COLOR
    
    def start_stroke(self, pos):
        if pos[0] < WIDTH and pos[1] < WIDTH:
            col = pos[0] // CELL_SIZE
            row = pos[1] // CELL_SIZE
            if self.original_board[row, col] == 0:
                self.select(row, col)
                self.current_stroke = Stroke()
                self.current_stroke.cell = (row, col)
                self.current_stroke.add_point(pos)
                self.last_written_cell = (row, col)
                
                # Initialize strokes for this cell if needed
                if (row, col) not in self.strokes:
                    self.strokes[(row, col)] = []
    
    def add_stroke_point(self, pos):
        if self.current_stroke:
            self.current_stroke.add_point(pos)
    
    def end_stroke(self):
        if self.current_stroke and len(self.current_stroke.points) > 5:
            # Add stroke to the current cell's strokes
            if self.current_stroke.cell in self.strokes:
                self.strokes[self.current_stroke.cell].append(self.current_stroke)
            
            # Try to recognize the number
            self.recognize_number()
            
        self.current_stroke = None
    
    def recognize_number(self):
        if not self.selected or self.selected not in self.strokes:
            return
        
        cell_strokes = self.strokes[self.selected]
        if not cell_strokes:
            return
        
        # Create a PIL image for OCR with larger size for better recognition
        cell_size = CELL_SIZE * 2  # Double the size for better recognition
        img = Image.new('RGB', (cell_size, cell_size), color='black')
        draw = ImageDraw.Draw(img)
        
        # Draw all strokes with thicker lines
        for stroke in cell_strokes:
            if len(stroke.points) > 1:
                # Scale points to the larger image size
                points = [(p[0] * 2 % cell_size, p[1] * 2 % cell_size) for p in stroke.points]
                draw.line(points, fill='white', width=6)  # Thicker lines
        
        try:
            # Convert to grayscale
            img = img.convert('L')
            
            # Apply threshold to make the image binary
            threshold = 128
            img = img.point(lambda x: 255 if x > threshold else 0, '1')
            
            # Add padding to the image
            padding = 10
            padded_img = Image.new('L', (cell_size + 2*padding, cell_size + 2*padding), 0)
            padded_img.paste(img, (padding, padding))
            
            # Perform OCR with improved configuration
            config = '--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789 --dpi 300'
            result = pytesseract.image_to_data(padded_img, config=config, output_type=pytesseract.Output.DICT)
            
            # Find the best match with highest confidence
            best_num = None
            best_confidence = 0
            
            for i in range(len(result['text'])):
                text = result['text'][i].strip()
                if text and text.isdigit():
                    confidence = float(result['conf'][i])
                    if confidence > best_confidence:
                        num = int(text)
                        if 1 <= num <= 9:
                            best_num = num
                            best_confidence = confidence
            
            # Only place the number if confidence is high enough
            if best_num is not None and best_confidence > 60:  # 60% confidence threshold
                self.place_number(best_num)
                
        except Exception as e:
            print(f"OCR Error: {e}")
    
    def toggle_recognition_mode(self):
        self.recognition_mode = not self.recognition_mode
        self.strokes = {}
        self.current_stroke = None
    
    def clear_current_cell(self):
        if self.selected in self.strokes:
            self.strokes[self.selected] = []

def main():
    # Set default theme to dark mode
    set_theme(True)
    
    # Show start screen
    start_screen = StartScreen()
    while True:
        result = start_screen.handle_events()
        if result == "quit":
            pygame.quit()
            return
        elif result == "start":
            break
        start_screen.draw(screen)
    
    game = SudokuGame()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                
                if game.recognition_mode:
                    game.start_stroke(pos)
                elif pos[0] < WIDTH and pos[1] < WIDTH:
                    col = pos[0] // CELL_SIZE
                    row = pos[1] // CELL_SIZE
                    game.select(row, col)
                
                if game.solve_button.is_hover(pos):
                    game.auto_solve()
                    
                if game.new_game_button.is_hover(pos):
                    game = SudokuGame()
                    
                if game.notes_button.is_hover(pos):
                    game.toggle_notes_mode()
                    
                if game.undo_button.is_hover(pos) and len(game.history) > 0:
                    game.undo()
                    
                if game.redo_button.is_hover(pos) and len(game.future) > 0:
                    game.redo()
                    
                if game.theme_button.is_hover(pos):
                    game.toggle_theme()
                    
                if game.recognition_button.is_hover(pos):
                    game.toggle_recognition_mode()
                    
                if game.clear_button.is_hover(pos):
                    game.clear_current_cell()
            
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                if game.recognition_mode and game.current_stroke:
                    game.add_stroke_point(pos)
                
                game.solve_button.is_hover(pos)
                game.new_game_button.is_hover(pos)
                game.notes_button.is_hover(pos)
                game.undo_button.is_hover(pos)
                game.redo_button.is_hover(pos)
                game.theme_button.is_hover(pos)
                game.recognition_button.is_hover(pos)
                game.clear_button.is_hover(pos)
            
            if event.type == pygame.MOUSEBUTTONUP:
                if game.recognition_mode:
                    game.end_stroke()
            
            if event.type == pygame.KEYDOWN:
                if game.selected and not game.recognition_mode:
                    if pygame.K_1 <= event.key <= pygame.K_9:
                        game.place_number(event.key - pygame.K_0)
                    elif event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                        row, col = game.selected
                        if game.original_board[row, col] == 0:
                            game.save_state()
                            game.board[row, col] = 0
                            game.notes[row][col].clear()
                
                if event.key == pygame.K_n:
                    game.toggle_notes_mode()
                elif event.key == pygame.K_z:
                    if len(game.history) > 0:
                        game.undo()
                elif event.key == pygame.K_y:
                    if len(game.future) > 0:
                        game.redo()
                elif event.key == pygame.K_f:
                    game.auto_solve()
                elif event.key == pygame.K_r:
                    game = SudokuGame()
                elif event.key == pygame.K_t:
                    game.toggle_theme()
                elif event.key == pygame.K_h:
                    game.toggle_recognition_mode()
                elif event.key == pygame.K_c:
                    game.clear_current_cell()
                elif event.key == pygame.K_q:
                    running = False
        
        game.draw()
        
        # Check for win and start animation
        if game.check_win() and not game.win_animation:
            game.win_animation = WinAnimation()
        
        pygame.display.update()
    
    pygame.quit()

if __name__ == "__main__":
    main() 