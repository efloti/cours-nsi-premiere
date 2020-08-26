let compteur = 0;

function suivant() {
    compteur++; // même effet que compteur = compteur + 1
    let vElt = document.querySelector('#valeur');
    vElt.textContent = compteur++;
}

let bouton = document.querySelector('#bouton');
bouton.addEventListener('click', suivant);
