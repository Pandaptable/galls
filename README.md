# galls (a CS2 selfbot)

Galls is a somewhat simple python script to generate responses to commands by sending a keystroke which executes a config file ingame.

## Features
- `!disconnect`
  - Disconnects you from the game.
- `!i <inspect link>`
  - Will open the inspect link inside of your client.
- `!switchhands`
  - Will switch your viewmodel between right and left
- `!play <sound>`
  - Will play the given sound on your client (look [here](https://github.com/redBDGR/CS2-Sound-List) for a sound list)
  - Note: I recommend setting the console command `snd_toolvolume` to a lower value (I use 0.2)
- `!fish`
  - Fishing minigame!
### Extra setup required to work.
- `!flash`
  - Will simulate a flashbang on your client (thanks psp <3)
  - Required setup: https://gist.github.com/Pandaptable/e2212377704d198c69aab6e1b5d22e86
 
### Demo Video

[Demo](https://github.com/Pandaptable/galls/assets/80334807/7a646185-6139-43b3-8f46-de1cdbc64c6c)

## Requirements

- [Python 3.11](https://www.python.org/downloads/release/python-3119/) (only version I tested)
- [Poetry](https://python-poetry.org/)

## Installing

1. Install [Python 3.11](https://www.python.org/downloads/release/python-3119/)
2. Install [Poetry](https://python-poetry.org/)
3. Clone the repo into a folder on your computer.
4. Run `cd galls` inside of a terminal window.
5. Run `poetry install` inside of a terminal window to install dependencies.
6. Make a copy of `.env.example` and name it `.env`, edit it to contain the correct environment variables needed for the script to work.
7. Run `python main.py` inside of the project directory.

## Authors

  - [Pandaptable](https://github.com/Pandaptable)
  - [DeaFPS](https://twitter.com/deafps_) for letting me yoink her code and convert it to python... also making the fish database because [fishbase](http://www.fishbase.us/) is way too big.. ly loser <3
