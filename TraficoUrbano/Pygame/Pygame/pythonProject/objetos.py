import pygame.sprite

#SPRITES(ANIMATION, OBJETS)
class Objeto(pygame.sprite.Sprite):
    def __init__(self, x, y, objeto_tipo, animacion_list):
        pygame.sprite.Sprite.__init__(self)
        self.objeto_tipo = objeto_tipo

        self.animacion_list = animacion_list
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image = self.animacion_list[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
#UPDATE THE POTION
    def update(self, personaje):
        if self.rect.colliderect(personaje.shape):
            if self.objeto_tipo == 0:
                personaje.energia = personaje.energia + 25
                if personaje.energia > 100:
                    personaje.energia = 100
                self.kill()
