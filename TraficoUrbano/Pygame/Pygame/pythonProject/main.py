import csv
import pygame
import constantes
from personaje import Personaje
from mundo import Mundo, Camera
from obstaculos import (casa_colisión, casa_grande_colision, lago_limite1,
                        lago_limite2, lago_limite3, lago_limite4, arbol1,
                        arbol2, fuente, puente1, puente2, puente3, paredes_colision,
                        lago_nivel_2, puente_nivel_2, paredes_abajo_nivel3,
                        paredes_arriba_nivel3, paredes_medio_nivel3, paredes_nivel4)
from objetos import Objeto
from AgregarObjeto import encontrar_y_agregar_objeto1
from Nivel999 import resetear_nivel_2
from Nivel3 import resetear_nivel_3
from Nivel4 import resetear_nivel_4


pygame.init()
#IMAGES
ventana = pygame.display.set_mode((constantes.WIDTH_VENTANA, constantes.HEIGHT_VENTANA))
pygame.display.set_caption("The legacy of the dungeon")
nivel = 1
imagen_fondo = pygame.image.load("Archivos/ImagenFond/Hollow.png")
imagen_fondo = pygame.transform.scale(imagen_fondo, (constantes.WIDTH_VENTANA, constantes.HEIGHT_VENTANA))
imagen_pausa = pygame.image.load("Archivos/ImagenFond/holl.jpg")
imagen_pausa = pygame.transform.scale(imagen_pausa, (constantes.WIDTH_VENTANA, constantes.HEIGHT_VENTANA))

