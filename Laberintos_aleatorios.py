import pygame
import random

# Dimensiones del laberinto
WIDTH = 800
HEIGHT = 600

# Dimensiones de las celdas
CELL_SIZE = 20
COLS = WIDTH // CELL_SIZE
ROWS = HEIGHT // CELL_SIZE

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Inicializar Pygame
pygame.init()

# Crear la ventana del laberinto
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Laberinto")

# Reloj para controlar la velocidad de actualización de la pantalla
clock = pygame.time.Clock()

# Matriz para representar el laberinto
maze = [[0] * COLS for _ in range(ROWS)]

# Función para generar el laberinto utilizando el algoritmo de Prim
def generate_maze():
    # Lista para almacenar las celdas visitadas
    visited = [(0, 0)]
    
    while visited:
        current = visited[-1]
        maze[current[0]][current[1]] = 1
        
        # Encontrar vecinos no visitados
        neighbors = []
        if current[0] > 1 and maze[current[0] - 2][current[1]] == 0:
            neighbors.append((current[0] - 2, current[1]))
        if current[0] < ROWS - 2 and maze[current[0] + 2][current[1]] == 0:
            neighbors.append((current[0] + 2, current[1]))
        if current[1] > 1 and maze[current[0]][current[1] - 2] == 0:
            neighbors.append((current[0], current[1] - 2))
        if current[1] < COLS - 2 and maze[current[0]][current[1] + 2] == 0:
            neighbors.append((current[0], current[1] + 2))
        
        if neighbors:
            # Elegir un vecino aleatorio
            next_cell = random.choice(neighbors)
            maze[next_cell[0]][next_cell[1]] = 1
            
            # Eliminar la pared entre la celda actual y la celda vecina
            maze[current[0] + (next_cell[0] - current[0]) // 2][current[1] + (next_cell[1] - current[1]) // 2] = 1
            
            visited.append(next_cell)
        else:
            visited.pop()
            
# Generar el laberinto
generate_maze()

# Dibujar el laberinto y las paredes exteriores
screen.fill(BLACK)

# Dibujar las paredes exteriores
pygame.draw.rect(screen, BLUE, (0, 0, WIDTH, CELL_SIZE))  # Pared superior
pygame.draw.rect(screen, BLUE, (0, HEIGHT - CELL_SIZE, WIDTH, CELL_SIZE))  # Pared inferior
pygame.draw.rect(screen, BLUE, (0, 0, CELL_SIZE, HEIGHT))  # Pared izquierda
pygame.draw.rect(screen, BLUE, (WIDTH - CELL_SIZE, 0, CELL_SIZE, HEIGHT))  # Pared derecha

# Dibujar el laberinto
for row in range(ROWS):
    for col in range(COLS):
        if maze[row][col] == 0:
            pygame.draw.rect(screen, BLUE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Actualizar la pantalla
pygame.display.flip()

# Bucle principal del juego
running = True
while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Actualizar la pantalla
    pygame.display.flip()
    clock.tick(60)

# Finalizar Pygame
pygame.quit()
