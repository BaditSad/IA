<div align="center">
  <img src=".github/assets/banner.png" alt="Voice Assistant banner" width="100%" />

  <h1>IA</h1>
  <p>
    Personal voice assistant in French, inspired by Jarvis-style assistants
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

## :notebook_with_decorative_cover: Table of Contents

- [About](#star2-about)
  * [Tech Stack](#space_invader-tech-stack)
  * [Features](#dart-features)
- [Getting Started](#toolbox-getting-started)
  * [Prerequisites](#bangbang-prerequisites)
  * [Installation](#gear-installation)
  * [Run Locally](#running-run-locally)
- [Contact](#handshake-contact)

## :star2: About

This project is a personal voice assistant written in Python. It listens for a command through the microphone,
transcribes it with Google's speech recognition in French, then analyzes it to pick an action from a set of
predefined options.

The data used by the assistant (cities and countries, configuration, conversation phrases) is stored locally as
JSON files, which makes the assistant's behavior easy to extend without touching the code.

### :space_invader: Tech Stack

<details>
  <summary>Language and Libraries</summary>
  <ul>
    <li><a href="https://www.python.org/">Python</a></li>
    <li><a href="https://pypi.org/project/SpeechRecognition/">SpeechRecognition</a></li>
    <li>Google Speech Recognition (online speech recognition)</li>
  </ul>
</details>

<details>
  <summary>Data</summary>
  <ul>
    <li>Local JSON files (configuration, cities, conversations)</li>
  </ul>
</details>

### :dart: Features

- Voice listening and transcription in French
- Voice-controlled calculator
- Date and time lookup
- Weather lookup
- Local database of countries and cities to enrich answers
- Debug mode to test a text command without using the microphone

## :toolbox: Getting Started

### :bangbang: Prerequisites

- Python 3 installed
- A working microphone
- An internet connection (speech recognition goes through the Google API)

### :gear: Installation

```bash
git clone https://github.com/BaditSad/IA.git
cd IA
pip install SpeechRecognition pyaudio
```

### :running: Run Locally

```bash
python Main.py
```

The `DEBUG` mode in `Main.py` allows testing a fixed text command without using the microphone.

## :handshake: Contact

Brieuc Dumortier

[LinkedIn](https://www.linkedin.com/in/dumortier-brieuc/) - [GitHub](https://github.com/BaditSad) - dumortier.contact@gmail.com
