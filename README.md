<h2 align="center">
   Install Locally Or On A VPS
</h2>


```console
shikhar@MacBook~ $ git clone https://github.com/LOGI-LAP/music-bot
shikhar@MacBook~ $ cd music-bot
shikhar@MacBook~ $ pip3 install -U -r requirements.txt
shikhar@MacBook~ $ cp sample.env .env
```

<h3 align="center">
    Edit <b>.env</b> with your own values and Run Bot
</h3>

```console
shikhar@MacBook~ $ bash start
```


<h2 align="center">
   Generating Pyrogram Session
</h2>

<p align="center">
<a href="https://replit.com/@AaravxD/PyroStringSession#main.py"><img src="https://img.shields.io/badge/Generate%20On%20Repl-blueviolet?style=for-the-badge&logo=appveyor" width="245""/></a>
 </p>  

<h3 align="center">
    OR
</h3>

```console
shikhar@MacBook~ $ git clone https://github.com/LOGI-LAP/music-bot
shikhar@MacBook~ $ cd music-bot
shikhar@MacBook~ $ pip3 install pyrogram TgCrypto
shikhar@MacBook~ $ python3 gen_session.py
```


<h2 align="center">
   Config Vars
</h2>

1. `API_ID` : Assistant Account Telegram API_ID, get it from my.telegram.org
2. `API_HASH` : Assistant Account Telegram API_HASH, get it from my.telegram.org
3. `BOT_TOKEN` : Your Telegram Bot Token, get it from @Botfather (Make sure Inline is turned On)
4. `SESSION_STRING` : Pyrogram Session String of Assistant Account.
5. `MUSIC_BOT_NAME` : A name for your Music bot.
6. `MONGO_DB_URI` : MongoDB Database URL.
7. `LOG_GROUP_ID` : Chat ID where bot will log everything. Use Group Chats Only.
8. `DURATION_LIMIT` : Duration Limit for Music (Mins)
9. `SUDO_USERS` : Sudo Users for Bot. (For multiple users seperate IDs with space)
10. `OWNER_ID`: Owner ID of Bot
11. `SUPPORT_GROUP` : Support Group Link (Leave blank if you don't have one)
12. `SUPPORT_CHANNEL` : Support Channel Link ( Leave blank if you don't have one)
13. `ASSISTANT_PREFIX` : Prefix for Assistant Commands
