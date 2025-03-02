import pygame
import constantes


class Personaje():
#ANIMATIONS
    def __init__(self, x, y, animaciones,animaciones_ataque, tipo, energia):
        self.energia= energia
        self.flip = False
        self.animaciones = animaciones
        self.animaciones_ataque = animaciones_ataque
        self.atacando = False
        self.tiempo_actualizacion = pygame.time.get_ticks()
        self.tiempo_animacion = 200
        self.ventana_index = 0
        self.image = self.animaciones[self.ventana_index]
        self.actualizar_tiempo = pygame.time.get_ticks()
        self.shape=pygame.Rect(0,0,40,40)
        self.shape.center = (x, y)
        self.tipo=tipo

#UPDATE_IMAGE
    def actualizar_imagen(self):
        cooldown_animación = 200
        self.image = self.animaciones[self.ventana_index]
        if pygame.time.get_ticks() - self.actualizar_tiempo >= cooldown_animación:
            self.ventana_index = self.ventana_index + 1
            self.actualizar_tiempo = pygame.time.get_ticks()
            if self.ventana_index >= 8:
                self.ventana_index = 0
#DRAW
    def dibujar(self, ventana):
        image_flip = pygame.transform.flip(self.image,self.flip,False)
        ventana.blit(image_flip, self.shape)
#MOVEMENT
    def movimiento(self,distancia_x, distancia_y, exit_tile):
        self.shape.x = self.shape.x + distancia_x
        self.shape.y = self.shape.y + distancia_y
        nivel_completado = False


        if distancia_x < 0:
            self.flip = True
        elif distancia_x > 0:
            self.flip =False

        posicion_pantalla = [0, 0]

        if exit_tile is not None and len(exit_tile) > 1:
            if exit_tile[1].colliderect(self.shape):
                # Your logic here

                nivel_completado = True
                print("Nivel completado")

            if self.shape.right > (constantes.WIDTH_VENTANA - constantes.LIMITE_PANTALLA):
                posicion_pantalla[0] = (constantes.WIDTH_VENTANA - constantes.LIMITE_PANTALLA)- self.shape.right
                self.shape.right = constantes.WIDTH_VENTANA - constantes.LIMITE_PANTALLA

            if self.shape.left < constantes.LIMITE_PANTALLA:
                posicion_pantalla[0] = constantes.LIMITE_PANTALLA - self.shape.left
                self.shape.left = constantes.LIMITE_PANTALLA

            if self.shape.top > (constantes.HEIGHT_VENTANA - constantes.LIMITE_PANTALLA):
                posicion_pantalla[1] = (constantes.HEIGHT_VENTANA - constantes.LIMITE_PANTALLA) -self.shape.top
                self.shape.top = constantes.HEIGHT_VENTANA - constantes.LIMITE_PANTALLA

            if self.shape.bottom < constantes.LIMITE_PANTALLA:
                posicion_pantalla[1] = constantes.LIMITE_PANTALLA - self.shape.bottom
                self.shape.bottom = constantes.LIMITE_PANTALLA

        return posicion_pantalla, nivel_completado
#UPDATE_IMAGE_ATTACK
    def actualizar_imagen(self):
        if self.atacando:
            self.animar(self.animaciones_ataque)
        else:
            self.animar(self.animaciones)
#ANIMATION
    def animar(self, animaciones):
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.tiempo_actualizacion > self.tiempo_animacion:
            self.tiempo_actualizacion = tiempo_actual
            self.ventana_index +=1
            if self.ventana_index >= len(animaciones):
                self.ventana_index = 0
                if self.atacando:
                    self.atacando = False
            self.image = animaciones[self.ventana_index]
#Attack
    def atacar(self):
        if not self.atacando:
            self.atacando = True
            self.ventana_index = 0
            self.tiempo_actualizacion = pygame.time.get_ticks()
#HURT CHARACTER
    def lastimar(self, cantidad):
        self.energia -=cantidad