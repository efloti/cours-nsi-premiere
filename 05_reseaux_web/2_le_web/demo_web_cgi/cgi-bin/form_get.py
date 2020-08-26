#!/opt/tljh/user/bin/python

import cgitb; cgitb.enable()

# pour gérer les données transmises par le formulaire
import cgi

formulaire = cgi.FieldStorage() 
couleur = formulaire.getvalue("couleur")

html_tpl = f"""
<!DOCTYPE html>
<head>
    <title>formulaire - get</title>
</head>
<body>
    <a href="/">retour...</a>
    <form method="get">
        Choisir une couleur: 
        <input type="color" name="couleur" value="{couleur}"/>
        <input type="submit"/>
    </form>
    <div style="background-color: {couleur}; height: 100px; width:100px;">100x100</div>
</body>
</html>
"""

print("Content-type: text/html; charset=utf-8\n")
print(
    html_tpl.format(
        # notez que le champ "couleur" n'existe pas
        # la première fois que l'utilisateur arrive sur cette page
        # dans ce cas couleur vaut None et on met du blanc #fff
        couleur=couleur if couleur else "#fff"
    )
)