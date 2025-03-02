class Mundo:
    def __init__(self, nivel):
        self.map_tiles = []
        self.exit_tile = None
        self.nivel = nivel


    def process_data(self, data, tile_list):
        self.level_length = len(data)
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                image = tile_list[tile]
                image_rect = image.get_rect()
                image_x = x * 50
                image_y = y * 50
                image_rect.topleft = (image_x, image_y)
                tile_data = (image, image_rect, image_x, image_y)
                if self.nivel == 1 and tile == 87:
                    self.exit_tile = tile_data
                elif self.nivel == 2 and tile == 115:
                    self.exit_tile = tile_data
                elif self.nivel == 3 and tile == 87:
                    self.exit_tile = tile_data

                self.map_tiles.append(tile_data)

#UPDATE THE CAMERA
    def update(self, camera):
        for tile in self.map_tiles:
            tile[1].x = tile[2] + camera.offset[0]
            tile[1].y = tile[3] + camera.offset[1]

    def draw(self, surface):
        for tile in self.map_tiles:
            surface.blit(tile[0], tile[1])

#CAMERA(WIDTH, HEIGHT)
class Camera():
    def __init__(self, screen_width, screen_height, world_width, world_height):
        self.offset = [0, 0]
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.world_width = world_width
        self.world_height = world_height
#RESET THE CAMERA
    def reset(self):
        self.offset = [0,0]
#MOVE THE CAMERA
    def mover(self, dx, dy):
        self.offset[0] = min(0, max(-(self.world_width * 50 - self.screen_width),self.offset[0]+dx))
        self.offset[1] = min(0, max(-(self.world_height * 50 - self.screen_height), self.offset[1] + dy))
