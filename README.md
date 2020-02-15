# Command line client for person management

This repository contains the command line client for person management. You can create, update, view and delete person data using this command line client. 

**NOTE :** Before running this client, you need to run the **REST API** from the repository : https://github.com/Nusky-cloud/ebi-masterdata-person-api.git

# How to run?

## Requirements

For running the client you need:

- [Python 3.8.1](https://www.python.org/downloads)
- Pip 19.2.3

**NOTE :** Pip will be installed with Python. You can check the Python and Pip version in a console by **python --version** and **pip --version** respectively.

After that, execute below command in a console.
```shell
pip install requests=2.22.0
```

## Running

- First, clone this repository on your computer or download as a zip file.
```shell
git clone https://github.com/Nusky-cloud/ebi-person-management-cli.git
```

- After that, open a console and change directory to project root and execute below command. This will run the client.

```shell
python ebi-person-management-cli.py
```

