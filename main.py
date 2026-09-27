import pygame
import math
import random

pygame.init()

GRID_WIDTH = 32
GRID_HEIGHT = 32
CELL_SIZE = 20
HUD_HEIGHT = 50
SCREEN_WIDTH = GRID_WIDTH * CELL_SIZE         
SCREEN_HEIGHT = GRID_HEIGHT * CELL_SIZE + HUD_HEIGHT 

BLACK      = (0, 0, 0)
RED        = (222, 33, 33)
WHITE      = (255, 184, 151)
YELLOW     = (255, 255, 0)
GRAY       = (200, 200, 200)
BLUE       = (50, 150, 250)
GREEN      = (50, 220, 50)
DARK_GRAY  = (40, 40, 40)
SKULL_BASE = (180, 205, 210)
SKULL_SHAD = (120, 145, 150)
EYE_DARK   = (30, 25, 35)
GLOW_RED   = (255, 40, 40)
CRIMSON    = (160, 10, 20)

INITIAL_MAP_LAYOUT = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,2,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,2,1],
    [1,0,1,1,1,1,1,0,1,0,1,1,1,1,0,1,1,0,1,1,1,1,0,1,0,1,1,1,1,1,0,1],
    [1,0,1,1,1,1,1,0,1,0,1,1,1,1,0,1,1,0,1,1,1,1,0,1,0,1,1,1,1,1,0,1],
    [1,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,1], 
    [1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,1,1,1,0,0,0,0,1,1,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,0,1,0,0,2,0,0,0,0,0,0,0,0,2,0,0,1,0,1,1,1,1,1,1,1], 
    [1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,0,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1],
    [1,2,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,2,1], 
    [1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1],
    [1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,1],
    [1,1,1,1,0,1,1,0,1,0,1,1,1,1,1,0,0,1,1,1,1,1,0,1,0,1,1,0,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,0,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,0,1,1,1,1],
    [1,1,1,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,1,1,1],
    [1,0,0,0,0,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,0,0,0,0,1],
    [1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1],
    [1,0,1,1,1,1,1,0,1,0,0,0,0,2,0,0,0,0,2,0,0,0,0,1,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1],
    [1,2,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,2,1], 
    [1,1,1,1,0,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,0,1,1,1,1],
    [1,1,1,1,0,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,0,1,1,1,1],
    [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
    [1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
    [1,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,1], 
    [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]
MAP_LAYOUT = [row[:] for row in INITIAL_MAP_LAYOUT]

def count_total_coins():
    total = 0
    for row in MAP_LAYOUT:
        for cell in row:
            if cell in (0, 2):
                total += 1
    return total

TOTAL_COINS = count_total_coins()

def is_valid_tile(gx, gy):
    wrapped_gx = gx % GRID_WIDTH
    wrapped_gy = gy % GRID_HEIGHT
    return MAP_LAYOUT[wrapped_gy][wrapped_gx] != 1

class Button:
    def __init__(self, x, y, width, height, text, bg_color, text_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.bg_color = bg_color
        self.text_color = text_color
        self.font = pygame.font.SysFont("arial", 20, bold=True)

    def draw(self, surface):
        pygame.draw.rect(surface, self.bg_color, self.rect, border_radius=6)
        pygame.draw.rect(surface, WHITE, self.rect, 2, border_radius=6)
        txt_surf = self.font.render(self.text, True, self.text_color)
        txt_rect = txt_surf.get_rect(center=self.rect.center)
        surface.blit(txt_surf, txt_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

class Player:
    def __init__(self, gx, gy):
        self.spawn_gx = gx
        self.spawn_gy = gy
        self.reset()

    def reset(self):
        self.gx = self.spawn_gx
        self.gy = self.spawn_gy
        self.pixel_x = self.gx * CELL_SIZE
        self.pixel_y = self.gy * CELL_SIZE + HUD_HEIGHT
        self.dir = (0, 0)
        self.next_dir = (0, 0)
        self.speed = 2
        self.power_timer = 0
        self.score = 0
        self.coins_eaten = 0
        self.is_alive = True

    def handle_input(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.next_dir = (-1, 0)
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.next_dir = (1, 0)
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            self.next_dir = (0, -1)
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.next_dir = (0, 1)

    def update(self):
        if not self.is_alive:
            return

        if self.power_timer > 0:
            self.power_timer -= 1

        grid_target_x = self.gx * CELL_SIZE
        grid_target_y = self.gy * CELL_SIZE + HUD_HEIGHT

        if self.pixel_x == grid_target_x and self.pixel_y == grid_target_y:
            cell = MAP_LAYOUT[self.gy][self.gx]
            if cell == 0:
                MAP_LAYOUT[self.gy][self.gx] = -1
                self.score += 10
                self.coins_eaten += 1
            elif cell == 2:
                MAP_LAYOUT[self.gy][self.gx] = -1
                self.score += 50
                self.coins_eaten += 1
                self.power_timer = 300 

            if self.next_dir != (0, 0) and is_valid_tile(self.gx + self.next_dir[0], self.gy + self.next_dir[1]):
                self.dir = self.next_dir

            if not is_valid_tile(self.gx + self.dir[0], self.gy + self.dir[1]):
                self.dir = (0, 0)

            self.gx = (self.gx + self.dir[0]) % GRID_WIDTH
            self.gy = (self.gy + self.dir[1]) % GRID_HEIGHT

            if abs(self.gx * CELL_SIZE - self.pixel_x) > CELL_SIZE * 2:
                self.pixel_x = self.gx * CELL_SIZE
            if abs((self.gy * CELL_SIZE + HUD_HEIGHT) - self.pixel_y) > CELL_SIZE * 2:
                self.pixel_y = self.gy * CELL_SIZE + HUD_HEIGHT

        target_x = self.gx * CELL_SIZE
        target_y = self.gy * CELL_SIZE + HUD_HEIGHT
        
        if self.pixel_x < target_x: self.pixel_x += self.speed
        if self.pixel_x > target_x: self.pixel_x -= self.speed
        if self.pixel_y < target_y: self.pixel_y += self.speed
        if self.pixel_y > target_y: self.pixel_y -= self.speed

    def draw(self, screen):
        if not self.is_alive:
            return
        color = YELLOW if self.power_timer == 0 or (self.power_timer // 10) % 2 == 0 else WHITE
        cx = int(self.pixel_x + CELL_SIZE // 2)
        cy = int(self.pixel_y + CELL_SIZE // 2)
        pygame.draw.circle(screen, color, (cx, cy), CELL_SIZE // 2 - 1)

class SkullEnemy:
    def __init__(self, gx, gy):
        self.spawn_gx = gx
        self.spawn_gy = gy
        self.reset()

    def reset(self):
        self.gx = self.spawn_gx
        self.gy = self.spawn_gy
        self.pixel_x = self.gx * CELL_SIZE
        self.pixel_y = self.gy * CELL_SIZE + HUD_HEIGHT
        self.dir = random.choice([(1,0), (-1,0), (0,1), (0,-1)])
        self.state = "PATROL"  
        self.anim_timer = random.uniform(0, 10)
        self.defeat_timer = 0
        self.particles = []
        self.speed = 2

    def update(self, player, other_enemies):
        self.anim_timer += 0.1

        if self.state == "DEFEATED":
            self.defeat_timer += 1
            if random.random() < 0.4:
                self.particles.append([self.pixel_x + 10, self.pixel_y + 10, random.uniform(-1, 1), random.uniform(1, 3)])
            
            for p in self.particles[:]:
                p[0] += p[2]
                p[1] += p[3]
                
            if self.defeat_timer > 90:
                self.reset()
            return

        if player.power_timer > 0:
            self.state = "PATROL"
        else:
            dist = math.hypot(player.gx - self.gx, player.gy - self.gy)
            if dist < 8:
                self.state = "AGGRESSIVE"
            else:
                self.state = "PATROL"

        grid_target_x = self.gx * CELL_SIZE
        grid_target_y = self.gy * CELL_SIZE + HUD_HEIGHT

        if self.pixel_x == grid_target_x and self.pixel_y == grid_target_y:
            occupied = [(e.gx, e.gy) for e in other_enemies if e != self and e.state != "DEFEATED"]
            occupied_targets = [(e.gx + e.dir[0], e.gy + e.dir[1]) for e in other_enemies if e != self and e.state != "DEFEATED"]
            
            valid_dirs = []
            for dx, dy in [(0,-1), (0,1), (-1,0), (1,0)]:
                if (dx, dy) == (-self.dir[0], -self.dir[1]):
                    continue
                nx, ny = self.gx + dx, self.gy + dy
                if is_valid_tile(nx, ny) and (nx % GRID_WIDTH, ny % GRID_HEIGHT) not in occupied and (nx % GRID_WIDTH, ny % GRID_HEIGHT) not in occupied_targets:
                    valid_dirs.append((dx, dy))

            if not valid_dirs:
                for dx, dy in [(0,-1), (0,1), (-1,0), (1,0)]:
                    nx, ny = self.gx + dx, self.gy + dy
                    if is_valid_tile(nx, ny) and (nx % GRID_WIDTH, ny % GRID_HEIGHT) not in occupied:
                        valid_dirs.append((dx, dy))

            if not valid_dirs:
                valid_dirs.append((0, 0))

            if self.state == "AGGRESSIVE" and valid_dirs and valid_dirs != [(0, 0)]:
                best_dir = valid_dirs[0]
                min_dist = float('inf')
                for d in valid_dirs:
                    nx, ny = (self.gx + d[0]) % GRID_WIDTH, (self.gy + d[1]) % GRID_HEIGHT
                    dist = math.hypot(player.gx - nx, player.gy - ny)
                    if dist < min_dist:
                        min_dist = dist
                        best_dir = d
                self.dir = best_dir
            else:
                self.dir = random.choice(valid_dirs)

            self.gx = (self.gx + self.dir[0]) % GRID_WIDTH
            self.gy = (self.gy + self.dir[1]) % GRID_HEIGHT

            if abs(self.gx * CELL_SIZE - self.pixel_x) > CELL_SIZE * 2:
                self.pixel_x = self.gx * CELL_SIZE
            if abs((self.gy * CELL_SIZE + HUD_HEIGHT) - self.pixel_y) > CELL_SIZE * 2:
                self.pixel_y = self.gy * CELL_SIZE + HUD_HEIGHT

        target_x = self.gx * CELL_SIZE
        target_y = self.gy * CELL_SIZE + HUD_HEIGHT
        
        if self.pixel_x < target_x: self.pixel_x += self.speed
        if self.pixel_x > target_x: self.pixel_x -= self.speed
        if self.pixel_y < target_y: self.pixel_y += self.speed
        if self.pixel_y > target_y: self.pixel_y -= self.speed

        if player.is_alive and math.hypot(player.pixel_x - self.pixel_x, player.pixel_y - self.pixel_y) < 12:
            if player.power_timer > 0:
                self.state = "DEFEATED"
                player.score += 200
            else:
                player.is_alive = False 

    def draw_base_skull(self, surface, eye_color, show_cracks=False):
        pygame.draw.circle(surface, SKULL_BASE, (10, 8), 7)
        pygame.draw.rect(surface, SKULL_BASE, (6, 9, 8, 8))
        pygame.draw.rect(surface, SKULL_SHAD, (6, 15, 8, 2))
        
        pygame.draw.rect(surface, eye_color, (5, 7, 3, 4))
        pygame.draw.rect(surface, eye_color, (12, 7, 3, 4))
        
        pygame.draw.polygon(surface, EYE_DARK, [(9, 11), (11, 11), (10, 13)])
        
        for tx in range(6, 14, 2):
            pygame.draw.line(surface, EYE_DARK, (tx, 14), (tx, 16), 1)

        if show_cracks:
            pygame.draw.line(surface, CRIMSON, (10, 2), (14, 8), 2)
            pygame.draw.line(surface, CRIMSON, (14, 8), (11, 12), 1)
            pygame.draw.circle(surface, CRIMSON, (14, 3), 2)

    def draw(self, screen):
        bob_offset = math.sin(self.anim_timer) * 3

        if self.state == "PATROL":
            surf = pygame.Surface((20, 20), pygame.SRCALPHA)
            self.draw_base_skull(surf, EYE_DARK)
            screen.blit(surf, (self.pixel_x, self.pixel_y + bob_offset))

        elif self.state == "AGGRESSIVE":
            surf = pygame.Surface((26, 26), pygame.SRCALPHA)
            for _ in range(6):
                fx = random.randint(0, 24)
                fy = random.randint(0, 24)
                pygame.draw.circle(surf, GLOW_RED, (fx, fy), random.randint(2, 4))

            self.draw_base_skull(surf, GLOW_RED)
            shake_x = random.randint(-1, 1)
            shake_y = random.randint(-1, 1)
            screen.blit(surf, (self.pixel_x - 3 + shake_x, self.pixel_y - 3 + shake_y + bob_offset))

        elif self.state == "DEFEATED":
            surf = pygame.Surface((20, 20), pygame.SRCALPHA)
            self.draw_base_skull(surf, CRIMSON, show_cracks=True)
            rotated_surf = pygame.transform.rotate(surf, -30)

            for p in self.particles:
                pygame.draw.circle(screen, CRIMSON, (int(p[0]), int(p[1])), 1)

            screen.blit(rotated_surf, (self.pixel_x, self.pixel_y + (self.defeat_timer * 0.5)))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man Skull Maze")
clock = pygame.time.Clock()

hud_font = pygame.font.SysFont("arial", 16, bold=True)
title_font = pygame.font.SysFont("arial", 42, bold=True)
game_over_font = pygame.font.SysFont("arial", 44, bold=True)

player = Player(15, 23)

enemies = [
    SkullEnemy(15, 10),
    SkullEnemy(16, 10),
    SkullEnemy(15, 11),
    SkullEnemy(16, 11),
    SkullEnemy(14, 10)
]

start_button_menu = Button(SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 + 30, 160, 45, "START GAME", GREEN, BLACK)
pause_button = Button(SCREEN_WIDTH - 95, 10, 80, 30, "PAUSE", BLUE, WHITE)

game_state = "MENU"
start_ticks = 0
accumulated_time = 0
pause_start_ticks = 0
game_over_reason = ""

def reset_game():
    global MAP_LAYOUT, start_ticks, accumulated_time, game_over_reason, game_state
    MAP_LAYOUT = [row[:] for row in INITIAL_MAP_LAYOUT]
    player.reset()
    for enemy in enemies:
        enemy.reset()
    start_ticks = pygame.time.get_ticks()
    accumulated_time = 0
    game_over_reason = ""
    game_state = "PLAYING"

running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    mouse_clicked = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_clicked = True
        elif event.type == pygame.KEYDOWN:
            if game_state in ("GAME_OVER", "VICTORY") and event.key == pygame.K_r:
                reset_game()
            elif game_state in ("PLAYING", "PAUSED") and event.key == pygame.K_p:
                if game_state == "PLAYING":
                    game_state = "PAUSED"
                    pause_start_ticks = pygame.time.get_ticks()
                    pause_button.text = "RESUME"
                else:
                    game_state = "PLAYING"
                    accumulated_time += (pygame.time.get_ticks() - pause_start_ticks)
                    pause_button.text = "PAUSE"

    keys = pygame.key.get_pressed()

    if game_state == "MENU":
        screen.fill(BLACK)
        title_surf = title_font.render("PAC-MAN SKULL MAZE", True, YELLOW)
        title_rect = title_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 60))
        screen.blit(title_surf, title_rect)

        start_button_menu.draw(screen)
        if mouse_clicked and start_button_menu.is_clicked(mouse_pos):
            reset_game()

    elif game_state in ("PLAYING", "PAUSED", "GAME_OVER", "VICTORY"):
        if game_state == "PLAYING":
            player.handle_input(keys)
            player.update()

            for enemy in enemies:
                enemy.update(player, enemies)

            elapsed_seconds = (pygame.time.get_ticks() - start_ticks - accumulated_time) // 1000
            remaining_time = max(0, 300 - elapsed_seconds)

            if not player.is_alive:
                game_state = "GAME_OVER"
                game_over_reason = "YOU WERE CAUGHT!"
            elif remaining_time <= 0:
                game_state = "GAME_OVER"
                game_over_reason = "TIME OUT! (300s EXPIRED)"
            elif player.coins_eaten >= TOTAL_COINS:
                game_state = "VICTORY"

            if mouse_clicked and pause_button.is_clicked(mouse_pos):
                game_state = "PAUSED"
                pause_start_ticks = pygame.time.get_ticks()
                pause_button.text = "RESUME"

        elif game_state == "PAUSED":
            if mouse_clicked and pause_button.is_clicked(mouse_pos):
                game_state = "PLAYING"
                accumulated_time += (pygame.time.get_ticks() - pause_start_ticks)
                pause_button.text = "PAUSE"

        screen.fill(BLACK)

        pygame.draw.line(screen, WHITE, (0, HUD_HEIGHT - 2), (SCREEN_WIDTH, HUD_HEIGHT - 2), 2)
        
        current_elapsed = (pygame.time.get_ticks() - start_ticks - accumulated_time) // 1000 if game_state == "PLAYING" else elapsed_seconds
        rem_seconds = max(0, 300 - current_elapsed)
        rem_coins = TOTAL_COINS - player.coins_eaten

        score_text = hud_font.render(f"SCORE: {player.score}", True, YELLOW)
        coins_text = hud_font.render(f"COINS LEFT: {rem_coins}", True, WHITE)
        timer_text = hud_font.render(f"TIME LEFT: {rem_seconds}s", True, WHITE)

        screen.blit(score_text, (10, 15))
        screen.blit(coins_text, (160, 15))
        screen.blit(timer_text, (340, 15))
        
        pause_button.draw(screen)

        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                cell = MAP_LAYOUT[row][col]
                x = col * CELL_SIZE
                y = row * CELL_SIZE + HUD_HEIGHT
                cx = x + CELL_SIZE // 2
                cy = y + CELL_SIZE // 2

                if cell == 1:
                    pygame.draw.rect(screen, RED, (x, y, CELL_SIZE, CELL_SIZE))
                elif cell == 0:
                    pygame.draw.circle(screen, WHITE, (cx, cy), 2)
                elif cell == 2:
                    pygame.draw.circle(screen, WHITE, (cx, cy), 5)

        player.draw(screen)

        for enemy in enemies:
            enemy.draw(screen)

        if game_state in ("PAUSED", "GAME_OVER", "VICTORY"):
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT - HUD_HEIGHT))
            overlay.set_alpha(180)
            overlay.fill(BLACK)
            screen.blit(overlay, (0, HUD_HEIGHT))

            if game_state == "PAUSED":
                p_text = game_over_font.render("GAME PAUSED", True, YELLOW)
                p_sub = hud_font.render("Click RESUME or press 'P' to continue", True, WHITE)
                p_rect = p_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20))
                sub_rect = p_sub.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30))
                screen.blit(p_text, p_rect)
                screen.blit(p_sub, sub_rect)

            elif game_state == "GAME_OVER":
                go_text = game_over_font.render("GAME OVER", True, RED)
                reason_text = hud_font.render(game_over_reason, True, WHITE)
                restart_text = hud_font.render("Press 'R' to Restart", True, YELLOW)

                go_rect = go_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40))
                reas_rect = reason_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 10))
                res_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))

                screen.blit(go_text, go_rect)
                screen.blit(reason_text, reas_rect)
                screen.blit(restart_text, res_rect)

            elif game_state == "VICTORY":
                vic_text = game_over_font.render("MAZE CLEARED!", True, GREEN)
                score_msg = hud_font.render(f"Final Score: {player.score}", True, WHITE)
                restart_text = hud_font.render("Press 'R' to Play Again", True, YELLOW)

                vic_rect = vic_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40))
                sc_rect = score_msg.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 10))
                res_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))

                screen.blit(vic_text, vic_rect)
                screen.blit(score_msg, sc_rect)
                screen.blit(restart_text, res_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()