#!/opt/tljh/user/bin/python

# Pour le débogage
import cgitb; cgitb.enable()

from random import randint

html_tpl = """
<!DOCTYPE html>
<head>
    <title>alea</title>
</head>
<body>
    <a href="/">retour...</a>
    <p>Un entier au hasard (entre 1 et 1000): <mark>{contenu}</mark>
    <p>Recharger la page avec <code>CTRL+R</code>...</p>
</body>
</html>
"""

html = html_tpl.format(
    contenu=randint(1, 1000)
)

# pour l'entête http de la réponse
print("content-type: text/html; charset=utf-8\n")

# le corps de la réponse http
print(html)
