# telegram-garage-opener
A garage opener based on a Raspberry Pi with a telegram chatbot.
An Pi Camera is also implemented to take a picture and check the status of the garage doors.
When you send the telegram bot the command: "Pic", it'll take a picture and send it to you.

## Needed: 
Install tg-bot.

Add your bot id in the script.

Pi Camera if you want to use the "Pic" command.

Relais connected to the Pi to control the garage.

## For running the telegram bot:
sudo python3 telegram-bot.py

## For running the telegram bot on startup:
command:
sudo nano /etc/rc.local

add "python3 /path/to/telegram-bot.py &" in the next line after "fi" in the file.

## Commands:
"Left door": opens left door using GPIO 3

"Right door": opens right door using GPIO 2

"Hi","What's the time", ...


