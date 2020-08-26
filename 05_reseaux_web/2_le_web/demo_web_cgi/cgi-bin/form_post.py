#!/opt/tljh/user/bin/python

import cgitb; cgitb.enable()
import cgi, os

SECRET = "secret"

entete_http = "Content-type: text/html; charset=utf-8\n"

html_form_tpl = """
<form method="post">
        Login: <input type="text" name="login" value="{login_v}"/><br/>
        Mot de passe: <input type="password" name="pass"/><br/>
        <input type="submit"/>
</form>
"""

message_secret_tpl = """
<h2>Bonjour {login}!</h2>
<p>Voici le contenu Super Secret .... shut!</p>
<p><a href="/" onclick="document.cookie='login=; Max-Age=-99999999;'">se déconnecter</a><p>
"""

formulaire = cgi.FieldStorage()
login = formulaire.getvalue("login")
password = formulaire.getvalue("pass")
cookie = os.environ["HTTP_COOKIE"]

# l'utilisateur est-il authentifié?
if "login" not in cookie: # non
    
    # vient-il de soumettre le formulaire?
    if not (login and password): # non
        
        # on affiche simplement le formulaire 
        contenu = html_form_tpl.format(
            login_v=""
        )
    
    # le formulaire a été soumis
    
    # l'utilisateur a-t-il saisi le bon mot de passe?
    elif login and password and password == SECRET: # oui
        
        # plaçons un cookie pour nous en souvenir
        entete_http += f"Set-Cookie: login={login}\n"
        
        # et affichons le message secret
        contenu = message_secret_tpl.format(
            login=login
        )
    
    else: # n'a pas saisi le bon mot de passe (ou login est vide)
        
        # réaffichons le formulaire (en laissant le login qu'il a saisi)
        contenu = html_form_tpl.format(
            login_v=login,
        )
        
        # indiquons lui le problème
        contenu += """
        <p style="color: red">Mot de passe incorrect.<p>
        """
        
else: # l'utilisateur est authentifié
    
    # parsons le cookie brut afin de retrouver son login
    
    #1: couper selon le séparateur ;
    split1 = cookie.split(';')
    
    #2: récupérons la bonne paire (login=<non_utilisateur>)
    sel = [
        paire 
        for paire in split1 
        if "login" in paire
    ][0]
    
    #3: couper la paire et récupérer le deuxième item
    nom = sel.split('=')[1]
    
    # nous sommes prêt à formater le message secret
    contenu = message_secret_tpl.format(
        login=nom
    )

# Produire le html final (avec une f-string)
html = f"""
<!DOCTYPE html>
<head>
    <title>login</title>
</head>
<body>
    <a href="/">retour...</a>
    {contenu}
</body>
</html>
"""

# et envoyer!
print(entete_http)
print(html)