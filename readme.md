## WaterBot - A water reminder discord bot <br>

WaterBot is a simple discord bot script to send direct messages to a user, as to remind them to drink enough water. Currently, it is very simple and offers just the baseline functionalities needed. 

### Built with
[![Python][python]][python-url]

### Getting started
- Python (at least v3.8.0, built with v3.12.0)
- discord.py | `pip install discord.py`

### Usage
If you just want to use the bot just for yourself, there is very little to do. If you instead intend on messaging more than one user, you'll need to fork and rework this code.

### Features
- The bot is able to send a direct message to one specified user.
    - The message reads "Don't forget to drink water! 💧".
    - The message will be send once at startup, then every 30 minutes after.
    - The bot will delete its previously sent message, before sending a new one.
        - This will help keep the chat clean.
    - The message can also be triggered by sending the message "debug" to the bot.
- All these values can be easily edited inside the config file.


### How to setup
1. Go to the [Discord Developer Portal][discord-dev-portal-url].
2. Create an Application.
    1. (And potentially note the Bot Token. If it was not displayed yet, don't worry about it.)
3. Invite the bot to a server of yours.
    1.You can follow [this tutorial][bot-adding-tutorial] as guidance.
4. In the script, add your User ID and Bot Token.
    1. Here is a [short tutorial][user-id-tutorial] how to get your User ID.
    2. If you could copy your Bot Token already, just insert it. If not, open the application on the discord dev portal and head to the bot submenu. There, click on reset token and copy paste it into the script.  
5. Run the script with `python script_name.py`.

The bot only runs if the script is running. If you want the bot to run as long as your machine is running, you might want to add the script to your startup applications.
I've provided easy to configure `.sh` and `.bat` scripts in the startup_scripts folder for this purpose. Just replace the filepath and add it to startup, then it should run.

<!--Links and Images-->
[python]:https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[python-url]:https://www.python.org/
[discord-dev-portal-url]:https://discord.com/developers/applications
[bot-adding-tutorial]:https://discordpy.readthedocs.io/en/stable/discord.html#inviting-your-bot
[user-id-tutorial]:https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-