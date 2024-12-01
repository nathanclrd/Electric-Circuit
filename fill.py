import pygame
import sys

pygame.init()

ecran = pygame.display.set_mode((1650,1000))

circuit = pygame.image.load("./circuit.png")

#43
interrup_closed = pygame.image.load("./closed.png")
interrupt_resized = pygame.transform.scale(interrup_closed,(5,30))


interrupteurs =[]

def new(id,pos,orientation="v"):
    interrupteur = {
        "id":id,
        "position":pos,
        "orientation":orientation,
        "status": "closed"
    }
    interrupteurs.append(interrupteur)

def afficher_circuit():
    circuit_resized = pygame.transform.scale(circuit,ecran.get_size())
    ecran.blit(circuit_resized,(0,0))


running = True
id =0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:  # Vérifier si un bouton de la souris est enfoncé
            if event.button == 1:  # Vérifier si c'est un clic gauche (button 1)
                m_pos = pygame.mouse.get_pos()  # Récupérer la position de la souris
                new(id,m_pos)
                id+=1
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_r:
                m_pos = pygame.mouse.get_pos()  # Récupérer la position de la souris
                new(id,m_pos,"h")
                id+=1

                


    afficher_circuit()



    pygame.display.flip()



with open("lines.txt","w") as f:
    for i in interrupteurs:
        f.write(f"{i},")
        print(i)
    f.close()



