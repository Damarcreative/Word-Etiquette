# Discord chat censorship
## Description
Censorship Bot for Discord is a Python program that aims to filter messages containing sensitive words on Discord servers. This program uses the discord.py library to interact with the Discord API and filter messages received by bots.

## Installation
To run this program, you need Python 3 and some of the required libraries, namely:
- discord

You can install the discord.py library using pip:
```sh
pip install discord.py
```
## How to use
- Create a bot on the Discord developer page and earn your bot tokens.
- Tambahkan bot ke server Discord Anda.
- Copy your bot token and paste it in the program code in the line ` client.run('TOKEN')`
- Run the program by running the command `python main.py`

## Ways of working
This program uses the `discord.Client` class to create an instance of the bot and connect to the Discord server. Then, the program uses `client.event` to determine the action to be performed when an event is received from the Discord server.

In this program, the event used is `on_message` to handle messages received by bots. When a message is received, the program will filter the message using the specified list of sensitive words.

If the message contains sensitive words, the program will delete the message and notify the message sender that the message has been deleted.
## Contribution
If you'd like to contribute to the program, feel free to submit a pull request or create a new issue on the GitHub repository.
## Lisensi
This program uses the MIT license. Please read the LICENSE file for more information.
## Contact
If you have any questions or concerns regarding this program, please contact us via [email](mailto:dev@damarcreative.my.id).


