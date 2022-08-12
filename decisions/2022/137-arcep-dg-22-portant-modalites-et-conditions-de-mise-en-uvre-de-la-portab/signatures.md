# Signatures
Fait à Lomé, le 18 juillet 2022
Le Directeur général
Michel Yaovi GALLEY
ANNEXE :
1. Spécifications relatives au RIO Mobile
Le RIO Mobile est constitué de quatre champs suivant la structure suivante « OO Q RRRRRR CCC » dans laquelle :
- Champ « OO » : champ codé sur deux caractères numériques identifiant J'Opérateur Donneur ; - Champ « Q » : champ codé sur un caractère alphanumérique correspondant à la qualité de l'abonné mobile. Ce champ peut prendre deux modalités « P » pour « particulier » ou « E » pour « Entreprise » ; - Champ « RRRRRR » : champ codé sur six caractères alphanumériques constituant une référence du contrat associé au numéro mobile pour J'Opérateur Donneur ; - Champ « CCC » : champ codé sur trois caractères alphanumériques constituant une clé permettant de vérifier la cohérence entre le numéro mobile de l'abonné mobile et les trois premiers champs du RIO Mobile.
2. Messages transmis à l'Abonné Mobile par les Opérateurs Mobiles lors du traitement de la Demande de Portage
✓ SMS n° 1 : Information de l'Abonné Mobile sur sa situation auprès de l'Opérateur Donneur et communication du RIO. L'Opérateur Donneur envoie à l'Abonné Mobile une série de SMS comportant de manière claire et intelligibles les messages suivants :
- « [Nom] [Prénom] est titulaire d'un contrat. Le RIO est : [OO Q RRRRRR CCC] » - « Le solde total de votre crédit est [à compléter]. Votre crédit expire le [à compléter] » - « Le solde de votre forfait est [à compléter forfait par forfait]. Votre forfait [o] expire le [à compléter forfait par forfait] » - « Le solde de votre porte-monnaie électronique est de [à compléter]. Il expire le [à compléter] »
Lorsqu'il existe un engagement non échu à la date d'interrogation du Serveur d'Information par l'Abonné Mobile : « L'engagement de [Nom] [Prénom] contracté le [JJ/MM/AAAA1] prendra fin le [JJ/MM/AAAA2]. Le RIO est : [OO Q RRRRRR CCC]. » ;
✓ SMS n° 2 : Confirmation de la programmation du Portage
Après confirmation de l'éligibilité au Portage par l'Opérateur Receveur, l'Opérateur Donneur envoie à l'Abonné Mobile le message suivant :
« Conformément à votre demande, la résiliation avec portabilité du numéro [9XXXXXXX] sera effectuée le [JJ/MM/AAAA] entre [Heure début] et [Heure fin] ».
✓ SMS n° 3 : Confirmation du Portage par l'Opérateur Receveur
L'Opérateur Receveur envoie à l'Abonné Mobile la veille ou le matin du Portage le message suivant :
« Conformément à votre demande, la portabilité de votre numéro [9XXXXXXX] sera effectuée vers [Dénomination commerciale de l'Opérateur] le [JJ/MM/AAAA] entre [Heure début] et [Heure fin]. »
✓ SMS n° 4 : Annulation d'une Demande de Portage à la suite d'une demande de l'Abonné Mobile
L'opérateur Receveur envoie à l'Abonné Mobile à la suite de la prise en compte de sa demande d'annulation le message suivant :
« Conformément à votre demande, la portabilité de votre numéro [9XXXXXXX] vers [Dénomination commerciale de l'opérateur] a été annulée. Pour plus d'informations contacter le service client au [compléter avec le numéro du service client]. »
✓ SMS n° 5 : Annulation d'une Demande de Portage en cas de non-éligibilité
L'Opérateur Receveur envoie à l'Abonné Mobile le message suivant :
« La portabilité du [9XXXXXXX] vers [Dénomination commerciale de l'Opérateur a été annulée pour une raison technique. Pour plus d'informations appeler le service client au [compléter avec le numéro du service client]. »
✓ SMS n° 6 : Message de bienvenue en cas de Portabilité effective.
L'Opérateur Receveur envoie à l'Abonné Mobile un message de bienvenue.
