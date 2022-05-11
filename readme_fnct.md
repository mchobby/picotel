# Minitel: Touches et fonctions avancées

Description des différents combinaisons de touches et fonctions avancées accessible depuis le clavier du Minitel.

Voici comment "Activer" le mode terminal pour le Raspberry-Pi Pico

1. '''Fnct+Sommaire''' : Passer du mode répertoire au mode terminal (dit mem)
2. '''Fnct+T --> A''' : Passage en mode périphérique UART (ASCII, US)
3. '''Fnct+T --> E''' : Désactivation de l’echo sur le terminal
4. '''Fnct+P --> 4''' : Connexion à 4800 bauds (utiliser 9 pour 9600 bauds)

# Terminal
|  Key Combination |  Description  |
|-----------|----------------------|
| Fnct+T --> I | EEProm memory reset. |
| Fnct+T --> V | Standard Téletél mode Vidéotext (40 colonnes) |
| Fnct+T --> A | Standard "téléinformatique" ASCII US (80 colonnes) |
| Fnct+T --> F | Standard "téléinformatique" ASCII FR (80 colonnes) |
| Fnct+T --> E | Echo local (On/Off) |
| Fnct+C --> E | Enable extended keyboard (ctrl, esc, arrows) |
| Fnct+C --> V | Disabled extended keyboard |

# Terminal speed
|  Key Combination |  Description  |
|-----------|----------------------|
| Fnct+P --> 1 | 1200 bauds  |
| Fnct+P -->  3 | 300 bauds   |
| Fnct+P --> 4 | 4800 bauds  |
| Fnct+P --> 9 | 9600 bauds  |
| Fnct+P --> I | Prise UART (on/off)  |

# Ecran
|  Key Combination |  Description  |
|-----------|----------------------|
| Fnct+E --> P | Ecran en mode page  |
| Fnct+E --> R | Ecran en mode rouleau (défilement?)   |
| Fnct+E --> F | Passage du mode 40/80 colonnes  |
| Fnct+E --> M | Activation de la veille des 3 heures (???)  |
| Fnct+E --> M | Désactivation de la veille des 3 heures (???)  |

# Clavier
|  Key Combination |  Description  |
|-----------|----------------------|
| Fnct+C --> M | Passage entre mode Majuscule/Minuscule  |
| Fnct+C --> E | Passer le clavier en étendu  |
| Fnct+C --> C | Modifie le codage des touches étendues (CO/CSI) |
| Fnct+C --> V | Clavier en mode VideoTex standard |


# Autre
|  Key Combination |  Description  |
|-----------|----------------------|
| Fnct+Correction | Augmenter le volume du Haut-Parleur  |
| Fnct+Annulation | Diminution du volume du Haut-Parleur |
| Fnct+Guide      | Copie d'écran vers l'UART (dans le jeu de caractères actif) |
| Fnct+I --> A    | Copie d'écran vers l'UART (jeu de caractères USA) |
| Fnct+I --> F    | Copie d'écran vers l'UART (jeu de caractères FR)  |

# A creuser
* Norme de visualisation CEPT 2 (Télétel), ISO 6429 (ASCII)
* Memoire EAROM de 256 octets
* Possibilité de télécharger deux jeux de 94 forms DRCS conformément à la norme CEPT T-TE-0601
