#!/opt/tljh/user/bin/python

import cgitb; cgitb.enable() # pour débogage

import os

entete_http = "Content-type: text/html; charset=utf-8\n"

# gabarit html ... deux zones d'insertions
html_tpl = """
<!DOCTYPE html>
<head>
    <title>cookie</title>
</head>
<body>
    <a href="/">retour...</a>
    <h2>{message}</h2>
    {suppr}
</body>
</html>
"""

# négliger cela pour l'instant
lien_suppression = """
<a href="/" onclick="document.cookie='test=; Max-Age=-99999999;'">oublie moi ...</a>
"""

# récupérons le cookie éventuel
cookie = os.environ["HTTP_COOKIE"]

# l'a-t-on déjà enregistré ?
if "test" in cookie: # oui
    
    message = "Tu es déjà venue par ici toi..."
    suppr = lien_suppression

else: # non

    # demandons au navigateur d'enregistrer un cookie
    entete_http += "Set-Cookie: test=ok\n"
    
    message = "Première visite sur cette page?"
    suppr = ""
    
# nous sommes prêt pour produire la page finale
html = html_tpl.format(
    message=message,
    suppr=suppr,
)

# envoie de la réponse
print(entete_http)
print(html)