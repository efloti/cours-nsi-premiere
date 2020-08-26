from socket import socket, gethostbyname

IP = gethostbyname('jhub.fdex.eu')
PORT = ___
adresse_serveur = IP, PORT

s = socket()
s.connect(adresse_serveur)

while True:
    message = input('>>> ') # tester input(...) dans un notebook si besoin
    if not message:
        s.close()
        print("Déconnexion")
        break
    octets = message.encode()
    s.send(octets)
    
    reponse_brut = s.recv(1024)
    print('<<<', reponse_brut.decode())
    # if m_serv == b'':
        # s.close()
        # break