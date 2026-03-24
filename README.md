# musicemoji
Telegram bot which updates your Telegram account status with emoji of current track

>[!NOTE]
> Granting permission relies on this simple Github Pages [webapp](https://github.com/ugliestie/emojistatuspermission) which do only that action. It's source code is open like this repo :3 

### How does this work?

When user scrobble something on Last.fm and this script enabled, user's Telegram Premium emoji status changes to cover of song they are listening to!
Sometimes Last.fm doesn't have cover for scrobble, but for this reason this script use free Deezer and iTunes API endpoints as fallback to find a cover.

This script has two modes which can be changed in `NOW_PLAYING` .env variable: 
1) Show only 'Scrobbling now'-like scrobbles and set custom emoji (`/custom_emoji`) or default star when nothing is playing 
2) Just change status to last scrobble (for scrobblers which doesn't support 'Scrobbling now')

>[!IMPORTANT]
> This is better than userbot because you can safely selfhost it everywhere without scares of stealing your Telegram account, it's just simple bot without direct access to account. Stay safe! <3

### Install
```sh
git clone https://github.com/ugliestie/musicemoji.git

cd musicemoji

pip install -r requirements.txt
```
### Settings

>Rename example.env to .env and fill up:

```sh
TOKEN="TOKEN"   # Bot token
BOT_USERNAME="USERNAME_BOT" # Bot username
USER_ID="12232111" # User ID

LAST_FM_USERNAME="" # Last.fm username
API_KEY="" # Last.fm API key
API_SECRET="" # Last.fm secret key

UPDATE_INTERVAL=15 # Time in seconds script tries to retrieve last or current track

NOW_PLAYING=False # Set True to update status only with current track and replace it to set custom emoji when nothing is playing right now
CUSTOM_EMOJI="" # When empty script sets default Premium badge when nothing playing and NOW_PLAYING set True. To fill, send /custom_emoji to bot

```
### How to use it?

- Firstly, boot the bot

```sh
python main.py
```

- After bot loading, firstly grant permission for by pressing button which bot gives you after `/start` command
- Reboot script
- Change custom emoji using `/custom_emoji` command or skip if you satisfied with default star or don't want to use `PLAYING_NOW` mode
- Profit! 
