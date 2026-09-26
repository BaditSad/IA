<div align="center">

  <h1>IA</h1>

  <p>
    Assistant vocal personnel en français, inspiré des assistants type Jarvis
  </p>

<p>
  <a href="https://github.com/BaditSad/IA/commits/main">
    <img src="https://img.shields.io/github/last-commit/BaditSad/IA" alt="last update" />
  </a>
  <a href="https://github.com/BaditSad/IA">
    <img src="https://img.shields.io/github/languages/top/BaditSad/IA" alt="top language" />
  </a>
</p>

</div>

<br />

# Table des matières

- [À propos](#à-propos)
  * [Stack technique](#stack-technique)
  * [Fonctionnalités](#fonctionnalités)
- [Démarrage](#démarrage)
  * [Prérequis](#prérequis)
  * [Installation](#installation)
  * [Lancer en local](#lancer-en-local)
- [Contact](#contact)

## À propos

Ce projet est un assistant vocal personnel écrit en Python. Il écoute une commande via le microphone, la transcrit avec la reconnaissance vocale de Google en français, puis l'analyse pour choisir une action à exécuter parmi un ensemble d'options prédéfinies.

Les données utilisées par l'assistant (villes et pays, configuration, phrases de conversation) sont stockées en local sous forme de fichiers JSON, ce qui rend le comportement de l'assistant facile à étendre sans toucher au code.

### Stack technique

<details>
  <summary>Langage et bibliothèques</summary>
  <ul>
    <li><a href="https://www.python.org/">Python</a></li>
    <li><a href="https://pypi.org/project/SpeechRecognition/">SpeechRecognition</a></li>
    <li>Google Speech Recognition (reconnaissance vocale en ligne)</li>
  </ul>
</details>

<details>
  <summary>Données</summary>
  <ul>
    <li>Fichiers JSON locaux (configuration, villes, conversations)</li>
  </ul>
</details>

### Fonctionnalités

- Écoute et transcription vocale en français
- Calculatrice vocale
- Consultation de la date et de l'heure
- Consultation de la météo
- Base de données locale de pays et villes pour enrichir les réponses
- Mode debug pour tester une commande texte sans passer par le micro

## Démarrage

### Prérequis

- Python 3 installé
- Un microphone fonctionnel
- Une connexion internet (la reconnaissance vocale passe par l'API Google)

### Installation

```bash
git clone https://github.com/BaditSad/IA.git
cd IA
pip install SpeechRecognition pyaudio
```

### Lancer en local

```bash
python Main.py
```

Le mode `DEBUG` dans `Main.py` permet de tester une commande texte fixe sans passer par le microphone.

## Contact

Brieuc Dumortier

[LinkedIn](https://www.linkedin.com/in/dumortier-brieuc/) - [GitHub](https://github.com/BaditSad) - dumortier.contact@gmail.com
