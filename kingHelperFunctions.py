
from helperFunctions import ally_colision, border_colision, enemy_colision
from constants import bijeli, crni


def king_checked(pieces):
    for objekat in pieces:
        if objekat.color == "white":
            if objekat.obj == "Pawn":
                if enemy_colision(objekat, objekat.x + 75, objekat.y - 75) != "None":
                    if enemy_colision(objekat, objekat.x + 75, objekat.y - 75).obj == "King":
                        return objekat
                if enemy_colision(objekat, objekat.x - 75, objekat.y - 75) != "None":
                    if enemy_colision(objekat, objekat.x - 75, objekat.y - 75).obj == "King":
                        return objekat
        else:
            if objekat.obj == "Pawn":
                if enemy_colision(objekat, objekat.x + 75, objekat.y + 75) != "None":
                    if enemy_colision(objekat, objekat.x + 75, objekat.y + 75).obj == "King":
                        return objekat
                if enemy_colision(objekat, objekat.x - 75, objekat.y + 75) != "None":
                    if enemy_colision(objekat, objekat.x - 75, objekat.y + 75).obj == "King":
                        return objekat

        if objekat.obj == "Knight":
            if enemy_colision(objekat, objekat.x + 75, objekat.y + 150) != "None":
                if enemy_colision(objekat, objekat.x + 75, objekat.y + 150).obj == "King":
                    return objekat

            if enemy_colision(objekat, objekat.x - 75, objekat.y + 150) != "None":
                if enemy_colision(objekat, objekat.x - 75, objekat.y + 150).obj == "King":
                    return objekat

            if enemy_colision(objekat, objekat.x + 75, objekat.y - 150) != "None":
                if enemy_colision(objekat, objekat.x + 75, objekat.y - 150).obj == "King":
                    return objekat

            if enemy_colision(objekat, objekat.x - 75, objekat.y - 150) != "None":
                if enemy_colision(objekat, objekat.x - 75, objekat.y - 150).obj == "King":
                    return objekat

            if enemy_colision(objekat, objekat.x + 150, objekat.y + 75) != "None":
                if enemy_colision(objekat, objekat.x + 150, objekat.y + 75).obj == "King":
                    return objekat

            if enemy_colision(objekat, objekat.x + 150, objekat.y - 75) != "None":
                if enemy_colision(objekat, objekat.x + 150, objekat.y - 75).obj == "King":
                    return objekat

            if enemy_colision(objekat, objekat.x - 150, objekat.y + 75) != "None":
                if enemy_colision(objekat, objekat.x - 150, objekat.y + 75).obj == "King":
                    return objekat

            if enemy_colision(objekat, objekat.x - 150, objekat.y - 75) != "None":
                if enemy_colision(objekat, objekat.x - 150, objekat.y - 75).obj == "King":
                    return objekat

        if objekat.obj == "Bishop":
            novix = objekat.x
            noviy = objekat.y
            prvi = True
            drugi = True
            treci = True
            cetvrti = True
            for i in range(7):
                if prvi == True:
                    if enemy_colision(objekat, novix + (i * 75) + 75, noviy + (i * 75) + 75) != "None":
                        if enemy_colision(objekat, novix + (i * 75) + 75, noviy + (i * 75) + 75).obj == "King":
                            return objekat
                        else:
                            prvi = False
                if ally_colision(objekat, novix + (i * 75) + 75, noviy + (i * 75) + 75) != "None":
                    prvi = False

                if drugi == True:
                    if enemy_colision(objekat, novix + (i * 75) + 75, noviy - (i * 75) - 75) != "None":
                        if enemy_colision(objekat, novix + (i * 75) + 75, noviy - (i * 75) - 75).obj == "King":
                            return objekat
                        else:
                            drugi = False
                    if ally_colision(objekat, novix + (i * 75) + 75, noviy - (i * 75) - 75) != "None":
                        drugi = False

                if treci == True:
                    if enemy_colision(objekat, novix - (i * 75) - 75, noviy + (i * 75) + 75) != "None":
                        if enemy_colision(objekat, novix - (i * 75) - 75, noviy + (i * 75) + 75).obj == "King":
                            return objekat
                        else:
                            treci = False
                    if ally_colision(objekat, novix - (i * 75) - 75, noviy + (i * 75) + 75) != "None":
                        treci = False

                if cetvrti == True:
                    if enemy_colision(objekat, novix - (i * 75) - 75, noviy - (i * 75) - 75) != "None":
                        if enemy_colision(objekat, novix - (i * 75) - 75, noviy - (i * 75) - 75).obj == "King":
                            return objekat
                        else:
                            cetvrti = False
                    if ally_colision(objekat, novix - (i * 75) - 75, noviy - (i * 75) - 75) != "None":
                        cetvrti = False

        if objekat.obj == "Rook":
            novix = objekat.x
            noviy = objekat.y
            prvi = True
            drugi = True
            treci = True
            cetvrti = True
            for i in range(7):
                if prvi == True:
                    if enemy_colision(objekat, novix + (i * 75) + 75, noviy) != "None":
                        if enemy_colision(objekat, novix + (i * 75) + 75, noviy).obj == "King":
                            return objekat
                        else:
                            prvi = False
                if ally_colision(objekat, novix + (i * 75) + 75, noviy) != "None":
                    prvi = False

                if drugi == True:
                    if enemy_colision(objekat, novix, noviy - (i * 75) - 75) != "None":
                        if enemy_colision(objekat, novix, noviy - (i * 75) - 75).obj == "King":
                            return objekat
                        else:
                            drugi = False
                    if ally_colision(objekat, novix, noviy - (i * 75) - 75) != "None":
                        drugi = False

                if treci == True:
                    if enemy_colision(objekat, novix, noviy + (i * 75) + 75) != "None":
                        if enemy_colision(objekat, novix, noviy + (i * 75) + 75).obj == "King":
                            return objekat
                        else:
                            treci = False
                    if ally_colision(objekat, novix, noviy + (i * 75) + 75) != "None":
                        treci = False

                if cetvrti == True:
                    if enemy_colision(objekat, novix - (i * 75) - 75, noviy) != "None":
                        if enemy_colision(objekat, novix - (i * 75) - 75, noviy).obj == "King":
                            return objekat
                        else:
                            cetvrti = False
                    if ally_colision(objekat, novix - (i * 75) - 75, noviy) != "None":
                        cetvrti = False

        if objekat.obj == "Queen":
            novix = objekat.x
            noviy = objekat.y
            prvi = True
            drugi = True
            treci = True
            cetvrti = True
            peti = True
            sesti = True
            sedmi = True
            osmi = True
            for i in range(7):

                if prvi == True:
                    if enemy_colision(objekat, novix + (i * 75) + 75, noviy + (i * 75) + 75) != "None":
                        if enemy_colision(objekat, novix + (i * 75) + 75, noviy + (i * 75) + 75).obj == "King":
                            return objekat
                        else:
                            prvi = False
                if ally_colision(objekat, novix + (i * 75) + 75, noviy + (i * 75) + 75) != "None":
                    prvi = False

                if drugi == True:
                    if enemy_colision(objekat, novix + (i * 75) + 75, noviy - (i * 75) - 75) != "None":
                        if enemy_colision(objekat, novix + (i * 75) + 75, noviy - (i * 75) - 75).obj == "King":
                            return objekat
                        else:
                            drugi = False
                    if ally_colision(objekat, novix + (i * 75) + 75, noviy - (i * 75) - 75) != "None":
                        drugi = False

                if treci == True:
                    if enemy_colision(objekat, novix - (i * 75) - 75, noviy + (i * 75) + 75) != "None":
                        if enemy_colision(objekat, novix - (i * 75) - 75, noviy + (i * 75) + 75).obj == "King":
                            return objekat
                        else:
                            treci = False
                    if ally_colision(objekat, novix - (i * 75) - 75, noviy + (i * 75) + 75) != "None":
                        treci = False

                if cetvrti == True:
                    if enemy_colision(objekat, novix - (i * 75) - 75, noviy - (i * 75) - 75) != "None":
                        if enemy_colision(objekat, novix - (i * 75) - 75, noviy - (i * 75) - 75).obj == "King":
                            return objekat
                        else:
                            cetvrti = False
                    if ally_colision(objekat, novix - (i * 75) - 75, noviy - (i * 75) - 75) != "None":
                        cetvrti = False

                if peti == True:
                    if enemy_colision(objekat, novix + (i * 75) + 75, noviy) != "None":
                        if enemy_colision(objekat, novix + (i * 75) + 75, noviy).obj == "King":
                            return objekat
                        else:
                            peti = False
                if ally_colision(objekat, novix + (i * 75) + 75, noviy) != "None":
                    peti = False

                if sesti == True:
                    if enemy_colision(objekat, novix, noviy - (i * 75) - 75) != "None":
                        if enemy_colision(objekat, novix, noviy - (i * 75) - 75).obj == "King":
                            return objekat
                        else:
                            sesti = False
                    if ally_colision(objekat, novix, noviy - (i * 75) - 75) != "None":
                        sesti = False

                if sedmi == True:
                    if enemy_colision(objekat, novix, noviy + (i * 75) + 75) != "None":
                        if enemy_colision(objekat, novix, noviy + (i * 75) + 75).obj == "King":
                            return objekat
                        else:
                            sedmi = False
                    if ally_colision(objekat, novix, noviy + (i * 75) + 75) != "None":
                        sedmi = False

                if osmi == True:
                    if enemy_colision(objekat, novix - (i * 75) - 75, noviy) != "None":
                        if enemy_colision(objekat, novix - (i * 75) - 75, noviy).obj == "King":
                            return objekat
                        else:
                            osmi = False
                    if ally_colision(objekat, novix - (i * 75) - 75, noviy) != "None":
                        osmi = False

        if objekat.obj == "King":
            if enemy_colision(objekat, objekat.x + 75, objekat.y) != "None":
                if enemy_colision(objekat, objekat.x + 75, objekat.y).obj == "King":
                    return objekat

            if enemy_colision(objekat, objekat.x - 75, objekat.y) != "None":
                if enemy_colision(objekat, objekat.x - 75, objekat.y).obj == "King":
                    return objekat

            if enemy_colision(objekat, objekat.x, objekat.y + 75) != "None":
                if enemy_colision(objekat, objekat.x, objekat.y + 75).obj == "King":
                    return objekat

            if enemy_colision(objekat, objekat.x, objekat.y - 75) != "None":
                if enemy_colision(objekat, objekat.x, objekat.y - 75).obj == "King":
                    return objekat

            if enemy_colision(objekat, objekat.x + 75, objekat.y - 75) != "None":
                if enemy_colision(objekat, objekat.x + 75, objekat.y - 75).obj == "King":
                    return objekat

            if enemy_colision(objekat, objekat.x - 75, objekat.y - 75) != "None":
                if enemy_colision(objekat, objekat.x - 75, objekat.y - 75).obj == "King":
                    return objekat

            if enemy_colision(objekat, objekat.x - 75, objekat.y + 75) != "None":
                if enemy_colision(objekat, objekat.x - 75, objekat.y + 75).obj == "King":
                    return objekat

            if enemy_colision(objekat, objekat.x + 75, objekat.y + 75) != "None":
                if enemy_colision(objekat, objekat.x + 75, objekat.y + 75).obj == "King":
                    return objekat

    return "None"

