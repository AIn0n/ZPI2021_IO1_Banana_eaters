# Web application - exchange rate app

App prepared for ZPI course at TUL.

## Team

| position | name | github nick |
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

## Dev ops platform

We are using github actions as a main place for developing pipeline - mostly for running automated tests before each merge. This give us sanity and insure as that every new commit will not break any existing functionality. You can check the details [here](https://github.com/IIS-ZPI/ZPI2021_IO1_Banana_eaters/actions).

## MVP
Functionalities demanded for minimal value product are list in this [file]().

