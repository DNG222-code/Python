#Importam llibreries per als nombres aleatoris i per al joc.
import random
import pygame
#Una funció per al menu principal.
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
#Programa dels nombres aleatoris.
def aleatori():
    l = []
    #Dona 50 nombres del 1 al 100.
    for i in range(1, 50):
        x = random.randint(1, 100)
        l.append(x)
    print(l)
#Programa de fer lliestes amb les lletres que fica el usuari i una opció per a les vegades que vulguis.
def lletres():
    l = []
    count = int(input("¿Cuantas vegaes vols introduir una lletra/paraula?: "))
    for i in range(count):
        x = input("Introdueix una lletra/paraula: ")
        l.append(x)
    print(l)
#Funció completa dels joc en 2D.
def juego_2D():
    #Funció per a iniciar el joc.
    pygame.init()
    #Mida de la pantalla del joc.
    width = 800
    height = 600
    #Color del escenari del joc.
    negro = (0, 0, 0)
    blanco = (255, 255, 255)
    #Funció per a la pantalla on el usuari juga.
    pantalla = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Juego 2D")

    clock = pygame.time.Clock()
#Definició de una clase per al jugador que empres.
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.Surface([50, 50])
            self.image.fill(blanco)
            self.rect = self.image.get_rect()
            self.rect.x = width // 2
            self.rect.y = height - 70
#Funció per als controls del jugador.
        def update(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.rect.x -= 5
            if keys[pygame.K_RIGHT]:
                self.rect.x += 5

            if self.rect.x < 0:
                self.rect.x = 0
            if self.rect.x > width - 50:
                self.rect.x = width - 50
#Una clase per a crear les figures enemigues del joc.
    class Obstacle(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.Surface([random.randint(10, 30), 20])
            self.image.fill((random.randint(50, 255), random.randint(30, 155), random.randint(50, 255)))
            self.rect = self.image.get_rect()
            self.rect.x = random.randint(0, width - self.rect.width)
            self.rect.y = -self.rect.height
#Funció per a que els blocs enemigs surtin de una forma diferente, quan tornis a jugar.
        def update(self):
            self.rect.y += 3
            if self.rect.y > height:
                self.rect.x = random.randint(0, width - self.rect.width)
                self.rect.y = -self.rect.height
#Variables per als obtacles i per a que s'agrupin.
    all_sprites = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()

    player = Player()
    all_sprites.add(player)
#Un bucle per a que aranqui el joc fins a que et moris.
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
#Funció per a obstacles aleatoris del 0 al 100.
        if random.randint(0, 100) < 2:
            obstacle = Obstacle()
            all_sprites.add(obstacle)
            obstacles.add(obstacle)

        all_sprites.update()

        if pygame.sprite.spritecollide(player, obstacles, False):
            running = False

        pantalla.fill(negro)
        all_sprites.draw(pantalla)
        pygame.display.flip()

        clock.tick(60)
#Amb aquesta funció es lleva el joc.
    pygame.quit()

#Estructura de una funció de bucle per a 
a = True
while a:
    a = menu()
    if a == 1:
        aleatori()
    elif a == 2:
        lletres()
    elif a == 3:
        juego_2D()
    elif a == 4:
        
        pass
    elif a == 0:
        a = False
        print("Adéu, ara sortirem de l'app")
    else:
        print("Error, opció no vàlida")