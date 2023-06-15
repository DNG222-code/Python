import pygame
import random

# Inicialización de Pygame
pygame.init()

# Dimensiones de la pantalla
width = 800
height = 600

# Colores
black = (0, 0, 0)
white = (255, 255, 255)

# Creación de la pantalla del juego
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Juego 2D")

clock = pygame.time.Clock()

# Clase para el jugador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.x = width // 2
        self.rect.y = height - 70

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        # Limitar el movimiento dentro de la pantalla
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > width - 50:
            self.rect.x = width - 50

# Clase para los obstáculos
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([random.randint(20, 80), 20])
        self.image.fill((random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width - self.rect.width)
        self.rect.y = -self.rect.height

    def update(self):
        self.rect.y += 3
        if self.rect.y > height:
            self.rect.x = random.randint(0, width - self.rect.width)
            self.rect.y = -self.rect.height

# Creación de los grupos de sprites
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()

# Creación del jugador
player = Player()
all_sprites.add(player)

# Ciclo principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Crear nuevos obstáculos aleatoriamente
    if random.randint(0, 100) < 2:
        obstacle = Obstacle()
        all_sprites.add(obstacle)
        obstacles.add(obstacle)

    # Actualizar los sprites
    all_sprites.update()

    # Comprobar colisiones entre el jugador y los obstáculos
    if pygame.sprite.spritecollide(player, obstacles, False):
        running = False

    # Dibujar en la pantalla
    screen.fill(black)
    all_sprites.draw(screen)
    pygame.display.flip()

    clock.tick(60)

# Salir del juego
pygame.quit()