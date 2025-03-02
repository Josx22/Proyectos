from objetos import Objeto
#find_and_add_object1
def encontrar_y_agregar_objeto1(world_data, tile_index, imagen):
    tile_pos = None
    for x, fila in enumerate(world_data):
        for y, tile in enumerate(fila):
            if tile == tile_index + 1:
                tile_pos = (y * 50, x * 50)
                break
        if tile_pos:
            break

    if tile_pos:
        return Objeto(tile_pos[0], tile_pos[1],0,[imagen]), tile_pos
    else:
        print(f"Tile {tile_index} no encontrado")
        return None, None