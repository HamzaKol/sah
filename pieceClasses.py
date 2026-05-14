
from helperFunctions import ally_colision, border_colision, enemy_colision
from constants import bijeli, crni
from kingHelperFunctions import king_checked
from constants import Black_Bishop, Black_King, Black_Knight, Black_Pawn, Black_Queen, Black_Rook, White_Bishop, White_King, White_Knight, White_Pawn, White_Queen, White_Rook

class Pawn:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.starix = x
        self.stariy = y
        self.enp = 0
        self.obj = "Pawn"
        if color == 'white':
            self.color = 'white'
            self.object = White_Pawn
        else:
            self.color = 'black'
            self.object = Black_Pawn

    def draw(self, win):
        win.blit(self.object, (self.x, self.y))

    def move(self, potez):
        if self.color == "white":
            if ((self.stariy - 77.5) <= self.y + 37.5 <= (self.stariy + 2.5)) and (
                    self.starix - 77.5 <= self.x + 37.5 <= self.starix - 2.5):
                if((enemy_colision(self, self.starix - 75, self.stariy)) != "None"):   #EnPassant lijevi
                    if(enemy_colision(self, self.starix - 75, self.stariy)).obj == "Pawn":
                        if enemy_colision(self, self.starix - 75, self.stariy).enp == (potez-1):
                            self.x = self.starix - 75
                            self.y = self.stariy - 75
                            za_brisanje = enemy_colision(self, self.starix - 75, self.stariy)
                            crni.pop(crni.index(za_brisanje))
                            if king_checked(crni) != "None" or border_colision(self.x, self.y):
                                self.x = self.starix
                                self.y = self.stariy
                                crni.append(za_brisanje)
                                return False
                            self.starix = self.starix - 75
                            self.stariy = self.stariy - 75
                            return True
                if(enemy_colision(self, self.starix - 75, self.stariy - 75) != 'None'):
                    self.x = self.starix - 75
                    self.y = self.stariy - 75
                    za_brisanje = enemy_colision(self, self.starix - 75, self.stariy - 75)
                    crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        crni.append(za_brisanje)
                        return False
                    self.starix = self.starix - 75
                    self.stariy = self.stariy - 75
                    return True
                self.x = self.starix
                self.y = self.stariy
                return False
            if ((self.stariy - 77.5) <= self.y + 37.5 <= (self.stariy + 2.5)) and (
                    self.starix + 72.5 <= self.x + 37.5 <= self.starix + 147.5):

                if ((enemy_colision(self, self.starix + 75, self.stariy)) != "None"):  # EnPassant desni
                    if (enemy_colision(self, self.starix + 75, self.stariy)).obj == "Pawn":
                        if enemy_colision(self, self.starix + 75, self.stariy).enp == (potez - 1):
                            self.x = self.starix + 75
                            self.y = self.stariy - 75
                            za_brisanje = enemy_colision(self, self.starix + 75, self.stariy)
                            crni.pop(crni.index(za_brisanje))
                            if king_checked(crni) != "None" or border_colision(self.x, self.y):
                                self.x = self.starix
                                self.y = self.stariy
                                crni.append(za_brisanje)
                                return False
                            self.starix = self.starix + 75
                            self.stariy = self.stariy - 75
                            return True

                if(enemy_colision(self, self.starix + 75, self.stariy - 75) != 'None'):
                    self.x = self.starix + 75
                    self.y = self.stariy - 75
                    za_brisanje = enemy_colision(self, self.starix + 75, self.stariy - 75)
                    crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        crni.append(za_brisanje)
                        return False
                    self.starix = self.starix + 75
                    self.stariy = self.stariy - 75
                    return True
                self.x = self.starix
                self.y = self.stariy
                return False
            if self.stariy == 452.5:
                if ((self.stariy - 152.5) <= self.y + 37.5 <= (self.stariy - 72.5)) and (
                        self.starix - 2.5 <= self.x + 37.5 <= self.starix + 72.5):
                    if(ally_colision(self, self.starix, self.stariy - 150) != 'None' or enemy_colision(self, self.starix, self.stariy - 150) != 'None'):
                        self.x = self.starix
                        self.y = self.stariy
                        return False
                    if (ally_colision(self, self.starix, self.stariy - 75) != 'None' or enemy_colision(self, self.starix,
                                                                                              self.stariy - 75) != 'None'):
                        self.x = self.starix
                        self.y = self.stariy
                        return False
                    self.x = self.starix
                    self.y = self.stariy - 150
                    if king_checked(crni) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        return False
                    self.starix = self.x
                    self.stariy = self.y
                    self.enp = potez
                    return True
                elif (self.stariy - 75 <= self.y + 37.5 <= self.stariy) and (
                        self.starix - 2.5 <= self.x + 37.5 <= self.starix + 72.5):
                    if (ally_colision(self, self.starix, self.stariy - 75) != 'None' or enemy_colision(self, self.starix,
                                                                                              self.stariy - 75) != 'None'):
                        self.x = self.starix
                        self.y = self.stariy
                        return False
                    self.x = self.starix
                    self.y = self.stariy - 75
                    if king_checked(crni) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        return False
                    self.starix = self.x
                    self.stariy = self.y
                    return True
                else:
                    self.x = self.starix
                    self.y = self.stariy
                    return False
            else:
                if (self.stariy - 77.5 <= self.y + 37.5 <= self.stariy + 2.5) and (
                        self.starix - 2.5 <= self.x + 37.5 <= self.starix + 72.5):
                    if (ally_colision(self, self.starix, self.stariy - 75) != 'None' or enemy_colision(self, self.starix,
                                                                                              self.stariy - 75) != 'None'):
                        self.x = self.starix
                        self.y = self.stariy
                        return False
                    self.x = self.starix
                    self.y = self.stariy - 75
                    if king_checked(crni) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        return False
                    self.starix = self.x
                    self.stariy = self.y
                    return True
                else:
                    self.x = self.starix
                    self.y = self.stariy
                    return False
        else:
            if ((self.stariy + 77.5) <= self.y + 37.5 <= (self.stariy + 152.5)) and (
                    self.starix + 72.5 <= self.x + 37.5 <= self.starix + 147.5):
                if ((enemy_colision(self, self.starix + 75, self.stariy)) != "None"):  # EnPassant desni
                    if (enemy_colision(self, self.starix + 75, self.stariy)).obj == "Pawn":
                        if enemy_colision(self, self.starix + 75, self.stariy).enp == (potez - 1):
                            self.x = self.starix + 75
                            self.y = self.stariy + 75
                            za_brisanje = enemy_colision(self, self.starix + 75, self.stariy)
                            bijeli.pop(bijeli.index(za_brisanje))
                            if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                                self.x = self.starix
                                self.y = self.stariy
                                bijeli.append(za_brisanje)
                                return False
                            self.starix = self.starix + 75
                            self.stariy = self.stariy + 75
                            return True

                if(enemy_colision(self, self.starix + 75, self.stariy + 75) != 'None'):
                    self.x = self.starix + 75
                    self.y = self.stariy + 75
                    za_brisanje = enemy_colision(self, self.starix + 75, self.stariy + 75)
                    bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        bijeli.append(za_brisanje)
                        return False
                    self.starix = self.starix + 75
                    self.stariy = self.stariy + 75
                    return True
                self.x = self.starix
                self.y = self.stariy
                return False
            if ((self.stariy + 77.5) <= self.y + 37.5 <= (self.stariy + 152.5)) and (
                    self.starix - 77.5 <= self.x + 37.5 <= self.starix - 2.5):

                if ((enemy_colision(self, self.starix - 75, self.stariy)) != "None"):  # EnPassant lijevi
                    if (enemy_colision(self, self.starix - 75, self.stariy)).obj == "Pawn":
                        if enemy_colision(self, self.starix - 75, self.stariy).enp == (potez - 1):
                            self.x = self.starix - 75
                            self.y = self.stariy + 75
                            za_brisanje = enemy_colision(self, self.starix - 75, self.stariy)
                            bijeli.pop(bijeli.index(za_brisanje))
                            if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                                self.x = self.starix
                                self.y = self.stariy
                                bijeli.append(za_brisanje)
                                return False
                            self.starix = self.starix - 75
                            self.stariy = self.stariy + 75
                            return True

                if(enemy_colision(self, self.starix - 75, self.stariy + 75) != 'None'):
                    self.x = self.starix - 75
                    self.y = self.stariy + 75
                    za_brisanje = enemy_colision(self, self.starix - 75, self.stariy + 75)
                    bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        bijeli.append(za_brisanje)
                        return False
                    self.starix = self.starix - 75
                    self.stariy = self.stariy + 75
                    return True
                self.x = self.starix
                self.y = self.stariy
                return False
            if self.stariy == 77.5:
                if ((self.stariy + 147.5) <= self.y + 37.5 <= (self.stariy + 222.5)) and (
                        self.starix - 2.5 <= self.x + 37.5 <= self.starix + 72.5):
                    if (ally_colision(self, self.starix, self.stariy + 150) != 'None' or enemy_colision(self, self.starix,
                                                                                              self.stariy + 150) != 'None'):
                        self.x = self.starix
                        self.y = self.stariy
                        return False
                    if (ally_colision(self, self.starix, self.stariy + 75) != 'None' or enemy_colision(self, self.starix,
                                                                                              self.stariy + 75) != 'None'):
                        self.x = self.starix
                        self.y = self.stariy
                        return False
                    self.x = self.starix
                    self.y = self.stariy + 150
                    if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        return False
                    self.starix = self.x
                    self.stariy = self.y
                    self.enp = potez
                    return True
                elif (self.stariy + 72.5 <= self.y + 37.5 <= self.stariy + 147.5) and (
                        self.starix - 2.5 <= self.x + 37.5 <= self.starix + 72.5):
                    if (ally_colision(self, self.starix, self.stariy + 75) != 'None' or enemy_colision(self, self.starix,
                                                                                              self.stariy + 75) != 'None'):
                        self.x = self.starix
                        self.y = self.stariy
                        return False
                    self.x = self.starix
                    self.y = self.stariy + 75
                    if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        return False
                    self.starix = self.x
                    self.stariy = self.y
                    return True
                else:
                    self.x = self.starix
                    self.y = self.stariy
                    return False
            else:
                if (self.stariy + 72.5 <= self.y + 37.5 <= self.stariy + 147.5) and (
                        self.starix - 2.5 <= self.x + 37.5 <= self.starix + 72.5):
                    if (ally_colision(self, self.starix, self.stariy + 75) != 'None' or enemy_colision(self, self.starix,
                                                                                              self.stariy + 75) != 'None'):
                        self.x = self.starix
                        self.y = self.stariy
                        return False
                    self.x = self.starix
                    self.y = self.stariy + 75
                    if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        return False
                    self.starix = self.x
                    self.stariy = self.y
                    return True
                else:
                    self.x = self.starix
                    self.y = self.stariy
                    return False

