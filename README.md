# Web application - exchange rate app

App prepared for the ZPI course at TUL.

## Team

| position | name | github nickname |
|----------|------|-------------|
| developer + scrum master| Szymon Górka | [AIn0n](https://github.com/AIn0n) |
| developer | Daniel Wieczorek | [Panzer0](https://github.com/Panzer0) |
| devOps | Adam Tadzik | [VermiIion](https://github.com/VermiIion) |
| tester | Oskar Schilling | [GROMoOS](https://github.com/GROMoOS) |

## run application

Before you start - please prepare python virtual environment by typing in console:
```bash
python3 -m virtualenv venv
```
And install all dependencies list in requirements.txt file:
```bash
pip install -r requirements.txt
```
after that you can run application with command:
```bash
make run
```

## Technologies

We use streamlit library to create this site. It gives us enough flexibility to prepare all required functionalities without splitting project at classical, three pillars architecture - frontend, backend and database. This makes our development time much faster and codebase easier to maintain, cause everything is written in one language.

## Dev ops platform

We are using github actions as a main place for developing pipeline - mostly for running automated tests before each merge.This gives us the peace of mind and ensures that no existing functionality is broken by new commits. You can check the details [here](https://github.com/IIS-ZPI/ZPI2021_IO1_Banana_eaters/actions).

## MVP
Functionalities demanded for the minimal value product are listed in this [file](https://github.com/IIS-ZPI/ZPI2021_IO1_Banana_eaters/blob/readme/technical_requirements.pdf).

