import pygame
import csv
import constantes
from personaje import Personaje
from mundo import Mundo
from objetos import Objeto
from AgregarObjeto import encontrar_y_agregar_objeto1


def resetear_nivel_4(jugador, grupo_objetos, camera, animaciones_esqueleto):
    nivel = 4

    camera.reset()


    world_data = []
    for fila in range(constantes.FILAS):
        filas = [1]*constantes.COLUMNAS
        world_data.append(filas)
    #Archivo csv nivel3
    with open(r'Archivos/Niveles/Nivel.csv' , newline= '') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for x, fila in enumerate(reader):
            for y, columna in enumerate(fila):
                world_data[x][y] = int(columna)


    tile_list = []
    for x in range(300):
        tile_image = pygame.image.load(f"Archivos/Niveles/Mundo4Set/Mundo4 ({x + 1}).png")
        tile_image = pygame.transform.scale(tile_image, (50, 50))
        tile_list.append(tile_image)

    world = Mundo(nivel)
    world.process_data(world_data, tile_list)
    jugador.shape.center = (62, 198)
    esqueleto = Personaje(740, 470, animaciones_esqueleto, False, 0, 500)
    esqueleto2 = Personaje(1258, 200, animaciones_esqueleto, False, 0, 500)




    return nivel,world, jugador, grupo_objetos, camera, esqueleto, esqueleto2