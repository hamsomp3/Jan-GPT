# Chatbot JanGPT

Welcome to the JanGPT project! JanGPT is a unique chatbot created to simulate conversations with the author, inspired by his social media posts from platforms like Facebook and Twitter. This innovative concept leverages the power of the [GPT-3.5 turbo](https://openai.com/blog/new-models-and-developer-products-announced-at-devday) API, a state-of-the-art transformer-based language model. With a contextual understanding spanning 4,096 tokens and training data up until September 2021, JanGPT promises a rich and engaging chat experience.

One of the standout features of JanGPT is its ability to mimic the "voice" of the author. This is achieved through the advanced Text-To-Speech (TTS) capabilities of the OpenAI API, adding an extra layer of immersion to your interactions with the chatbot.


## Prerequisites

Before diving into JanGPT, ensure you have the following prerequisites installed:

- [Python 3.10](https://www.python.org/downloads/release/python-3100/) The core programming language used.
- [Git](https://git-scm.com/downloads) Essential for cloning the repository.

# Getting Started

## Clone the repository

Begin by cloning the repository to your local machine using this command:

```sh
git clone https://github.com/hamsomp3/Jan-GPT.git
```

# Environment Setup (Requirements)

Navigate to your project directory. Set up your environment by installing the necessary packages:

## Quick Start ⚡

## Windows Installation

For window users, please install [Chocolatey](https://chocolatey.org/install) and then execute the following command in the cmd.exe as administrator to install the packages:

```sh
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```
This instruction will install the Chocolatey package manager in your computer.

Then, install the make package with the following command:

```sh
choco install make
```

This instruction will install the make package in your computer.


```sh
local-setup-windows: install-windows
```

This instruction will install the libraries of the requirements.txt file.

## Unix Installation

If this is your first time using the template, you will need to install the necessary packages to set up the project environment. To do so, run the following command:

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python
```

Make sure you have the right path in the shell, if not, please run the following command:

```sh
export PATH="/usr/local/bin:$PATH"
```

Set up the project environment on Unix-like systems, including the creation of a Python virtual environment and installation of necessary packages.

```sh
local-setup-mac: install-unix
```

## Streamlit

To execute/run the streamlit app, please run the following command:

```sh
make stream
```

## Contributing
We welcome contributions to this template. Please read our contribution guidelines for more information on how to submit pull requests.

## License

## Contact

For additional information or questions about the project, you can reach out to the following individuals:

- hamsomp3@hotmail.com
- janpolanco@javerianacali.edu.co
- [LinkedIn](https://www.linkedin.com/in/jan-polanco-velasco/)

We will be happy to assist you. Thank you for your interest in this project!