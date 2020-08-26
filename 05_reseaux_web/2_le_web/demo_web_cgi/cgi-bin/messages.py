#!/opt/tljh/user/bin/python

import cgitb; cgitb.enable()

import os, cgi, pickle

# pour gérer plus facilement les cookie.
from http import cookies

entete_http = "Content-type: text/html; charset=utf-8/n"

# cette balise d'entête html demande d'effectuer
# une nouvelle requête après 2 secondes
# d'attente, on parle de redirection.
redirect = """
<meta http-equiv="refresh" content="2;URL=/cgi-bin/form_post.py">
"""
redirect_message = """
<h2>Vous allez être redirigé vers la page d'authentification...</h2>
"""

html_tpl = """
<!DOCTYPE html>
<head>
    <meta charset="utf8"/>
    {redirect}
    <title>message</title>
</head>
<body>
    <a href="/">retour...</a> - <a href="/" onclick="document.cookie='login=; Max-Age=-99999999;'">se déconnecter</a>
    {contenu}
</body>
</html>
"""

formulaire_html = """
<form method="post">
    Votre message:<br/>
    <textarea name="message"></textarea><br/>
    <input type="submit" />
</form>
"""

# récupérons les éventuels données du formulaire
form = cgi.FieldStorage()

# ainsi qu'un éventuel cookie
cookie = cookies.SimpleCookie(
    os.environ["HTTP_COOKIE"]
)

# l'utilisateur est-il authentifié?
if "login" not in cookie: # non
    
    # redirigons le vers la page d'authentification
    print(entete_http)
    print(html_tpl.format(
        redirect=redirect,
        contenu=redirect_message,
        )
    )
    
else: # oui
    
    # essayons de récupérer les messages
    try:
        with open("messages", "rb") as m:
            messages = pickle.load(m)
    
    # en cas d'erreur (si le fichier n'existe pas encore!)
    except:
        # création de la structure 
        # dictionnaire dont les clés sont les nom d'utilisateur (login)
        # et la valeur associé la liste de leurs messages.
        messages = {}

    # récupérons le nom de l'utilisateur
    login = cookie["login"].value
    
    # si ce n'est pas une clé du dictionnaire messages ...
    if login not in messages:
        
        # ... créons cette entrée
        messages[login] = []
    
    # récupérons le message éventuel
    message = form.getvalue("message")
    
    # s'il est non vide!
    if message:
        
        # ajoutons le à la fin de la liste associée 
        # à la clé login
        messages[login].append(message)
        
        # sauvegardons le dictionnaire
        with open("messages", "wb") as m:
            pickle.dump(messages, m)
    
    # préparation du html
    contenu = formulaire_html 

    # récupérons la liste des messages de l'utilisateur
    # (s'il en a) et affichons les dans une liste.
    if len(messages[login]) > 0:
        
        # Préparons les gabarits,
        liste_tpl = "<ol>{}</ol>"
        ligne_tpl = "<li>{}</li>"
        
        # puis la liste python des lignes de message
        lignes = [
            ligne_tpl.format(m)
            # procédons du plus récent au plus ancien
            for m in reversed(messages[login])
        ]
        
        # puis la liste html,
        liste = liste_tpl.format("\n".join(lignes))
        
        # et enfin, ajoutons le tout au «contenu»
        contenu += "\n" + liste

    # Envoyons le tout.
    print(entete_http)
    print(html_tpl.format(redirect="", contenu=contenu))