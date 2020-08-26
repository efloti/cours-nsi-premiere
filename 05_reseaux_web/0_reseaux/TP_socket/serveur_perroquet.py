from socket import socket
from random import randint

IP = '' # signifie «toutes les interfaces réseau de la machine locale»
PORT = randint(10000, 50000)
print(f"j'utilise le port {PORT}")

# connexion et écoute d'une interface réseau
interface = socket()
adresse_serveur = IP, PORT
interface.bind(adresse_serveur)
interface.listen()

# boucle principale:
while True:
    # attente d'une connexion
    print("En attente d'une connexion...")
    c, adr_c = interface.accept()
    print(f"Connexion de: {adr_c}")
    
    # boucle de dialogue avec LE client connecté
    while True:
        recu_brut = c.recv(1024)
        if recu_brut == b'': # rien ? le client s'est déconnecté!
            c.close()
            print(f"Déconnexion de {adr_c}")
            break
        
        recu_txt = recu_brut.decode()
        print(f"<<< texte: {recu_txt}, brut: {recu_brut}")
        reponse = f"bien reçu: «{recu_txt}»"
        c.send(reponse.encode())