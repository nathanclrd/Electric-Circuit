import pygame
import sys
import os 
import shutil

pygame.init()

import shutil

def resource_path(relative_path):
    try:
        # Si l'application est empaquetée (frozen)
        if hasattr(sys, '_MEIPASS'):
            # _MEIPASS est un répertoire temporaire créé lors de l'exécution d'un exécutable cx_Freeze
            base_path = sys._MEIPASS
        else:
            # Si ce n'est pas une application empaquetée, utiliser le répertoire du script
            base_path = os.path.abspath(os.path.dirname(sys.argv[0]))  # Répertoire de l'exécutable ou script

        # Retourner le chemin absolu de la ressource
        return os.path.join(base_path, 'resources', relative_path)
    except Exception as e:
        print(f"Erreur lors de l'accès à la ressource : {e}")
        return None

# Charger les images
circuit_path = resource_path("circuit.png")
closed_path = resource_path("closed.png")

circuit = pygame.image.load(circuit_path)
interrup_closed = pygame.image.load(closed_path)


ecran = pygame.display.set_mode((1650,1000))


interrupt_closed_resized = pygame.transform.scale(interrup_closed,(5,30))




interrupteurs = [{'id': 0, 'position': (213, 147), 'orientation': 'v', 'status': 'closed'}, {'id': 1, 'position': (213, 214), 'orientation': 'v', 'status': 'closed'}, {'id': 2, 'position': (212, 247), 'orientation': 'v', 'status': 'closed'}, {'id': 3, 'position': (812, 257), 'orientation': 'v', 'status': 'closed'}, {'id': 4, 'position': (812, 291), 'orientation': 'v', 'status': 'closed'}, {'id': 5, 'position': (1386, 148), 'orientation': 'v', 'status': 'closed'}, {'id': 6, 'position': (1385, 214), 'orientation': 'v', 'status': 'closed'}, {'id': 7, 'position': (1388, 250), 'orientation': 'v', 'status': 'closed'}, {'id': 8, 'position': (1484, 533), 'orientation': 'v', 'status': 'closed'}, {'id': 9, 'position': (1397, 502), 'orientation': 'v', 'status': 'closed'}, {'id': 10, 'position': (1368, 535), 'orientation': 'v', 'status': 'closed'}, {'id': 11, 'position': (1292, 535), 'orientation': 'v', 'status': 'closed'}, {'id': 12, 'position': (1233, 536), 'orientation': 'v', 'status': 'closed'}, {'id': 13, 'position': (1196, 535), 'orientation': 'v', 'status': 'closed'}, {'id': 14, 'position': (890, 538), 'orientation': 'v', 'status': 'closed'}, {'id': 15, 'position': (814, 516), 'orientation': 'v', 'status': 'closed'}, {'id': 16, 'position': (719, 549), 'orientation': 'v', 'status': 'closed'}, {'id': 17, 'position': (664, 547), 'orientation': 'v', 'status': 'closed'}, {'id': 18, 'position': (376, 550), 'orientation': 'v', 'status': 'closed'}, {'id': 19, 'position': (211, 512), 'orientation': 'v', 'status': 'closed'}, {'id': 20, 'position': (158, 550), 'orientation': 'v', 'status': 'closed'}, {'id': 21, 'position': (74, 549), 'orientation': 'v', 'status': 'closed'}, {'id': 22, 'position': (157, 762), 'orientation': 'v', 'status': 'closed'}, {'id': 23, 'position': (157, 806), 'orientation': 'v', 'status': 'closed'}, {'id': 24, 'position': (156, 852), 'orientation': 'v', 'status': 'closed'}, {'id': 25, 'position': (307, 761), 'orientation': 'v', 'status': 'closed'}, {'id': 26, 'position': (307, 806), 'orientation': 'v', 'status': 'closed'}, {'id': 27, 'position': (306, 852), 'orientation': 'v', 'status': 'closed'}, {'id': 28, 'position': (503, 769), 'orientation': 'v', 'status': 'closed'}, {'id': 29, 'position': (504, 813), 'orientation': 'v', 'status': 'closed'}, {'id': 30, 'position': (503, 858), 'orientation': 'v', 'status': 'closed'}, {'id': 31, 'position': (710, 810), 'orientation': 'v', 'status': 'closed'}, {'id': 32, 'position': (943, 761), 'orientation': 'v', 'status': 'closed'}, {'id': 33, 'position': (946, 805), 'orientation': 'v', 'status': 'closed'}, {'id': 34, 'position': (947, 853), 'orientation': 'v', 'status': 'closed'}, {'id': 35, 'position': (1095, 764), 'orientation': 'v', 'status': 'closed'}, {'id': 36, 'position': (1097, 804), 'orientation': 'v', 'status': 'closed'}, {'id': 37, 'position': (1098, 853), 'orientation': 'v', 'status': 'closed'}, {'id': 38, 'position': (579, 312), 'orientation': 'h', 'status': 'closed'}, {'id': 39, 'position': (688, 186), 'orientation': 'h', 'status': 'closed'}, {'id': 40, 'position': (908, 175), 'orientation': 'h', 'status': 'closed'}, {'id': 41, 'position': (1008, 295), 'orientation': 'h', 'status': 'closed'}]

