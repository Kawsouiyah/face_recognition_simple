# Face Recognition Simple

Un projet Python simple utilisant OpenCV pour reconnaître un visage à partir d'une image de référence (ex: Angelina Jolie ou toute autre personne), en temps réel via webcam.

## Fonctionnalités

-  Capture vidéo en direct via webcam.
-  Détection faciale avec le classificateur Haar de OpenCV.
-  Comparaison de visage via différence absolue.
-  Affichage d'une étiquette "Angelina Jolie" si le visage est reconnu, sinon "Inconnu".

##  Technologies utilisées

- Python 3.x
- OpenCV (cv2)

## Personnalisation
Tu peux changer le nom affiché en remplaçant "Angelina Jolie" par le nom de ton choix dans la ligne suivante :
```bash
label = "Angelina Jolie" if score < 50 else "Inconnu"

## Améliorations futures 
Remplacer la méthode de comparaison par un modèle deep learning (ex: FaceNet, Dlib).

Support multi-visages enregistrés.


