# Message of the Day Discord Bot
This Discord bot sends a message to a specific Discord channel every day at the same hour.
## Requirements
- Python
- [Discord.py](https://discordpy.readthedocs.io/en/stable/)
## Usage
1. Set up your bot's token in the **TOKEN** variable.
2. Set up the target channel to send the message in the **channel_id** variable. (Make sure that your bot is on the server and has rights to send messages to the channel)
3. Write some sentences to send each day.
4. Change the hour to send the messages (Default: 7 AM UTC)
5. Run the script and leave it running.
## Notes
The code of this script was not designed by me, I just stitched together a couple of snippets I found online. Leaving this here in case someone needs it.
In addition, it might be interesting to point out that there are a great number of more feature rich Discord bots around that also implement the simple feature of this bot here. I made this quickly because I wanted a dedicated bot that only does this.
## To-do and possible enhancements
Currently the target channel and the messages are hard-coded in the script. It would be far more elegant to be able to set them at runtime from a user command, for example.