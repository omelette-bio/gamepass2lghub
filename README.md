# gamepass2lghub
> project to automate the process of adding a gamepass game to lghub (hope that this will become obsolete)
<img src="https://img.shields.io/badge/code%20style-black-000000.svg">

### execution
the project works with the terminal just type 
```zsh
python3 main.py
```
and follow the instructions displayed on the terminal

### requirements
you'll need :
- the path of settings.db (back it up just in case)
- name of the game
- the path of the executable
- the path for the picture (not mandatory)

### paths typing
if you're on windows, don't type paths with `"` or `\\`, the program normally converts it, I will do more checking in the program.

### autofetch
I've started making two autofetches :
- one for the games
- one for the settings.db file

for the first, because each game have a different exe file name, I made a json file with `name of the game: exe_path` only problem is that we have to manually add games to json file
