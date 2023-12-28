# Data Science Project Template

Welcome to our Data Science Project Template, a streamlined foundation for kick-starting your data science endeavors. This repository is designed to provide an efficient, reproducible, and easy-to-use framework for data science projects of any scale.

Our template leverages a Makefile to automate various tasks associated with setting up and maintaining a data science project environment. The Makefile is a powerful tool that simplifies the process of managing dependencies, virtual environments, and other routine tasks, allowing you to focus on the core aspects of your data analysis.

## Prerequisites

- [Python 3.10](https://www.python.org/downloads/release/python-3100/)
- [Git](https://git-scm.com/downloads)



## Clone the repository

To get started with this template, clone the repository using the following command:

```sh
git clone https://github.com/hamsomp3/plantilla_ds.git
```

# Environment Setup (Requirements)

After cloning the repository, navigate to the project directory and run the following command to set up your environment:

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

Set up the project environment on Unix-like systems, including the creation of a Python virtual environment and installation of necessary packages.

```sh
local-setup-mac: install-unix
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