class Knight:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.starix = x
        self.stariy = y
        self.obj = "Knight"
        if color == 'white':
            self.color = 'white'
            self.object = White_Knight
        else:
            self.color = 'black'
            self.object = Black_Knight

    def draw(self, win):
        win.blit(self.object, (self.x, self.y))

    def move(self, potez):
        kontrola = 0
        if ((self.stariy - 152.5) <= self.y + 37.5 <= (self.stariy - 72.5)):
            if (self.starix +72.5 <= self.x + 37.5 <= self.starix + 147.5):
                if (ally_colision(self, self.starix + 75, self.stariy - 150) != 'None'):
                    self.x = self.starix
                    self.y = self.stariy
                    return False

                self.x = self.starix + 75
                self.y = self.stariy - 150

                if (enemy_colision(self, self.starix + 75, self.stariy - 150) != 'None'):
                    za_brisanje = enemy_colision(self, self.starix + 75, self.stariy - 150)
                    kontrola = 1
                    if self.color == 'white':
                        crni.pop(crni.index(za_brisanje))
                    else:
                        bijeli.pop(bijeli.index(za_brisanje))

                if self.color == "white":
                    if king_checked(crni) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        if kontrola == 1:
                            crni.append(za_brisanje)
                        return False
                else:
                    if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        if kontrola == 1:
                            bijeli.append(za_brisanje)
                        return False

                self.starix = self.x
                self.stariy = self.y
                return True

            elif (self.starix - 77.5 <= self.x + 37.5 <= self.starix - 2.5):
                if (ally_colision(self, self.starix - 75, self.stariy - 150) != 'None'):
                    self.x = self.starix
                    self.y = self.stariy
                    return False
                self.x = self.starix - 75
                self.y = self.stariy - 150

                if (enemy_colision(self, self.starix - 75, self.stariy - 150) != 'None'):
                    za_brisanje = enemy_colision(self, self.starix - 75, self.stariy - 150)
                    kontrola = 1
                    if self.color == 'white':
                        crni.pop(crni.index(za_brisanje))
                    else:
                        bijeli.pop(bijeli.index(za_brisanje))

                if self.color == "white":
                    if king_checked(crni) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        if kontrola == 1:
                            crni.append(za_brisanje)
                        return False
                else:
                    if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        if kontrola == 1:
                            bijeli.append(za_brisanje)
                        return False
                self.starix = self.x
                self.stariy = self.y
                return True
            else:
                self.x = self.starix
                self.y = self.stariy
                return False
        elif((self.stariy + 147.5) <= self.y + 37.5 <= (self.stariy + 222.5)):
            if (self.starix + 72.5 <= self.x + 37.5 <= self.starix + 147.5):
                if (ally_colision(self, self.starix + 75, self.stariy + 150) != 'None'):
                    self.x = self.starix
                    self.y = self.stariy
                    return False
                self.x = self.starix + 75
                self.y = self.stariy + 150
                if (enemy_colision(self, self.starix + 75, self.stariy + 150) != 'None'):
                    za_brisanje = enemy_colision(self, self.starix + 75, self.stariy + 150)
                    kontrola = 1
                    if self.color == 'white':
                        crni.pop(crni.index(za_brisanje))
                    else:
                        bijeli.pop(bijeli.index(za_brisanje))
                if self.color == "white":
                    if king_checked(crni) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        if kontrola == 1:
                            crni.append(za_brisanje)
                        return False
                else:
                    if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        if kontrola == 1:
                            bijeli.append(za_brisanje)
                        return False

                self.starix = self.x
                self.stariy = self.y
                return True
            elif (self.starix - 77.5 <= self.x + 37.5 <= self.starix - 2.5):
                if (ally_colision(self, self.starix - 75, self.stariy + 150) != 'None'):
                    self.x = self.starix
                    self.y = self.stariy
                    return False
                self.x = self.starix - 75
                self.y = self.stariy + 150

                if (enemy_colision(self, self.starix - 75, self.stariy + 150) != 'None'):
                    za_brisanje = enemy_colision(self, self.starix - 75, self.stariy + 150)
                    kontrola = 1
                    if self.color == 'white':
                        crni.pop(crni.index(za_brisanje))
                    else:
                        bijeli.pop(bijeli.index(za_brisanje))

                if self.color == "white":
                    if king_checked(crni) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        if kontrola == 1:
                            crni.append(za_brisanje)
                        return False
                else:
                    if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        if kontrola == 1:
                            bijeli.append(za_brisanje)
                        return False

                self.starix = self.x
                self.stariy = self.y
                return True
            else:
                self.x = self.starix
                self.y = self.stariy
                return False
        elif (self.starix + 147.5 <= self.x + 37.5 <= self.starix + 222.5):
            if (self.stariy - 77.5 <= self.y + 37.5 <= self.stariy + 2.5):
                if (ally_colision(self, self.starix + 150, self.stariy - 75) != 'None'):
                    self.x = self.starix
                    self.y = self.stariy
                    return False
                self.x = self.starix + 150
                self.y = self.stariy - 75
                if (enemy_colision(self, self.starix + 150, self.stariy - 75) != 'None'):
                    za_brisanje = enemy_colision(self, self.starix + 150, self.stariy - 75)
                    kontrola = 1
                    if self.color == 'white':
                        crni.pop(crni.index(za_brisanje))
                    else:
                        bijeli.pop(bijeli.index(za_brisanje))
                if self.color == "white":
                    if king_checked(crni) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        if kontrola == 1:
                            crni.append(za_brisanje)
                        return False
                else:
                    if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        if kontrola == 1:
                            bijeli.append(za_brisanje)
                        return False
                self.starix = self.x
                self.stariy = self.y
                return True
            elif (self.stariy + 72.5 <= self.y + 37.5 <= self.stariy + 147.5):
                if (ally_colision(self, self.starix + 150, self.stariy + 75) != 'None'):
                    self.x = self.starix
                    self.y = self.stariy
                    return False

                self.x = self.starix + 150
                self.y = self.stariy + 75
                if (enemy_colision(self, self.starix + 150, self.stariy + 75) != 'None'):
                    za_brisanje = enemy_colision(self, self.starix + 150, self.stariy + 75)
                    kontrola = 1
                    if self.color == 'white':
                        crni.pop(crni.index(za_brisanje))
                    else:
                        bijeli.pop(bijeli.index(za_brisanje))
                if self.color == "white":
                    if king_checked(crni) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        if kontrola == 1:
                            crni.append(za_brisanje)
                        return False
                else:
                    if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        if kontrola == 1:
                            bijeli.append(za_brisanje)
                        return False

                self.starix = self.x
                self.stariy = self.y
                return True
            else:
                self.x = self.starix
                self.y = self.stariy
                return False



        elif (self.starix - 152.5 <= self.x + 37.5 <= self.starix + 77.5):
            if (self.stariy - 77.5 <= self.y + 37.5 <= self.stariy + 2.5):
                if (ally_colision(self, self.starix - 150, self.stariy - 75) != 'None'):
                    self.x = self.starix
                    self.y = self.stariy
                    return False

                self.x = self.starix - 150
                self.y = self.stariy - 75
                if (enemy_colision(self, self.starix - 150, self.stariy - 75) != 'None'):
                    za_brisanje = enemy_colision(self, self.starix - 150, self.stariy - 75)
                    kontrola = 1
                    if self.color == 'white':
                        crni.pop(crni.index(za_brisanje))
                    else:
                        bijeli.pop(bijeli.index(za_brisanje))
                if self.color == "white":
                    if king_checked(crni) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        if kontrola == 1:
                            crni.append(za_brisanje)
                        return False
                else:
                    if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        if kontrola == 1:
                            bijeli.append(za_brisanje)
                        return False

                self.starix = self.x
                self.stariy = self.y
                return True
            elif (self.stariy + 72.5 <= self.y + 37.5 <= self.stariy + 147.5):
                if (ally_colision(self, self.starix - 150, self.stariy + 75) != 'None'):
                    self.x = self.starix
                    self.y = self.stariy
                    return False

                self.x = self.starix - 150
                self.y = self.stariy + 75
                if (enemy_colision(self, self.starix - 150, self.stariy + 75) != 'None'):
                    za_brisanje = enemy_colision(self, self.starix - 150, self.stariy + 75)
                    kontrola = 1
                    if self.color == 'white':
                        crni.pop(crni.index(za_brisanje))
                    else:
                        bijeli.pop(bijeli.index(za_brisanje))
                if self.color == "white":
                    if king_checked(crni) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        if kontrola == 1:
                            crni.append(za_brisanje)
                        return False
                else:
                    if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        if kontrola == 1:
                            bijeli.append(za_brisanje)
                        return False

                self.starix = self.x
                self.stariy = self.y
                return True
            else:
                self.x = self.starix
                self.y = self.stariy
                return False
        else:
            self.x = self.starix
            self.y = self.stariy
            return False

