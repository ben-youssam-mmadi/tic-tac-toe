nb1 = "1"
nb2 = "2"
nb3 = "3"
nb4 = "4"
nb5 = "5"
nb6 = "6"
nb7 = "7"
nb8 = "8"
nb9 = "9"
gagnant = ""
nb_choisi = ""
valide = 0
bleu = "\033[1;34mX\033[0;00m"
rouge = "\033[1;31mO\033[0;00m"

def print_case():
    print("")
    print(nb1,"|", nb2,"|", nb3)
    print("-- --- --")
    print(nb4,"|", nb5,"|", nb6)
    print("-- --- --")
    print(nb7,"|", nb8,"|", nb9)
    print("")

def res_gagnant():
    print("BRAVO !! Le joueur " + gagnant + " a gagné")
    print("")

def res_nul():
    print("\033[1;33mIl y'a match nul\033[0;0m")
    print("")
    

print_case()

while gagnant == "":

    while valide != 1:
            nb_choisi = input("\033[1;34m Joueur X \033[0;0m Choisissez un nombre ou vous placer : ")
            if nb_choisi == "1" and nb1 == "1":
                nb1 = bleu
                valide = 1
            elif nb_choisi == "2" and nb2 == "2":
                nb2 = bleu
                valide = 1
            elif nb_choisi == "3" and nb3 == "3":
                nb3 = bleu
                valide = 1
            elif nb_choisi == "4" and nb4 == "4":
                nb4 = bleu
                valide = 1
            elif nb_choisi == "5" and nb5 == "5":
                nb5 = bleu
                valide = 1
            elif nb_choisi == "6" and nb6 == "6":
                nb6 = bleu
                valide = 1
            elif nb_choisi == "7" and nb7 == "7":
                nb7 = bleu
                valide = 1
            elif nb_choisi == "8" and nb8 == "8":
                nb8 = bleu
                valide = 1
            elif nb_choisi == "9" and nb9 == "9":
                nb9 = bleu
                valide = 1
            else:
                print("\033[1;32m ERREUR \033[0;0m")
            print_case()

    if nb1 == bleu and nb2 == bleu and nb3 == bleu:
        gagnant = bleu
        break
    elif nb4 == bleu and nb5 == bleu and nb6 == bleu:
        gagnant = bleu
        break
    elif nb7 == bleu and nb8 == bleu and nb9 == bleu:
        gagnant = bleu
        break
    elif nb1 == bleu and nb4 == bleu and nb7 == bleu:
        gagnant = bleu
        break
    elif nb2 == bleu and nb5 == bleu and nb8 == bleu:
        gagnant = bleu
        break
    elif nb3 == bleu and nb6 == bleu and nb9 == bleu:
        gagnant = bleu
        break
    elif nb1 == bleu and nb5 == bleu and nb9 == bleu:
        gagnant = bleu
        break
    elif nb3 == bleu and nb5 == bleu and nb7 == bleu:
        gagnant = bleu
        break
    
    elif (nb1 != "1" and nb2 != "2" and nb3 != "3" and nb4 != "4" and nb5 != "5" and nb6 != "6" and nb7 != "7" and nb8 != "8" and nb9 != "9") and gagnant == "":
        break

    valide = 0
    nb_choisi = ""

    while valide != 1:
            nb_choisi = input("\033[1;31m Joueur O \033[0;00m Choisissez un nombre ou vous placer : ")
            if nb_choisi == "1" and nb1 == "1":
                nb1 = rouge
                valide = 1
            elif nb_choisi == "2" and nb2 == "2":
                nb2 = rouge
                valide = 1
            elif nb_choisi == "3" and nb3 == "3":
                nb3 = rouge
                valide = 1
            elif nb_choisi == "4" and nb4 == "4":
                nb4 = rouge
                valide = 1
            elif nb_choisi == "5" and nb5 == "5":
                nb5 = rouge
                valide = 1
            elif nb_choisi == "6" and nb6 == "6":
                nb6 = rouge
                valide = 1
            elif nb_choisi == "7" and nb7 == "7":
                nb7 = rouge
                valide = 1
            elif nb_choisi == "8" and nb8 == "8":
                nb8 = rouge
                valide = 1
            elif nb_choisi == "9" and nb9 == "9":
                nb9 = rouge
                valide = 1
            else:
                print("\033[1;32m ERREUR \033[0;0m")
            print_case()

    if nb1 == rouge and nb2 == rouge and nb3 == rouge:
        gagnant = rouge
        break
    elif nb4 == rouge and nb5 == rouge and nb6 == rouge:
        gagnant = rouge
        break
    elif nb7 == rouge and nb8 == rouge and nb9 == rouge:
        gagnant = rouge
        break
    elif nb1 == rouge and nb4 == rouge and nb7 == rouge:
        gagnant = rouge
        break
    elif nb2 == rouge and nb5 == rouge and nb8 == rouge:
        gagnant = rouge
        break
    elif nb3 == rouge and nb6 == rouge and nb9 == rouge:
        gagnant = rouge
        break
    elif nb1 == rouge and nb5 == rouge and nb9 == rouge:
        gagnant = rouge
        break
    elif nb3 == rouge and nb5 == rouge and nb7 == rouge:
        gagnant = rouge
        break    

    if (nb1 != "1" and nb2 != "2" and nb3 != "3" and nb4 != "4" and nb5 != "5" and nb6 != "6" and nb7 != "7" and nb8 != "8" and nb9 != "9") and gagnant == "":
        break

    valide = 0
    nb_choisi = ""

if gagnant == "":
    res_nul()
else:
    res_gagnant()