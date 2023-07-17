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
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Inicializar Pygame
pygame.init()

# Función para generar un laberinto
def generate_maze():
    maze = [[1] * COLS for _ in range(ROWS)]  # Inicializar todas las celdas como pasadizos blancos
    start_cell = (0, 0)
    end_cell = (ROWS - 1, COLS - 1)

    # Lista para almacenar las celdas visitadas
    visited = [start_cell]

    while visited:
        current = visited[-1]
        maze[current[0]][current[1]] = 0  # Cambiar el valor de la celda a 0 (pasadizo blanco)

        # Encontrar vecinos no visitados
        neighbors = []
        if current[0] > 1 and maze[current[0] - 2][current[1]] == 1:
            neighbors.append((current[0] - 2, current[1]))
        if current[0] < ROWS - 2 and maze[current[0] + 2][current[1]] == 1:
            neighbors.append((current[0] + 2, current[1]))
        if current[1] > 1 and maze[current[0]][current[1] - 2] == 1:
            neighbors.append((current[0], current[1] - 2))
        if current[1] < COLS - 2 and maze[current[0]][current[1] + 2] == 1:
            neighbors.append((current[0], current[1] + 2))

        if neighbors:
            # Elegir un vecino aleatorio
            next_cell = random.choice(neighbors)
            maze[next_cell[0]][next_cell[1]] = 0  # Cambiar el valor de la celda vecina a 0 (pasadizo blanco)

            # Eliminar la pared entre la celda actual y la celda vecina
            maze[current[0] + (next_cell[0] - current[0]) // 2][current[1] + (next_cell[1] - current[1]) // 2] = 0

            visited.append(next_cell)
        else:
            visited.pop()

    return maze

# Obtener la cantidad de laberintos que el usuario desea generar
num_laberintos = int(input("Ingrese la cantidad de laberintos que desea generar: "))

# Generar los laberintos y guardar las imágenes
for i in range(num_laberintos):
    # Generar el laberinto
    maze = generate_maze()

    # Crear la ventana del laberinto
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Laberinto")

    # Reloj para controlar la velocidad de actualización de la pantalla
    clock = pygame.time.Clock()

    # Dibujar el laberinto y las paredes exteriores
    screen.fill(BLACK)

    # Dibujar las paredes exteriores
    pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, CELL_SIZE))  # Pared superior
    pygame.draw.rect(screen, BLACK, (0, HEIGHT - CELL_SIZE, WIDTH, CELL_SIZE))  # Pared inferior
    pygame.draw.rect(screen, BLACK, (0, 0, CELL_SIZE, HEIGHT))  # Pared izquierda
    pygame.draw.rect(screen, BLACK, (WIDTH - CELL_SIZE, 0, CELL_SIZE, HEIGHT))  # Pared derecha

    # Dibujar el laberinto
    for row in range(ROWS):
        for col in range(COLS):
            if maze[row][col] == 1:
                pygame.draw.rect(screen, BLACK, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif (row, col) == (0, 0):
                pygame.draw.rect(screen, BLUE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif (row, col) == (ROWS - 1, COLS - 1):
                pygame.draw.rect(screen, GREEN, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            else:
                pygame.draw.rect(screen, WHITE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

                # Dibujar la marca 'X' en el cuadro verde
                if maze[row][col] == 0:
                    pygame.draw.line(screen, BLACK, (col * CELL_SIZE, row * CELL_SIZE), ((col + 1) * CELL_SIZE, (row + 1) * CELL_SIZE))
                    pygame.draw.line(screen, BLACK, ((col + 1) * CELL_SIZE, row * CELL_SIZE), (col * CELL_SIZE, (row + 1) * CELL_SIZE))

    # Rellenar la última celda negra generada de color verde
    last_cell = (ROWS - 1, COLS - 2)
    pygame.draw.rect(screen, GREEN, (last_cell[1] * CELL_SIZE, last_cell[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Guardar la imagen del laberinto como archivo .jpg
    pygame.image.save(screen, f"laberinto{i + 1}.jpg")

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
