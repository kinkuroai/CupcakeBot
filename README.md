# CupcakeBot
A Discord bot for my personal use.

I made this bot for the sole purpose of using it on my own small server and to learn more about Python. I also wanted to share it here just in case there are new people who want to get into making their own Discord bots. Take note that this is a very basic Discord bot without all the advanced programming shenanigans since it's mainly focused to have beginners like myself know that it is simple as it can be.

This bot was made using the amazing [Discord.py API](https://github.com/Rapptz/discord.py).

# To-Do
- [X] Update to make it work for Discord.py 2.0
- [X] Migrate fully to hybrid commands
- [X] Add more commands
- [X] Find a better MAL API
- [X] Switched to '[aiohttp](https://pypi.org/project/aiohttp/)' from '[requests](https://pypi.org/project/requests/)'
- [X] Add logging stuff
- [X] Switched to `TOML` from `.env`
- [X] Add command descriptions
- [ ] Add a better syncing command
- [ ] Add modals and views
- [X] Add a database
- [ ] Add economy
- [ ] Level up system
- [ ] Starboard stuff

# User Commands
* Default prefix is `?`
* >say <What you want to say> - Makes the bot say something
* >anime <title> - Searches [MyAnimeList.net](https://myanimelist.net/) for anime
* >waifu <sfw/nsfw> - Posts a random waifu picture based on your preference
* >facts - Sends a random fun fact
* >aniquote <name of character> - Posts a random quote of a specified character. If no characters are specified, it randomly grabs a quote.
* >slap <name> - Slaps someone in the server
* >wtfys <name> - WTF did he just say?
* >hug <name> - Hugs someone in the server
* >baka <name> - Calls someone baka
* >shorten <url> - Shortens a url
* >verify - Verifies your existence in the server and adds you to the database (make sure you have ran `?db create` once for this to work)

# Moderator Commands
* Default prefix is `?`
* I will be updating the commands here because most of them, discord does better.
* >kick <member> - Kicks someone off the guild
* >addrole <member> <role> - Adds a role to someone (ex: `?addrole @Member fool`)
* >remrole <member> <role> - Removes a role from someone (ex: `?remrole @Member fool`)
* >warn <member> - Gives a warning to a guild member (ex: `?warn @Member`) | **Uses DB**
* >clearwarn <member> - Removes warnings of a user | **Uses DB**

# Admin Commands
* Default prefix is `?`
* >getchaninfo - Gets the channel ID
* >changepresence <type> <status> - Changes bot's presence (ex: `?changepresence playing with my nuts`)
* >purge <amount> - Purges the messages in a channel with the specified amount
* >syncnow - Syncs commands
* >load <extension_name> - Loads specific cogs (ex: `?load cogs.anime` | `?load helpers.listener`)
* >unload <extension_name> - Unloads specific cogs (ex: `?unload cogs.anime` | `?unload helpers.listener`)
* >reload <extension_name> - Reloads specific cogs (ex: `?reload cogs.anime` | `?reload helpers.listener`)
* >reloadall - Reloads all extensions (Kinda wonky at the moment)

# Database Commands
* Default prefix is `?`
* >db - Parent command (does nothing)
* >db create - Creates the necessary database tables and entries
* >db destroy - Deletes the whole database

# Notes
* CupcakeBot relies heavily on '[tomli](https://pypi.org/project/tomli/)', '[aiohttp](https://pypi.org/project/aiohttp/)', and a number of public APIs
* You can set or define new variables in the '[config.toml.example](https://github.com/mavz42/CupcakeBot/blob/main/config.toml.example)' file and change it to your liking - just make sure you rename it to `config.toml`
* Some commands are still a work in progress since this bot is supposedly just for my personal use
* This bot is a work in progress so expect a lot of bugs

# Notes++
So yeah, there's a config file and a database. The reason why I wanted it this way is to keep easy-to-change stuff inside the `config.toml` file and some saveable stuff in the database. Dirty, bad practice, I know. But that's just me.

# Requirements
Do `pip install -r requirements.txt` in the cloned directory.

# Installation
* Clone the repo: `git clone https://github.com/mavz42/CupcakeBot.git`
* If you prefer on having a virtualenv then do it
* Go into the cloned directory and install requirements: `pip install -r requirements.txt`
* Copy `config.toml.example` and rename it to `config.toml`
* Change the values inside `config.toml`
* Run the bot: `python3 main.py`
* Default prefix is `?`
* Create database by running `?db create`. This creates the `USERS` and `BANS` tables and generates a file named `bot.db`
* If you're having some problems with the bot, create a new issue and let's sort it out