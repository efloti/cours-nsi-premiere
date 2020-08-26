#!/opt/tljh/user/bin/python

# sert au débogage pendant le développement
import cgitb; cgitb.enable()

# pour accéder à l'environnement: os.environ
import os

# gabarit html (template d'où _tpl)
# zone d'insertion {environnement}
html_tpl = """
<!DOCTYPE html>
<head>
    <title>environ</title>
</head>
<body>
    <a href="/">retour...</a>
    <p>Quelques variables d'environnement importantes transmises au script (il y en a bien d'autres!)</p>
    <ol>
        {environnement}
    </ol>
</body>
</html>
"""

# variables d'environnement qu'on souhaite afficher
a_filtrer = [
    'SERVER_SOFTWARE',
    'REQUEST_METHOD',
    'QUERY_STRING',
    'HTTP_REFERER',
    'HTTP_COOKIE',
    'HTTP_USER_AGENT'
]

# gabarit pour une ligne de la liste <ol>
# zones d'insertion {cle} et {valeur}
item_tpl = '<li><strong>{cle}</strong>: {valeur}</li>'

# construction de la liste des lignes
lignes = [
    item_tpl.format(cle=k, valeur=v)
    for k, v in os.environ.items() 
    if k in a_filtrer
]
# reste à les joindre en une chaîne unique
lignes = '\n'.join(lignes)

# on finalise le gabarit html
html = html_tpl.format(environnement=lignes)

# envoie de la réponse au serveur
print("Content-type: text/html; charset=utf-8\n")
print(html)