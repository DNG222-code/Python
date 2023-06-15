#Importar funcions per al menu principal.
from curses.ascii import isdigit
#Importar funció per a els numeros aleatoris.
import random
#Importat funcions per a el joc 2D.
import pygame
import Juego_2D as juego

#Importam la funció de isdigit per a poder llegir els números del menú.
def menu():
    print("""
            0. Sortir
            1. Aleatori.
            2. Lletres.
            3. Juego 2D.
            4. Clases.
    """)
    a = int(input("Introdueix un número de selecció: "))
    return a

#Genera 50 nombres aleatoris entre 1 al 100.
def aleatori():
    l = []
    for i in range(1,50):
        x = random.randint(1,100)
        l.append(x)
    print(l)

#Introduim el número de vegades que vols escriure lletres o paraules i fiques les lletres/paraules.
def lletres():
    l = []
    for i in range(int(input("¿Cuantas vegaes vols introduir una lletra/paraula?: "))):
        x = (input("Introdueix una lletra/paraula: "))
        l.append(x)
    print(l)

def juego_2D():
    # Inicialización de Pygame
    pygame.init()

# Dimensiones de la pantalla
width = 800
height = 600

# Colores
negro = (0, 0, 0)
blanco = (255, 255, 255)

# Creación de la pantalla del juego
pantalla = pygame.display.set_mode((width, height))
pygame.display.set_caption("Juego 2D")

clock = pygame.time.Clock()

# Clase para el jugador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(blanco)
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
        self.image = pygame.Surface([random.randint(10, 30), 20])
        self.image.fill((random.randint(50, 255), random.randint(30, 155), random.randint(50, 255)))
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
    pantalla.fill(negro)
    all_sprites.draw(pantalla)
    pygame.display.flip()

    clock.tick(60)

# Salir del juego
pygame.quit()

#programa principal
a = True
while a:
    a = menu()
    match a:
        #En la terminal surt en la part superior el input.
        case 1:
            aleatori()
        case 2:
            lletres()
        case 3:
            juego_2D()
        case 4:
            ()
        case 0:
            a = False
            print("Adéu, ara sortirem de l'app")
        case other:
            print("Error, opció no vàlida")