def rotate_with_bottom_pivot(image, angle):
    # Obtenir les dimensions de l'image
    width, height = image.get_size()

    # Effectuer la rotation de l'image autour du centre
    rotated_image = pygame.transform.rotate(image, angle)  # Utiliser un angle négatif pour une rotation vers la gauche

    # Nouvelle taille de l'image après la rotation
    rotated_width, rotated_height = rotated_image.get_size()

    # Calculer l'offset pour que le bas de l'image reste au même endroit
    # Le bas de l'image doit rester fixe, donc l'offset en Y est la différence entre la hauteur d'origine et la hauteur après rotation.
    offset_x = (rotated_width - width) // 2  # Centrer l'image horizontalement après rotation
    offset_y = rotated_height - height  # Décalage en Y pour maintenir le bas en place

    return rotated_image, offset_x, offset_y

    
rotated_image, offset_x, offset_y = rotate_with_bottom_pivot(interrupt_closed_resized, 30)

def afficher_circuit():
    circuit_resized = pygame.transform.scale(circuit,ecran.get_size())
    ecran.blit(circuit_resized,(0,0))

def afficher_interrupteurs():
    for u in interrupteurs:
        if u["status"] == "closed":
            if u["orientation"]=="h":
                rotatedi = pygame.transform.rotate(interrupt_closed_resized,90)
                ecran.blit(rotatedi,(u["position"][0],u["position"][1]-rotatedi.get_size()[1]//2))
            elif u["orientation"]=="v":
                ecran.blit(interrupt_closed_resized,(u["position"][0],u["position"][1]-5))
        if u["status"] =="open":
            if u["orientation"]=="h":
                rotateds =pygame.transform.rotate(interrupt_closed_resized,120)
                ecran.blit(rotateds,(u["position"][0],u["position"][1]))
            elif u["orientation"]=="v":
                ecran.blit(rotated_image, (u['position'][0] - rotated_image.get_width() // 2-offset_x, u['position'][1] -offset_y-5))
def catch_mouse(m_pos):
    tolerance = 5  # Taille du rectangle de détection autour de chaque interrupteur

    for interrupteur in interrupteurs:
        x, y = interrupteur["position"]
        
        # Créer un rectangle de détection autour de l'interrupteur (en fonction de son orientation)
        if interrupteur["orientation"] == 'v':  # Si l'interrupteur est vertical
            rect = pygame.Rect(x - tolerance, y - tolerance, 10 + 2 * tolerance, 30 + 2 * tolerance)  # Ajuster les dimensions du rectangle
        else:  # Si l'interrupteur est horizontal
            rect = pygame.Rect(x - tolerance, y - tolerance, 30 + 2 * tolerance, 10 + 2 * tolerance)  # Ajuster les dimensions du rectangle

        # Vérifier si la souris est dans le rectangle de l'interrupteur
        if rect.collidepoint(m_pos):
            if interrupteur["status"] == "closed":
                interrupteur["status"] = "open"
                break
            elif interrupteur["status"] == "open":
                interrupteur["status"] = "closed"
                break


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:  # Vérifier si un bouton de la souris est enfoncé
            if event.button == 1:  # Vérifier si c'est un clic gauche (button 1)
                m_pos = pygame.mouse.get_pos()  # Récupérer la position de la souris
                catch_mouse(m_pos)  # Vérifie si un interrupteur a été cliqué


    afficher_circuit()
    afficher_interrupteurs()


    pygame.display.flip()

# pygame.quit()

