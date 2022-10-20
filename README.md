# CupcakeBot
A Discord bot for my personal use.

Updated mostly for Discord.py 2.0

* >[] Migrate fully to hybrid commands
* >[X] Add more commands
* >[X] Find a better MAL API
* >[X] Switched to 'aiohttp' from 'requests'
* >[] Add a better syncing command

# User Commands
* >say <What you want to say> - Makes the bot say something
* >anime <title> - Searches MAL for anime
* >waifu <sfw/nsfw> - Posts a random waifu picture based on your preference
* >facts - Sends a random fun fact

# Moderator Commands
* >ban <user> <reason> - Bans a user
* >unban <user> - Unbans a user | Format: Name#Discriminator
* >kick <name> <reason> - Kicks someone off the server

# Admin Commands
* >getchid <channel name> - Gets the channel ID
* >purge <amount> - Purges the messages in a channel with the specified amount
* >getbans - Sends the ban list over at the console
* >load <extension_name> - Loads specific cogs
* >unload <extension_name> - Unloads specific cogs
* >reload <extension_name> - Reloads specific cogs
* >sync <~/*/^> - Syncs commands guild-wide/globally and clears commands respectively.
