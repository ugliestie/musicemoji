# musicemoji
Telegram bot which updates your Telegram accout status with emoji of current track

### Install
```sh
git clone https://github.com/ugliestie/musicemoji.git

cd musicemoji

pip install -r requirements.txt
```
### Settings

>Rename example.env to .env и fill up:

```sh
TOKEN="TOKEN"   # Bot token
BOT_USERNAME="USERNAME_BOT" # Bot username
USER_ID="12232111" # User ID

LAST_FM_USERNAME="" # Last.fm username
API_KEY="" # Last.fm API key
API_SECRET="" # Last.fm secret key

UPDATE_INTERVAL="15"

```
### How to use it?

- Firstly, boot the bot

```sh
python main.py
```

- After bot loading, firstly grant permission for by pressing button which bot gives you after `/start` command
- After granting send `/update` command
- Profit! 