def king_checkmated(pieces, potez):
    for objekat in pieces:
        za_brisanje = "None"
        if objekat.obj == "Pawn":
            if objekat.color == "white":
                if (ally_colision(objekat, objekat.x, objekat.y - 75) != "None" or enemy_colision(objekat, objekat.x, objekat.y - 75) != "None" or border_colision(objekat.x,
                                                                                                   objekat.y - 75)):
                    pass
                else:
                    objekat.y -= 75
                    if king_checked(crni) == "None":
                        objekat.y = objekat.stariy
                        return False
                objekat.y = objekat.stariy

                if(objekat.stariy == 452.5):
                    if (ally_colision(objekat, objekat.x, objekat.y - 150) != "None" or enemy_colision(objekat, objekat.x, objekat.y - 150) != "None" or border_colision(objekat.x, objekat.y - 150)):
                        pass
                    else:
                        objekat.y -= 150
                        if king_checked(crni) == "None":
                            objekat.y = objekat.stariy
                            return False
                    objekat.y = objekat.stariy

                if (ally_colision(objekat, objekat.x - 75, objekat.y - 75) != "None" or border_colision(objekat.x - 75, objekat.y - 75)):
                    pass
                else:
                    if(enemy_colision(objekat, objekat.x - 75, objekat.y - 75) != "None"):
                        objekat.x -= 75
                        objekat.y -= 75
                        za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                        crni.pop(crni.index(za_brisanje))
                        if king_checked(crni) == "None":
                            objekat.y = objekat.stariy
                            objekat.x = objekat.starix
                            crni.append(za_brisanje)
                            return False
                        crni.append(za_brisanje)
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy


                if (ally_colision(objekat, objekat.x + 75, objekat.y - 75) != "None" or border_colision(objekat.x + 75, objekat.y - 75)):
                    pass
                else:
                    if(enemy_colision(objekat, objekat.x + 75, objekat.y - 75) != "None"):
                        objekat.x += 75
                        objekat.y -= 75
                        za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                        crni.pop(crni.index(za_brisanje))
                        if king_checked(crni) == "None":
                            objekat.y = objekat.stariy
                            objekat.x = objekat.starix
                            crni.append(za_brisanje)
                            return False
                        crni.append(za_brisanje)
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy


                if (ally_colision(objekat, objekat.x - 75, objekat.y) != "None" or border_colision(objekat.x - 75, objekat.y - 75)):
                    pass
                else:
                    if(enemy_colision(objekat, objekat.x - 75, objekat.y) != "None"):
                        if (enemy_colision(objekat, objekat.x - 75, objekat.y)).obj == "Pawn":
                            if(enemy_colision(objekat, objekat.x - 75, objekat.y).enp == potez - 1):
                                za_brisanje = enemy_colision(objekat, objekat.x - 75, objekat.y)
                                objekat.x -= 75
                                objekat.y -= 75
                                crni.pop(crni.index(za_brisanje))
                                if king_checked(crni) == "None":
                                    objekat.y = objekat.stariy
                                    objekat.x = objekat.starix
                                    crni.append(za_brisanje)
                                    return False
                                crni.append(za_brisanje)
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy

                if (ally_colision(objekat, objekat.x + 75, objekat.y) != "None" or border_colision(objekat.x + 75, objekat.y - 75)):
                    pass
                else:
                    if(enemy_colision(objekat, objekat.x + 75, objekat.y) != "None"):
                        if(enemy_colision(objekat, objekat.x + 75, objekat.y)).obj == "Pawn":
                            if(enemy_colision(objekat, objekat.x + 75, objekat.y).enp == potez - 1):
                                za_brisanje = enemy_colision(objekat, objekat.x + 75, objekat.y)
                                objekat.x += 75
                                objekat.y -= 75
                                crni.pop(crni.index(za_brisanje))
                                if king_checked(crni) == "None":
                                    objekat.y = objekat.stariy
                                    objekat.x = objekat.starix
                                    crni.append(za_brisanje)
                                    return False
                                crni.append(za_brisanje)
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy




            else:

                if (ally_colision(objekat, objekat.x, objekat.y + 75) != "None" or enemy_colision(objekat, objekat.x, objekat.y + 75) != "None" or border_colision(objekat.x,
                                                                                                   objekat.y + 75)):
                    pass
                else:
                    objekat.y += 75
                    if king_checked(bijeli) == "None":
                        objekat.y = objekat.stariy
                        return False
                    objekat.y = objekat.stariy


                if (objekat.stariy == 77.5):
                    if (ally_colision(objekat, objekat.x, objekat.y + 150) != "None" or enemy_colision(objekat,
                                                                                                       objekat.x,
                                                                                                       objekat.y + 150) != "None" or border_colision(
                            objekat.x, objekat.y + 150)):
                        pass
                    else:
                        objekat.y += 150
                        if king_checked(bijeli) == "None":
                            objekat.y = objekat.stariy
                            return False
                    objekat.y = objekat.stariy

                if (ally_colision(objekat, objekat.x - 75, objekat.y + 75) != "None" or border_colision(objekat.x - 75, objekat.y + 75)):
                    pass
                else:
                    if(enemy_colision(objekat, objekat.x - 75, objekat.y + 75) != "None"):
                        objekat.x -= 75
                        objekat.y += 75
                        za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                        bijeli.pop(bijeli.index(za_brisanje))
                        if king_checked(bijeli) == "None":
                            objekat.y = objekat.stariy
                            objekat.x = objekat.starix
                            bijeli.append(za_brisanje)
                            return False
                        bijeli.append(za_brisanje)
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy


                if (ally_colision(objekat, objekat.x + 75, objekat.y + 75) != "None" or border_colision(objekat.x + 75, objekat.y + 75)):
                    pass
                else:
                    if(enemy_colision(objekat, objekat.x + 75, objekat.y + 75) != "None"):
                        objekat.x += 75
                        objekat.y += 75
                        za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                        bijeli.pop(bijeli.index(za_brisanje))
                        if king_checked(bijeli) == "None":
                            objekat.y = objekat.stariy
                            objekat.x = objekat.starix
                            bijeli.append(za_brisanje)
                            return False
                        bijeli.append(za_brisanje)
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy



                if (ally_colision(objekat, objekat.x - 75, objekat.y) != "None" or border_colision(objekat.x - 75, objekat.y + 75)):
                    pass
                else:
                    if(enemy_colision(objekat, objekat.x - 75, objekat.y) != "None"):
                        if (enemy_colision(objekat, objekat.x - 75, objekat.y)).obj == "Pawn":
                            if(enemy_colision(objekat, objekat.x - 75, objekat.y).enp == potez - 1):
                                za_brisanje = enemy_colision(objekat, objekat.x - 75, objekat.y)
                                objekat.x -= 75
                                objekat.y += 75
                                bijeli.pop(bijeli.index(za_brisanje))
                                if king_checked(bijeli) == "None":
                                    objekat.y = objekat.stariy
                                    objekat.x = objekat.starix
                                    bijeli.append(za_brisanje)
                                    return False
                                bijeli.append(za_brisanje)
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy

                if (ally_colision(objekat, objekat.x + 75, objekat.y) != "None" or border_colision(objekat.x + 75, objekat.y + 75)):
                    pass
                else:
                    if(enemy_colision(objekat, objekat.x + 75, objekat.y) != "None"):
                        if(enemy_colision(objekat, objekat.x + 75, objekat.y).enp == potez + 1):
                            if (enemy_colision(objekat, objekat.x + 75, objekat.y)).obj == "Pawn":
                                za_brisanje = enemy_colision(objekat, objekat.x + 75, objekat.y)
                                objekat.x += 75
                                objekat.y += 75
                                bijeli.pop(bijeli.index(za_brisanje))
                                if king_checked(bijeli) == "None":
                                    objekat.y = objekat.stariy
                                    objekat.x = objekat.starix
                                    bijeli.append(za_brisanje)
                                    return False
                                bijeli.append(za_brisanje)
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy

        if objekat.obj == "Knight":
            objekat.x -= 75
            objekat.y += 150
            if(enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
            if objekat.color == "white":
                if(za_brisanje != "None"):
                    crni.pop(crni.index(za_brisanje))
                if king_checked(crni) == "None":
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)
                    return False
                objekat.x = objekat.starix
                objekat.y = objekat.stariy
                if (za_brisanje != "None"):
                    crni.append(za_brisanje)
            else:
                if (za_brisanje != "None"):
                    bijeli.pop(bijeli.index(za_brisanje))
                if king_checked(bijeli) == "None":
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)
                    return False
                objekat.x = objekat.starix
                objekat.y = objekat.stariy
                if (za_brisanje != "None"):
                    bijeli.append(za_brisanje)

            objekat.x -= 75
            objekat.y -= 150
            if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
            if objekat.color == "white":
                if (za_brisanje != "None"):
                    crni.pop(crni.index(za_brisanje))
                if king_checked(crni) == "None":
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)
                    return False
                objekat.x = objekat.starix
                objekat.y = objekat.stariy
                if (za_brisanje != "None"):
                    crni.append(za_brisanje)
            else:
                if (za_brisanje != "None"):
                    bijeli.pop(bijeli.index(za_brisanje))
                if king_checked(bijeli) == "None":
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)
                    return False
            objekat.x = objekat.starix
            objekat.y = objekat.stariy
            if (za_brisanje != "None"):
                bijeli.append(za_brisanje)

            objekat.x += 75
            objekat.y += 150
            if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
            if objekat.color == "white":
                if (za_brisanje != "None"):
                    crni.pop(crni.index(za_brisanje))
                if king_checked(crni) == "None":
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)
                    return False
                objekat.x = objekat.starix
                objekat.y = objekat.stariy
                if(za_brisanje != "None"):
                    crni.append(za_brisanje)
            else:
                if(za_brisanje != "None"):
                    bijeli.pop(bijeli.index(za_brisanje))
                if king_checked(bijeli) == "None":
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)
                    return False
            objekat.x = objekat.starix
            objekat.y = objekat.stariy
            if(za_brisanje != "None"):
                bijeli.append(za_brisanje)

            objekat.x += 75
            objekat.y -= 150
            if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
            if objekat.color == "white":
                if(za_brisanje != "None"):
                    crni.pop(crni.index(za_brisanje))
                if king_checked(crni) == "None":
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)
                    return False
                objekat.x = objekat.starix
                objekat.y = objekat.stariy
                if(za_brisanje != "None"):
                    crni.append(za_brisanje)
            else:
                if(za_brisanje != "None"):
                    bijeli.pop(bijeli.index(za_brisanje))
                if king_checked(bijeli) == "None":
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)
                    return False
            objekat.x = objekat.starix
            objekat.y = objekat.stariy
            if(za_brisanje != "None"):
                bijeli.append(za_brisanje)

            objekat.x -= 150
            objekat.y += 75
            if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
            if objekat.color == "white":
                if(za_brisanje != "None"):
                    crni.pop(crni.index(za_brisanje))
                if king_checked(crni) == "None":
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)
                    return False
                objekat.x = objekat.starix
                objekat.y = objekat.stariy
                if(za_brisanje != "None"):
                    crni.append(za_brisanje)
            else:
                if(za_brisanje != "None"):
                    bijeli.pop(bijeli.index(za_brisanje))
                if king_checked(bijeli) == "None":
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)
                    return False
            objekat.x = objekat.starix
            objekat.y = objekat.stariy
            if(za_brisanje != "None"):
                bijeli.append(za_brisanje)

            objekat.x -= 150
            objekat.y -= 75
            if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
            if objekat.color == "white":
                if(za_brisanje != "None"):
                    crni.pop(crni.index(za_brisanje))
                if king_checked(crni) == "None":
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)
                    return False
                objekat.x = objekat.starix
                objekat.y = objekat.stariy
                if(za_brisanje != "None"):
                    crni.append(za_brisanje)
            else:
                if(za_brisanje != "None"):
                    bijeli.pop(bijeli.index(za_brisanje))
                if king_checked(bijeli) == "None":
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)
                    return False
            objekat.x = objekat.starix
            objekat.y = objekat.stariy
            if(za_brisanje != "None"):
                bijeli.append(za_brisanje)

            objekat.x += 150
            objekat.y += 75
            if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
            if objekat.color == "white":
                if(za_brisanje != "None"):
                    crni.pop(crni.index(za_brisanje))
                if king_checked(crni) == "None":
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)
                    return False
                objekat.x = objekat.starix
                objekat.y = objekat.stariy
                if(za_brisanje != "None"):
                    crni.append(za_brisanje)
            else:
                if(za_brisanje != "None"):
                    bijeli.pop(bijeli.index(za_brisanje))
                if king_checked(bijeli) == "None":
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)
                    return False
            objekat.x = objekat.starix
            objekat.y = objekat.stariy
            if(za_brisanje != "None"):
                bijeli.append(za_brisanje)

            objekat.x += 150
            objekat.y -= 75
            if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
            if objekat.color == "white":
                if(za_brisanje != "None"):
                    crni.pop(crni.index(za_brisanje))
                if king_checked(crni) == "None":
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)
                    return False
                objekat.x = objekat.starix
                objekat.y = objekat.stariy
                if(za_brisanje != "None"):
                    crni.append(za_brisanje)
            else:
                if(za_brisanje != "None"):
                    bijeli.pop(bijeli.index(za_brisanje))
                if king_checked(bijeli) == "None":
                    objekat.x = objekat.starix
                    objekat.y = objekat.stariy
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)
                    return False
            objekat.x = objekat.starix
            objekat.y = objekat.stariy
            if(za_brisanje != "None"):
                bijeli.append(za_brisanje)
        if objekat.obj == "Bishop":
            kraj = 0
            za_brisanje = "None"
            for i in range(7):
                if(kraj == 1):
                    break
                objekat.x = objekat.starix + (i * 75)
                objekat.y = objekat.stariy + (i * 75)
                if (ally_colision(objekat, objekat.x + 75, objekat.y + 75) != "None"):
                    kraj = 1
                    continue
                objekat.x += 75
                objekat.y += 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)  #Ovdje si
                    kraj = 1
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy

            kraj = 0
            za_brisanje = "None"
            for i in range(7):
                if (kraj == 1):
                    break
                objekat.x = objekat.starix - (i * 75)
                objekat.y = objekat.stariy + (i * 75)
                if (ally_colision(objekat, objekat.x - 75, objekat.y + 75) != "None"):
                    kraj = 1
                    continue
                objekat.x -= 75
                objekat.y += 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                    kraj = 1
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy

            kraj = 0
            za_brisanje = "None"
            for i in range(7):
                if (kraj == 1):
                    break
                objekat.x = objekat.starix + (i * 75)
                objekat.y = objekat.stariy - (i * 75)
                if (ally_colision(objekat, objekat.x + 75, objekat.y - 75) != "None"):
                    kraj = 1
                    continue
                objekat.x += 75
                objekat.y -= 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                    kraj = 1
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy

            kraj = 0
            za_brisanje = "None"
            for i in range(7):
                if (kraj == 1):
                    break
                objekat.x = objekat.starix - (i * 75)
                objekat.y = objekat.stariy - (i * 75)
                if (ally_colision(objekat, objekat.x - 75, objekat.y - 75) != "None"):
                    kraj = 1
                    continue
                objekat.x -= 75
                objekat.y -= 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                    kraj = 1
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy
        if objekat.obj == "Rook":
            kraj = 0
            za_brisanje = "None"
            for i in range(7):
                if (kraj == 1):
                    break
                objekat.x = objekat.starix + (i * 75)
                if (ally_colision(objekat, objekat.x + 75, objekat.y) != "None"):
                    kraj = 1
                    continue
                objekat.x += 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)  # Ovdje si
                    kraj = 1
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)
            objekat.x = objekat.starix
            objekat.y = objekat.stariy

            kraj = 0
            za_brisanje = "None"
            for i in range(7):
                if (kraj == 1):
                    break
                objekat.x = objekat.starix - (i * 75)
                if (ally_colision(objekat, objekat.x - 75, objekat.y) != "None"):
                    kraj = 1
                    continue
                objekat.x -= 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                    kraj = 1
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy

            kraj = 0
            za_brisanje = "None"
            for i in range(7):
                if (kraj == 1):
                    break
                objekat.y = objekat.stariy + (i * 75)
                if (ally_colision(objekat, objekat.x, objekat.y + 75) != "None"):
                    kraj = 1
                    continue
                objekat.y += 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                    kraj = 1
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy

            kraj = 0
            za_brisanje = "None"
            for i in range(7):
                if (kraj == 1):
                    break
                objekat.y = objekat.stariy - (i * 75)
                if (ally_colision(objekat, objekat.x, objekat.y - 75) != "None"):
                    kraj = 1
                    continue
                objekat.y -= 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                    kraj = 1
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy
        if objekat.obj == "Queen":
            kraj = 0
            za_brisanje = "None"
            for i in range(7):
                if (kraj == 1):
                    break
                objekat.x = objekat.starix + (i * 75)
                objekat.y = objekat.stariy + (i * 75)
                if (ally_colision(objekat, objekat.x + 75, objekat.y + 75) != "None"):
                    kraj = 1
                    continue
                objekat.x += 75
                objekat.y += 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)  # Ovdje si
                    kraj = 1
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy

            kraj = 0
            za_brisanje = "None"
            for i in range(7):
                if (kraj == 1):
                    break
                objekat.x = objekat.starix - (i * 75)
                objekat.y = objekat.stariy + (i * 75)
                if (ally_colision(objekat, objekat.x - 75, objekat.y + 75) != "None"):
                    kraj = 1
                    continue
                objekat.x -= 75
                objekat.y += 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                    kraj = 1
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy

            kraj = 0
            za_brisanje = "None"
            for i in range(7):
                if (kraj == 1):
                    break
                objekat.x = objekat.starix + (i * 75)
                objekat.y = objekat.stariy - (i * 75)
                if (ally_colision(objekat, objekat.x + 75, objekat.y - 75) != "None"):
                    kraj = 1
                    continue
                objekat.x += 75
                objekat.y -= 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                    kraj = 1
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy

            kraj = 0
            za_brisanje = "None"
            for i in range(7):
                if (kraj == 1):
                    break
                objekat.x = objekat.starix - (i * 75)
                objekat.y = objekat.stariy - (i * 75)
                if (ally_colision(objekat, objekat.x - 75, objekat.y - 75) != "None"):
                    kraj = 1
                    continue
                objekat.x -= 75
                objekat.y -= 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                    kraj = 1
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy

            kraj = 0
            za_brisanje = "None"
            for i in range(7):
                if (kraj == 1):
                    break
                objekat.x = objekat.starix + (i * 75)
                if (ally_colision(objekat, objekat.x + 75, objekat.y) != "None"):
                    kraj = 1
                    continue
                objekat.x += 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)  # Ovdje si
                    kraj = 1
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)
            objekat.x = objekat.starix
            objekat.y = objekat.stariy

            kraj = 0
            za_brisanje = "None"
            for i in range(7):
                if (kraj == 1):
                    break
                objekat.x = objekat.starix - (i * 75)
                if (ally_colision(objekat, objekat.x - 75, objekat.y) != "None"):
                    kraj = 1
                    continue
                objekat.x -= 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                    kraj = 1
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy

            kraj = 0
            za_brisanje = "None"
            for i in range(7):
                if (kraj == 1):
                    break
                objekat.y = objekat.stariy + (i * 75)
                if (ally_colision(objekat, objekat.x, objekat.y + 75) != "None"):
                    kraj = 1
                    continue
                objekat.y += 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                    kraj = 1
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy

            kraj = 0
            za_brisanje = "None"
            for i in range(7):
                if (kraj == 1):
                    break
                objekat.y = objekat.stariy - (i * 75)
                if (ally_colision(objekat, objekat.x, objekat.y - 75) != "None"):
                    kraj = 1
                    continue
                objekat.y -= 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                    kraj = 1
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy
        if objekat.obj == "King":
            if (ally_colision(objekat, objekat.x + 75, objekat.y) != "None" or border_colision(objekat.x + 75, objekat.y)):
                pass
            else:
                objekat.x += 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy

            if (ally_colision(objekat, objekat.x - 75, objekat.y) != "None" or border_colision(objekat.x - 75, objekat.y)):
                pass
            else:
                objekat.x -= 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy

            if (ally_colision(objekat, objekat.x, objekat.y + 75) != "None" or border_colision(objekat.x, objekat.y + 75)):
                pass
            else:
                objekat.y += 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy

            if (ally_colision(objekat, objekat.x, objekat.y - 75) != "None" or border_colision(objekat.x, objekat.y - 75)):
                pass
            else:
                objekat.y -= 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy

            if (ally_colision(objekat, objekat.x + 75, objekat.y + 75) != "None" or border_colision(objekat.x + 75, objekat.y + 75)):
                pass
            else:
                objekat.x += 75
                objekat.y += 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy

            if (ally_colision(objekat, objekat.x + 75, objekat.y - 75) != "None" or border_colision(objekat.x + 75, objekat.y - 75)):
                pass
            else:
                objekat.x += 75
                objekat.y -= 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy

            if (ally_colision(objekat, objekat.x - 75, objekat.y + 75) != "None" or border_colision(objekat.x - 75, objekat.y + 75)):
                pass
            else:
                objekat.x -= 75
                objekat.y += 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy

            if (ally_colision(objekat, objekat.x - 75, objekat.y - 75) != "None" or border_colision(objekat.x - 75, objekat.y - 75)):
                pass
            else:
                objekat.x -= 75
                objekat.y -= 75
                if (enemy_colision(objekat, objekat.x, objekat.y) != "None"):
                    za_brisanje = enemy_colision(objekat, objekat.x, objekat.y)
                if objekat.color == "white":
                    if (za_brisanje != "None"):
                        crni.pop(crni.index(za_brisanje))
                    if king_checked(crni) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            crni.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        crni.append(za_brisanje)

                else:
                    if (za_brisanje != "None"):
                        bijeli.pop(bijeli.index(za_brisanje))
                    if king_checked(bijeli) == "None":
                        objekat.x = objekat.starix
                        objekat.y = objekat.stariy
                        if (za_brisanje != "None"):
                            bijeli.append(za_brisanje)
                        return False
                    if (za_brisanje != "None"):
                        bijeli.append(za_brisanje)

            objekat.x = objekat.starix
            objekat.y = objekat.stariy

    return True
