# CupcakeBot
A Discord bot for my personal use.

I made this bot for the sole purpose of using it on my own small server and to learn more about Python. I also wanted to share it here just in case there are new people who want to get into making their own Discord bots. Take note that this is a very basic Discord bot without all the advenced programming shenanigans since it's mainly focused to have beginners like myself know that it is simple as it can be.

This bot was made using the amazing [Discord.py API](https://github.com/Rapptz/discord.py).

# To-Do
- [ ] Migrate fully to hybrid commands
- [X] Add more commands
- [X] Find a better MAL API
- [X] Switched to 'aiohttp' from 'requests'
- [ ] Add a better syncing command
- [ ] Fix README

# User Commands
* >say <What you want to say> - Makes the bot say something
* >anime <title> - Searches MAL for anime
* >waifu <sfw/nsfw> - Posts a random waifu picture based on your preference
* >facts - Sends a random fun fact
* >aniquote <name of character> - Posts a random quote of a specified character. If no characters are specified, it randomly grabs a quote.


# Moderator Commands
* I will be updating the commands here because most of them, discord does better.

# Admin Commands
* >getchaninfo - Gets the channel ID
* >purge <amount> - Purges the messages in a channel with the specified amount
* >syncnow - Syncs commands
* >load <extension_name> - Loads specific cogs (ex: ?load cogs.anime | ?load helpers.listener)
* >unload <extension_name> - Unloads specific cogs (ex: ?unload cogs.anime | ?unload helpers.listener)
* >reload <extension_name> - Reloads specific cogs (ex: ?reload cogs.anime | ?reload helpers.listener)

# Notes
* >CupcakeBot relies heavily on 'dotenv' and 'aiohttp'. You can set various variables in the '.env.example' file and change it to your liking - just make sure you rename it to '.env'.
* >Some commands are still a work in progress since this bot is supposedly just for my personal use.

# Requirements
To do

# Usage
To do