class Bishop:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.starix = x
        self.stariy = y
        self.obj = "Bishop"
        if color == 'white':
            self.color = 'white'
            self.object = White_Bishop
        else:
            self.color = 'black'
            self.object = Black_Bishop

    def draw(self, win):
        win.blit(self.object, (self.x, self.y))
    def move(self, potez):
        kontrola = 0
        novix = self.starix
        noviy = self.stariy
        for i in range(7):
            if (ally_colision(self, novix - 75, noviy - 75) != 'None'):
                break
            if(noviy - 77.5 <= self.y + 37.5 <= noviy - 2.5):
                if(novix - 77.5 <= self.x + 37.5 <= novix - 2.5):
                    if (ally_colision(self, novix - 75, noviy - 75) != 'None'):
                        break
                    if (enemy_colision(self, novix - 75, noviy - 75) != 'None'):
                        kontrola = 1
                        za_brisanje = enemy_colision(self, novix - 75, noviy - 75)
                        if(self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix - 75
                    self.y = noviy - 75
                    if self.color == "white":
                        if king_checked(crni) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                crni.append(za_brisanje)
                            return False
                    else:
                        if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                bijeli.append(za_brisanje)
                            return False
                    self.starix = novix - 75
                    self.stariy = noviy - 75
                    return True
            if (enemy_colision(self, novix - 75, noviy - 75) != 'None'):
                break
            novix -= 75
            noviy -= 75
        kontrola = 0
        novix = self.starix
        noviy = self.stariy
        for i in range(7):
            if (ally_colision(self, novix + 75, noviy - 75) != 'None'):
                break
            if (noviy - 77.5 <= self.y + 37.5 <= noviy - 2.5):
                if(novix + 72.5 <= self.x + 37.5 <= novix + 147.5):
                    if (ally_colision(self, novix + 75, noviy - 75) != 'None'):
                        break
                    if (enemy_colision(self, novix + 75, noviy - 75) != 'None'):
                        za_brisanje = enemy_colision(self, novix + 75, noviy - 75)
                        kontrola = 1
                        if(self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix + 75
                    self.y = noviy - 75
                    if self.color == "white":
                        if king_checked(crni) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                crni.append(za_brisanje)
                            return False
                    else:
                        if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                bijeli.append(za_brisanje)
                            return False
                    self.starix = novix + 75
                    self.stariy = noviy - 75
                    return True
            if (enemy_colision(self, novix + 75, noviy - 75) != 'None'):
                break
            novix += 75
            noviy -= 75
        kontrola = 0
        novix = self.starix
        noviy = self.stariy
        for i in range(7):
            if (ally_colision(self, novix - 75, noviy + 75) != 'None'):
                break
            if (noviy + 72.5 <= self.y + 37.5 <= noviy + 147.5):
                if (novix - 77.5 <= self.x + 37.5 <= novix - 2.5):
                    if (ally_colision(self, novix - 75, noviy + 75) != 'None'):
                        break
                    if (enemy_colision(self, novix - 75, noviy + 75) != 'None'):
                        za_brisanje = enemy_colision(self, novix - 75, noviy + 75)
                        kontrola = 1
                        if(self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix - 75
                    self.y = noviy + 75
                    if self.color == "white":
                        if king_checked(crni) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                crni.append(za_brisanje)
                            return False
                    else:
                        if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                bijeli.append(za_brisanje)
                            return False
                    self.starix = novix - 75
                    self.stariy = noviy + 75
                    return True
            if (enemy_colision(self, novix - 75, noviy + 75) != 'None'):
                break
            novix -= 75
            noviy += 75
        kontrola = 0
        novix = self.starix
        noviy = self.stariy
        for i in range(7):
            if (ally_colision(self, novix + 75, noviy + 75) != 'None'):
                break
            if (noviy + 72.5 <= self.y + 37.5 <= noviy + 147.5):
                if (novix + 72.5 <= self.x + 37.5 <= novix + 147.5):
                    if (ally_colision(self, novix + 75, noviy + 75) != 'None'):
                        break
                    if (enemy_colision(self, novix + 75, noviy + 75) != 'None'):
                        za_brisanje = enemy_colision(self, novix + 75, noviy + 75)
                        kontrola = 1
                        if(self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix + 75
                    self.y = noviy + 75
                    if self.color == "white":
                        if king_checked(crni) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                crni.append(za_brisanje)
                            return False
                    else:
                        if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                bijeli.append(za_brisanje)
                            return False
                    self.starix = novix + 75
                    self.stariy = noviy + 75
                    return True
            if (enemy_colision(self, novix + 75, noviy + 75) != 'None'):
                break
            novix += 75
            noviy += 75
        self.x = self.starix
        self.y = self.stariy
        return False

class Rook:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.starix = x
        self.stariy = y
        self.castle = 0
        self.obj = "Rook"
        if color == 'white':
            self.color = 'white'
            self.object = White_Rook
        else:
            self.color = 'black'
            self.object = Black_Rook

    def draw(self, win):
        win.blit(self.object, (self.x, self.y))

    def move(self, potez):
        kontrola = 0
        noviy = self.stariy
        novix = self.starix
        for i in range(7):
            if (ally_colision(self, novix, noviy - 75) != 'None'):
                break
            if (noviy - 77.5 <= self.y + 37.5 <= noviy - 2.5):
                if (novix - 2.5 <= self.x + 37.5 <= novix + 72.5):
                    if (ally_colision(self, novix, noviy - 75) != 'None'):
                        break
                    if (enemy_colision(self, novix, noviy - 75) != 'None'):
                        za_brisanje = enemy_colision(self, novix, noviy - 75)
                        kontrola = 1
                        if (self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix
                    self.y = noviy - 75
                    if self.color == "white":
                        if king_checked(crni) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                crni.append(za_brisanje)
                            return False
                    else:
                        if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                bijeli.append(za_brisanje)
                            return False
                    self.starix = novix
                    self.stariy = noviy - 75
                    self.castle = potez
                    return True
            if (enemy_colision(self, novix, noviy - 75) != 'None'):
                break
            noviy -= 75
        kontrola = 0
        noviy = self.stariy

        for i in range(7):
            if (ally_colision(self, novix, noviy + 75) != 'None'):
                break
            if (noviy + 72.5 <= self.y + 37.5 <= noviy + 147.5):
                if (novix - 2.5 <= self.x + 37.5 <= novix + 72.5):
                    if (ally_colision(self, novix, noviy + 75) != 'None'):
                        break
                    if (enemy_colision(self, novix, noviy + 75) != 'None'):
                        za_brisanje = enemy_colision(self, novix, noviy + 75)
                        kontrola = 1
                        if (self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix
                    self.y = noviy + 75
                    if self.color == "white":
                        if king_checked(crni) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                crni.append(za_brisanje)
                            return False
                    else:
                        if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                bijeli.append(za_brisanje)
                            return False
                    self.starix = novix
                    self.stariy = noviy + 75
                    self.castle = potez
                    return True
            if (enemy_colision(self, novix, noviy + 75) != 'None'):
                break
            noviy += 75
        kontrola = 0
        noviy = self.stariy

        for i in range(7):
            if (ally_colision(self, novix  - 75, noviy) != 'None'):
                break
            if(novix - 77.5 <= self.x + 37.5 <= novix - 2.5):
                if (noviy - 2.5 <= self.y + 37.5 <= noviy + 72.5):
                    if (ally_colision(self, novix - 75, noviy) != 'None'):
                        break
                    if (enemy_colision(self, novix - 75, noviy) != 'None'):
                        za_brisanje = enemy_colision(self, novix - 75, noviy)
                        kontrola = 1
                        if (self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix - 75
                    self.y = noviy
                    if self.color == "white":
                        if king_checked(crni) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                crni.append(za_brisanje)
                            return False
                    else:
                        if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                bijeli.append(za_brisanje)
                            return False
                    self.starix = novix - 75
                    self.stariy = noviy
                    self.castle = potez
                    return True
            if (enemy_colision(self, novix  - 75, noviy) != 'None'):
                break
            novix -= 75
        kontrola = 0
        novix = self.starix

        for i in range(7):
            if (ally_colision(self, novix  + 75, noviy) != 'None'):
                break
            if(novix + 72.5 <= self.x + 37.5 <= novix + 147.5):
                if (noviy - 2.5 <= self.y + 37.5 <= noviy + 72.5):
                    if (ally_colision(self, novix + 75, noviy) != 'None'):
                        break
                    if (enemy_colision(self, novix + 75, noviy) != 'None'):
                        za_brisanje = enemy_colision(self, novix + 75, noviy)
                        kontrola = 1
                        if (self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix + 75
                    self.y = noviy
                    if self.color == "white":
                        if king_checked(crni) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                crni.append(za_brisanje)
                            return False
                    else:
                        if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                bijeli.append(za_brisanje)
                            return False
                    self.starix = novix + 75
                    self.stariy = noviy
                    self.castle = potez
                    return True
            if (enemy_colision(self, novix  + 75, noviy) != 'None'):
                break
            novix += 75

        self.x = self.starix
        self.y = self.stariy
        return False

class Queen:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.starix = x
        self.stariy = y
        self.obj = "Queen"
        if color == 'white':
            self.color = 'white'
            self.object = White_Queen
        else:
            self.color = 'black'
            self.object = Black_Queen

    def draw(self, win):
        win.blit(self.object, (self.x, self.y))

    def move(self, potez):
        kontrola = 0
        noviy = self.stariy
        novix = self.starix
        for i in range(7):
            if (ally_colision(self, novix, noviy - 75) != 'None'):
                break
            if (noviy - 77.5 <= self.y + 37.5 <= noviy - 2.5):
                if (novix - 2.5 <= self.x + 37.5 <= novix + 72.5):
                    if (ally_colision(self, novix, noviy - 75) != 'None'):
                        break
                    if (enemy_colision(self, novix, noviy - 75) != 'None'):
                        za_brisanje = enemy_colision(self, novix, noviy - 75)
                        kontrola = 1
                        if (self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix
                    self.y = noviy - 75
                    if self.color == "white":
                        if king_checked(crni) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                crni.append(za_brisanje)
                            return False
                    else:
                        if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                bijeli.append(za_brisanje)
                            return False
                    self.starix = novix
                    self.stariy = noviy - 75
                    return True
            if (enemy_colision(self, novix, noviy - 75) != 'None'):
                break
            noviy -= 75
        kontrola = 0
        noviy = self.stariy

        for i in range(7):
            if (ally_colision(self, novix, noviy + 75) != 'None'):
                break
            if (noviy + 72.5 <= self.y + 37.5 <= noviy + 147.5):
                if (novix - 2.5 <= self.x + 37.5 <= novix + 72.5):
                    if (ally_colision(self, novix, noviy + 75) != 'None'):
                        break
                    if (enemy_colision(self, novix, noviy + 75) != 'None'):
                        za_brisanje = enemy_colision(self, novix, noviy + 75)
                        kontrola = 1
                        if (self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix
                    self.y = noviy + 75
                    if self.color == "white":
                        if king_checked(crni) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                crni.append(za_brisanje)
                            return False
                    else:
                        if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                bijeli.append(za_brisanje)
                            return False
                    self.starix = novix
                    self.stariy = noviy + 75
                    return True
            if (enemy_colision(self, novix, noviy + 75) != 'None'):
                break
            noviy += 75
        kontrola = 0
        noviy = self.stariy

        for i in range(7):
            if (ally_colision(self, novix - 75, noviy) != 'None'):
                break
            if (novix - 77.5 <= self.x + 37.5 <= novix - 2.5):
                if (noviy - 2.5 <= self.y + 37.5 <= noviy + 72.5):
                    if (ally_colision(self, novix - 75, noviy) != 'None'):
                        break
                    if (enemy_colision(self, novix - 75, noviy) != 'None'):
                        za_brisanje = enemy_colision(self, novix - 75, noviy)
                        kontrola = 1
                        if (self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix - 75
                    self.y = noviy
                    if self.color == "white":
                        if king_checked(crni) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                crni.append(za_brisanje)
                            return False
                    else:
                        if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                bijeli.append(za_brisanje)
                            return False
                    self.starix = novix - 75
                    self.stariy = noviy
                    return True
            if (enemy_colision(self, novix - 75, noviy) != 'None'):
                break
            novix -= 75
        kontrola = 0
        novix = self.starix

        for i in range(7):
            if (ally_colision(self, novix + 75, noviy) != 'None'):
                break
            if (novix + 72.5 <= self.x + 37.5 <= novix + 147.5):
                if (noviy - 2.5 <= self.y + 37.5 <= noviy + 72.5):
                    if (ally_colision(self, novix + 75, noviy) != 'None'):
                        break
                    if (enemy_colision(self, novix + 75, noviy) != 'None'):
                        za_brisanje = enemy_colision(self, novix + 75, noviy)
                        kontrola = 1
                        if (self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix + 75
                    self.y = noviy
                    if self.color == "white":
                        if king_checked(crni) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                crni.append(za_brisanje)
                            return False
                    else:
                        if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                bijeli.append(za_brisanje)
                            return False
                    self.starix = novix + 75
                    self.stariy = noviy
                    return True
            if (enemy_colision(self, novix + 75, noviy) != 'None'):
                break
            novix += 75
        kontrola = 0
        novix = self.starix
        noviy = self.stariy
        for i in range(7):
            if (ally_colision(self, novix - 75, noviy - 75) != 'None'):
                break
            if (noviy - 77.5 <= self.y + 37.5 <= noviy - 2.5):
                if (novix - 77.5 <= self.x + 37.5 <= novix - 2.5):
                    if (ally_colision(self, novix - 75, noviy - 75) != 'None'):
                        break
                    if (enemy_colision(self, novix - 75, noviy - 75) != 'None'):
                        za_brisanje = enemy_colision(self, novix - 75, noviy - 75)
                        kontrola = 1
                        if (self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix - 75
                    self.y = noviy - 75
                    if self.color == "white":
                        if king_checked(crni) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                crni.append(za_brisanje)
                            return False
                    else:
                        if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                bijeli.append(za_brisanje)
                            return False
                    self.starix = novix - 75
                    self.stariy = noviy - 75
                    return True
            if (enemy_colision(self, novix - 75, noviy - 75) != 'None'):
                break
            novix -= 75
            noviy -= 75
        kontrola = 0
        novix = self.starix
        noviy = self.stariy
        for i in range(7):
            if (ally_colision(self, novix + 75, noviy - 75) != 'None'):
                break
            if (noviy - 77.5 <= self.y + 37.5 <= noviy - 2.5):
                if (novix + 72.5 <= self.x + 37.5 <= novix + 147.5):
                    if (ally_colision(self, novix + 75, noviy - 75) != 'None'):
                        break
                    if (enemy_colision(self, novix + 75, noviy - 75) != 'None'):
                        za_brisanje = enemy_colision(self, novix + 75, noviy - 75)
                        kontrola = 1
                        if (self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix + 75
                    self.y = noviy - 75
                    if self.color == "white":
                        if king_checked(crni) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                crni.append(za_brisanje)
                            return False
                    else:
                        if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                bijeli.append(za_brisanje)
                            return False
                    self.starix = novix + 75
                    self.stariy = noviy - 75
                    return True
            if (enemy_colision(self, novix + 75, noviy - 75) != 'None'):
                break
            novix += 75
            noviy -= 75
        kontrola = 0
        novix = self.starix
        noviy = self.stariy
        for i in range(7):
            if (ally_colision(self, novix - 75, noviy + 75) != 'None'):
                break
            if (noviy + 72.5 <= self.y + 37.5 <= noviy + 147.5):
                if (novix - 77.5 <= self.x + 37.5 <= novix - 2.5):
                    if (ally_colision(self, novix - 75, noviy + 75) != 'None'):
                        break
                    if (enemy_colision(self, novix - 75, noviy + 75) != 'None'):
                        za_brisanje = enemy_colision(self, novix - 75, noviy + 75)
                        kontrola = 1
                        if (self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix - 75
                    self.y = noviy + 75
                    if self.color == "white":
                        if king_checked(crni) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                crni.append(za_brisanje)
                            return False
                    else:
                        if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                bijeli.append(za_brisanje)
                            return False
                    self.starix = novix - 75
                    self.stariy = noviy + 75
                    return True
            if (enemy_colision(self, novix - 75, noviy + 75) != 'None'):
                break
            novix -= 75
            noviy += 75
        kontrola = 0
        novix = self.starix
        noviy = self.stariy
        for i in range(7):
            if (ally_colision(self, novix + 75, noviy + 75) != 'None'):
                break
            if (noviy + 72.5 <= self.y + 37.5 <= noviy + 147.5):
                if (novix + 72.5 <= self.x + 37.5 <= novix + 147.5):
                    if (ally_colision(self, novix + 75, noviy + 75) != 'None'):
                        break
                    if (enemy_colision(self, novix + 75, noviy + 75) != 'None'):
                        za_brisanje = enemy_colision(self, novix + 75, noviy + 75)
                        kontrola = 1
                        if (self.color == 'white'):
                            crni.pop(crni.index(za_brisanje))
                        else:
                            bijeli.pop(bijeli.index(za_brisanje))
                    self.x = novix + 75
                    self.y = noviy + 75
                    if self.color == "white":
                        if king_checked(crni) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                crni.append(za_brisanje)
                            return False
                    else:
                        if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                            self.x = self.starix
                            self.y = self.stariy
                            if kontrola == 1:
                                bijeli.append(za_brisanje)
                            return False
                    self.starix = novix + 75
                    self.stariy = noviy + 75
                    return True
            if (enemy_colision(self, novix + 75, noviy + 75) != 'None'):
                break
            novix += 75
            noviy += 75
        self.x = self.starix
        self.y = self.stariy
        return False

class King:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.starix = x
        self.stariy = y
        self.castle = 0
        self.obj = "King"
        if color == 'white':
            self.color = 'white'
            self.object = White_King
        else:
            self.color = 'black'
            self.object = Black_King

    def draw(self, win):
        win.blit(self.object, (self.x, self.y))

    def move(self, potez):
        kontrola = 0
        if self.castle == 0:
            if (self.starix + 147.5 <= self.x + 37.5 <= self.starix + 222.5) and (     #desni castle
                    self.stariy - 2.5 <= self.y + 37.5 <= self.stariy + 72.5):
                self.x = self.starix
                self.y = self.stariy
                if self.color == "white":
                    if king_checked(crni) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        return False
                else:
                    if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        return False
                noviy = self.stariy
                novix = self.starix + 75
                for i in range(4):
                    if enemy_colision(self, novix, noviy) != "None":
                        self.x = self.starix
                        self.y = self.stariy
                        return False
                    if ally_colision(self, novix, noviy)!= "None":
                        if ally_colision(self, novix, noviy).obj != "Rook":
                            self.x = self.starix
                            self.y = self.stariy
                            return False
                        if ally_colision(self, novix, noviy).castle != 0:
                            self.x = self.starix
                            self.y = self.stariy
                            return False
                        else:

                            self.x = self.starix + 75
                            self.y = self.stariy
                            if self.color == "white":
                                if king_checked(crni) != "None" or border_colision(self.x, self.y):
                                    self.x = self.starix
                                    self.y = self.stariy
                                    return False
                            else:
                                if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                                    self.x = self.starix
                                    self.y = self.stariy
                                    return False
                            self.x = self.starix + 150
                            if self.color == "white":
                                if king_checked(crni) != "None" or border_colision(self.x, self.y):
                                    self.x = self.starix
                                    self.y = self.stariy
                                    return False
                            else:
                                if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                                    self.x = self.starix
                                    self.y = self.stariy
                                    return False
                            self.starix += 150
                            self.castle = potez
                            ally_colision(self, novix, noviy).starix -= 150
                            ally_colision(self, novix, noviy).x -= 150
                            return True
                    novix += 75

            if (self.starix - 152.5 <= self.x + 37.5 <= self.starix - 77.5) and (         #lijevi castle
                    self.stariy - 2.5 <= self.y + 37.5 <= self.stariy + 72.5):
                self.x = self.starix
                self.y = self.stariy
                if self.color == "white":
                    if king_checked(crni) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        return False
                else:
                    if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                        self.x = self.starix
                        self.y = self.stariy
                        return False
                noviy = self.stariy
                novix = self.starix - 75
                for i in range(4):
                    if enemy_colision(self, novix, noviy) != "None":
                        return False
                    if ally_colision(self, novix, noviy)!= "None":
                        if ally_colision(self, novix, noviy).obj != "Rook":
                            return False
                        if ally_colision(self, novix, noviy).castle != 0:
                            return False
                        else:
                            self.x = self.starix - 75
                            if self.color == "white":
                                if king_checked(crni) != "None" or border_colision(self.x, self.y):
                                    self.x = self.starix
                                    self.y = self.stariy
                                    return False
                            else:
                                if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                                    self.x = self.starix
                                    self.y = self.stariy
                                    return False
                            self.x = self.starix - 150
                            if self.color == "white":
                                if king_checked(crni) != "None" or border_colision(self.x, self.y):
                                    self.x = self.starix
                                    self.y = self.stariy
                                    return False
                            else:
                                if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                                    self.x = self.starix
                                    self.y = self.stariy
                                    return False
                            ally_colision(self, novix, noviy).starix += 225
                            ally_colision(self, novix, noviy).x += 225
                            self.y = self.stariy
                            self.starix -= 150
                            self.castle = potez
                            return True
                    novix -= 75

        if (self.stariy - 77.5 <= self.y + 37.5 <= self.stariy + 2.5) and (
                self.starix - 2.5 <= self.x + 37.5 <= self.starix + 72.5):
            if (ally_colision(self, self.starix, self.stariy - 75) != 'None'):
                self.x = self.starix
                self.y = self.stariy
                return False
            if (enemy_colision(self, self.starix, self.stariy - 75) != 'None'):
                za_brisanje = enemy_colision(self, self.starix, self.stariy - 75)
                kontrola = 1
                if (self.color == 'white'):
                    crni.pop(crni.index(za_brisanje))
                else:
                    bijeli.pop(bijeli.index(za_brisanje))
            self.x = self.starix
            self.y = self.stariy - 75
            if self.color == "white":
                if king_checked(crni) != "None" or border_colision(self.x, self.y):
                    self.x = self.starix
                    self.y = self.stariy
                    if kontrola == 1:
                        crni.append(za_brisanje)
                    return False
            else:
                if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                    self.x = self.starix
                    self.y = self.stariy
                    if kontrola == 1:
                        bijeli.append(za_brisanje)
                    return False
            self.starix = self.x
            self.stariy = self.y
            self.castle = potez
            return True
        elif (self.stariy + 72.5 <= self.y + 37.5 <= self.stariy + 147.5) and (
                        self.starix - 2.5 <= self.x + 37.5 <= self.starix + 72.5):
            if (ally_colision(self, self.starix, self.stariy + 75) != 'None'):
                self.x = self.starix
                self.y = self.stariy
                return False
            if (enemy_colision(self, self.starix, self.stariy + 75) != 'None'):
                za_brisanje = enemy_colision(self, self.starix, self.stariy + 75)
                kontrola = 1
                if (self.color == 'white'):
                    crni.pop(crni.index(za_brisanje))
                else:
                    bijeli.pop(bijeli.index(za_brisanje))
            self.x = self.starix
            self.y = self.stariy + 75
            if self.color == "white":
                if king_checked(crni) != "None" or border_colision(self.x, self.y):
                    self.x = self.starix
                    self.y = self.stariy
                    if kontrola == 1:
                        crni.append(za_brisanje)
                    return False
            else:
                if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                    self.x = self.starix
                    self.y = self.stariy
                    if kontrola == 1:
                        bijeli.append(za_brisanje)
                    return False
            self.starix = self.x
            self.stariy = self.y
            self.castle = potez
            return True
        elif (self.starix - 77.5 <= self.x + 37.5 <= self.starix - 2.5) and (
                        self.stariy - 2.5 <= self.y + 37.5 <= self.stariy + 72.5):
            if (ally_colision(self, self.starix - 75, self.stariy) != 'None'):
                self.x = self.starix
                self.y = self.stariy
                return False
            if (enemy_colision(self, self.starix - 75, self.stariy) != 'None'):
                za_brisanje = enemy_colision(self, self.starix - 75, self.stariy)
                kontrola = 1
                if (self.color == 'white'):
                    crni.pop(crni.index(za_brisanje))
                else:
                    bijeli.pop(bijeli.index(za_brisanje))
            self.x = self.starix - 75
            self.y = self.stariy
            if self.color == "white":
                if king_checked(crni) != "None" or border_colision(self.x, self.y):
                    self.x = self.starix
                    self.y = self.stariy
                    if kontrola == 1:
                        crni.append(za_brisanje)
                    return False
            else:
                if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                    self.x = self.starix
                    self.y = self.stariy
                    if kontrola == 1:
                        bijeli.append(za_brisanje)
                    return False
            self.starix = self.x
            self.stariy = self.y
            self.castle = potez
            return True
        elif (self.starix + 72.5 <= self.x + 37.5 <= self.starix + 147.5) and (
                        self.stariy - 2.5 <= self.y + 37.5 <= self.stariy + 72.5):
            if (ally_colision(self, self.starix + 75, self.stariy) != 'None'):
                self.x = self.starix
                self.y = self.stariy
                return False
            if (enemy_colision(self, self.starix + 75, self.stariy) != 'None'):
                za_brisanje = enemy_colision(self, self.starix + 75, self.stariy)
                kontrola = 1
                if (self.color == 'white'):
                    crni.pop(crni.index(za_brisanje))
                else:
                    bijeli.pop(bijeli.index(za_brisanje))
            self.x = self.starix + 75
            self.y = self.stariy
            if self.color == "white":
                if king_checked(crni) != "None" or border_colision(self.x, self.y):
                    self.x = self.starix
                    self.y = self.stariy
                    if kontrola == 1:
                        crni.append(za_brisanje)
                    return False
            else:
                if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                    self.x = self.starix
                    self.y = self.stariy
                    if kontrola == 1:
                        bijeli.append(za_brisanje)
                    return False
            self.starix = self.x
            self.stariy = self.y
            self.castle = potez
            return True
        elif (self.stariy - 77.5 <= self.y + 37.5 <= self.stariy + 2.5) and (self.starix - 77.5 <= self.x + 37.5 <= self.starix - 2.5):
            if (ally_colision(self, self.starix - 75, self.stariy - 75) != 'None'):
                self.x = self.starix
                self.y = self.stariy
                return False
            if (enemy_colision(self, self.starix - 75, self.stariy - 75) != 'None'):
                za_brisanje = enemy_colision(self, self.starix - 75, self.stariy - 75)
                kontrola = 1
                if (self.color == 'white'):
                    crni.pop(crni.index(za_brisanje))
                else:
                    bijeli.pop(bijeli.index(za_brisanje))
            self.x = self.starix - 75
            self.y = self.stariy - 75
            if self.color == "white":
                if king_checked(crni) != "None" or border_colision(self.x, self.y):
                    self.x = self.starix
                    self.y = self.stariy
                    if kontrola == 1:
                        crni.append(za_brisanje)
                    return False
            else:
                if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                    self.x = self.starix
                    self.y = self.stariy
                    if kontrola == 1:
                        bijeli.append(za_brisanje)
                    return False
            self.starix = self.x
            self.stariy = self.y
            self.castle = potez
            return True
        elif (self.stariy - 77.5 <= self.y + 37.5 <= self.stariy + 2.5) and (self.starix + 72.5 <= self.x + 37.5 <= self.starix + 147.5):
            if (ally_colision(self, self.starix + 75, self.stariy - 75) != 'None'):
                self.x = self.starix
                self.y = self.stariy
                return False
            if (enemy_colision(self, self.starix + 75, self.stariy - 75) != 'None'):
                za_brisanje = enemy_colision(self, self.starix + 75, self.stariy - 75)
                kontrola = 1
                if (self.color == 'white'):
                    crni.pop(crni.index(za_brisanje))
                else:
                    bijeli.pop(bijeli.index(za_brisanje))
            self.x = self.starix + 75
            self.y = self.stariy - 75
            if self.color == "white":
                if king_checked(crni) != "None" or border_colision(self.x, self.y):
                    self.x = self.starix
                    self.y = self.stariy
                    if kontrola == 1:
                        crni.append(za_brisanje)
                    return False
            else:
                if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                    self.x = self.starix
                    self.y = self.stariy
                    if kontrola == 1:
                        bijeli.append(za_brisanje)
                    return False
            self.starix = self.x
            self.stariy = self.y
            self.castle = potez
            return True
        elif (self.stariy + 72.5 <= self.y + 37.5 <= self.stariy + 147.5) and (self.starix - 77.5 <= self.x + 37.5 <= self.starix - 2.5):
            if (ally_colision(self, self.starix - 75, self.stariy + 75) != 'None'):
                self.x = self.starix
                self.y = self.stariy
                return False
            if (enemy_colision(self, self.starix - 75, self.stariy + 75) != 'None'):
                za_brisanje = enemy_colision(self, self.starix - 75, self.stariy + 75)
                kontrola = 1
                if (self.color == 'white'):
                    crni.pop(crni.index(za_brisanje))
                else:
                    bijeli.pop(bijeli.index(za_brisanje))
            self.x = self.starix - 75
            self.y = self.stariy + 75
            if self.color == "white":
                if king_checked(crni) != "None" or border_colision(self.x, self.y):
                    self.x = self.starix
                    self.y = self.stariy
                    if kontrola == 1:
                        crni.append(za_brisanje)
                    return False
            else:
                if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                    self.x = self.starix
                    self.y = self.stariy
                    if kontrola == 1:
                        bijeli.append(za_brisanje)
                    return False
            self.starix = self.x
            self.stariy = self.y
            self.castle = potez
            return True
        elif (self.stariy + 72.5 <= self.y + 37.5 <= self.stariy + 147.5) and (self.starix + 72.5 <= self.x + 37.5 <= self.starix + 147.5):
            if (ally_colision(self, self.starix + 75, self.stariy + 75) != 'None'):
                self.x = self.starix
                self.y = self.stariy
                return False
            if (enemy_colision(self, self.starix + 75, self.stariy + 75) != 'None'):
                za_brisanje = enemy_colision(self, self.starix + 75, self.stariy + 75)
                kontrola = 1
                if (self.color == 'white'):
                    crni.pop(crni.index(za_brisanje))
                else:
                    bijeli.pop(bijeli.index(za_brisanje))
            self.x = self.starix + 75
            self.y = self.stariy + 75
            if self.color == "white":
                if king_checked(crni) != "None" or border_colision(self.x, self.y):
                    self.x = self.starix
                    self.y = self.stariy
                    if kontrola == 1:
                        crni.append(za_brisanje)
                    return False
            else:
                if king_checked(bijeli) != "None" or border_colision(self.x, self.y):
                    self.x = self.starix
                    self.y = self.stariy
                    if kontrola == 1:
                        bijeli.append(za_brisanje)
                    return False
            self.starix = self.x
            self.stariy = self.y
            self.castle = potez
            return True
        else:
            self.x = self.starix
            self.y = self.stariy
            return False