#MUSIC
def cambiar_musica(nivel):
    pygame.mixer.music.stop()
    if nivel == 1:
        pygame.mixer.music.load("Archivos/Music/Deltarune OST 13 - Field of Hopes and Dreams.mp3")
    elif nivel == 2:
        pygame.mixer.music.load("Archivos/Music/Deltarune OST 30 - Chaos King.mp3")
    elif nivel == 3:
        pygame.mixer.music.load("Archivos/Music/Deltarune Chapter 2 OST 15 - Smart Race.mp3")
    elif nivel == 4:
        pygame.mixer.music.load("Archivos/Music/BIG SHOT.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
cambiar_musica(1)

#initialize_potions
def inicializar_pociones(world_data):
    grupo_objetos = pygame.sprite.Group()
    pocion, tile_pos = encontrar_y_agregar_objeto1(world_data, 157, pocion_roja)
    if pocion:
        grupo_objetos.add(pocion)
    pocion2, tile_pos2 = encontrar_y_agregar_objeto1(world_data, 372, pocion_roja)
    if pocion2:
        grupo_objetos.add(pocion2)
    return grupo_objetos, tile_pos, tile_pos2

# Objets
corazon_vacio = pygame.image.load("Archivos/Imágenes/ITEMS/Vacio.png")
corazon_vacio = pygame.transform.scale(corazon_vacio, (corazon_vacio.get_width() * constantes.ESCALA_CORAZONES, corazon_vacio.get_height() * constantes.ESCALA_CORAZONES))
corazon_medio = pygame.image.load("Archivos/Imágenes/ITEMS/Medio.png")
corazon_medio = pygame.transform.scale(corazon_medio, (corazon_medio.get_width() * constantes.ESCALA_CORAZONES, corazon_medio.get_height() * constantes.ESCALA_CORAZONES))
corazon_lleno = pygame.image.load("Archivos/Imágenes/ITEMS/Lleno.png")
corazon_lleno = pygame.transform.scale(corazon_lleno, (corazon_lleno.get_width() * constantes.ESCALA_CORAZONES, corazon_lleno.get_height() * constantes.ESCALA_CORAZONES))

#FONTS
font_inicio = pygame.font.Font("Archivos/FUENTES/PixeloidMono.ttf",30)
font_titulo = pygame.font.Font("Archivos/FUENTES/PixeloidSans-Bold.ttf",40)

boton_jugar = pygame.Rect(constantes.WIDTH_VENTANA/2-100, constantes.HEIGHT_VENTANA/2-50,200,50)
boton_salir = pygame.Rect(constantes.WIDTH_VENTANA/2-100, constantes.HEIGHT_VENTANA/2+50,200,50)

texto_boton_jugar = font_inicio.render("Jugar",True,(0,0,0))
texto_boton_salir = font_inicio.render("Salir",True, (255,255,255))

#Functions
def pantalla_inicio():
    ventana.blit(imagen_fondo, (0, 0))
    dibujar_texto = font_titulo.render("The legacy of the dungeon   ",
                                       True, (255,255,255),)
    texto_titulo = dibujar_texto.get_rect(center=(constantes.WIDTH_VENTANA/2,
                                                  constantes.HEIGHT_VENTANA/2 - 120))
    ventana.blit(dibujar_texto, texto_titulo)

    pygame.draw.rect(ventana, (156,223,219),boton_jugar)
    pygame.draw.rect(ventana, (13,68,65),boton_salir)
    ventana.blit(texto_boton_jugar, (boton_jugar.x + 50, boton_jugar.y + 10))
    ventana.blit(texto_boton_salir, (boton_salir.x + 50, boton_salir.y + 10))
    pygame.display.update()

boton_voler_inicio = pygame.Rect(constantes.WIDTH_VENTANA/2-100, constantes.HEIGHT_VENTANA/2 + 50, 200,50)
texto_boton_voler_inicio = font_inicio.render("Volver al Inicio",True,(255,255,255))

#FUNCTION PAUSE THE GAME
def pausar_juego():
    ventana.blit(imagen_pausa, (0, 0))
    dibujar_texto = font_titulo.render("Has pausado el juego",
                                       True, (255, 255, 255))
    texto_titulo = dibujar_texto.get_rect(center=(constantes.WIDTH_VENTANA / 2,
                                                  constantes.HEIGHT_VENTANA / 2 - 120))
    ventana.blit(dibujar_texto, texto_titulo)
    pygame.draw.rect(ventana, (13, 68, 65), boton_salir)
    ventana.blit(texto_boton_salir, (boton_salir.x + 50, boton_salir.y + 10))
    pygame.display.update()

    # PAUSE THE GAME
    pausa = True
    while pausa:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Presionar 'p' para despausar
                    pausa = False
            elif event.type == pygame.MOUSEBUTTONDOWN and boton_salir.collidepoint(event.pos):
                pygame.quit()
                quit()
#GAME OVER SCREEN
def pantalla_game_over():
    ventana.fill((0,0,0))
    dibujar_texto = font_titulo.render("Game Over" ,True,(250, 0, 0))
    texto_titulo = dibujar_texto.get_rect(center=(constantes.WIDTH_VENTANA / 2, constantes.HEIGHT_VENTANA / 2 - 120))
    ventana.blit(dibujar_texto, texto_titulo)

    pygame.draw.rect(ventana, (13, 68 , 65), boton_voler_inicio)
    ventana.blit(texto_boton_voler_inicio, (boton_voler_inicio.x + 10, boton_voler_inicio.y + 10))
    pygame.display.update()
#WIN SCREEN
def pantalla_ganado():
    ventana.fill((0,0,0))
    dibujar_texto = font_titulo.render("Has ganado" ,True,(250, 0, 0))
    texto_titulo = dibujar_texto.get_rect(center=(constantes.WIDTH_VENTANA / 2, constantes.HEIGHT_VENTANA / 2 - 120))
    ventana.blit(dibujar_texto, texto_titulo)

    pygame.draw.rect(ventana, (13, 68 , 65), boton_voler_inicio)
    ventana.blit(texto_boton_voler_inicio, (boton_voler_inicio.x + 10, boton_voler_inicio.y + 10))
    pygame.display.update()


#Animations
animaciones = []
for i in range(1, 9):
    img = pygame.image.load(f"Archivos/Imágenes/CABALLERO/Fig.{i}.png")
    img = pygame.transform.scale(img, (img.get_width() * constantes.ESCALA_PERSONAJE, img.get_height() * constantes.ESCALA_PERSONAJE))
    animaciones.append(img)
animaciones_ataque = []
for i in range (1, 9):
    img = pygame.image.load(f"Archivos/Imágenes/Ataque Caballero/CAB_ATAQUE ({i}).png")
    img = pygame.transform.scale(img, (img.get_width()*constantes.ESCALA_PERSONAJE,
                                       img.get_height()*constantes.ESCALA_PERSONAJE))
    animaciones_ataque.append(img)
animaciones_villano = []
for i in range(1, 7):
    img = pygame.image.load(f"Archivos/Imágenes/CHICA/Fig1 ({i}).png")
    img = pygame.transform.scale(img,
                                 (img.get_width()*constantes.ESCALA_PERSONAJE,
                                  img.get_height()*constantes.ESCALA_PERSONAJE))
    animaciones_villano.append(img)
animaciones_esqueleto = []
for i in range (1, 7):
    img = pygame.image.load(f"Archivos/Imágenes/ESQUELETO/ESQUE ({i}).png")
    img = pygame.transform.scale(img,
                                 (img.get_width()*constantes.ESCALA_PERSONAJE,
                                  img.get_height()*constantes.ESCALA_PERSONAJE))
    animaciones_esqueleto.append(img)


# POTION
pocion_roja = pygame.image.load("Archivos/Imágenes/ITEMS/Pocion.png")
pocion_roja = pygame.transform.scale(pocion_roja, (pocion_roja.get_width() * constantes.ESCALA_POCION, pocion_roja.get_height() * constantes.ESCALA_POCION))

world_data = []
for fila in range(constantes.FILAS):
    filas = [1] * constantes.COLUMNAS
    world_data.append(filas)

with open(r'F:\Kadosh\Pygame3\Pygame\pythonProject\Archivos\Niveles\TilesetFinal.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=";")
    for x, fila in enumerate(reader):
        for y, columna in enumerate(fila):
            world_data[x][y] = int(columna)

def dibujar_grid():
    for x in range(constantes.COLUMNAS):
        pygame.draw.line(ventana, (255, 255, 255), (x * 50, 0), (x * 50, constantes.HEIGHT_VENTANA))
        pygame.draw.line(ventana, (255, 255, 255), (0, x * 50), (constantes.WIDTH_VENTANA, x * 50))

def vida_jugador():
    c_medio_dibujado = False
    for i in range(4):
        if jugador.energia >= ((i + 1) * 25):
            ventana.blit(corazon_lleno, (5 + i * 50, 5))
        elif jugador.energia % 25 > 0 and not c_medio_dibujado:
            ventana.blit(corazon_medio, (5 + i * 50, 5))
            c_medio_dibujado = True
        else:
            ventana.blit(corazon_vacio, (5 + i * 50, 5))

#CHARACTERS
jugador = Personaje(208, 332, animaciones,  animaciones_ataque,1,100)
Villano = Personaje(730,340, animaciones_villano, False, 0, 1000)
Esqueleto = Personaje(740, 470, animaciones_esqueleto, False, 0, 500)
Esqueleto2 = Personaje(890, 450, animaciones_esqueleto, False, 0, 500)

# GROUP OF OBJETS
grupo_objetos = pygame.sprite.Group()

pocion, tile_pos = encontrar_y_agregar_objeto1(world_data, 157, pocion_roja)
if pocion:
    grupo_objetos.add(pocion)
pocion2, tile_pos2 = encontrar_y_agregar_objeto1(world_data, 372, pocion_roja)
if pocion2:
    grupo_objetos.add(pocion2)



tile_list = []
for x in range(600):
    tile_image = pygame.image.load(f"Archivos/Niveles/Mundo1Set/Mundo1 ({x + 1}).png")
    tile_image = pygame.transform.scale(tile_image, (50, 50))
    tile_list.append(tile_image)

world = Mundo(nivel)
world.process_data(world_data, tile_list)

#MOVEMENTS
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

reloj = pygame.time.Clock()
camera = Camera(constantes.WIDTH_VENTANA, constantes.HEIGHT_VENTANA, constantes.COLUMNAS, constantes.FILAS)

tecla_o_presionada = False
visible = True
pausa = False
pausar_camara = False
game_over = False
ganado = False
mostrar_inicio = True

run = True

while run:
    if mostrar_inicio == True:
        pantalla_inicio()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and boton_jugar.collidepoint(event.pos):
                mostrar_inicio = False
            if event.type == pygame.MOUSEBUTTONDOWN and boton_salir.collidepoint(event.pos):
                run = False
    elif game_over:
        pantalla_game_over()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and boton_voler_inicio.collidepoint(event.pos):
                mostrar_inicio = True
                gamer_over = False
                jugador.energia = 100
                jugador.shape.topleft = (208, 332)
                Villano.energia = 100
                Villano.shape.topleft = (730, 340)
                Esqueleto.energia = 100
                Esqueleto.shape.topleft = (304, 506)
                visible = True
                camera.offset = [0, 0]
    elif ganado:
        pantalla_ganado()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and boton_voler_inicio.collidepoint(event.pos):
                mostrar_inicio = True
                gamer_over = False
                jugador.energia = 100
                jugador.shape.topleft = (208, 332)
                Villano.energia = 100
                Villano.shape.topleft = (730, 340)
                Esqueleto.energia = 100
                Esqueleto.shape.topleft = (304, 506)
                visible = True
                camera.offset = [0, 0]

    else:
        reloj.tick(constantes.FPS)
        ventana.fill(constantes.COLOR_FONDO)
        dibujar_grid()

        distancia_x = 0
        distancia_y = 0
#KEYS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    mover_izquierda = True
                elif event.key == pygame.K_d:
                    mover_derecha = True
                elif event.key == pygame.K_w:
                    mover_arriba = True
                elif event.key == pygame.K_s:
                    mover_abajo = True
                elif event.key == pygame.K_o:
                    teclado_o_presionada = True
                    jugador.atacar()
                elif event.key == pygame.K_p:
                    pausar_juego()



            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    mover_izquierda = False
                elif event.key == pygame.K_d:
                    mover_derecha = False
                elif event.key == pygame.K_w:
                    mover_arriba = False
                elif event.key == pygame.K_s:
                    mover_abajo = False
                elif event.key == pygame.K_o:
                    teclado_o_presionada = False

        if mover_derecha:
            distancia_x = constantes.VELOCIDAD
        if mover_izquierda:
            distancia_x = -constantes.VELOCIDAD
        if mover_arriba:
            distancia_y = -constantes.VELOCIDAD
        if mover_abajo:
            distancia_y = constantes.VELOCIDAD

        jugador_pos_mundo_x = jugador.shape.x - camera.offset[0]
        jugador_pos_mundo_y = jugador.shape.y - camera.offset[1]

     #IMPORTANT COLISIONS
        if nivel == 1:
            distancia_x, distancia_y = casa_colisión(jugador_pos_mundo_x, jugador_pos_mundo_y, distancia_x, distancia_y)
            distancia_x, distancia_y = casa_grande_colision(jugador_pos_mundo_x, jugador_pos_mundo_y, distancia_x,
                                                            distancia_y)
            distancia_x, distancia_y = lago_limite1(jugador_pos_mundo_x, jugador_pos_mundo_y, distancia_x, distancia_y)
            distancia_x, distancia_y = lago_limite2(jugador_pos_mundo_x, jugador_pos_mundo_y, distancia_x, distancia_y)
            distancia_x, distancia_y = lago_limite3(jugador_pos_mundo_x, jugador_pos_mundo_y, distancia_x, distancia_y)
            distancia_x, distancia_y = lago_limite4(jugador_pos_mundo_x, jugador_pos_mundo_y, distancia_x, distancia_y)
            distancia_x, distancia_y = arbol1(jugador_pos_mundo_x, jugador_pos_mundo_y, distancia_x, distancia_y)
            distancia_x, distancia_y = arbol2(jugador_pos_mundo_x, jugador_pos_mundo_y, distancia_x, distancia_y)
            distancia_x, distancia_y = fuente(jugador_pos_mundo_x, jugador_pos_mundo_y, distancia_x, distancia_y)
            distancia_x, distancia_y = puente1(jugador_pos_mundo_x, jugador_pos_mundo_y, distancia_x, distancia_y)
            distancia_x, distancia_y = puente2(jugador_pos_mundo_x, jugador_pos_mundo_y, distancia_x, distancia_y)
            distancia_x, distancia_y = puente3(jugador_pos_mundo_x, jugador_pos_mundo_y, distancia_x, distancia_y)
        if nivel == 2:
            distancia_x, distancia_y = paredes_colision(jugador_pos_mundo_x, jugador_pos_mundo_y, distancia_x,
                                                        distancia_y, nivel)
            distancia_x, distancia_y = lago_nivel_2(jugador_pos_mundo_x, jugador_pos_mundo_y, distancia_x,
                                                        distancia_y, nivel)
            distancia_x, distancia_y = puente_nivel_2(jugador_pos_mundo_x, jugador_pos_mundo_y, distancia_x,
                                                        distancia_y, nivel)
        if nivel == 3:
            distancia_x, distancia_y = paredes_abajo_nivel3(jugador_pos_mundo_x, jugador_pos_mundo_y, distancia_x,
                                                        distancia_y, nivel)
            distancia_x, distancia_y = paredes_arriba_nivel3(jugador_pos_mundo_x, jugador_pos_mundo_y, distancia_x,
                                                            distancia_y, nivel)
            distancia_x, distancia_y = paredes_medio_nivel3(jugador_pos_mundo_x, jugador_pos_mundo_y, distancia_x,
                                                            distancia_y, nivel)
        if nivel == 4:
            distancia_x, distancia_y = paredes_nivel4(jugador_pos_mundo_x, jugador_pos_mundo_y, distancia_x,
                                                            distancia_y, nivel)

        posicion_pantalla, nivel_completado = jugador.movimiento(distancia_x, distancia_y, world.exit_tile)
        print(f"posición del jugador en el mundo: x={jugador_pos_mundo_x}, y={jugador_pos_mundo_y}")

#DRAW OF THE THINGS
        print(nivel_completado)
        print(nivel)
        camera.mover(-distancia_x, -distancia_y)
        world.update(camera)
        world.draw(ventana)
        jugador.actualizar_imagen()
        jugador.dibujar(ventana)
        vida_jugador()
        grupo_objetos.update(jugador)
        grupo_objetos.draw(ventana)

        if nivel == 2 and visible == True:

            ene_dx = 0
            ene_dy = 0

            if Villano.shape.centerx > jugador.shape.centerx:
                ene_dx = -1
            if Villano.shape.centerx < jugador.shape.centerx:
                ene_dx = 1
            if Villano.shape.centery > jugador.shape.centery:
                ene_dy = -1
            if Villano.shape.centery < jugador.shape.centery:
                ene_dy = 1
            Villano.shape.x += ene_dx
            Villano.shape.y += ene_dy

            Villano.actualizar_imagen()
            posicion_pantalla, nivel_completado = Villano.movimiento(ene_dx, ene_dy, None)


            Villano.dibujar(ventana)

            if jugador.shape.colliderect(Villano.shape) and teclado_o_presionada:
                print("Colision detectada")
                print("Teclad o detectada")
                Villano.lastimar(10)
                print(f"Villano energia: {Villano.energia}")

            if Villano.energia > 0:

                if jugador.shape.colliderect(Villano.shape):
                    print("Colision detectada")
                    jugador.lastimar(0.1)
                    print(f"Jugador energia: {jugador.energia}")

            else:
                visible = False

        if nivel == 3 and visible == True:
            ene_dx = 0
            ene_dy = 0
            if Esqueleto.shape.centerx > jugador.shape.centerx:
                ene_dx = -1
            if Esqueleto.shape.centerx < jugador.shape.centerx:
                ene_dx = 1
            if Esqueleto.shape.centery > jugador.shape.centery:
                ene_dy = -1
            if Esqueleto.shape.centery < jugador.shape.centery:
                ene_dy = 1
            Esqueleto.shape.x += ene_dx
            Esqueleto.shape.y += ene_dy

            Esqueleto.actualizar_imagen()
            posicion_pantalla, nivel_completado = Esqueleto.movimiento(ene_dx, ene_dy, None)


            Esqueleto.dibujar(ventana)

            if jugador.shape.colliderect(Esqueleto.shape) and teclado_o_presionada:
                print("Colision detectada")
                print("Teclado detectada")
                Esqueleto.lastimar(10)
                print(f"Esqueleto energia: {Esqueleto.energia}")

            if Esqueleto.energia > 0:

                if jugador.shape.colliderect(Esqueleto.shape):
                    print("Colision detectada")
                    jugador.lastimar(0.1)
                    print(f"Jugador energia: {jugador.energia}")

            else:
                visible = False
        if nivel == 4 and visible == True:
            ene_dx = 0
            ene_dy = 0

            if Esqueleto2.shape.centerx > jugador.shape.centerx:
                ene_dx = -1
            if Esqueleto2.shape.centerx < jugador.shape.centerx:
                ene_dx = 1
            if Esqueleto2.shape.centery > jugador.shape.centery:
                ene_dy = -1
            if Esqueleto2.shape.centery < jugador.shape.centery:
                ene_dy = 1
            Esqueleto2.shape.x += ene_dx
            Esqueleto2.shape.y += ene_dy

            Esqueleto2.actualizar_imagen()
            posicion_pantalla, nivel_completado = Esqueleto2.movimiento(ene_dx, ene_dy, None)


            Esqueleto2.dibujar(ventana)

            if jugador.shape.colliderect(Esqueleto2.shape) and teclado_o_presionada:
                print("Colision detectada")
                print("Teclado detectada")
                Esqueleto2.lastimar(10)
                print(f"Esqueleto energia: {Esqueleto2.energia}")

            if Esqueleto2.energia > 0:

                if jugador.shape.colliderect(Esqueleto2.shape):
                    print("Colision detectada")
                    jugador.lastimar(0.1)
                    print(f"Jugador energia: {jugador.energia}")

            else:
                visible = False

#DRAW THE POTIONS
        if pocion:
            pocion.rect.topleft = (tile_pos[0] + camera.offset[0], tile_pos[1] + camera.offset[1])
        if pocion2:
            pocion2.rect.topleft = (tile_pos2[0] + camera.offset[0], tile_pos2[1] + camera.offset[1])

#THE LEVELS
        if nivel_completado == True and nivel == 1 and jugador.energia > 50:
            nivel, world, jugador, grupo_objetos, camera = resetear_nivel_2(jugador, grupo_objetos, camera)
            cambiar_musica(2)


        if nivel_completado == True and nivel == 2 and Villano.energia <= 0:
            nivel, world, jugador, grupo_objetos, camera, Esqueleto = resetear_nivel_3(jugador, grupo_objetos, camera, animaciones_esqueleto)
            visible = True
            cambiar_musica(3)


        if nivel_completado == True and nivel == 3 and Esqueleto.energia <= 0:
            nivel, world, jugador, grupo_objetos, camera, Esqueleto, Esqueleto2 = resetear_nivel_4(jugador, grupo_objetos, camera, animaciones_esqueleto)
            visible = True
            cambiar_musica(4)



                #CREATE GROUP OF OBJETS
            grupo_objetos = pygame.sprite.Group()
            #utilizar funciona encontrar posicion tile, agregar objeto
            pocion, tile_pos = encontrar_y_agregar_objeto1(world_data, 250, pocion_roja)
            grupo_objetos.add(pocion)
    if jugador.energia <= 0:
        game_over = True
        pygame.mixer.music.pause()
    if Esqueleto2.energia <= 0:
        ganado = True
        pygame.mixer.music.pause()




    pygame.display.update()

pygame.quit()

