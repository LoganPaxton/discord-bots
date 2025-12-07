# Discord Ticket Bot

A simple, clean ticket system built using `discord.py` and Discord slash commands.  
Users can open support tickets, and staff can manage or close them easily.

---

## 🚀 Features

- `/ticket` command to open a support ticket  
- Tickets auto-create inside a dedicated category  
- Private channels — only the user + staff can view  
- “Close Ticket” button inside each ticket  
- Prevents duplicate tickets  
- Simple and lightweight  

---

## 📁 Project Structure

ticket-bot/  
├── main.py  
├── .env  
├── requirements.txt  
└── README.md  

## 🔧 Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
````

### 2. Configure Environment Variables

Modify the file named `.env` to include this content, replacing the your token here with your actual bot token.

```
BOT_TOKEN=YOUR_TOKEN_HERE
```

⚠️ **Never hard-code your bot token in the code.**

---

## 🛠 Configuration

Inside `bot.py`, set:

* `TICKET_CATEGORY_ID` — ID of the category where ticket channels will be created.
* `STAFF_ROLE_ID` — Role that should have access to all tickets.

Example:

```python
TICKET_CATEGORY_ID = 123456789012345678
STAFF_ROLE_ID = 987654321098765432
```

---

## ▶️ Running the Bot

Start the bot with:

```bash
python main.py
```

If everything is configured correctly, you’ll see:

```
Logged in as YourBotName
Synced X command(s)
```

---

## 🧪 Usage

### Open a ticket

Type:

```
/ticket
```

The bot will:

* Create a private ticket channel named `ticket-<userID>`
* Allow only the ticket opener and staff to view the channel
* Send a message with a **Close Ticket** button

### Close a ticket

Click the **Close Ticket** button and the bot deletes the channel.

---

## ❗ Notes

* Users can only have **one ticket open at a time**.
* Staff channels are determined by `STAFF_ROLE_ID`.
* The bot requires `Manage Channels` permission to function.

---

## 📜 License

This project is licensed under the MIT License.
