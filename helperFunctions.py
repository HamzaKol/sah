from constants import bijeli, crni

def ally_colision(self, x, y):
    if self.color == 'white':
        for objekat in bijeli:
            if objekat.x == x and objekat.y == y:
                return objekat
    else:
        for objekat in crni:
            if objekat.x == x and objekat.y == y:
                return objekat
    return 'None'

def enemy_colision(self, x, y):
    if self.color == 'black':
        for objekat in bijeli:
            if objekat.x == x and objekat.y == y:
                return objekat
    else:
        for objekat in crni:
            if objekat.x == x and objekat.y == y:
                return objekat
    return 'None'

def border_colision(x, y):
    if(x<0 or y<0 or x > 600 or y > 600):
        return True
    return False
