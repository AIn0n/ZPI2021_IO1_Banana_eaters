# Web application - exchange rate app

App prepared for the ZPI course at TUL. Hosted at [streamlit](https://zpi-banana-eaters.streamlit.app/).

## Team

| position | name | github nickname |
|----------|------|-------------|
| developer + scrum master| Szymon Górka | [AIn0n](https://github.com/AIn0n) |
| developer | Daniel Wieczorek | [Panzer0](https://github.com/Panzer0) |
| devOps | Adam Tadzik | [VermiIion](https://github.com/VermiIion) |
| tester | Oskar Schilling | [GROMoOS](https://github.com/GROMoOS) |

## Run application

Before you start - please prepare a python virtual environment by typing the following in your console:
```bash
python3 -m virtualenv venv
```

Subsequently, turn on the virtual environment with the following command:
```bash
source tutorial-env/bin/activate
```

Afterwards, install all dependencies listed in requirements.txt file:
```bash
pip install -r requirements.txt
```

Finally, you can run the application with command:
```bash
make run
```

## Technologies

We use streamlit library to create this site. It gives us enough flexibility to prepare all required functionalities without splitting project at the classical, three pillars architecture - frontend, backend and database. This makes our development time much faster and codebase easier to maintain, since everything is written in one language.

## Dev ops platform

We are using github actions as a main place for developing pipeline - mostly for running automated tests before each merge.This gives us the peace of mind and ensures that no existing functionality is broken by new commits. You can check the details [here](https://github.com/IIS-ZPI/ZPI2021_IO1_Banana_eaters/actions).

## MVP
Functionalities demanded for the minimal value product are listed in this [file](https://github.com/IIS-ZPI/ZPI2021_IO1_Banana_eaters/blob/readme/technical_requirements.pdf).

