import random

VIE_MAX = 100
POTION_SOIN = 35
DEGATS_MIN = 10
DEGATS_MAX = 25
CHANCE_CRITIQUE = 20


def choisir_action_ennemi(vie_ennemi, potions_ennemi, vie_joueur):
    """Choisit une action selon les PV restants et les potions disponibles."""
    soin_possible = min(POTION_SOIN, VIE_MAX - vie_ennemi)

    # En grand danger, l'ennemi se soigne avant de penser à achever le joueur.
    if potions_ennemi > 0 and vie_ennemi <= 25 and soin_possible >= 15:
        return "potion"

    # Il garde ses potions tant qu'il peut encore attaquer un joueur presque vaincu.
    if vie_joueur <= 20:
        return "attaque"

    # Il se soigne quand le gain est important, mais conserve une potion s'il
    # est seulement modérément blessé.
    if potions_ennemi > 0 and vie_ennemi <= 40 and soin_possible >= 20:
        return "potion"

    # À santé moyenne, il utilise parfois une potion s'il en a encore plusieurs.
    if potions_ennemi > 1 and vie_ennemi <= 60 and soin_possible >= 25:
        chance_de_boire = (60 - vie_ennemi) * 3
        if random.randint(1, 100) <= chance_de_boire:
            return "potion"

    return "attaque"


def demander_action_joueur():
    print("\nQue fais-tu ?")
    print("1 - Attaquer")
    print("2 - Boire une potion")
    print("3 - Se défendre (réduit les dégâts du prochain coup)")
    return input("Ton choix : ").strip()


def tour_ennemi(vie_joueur, vie_ennemi, potions_ennemi, joueur_se_defend):
    """Joue le tour de l'ennemi et renvoie les états mis à jour."""
    action = choisir_action_ennemi(vie_ennemi, potions_ennemi, vie_joueur)

    if action == "potion":
        soin = min(POTION_SOIN, VIE_MAX - vie_ennemi)
        vie_ennemi += soin
        potions_ennemi -= 1
        print(
            f"L'ennemi boit une potion et récupère {soin} PV "
            f"({vie_ennemi} PV, {potions_ennemi} potion(s) restante(s))."
        )
    else:
        degats = random.randint(DEGATS_MIN, DEGATS_MAX)
        if random.randint(1, 100) <= CHANCE_CRITIQUE:
            degats = int(degats * 1.5)
            print("Coup critique de l'ennemi !")
        if joueur_se_defend:
            degats = max(1, degats // 2)
            print("Ta défense réduit les dégâts !")

        vie_joueur = max(0, vie_joueur - degats)
        print(f"L'ennemi attaque et inflige {degats} dégâts.")

    return vie_joueur, vie_ennemi, potions_ennemi


def jouer_combat():
    vie_joueur = VIE_MAX
    vie_ennemi = VIE_MAX
    potions_joueur = 3
    potions_ennemi = 3

    noms_ennemis = ["le Gobelin rusé", "le Loup des ombres", "le Chevalier déchu"]
    nom_ennemi = random.choice(noms_ennemis)

    print("=== COMBAT ===")
    print(f"{nom_ennemi} apparaît et te barre la route !")
    print("Astuce : défends-toi avant une attaque pour en réduire les dégâts.")

    while vie_joueur > 0 and vie_ennemi > 0:
        print(
            f"\nTes PV : {vie_joueur}/{VIE_MAX} | "
            f"PV de l'ennemi : {vie_ennemi}/{VIE_MAX}"
        )
        print(f"Tes potions : {potions_joueur} | Potions ennemies : {potions_ennemi}")

        choix = demander_action_joueur()
        joueur_se_defend = False

        if choix == "1":
            degats = random.randint(DEGATS_MIN, DEGATS_MAX)
            if random.randint(1, 100) <= CHANCE_CRITIQUE:
                degats *= 2
                print("Coup critique !")
            vie_ennemi = max(0, vie_ennemi - degats)
            print(f"Tu attaques et infliges {degats} dégâts.")
        elif choix == "2":
            if potions_joueur == 0:
                print("Tu n'as plus de potion : tu perds ton tour.")
            elif vie_joueur == VIE_MAX:
                print("Tu as déjà tous tes PV : ta potion serait gaspillée.")
            else:
                soin = min(POTION_SOIN, VIE_MAX - vie_joueur)
                vie_joueur += soin
                potions_joueur -= 1
                print(
                    f"Tu récupères {soin} PV "
                    f"({vie_joueur} PV, {potions_joueur} potion(s) restante(s))."
                )
        elif choix == "3":
            joueur_se_defend = True
            print("Tu te mets en garde.")
        else:
            print("Choix invalide : tu perds ton tour.")

        # Le mauvais choix consomme bien le tour du joueur, puis l'ennemi agit.
        if vie_ennemi > 0:
            vie_joueur, vie_ennemi, potions_ennemi = tour_ennemi(
                vie_joueur, vie_ennemi, potions_ennemi, joueur_se_defend
            )

    if vie_joueur <= 0:
        print(f"\nTu as été vaincu par {nom_ennemi}... GAME OVER.")
    else:
        print(f"\nVictoire ! Tu as vaincu {nom_ennemi} avec {vie_joueur} PV.")


if __name__ == "__main__":
    jouer_combat()
