# Introducing TiesBot

**A Multi-Use Discord Bot specifically for TiesKey's FreeBuild Server.**\
Developed by @meilaleinalainen ;)

---

## Hosting

TiesBot is not currently hosted 24/7. Instead, it runs whenever @meilaleinalainen is actively working on it or idling. This will change in the future as more features are added.

---

## Usage
### Manager-Only Commands

#### `/echo (message: str, channel: discord.TextChannel, copy: bool = False, delete_origin: bool = False)`

Send a message using @TiesBot.

**Arguments:**

- `message: str` *(Required)* – The message to send. If `copy` is `True`, input the message ID here.
- `channel: discord.TextChannel` *(Optional, defaults to the command's channel)* – Use the `#channel` format.
- `copy: bool = False` *(Optional, defaults to False)* – Whether to copy an already sent message.
- `delete_origin: bool = False` *(Optional, defaults to False)* – Whether to delete the original message after copying.

---

#### `/bulk-echo (message: str, channel: discord.TextChannel, copy: bool = False)`

Bulk-send up to 10 messages using @TiesBot.

**Arguments:**

- `message: str` *(Required)* – Message to send. If `copy` is True, input the message ID here. Separate messages with a comma (no spaces).
- `channel: discord.TextChannel` *(Optional, defaults to the command's channel)* – Use the `#channel` format.
- `copy: bool = False` *(Optional, defaults to False)* – Whether to copy an already sent message.

---

#### `/edit (old_message: str, new_message: str, is_id: bool = False, delete_origin: bool = False)`

Edit a message sent by @TiesBot.

**Arguments:**

- `old_message: str` *(Required)* – The message to edit. If `is_id` is `True`, this should be a message ID.
- `new_message: str` *(Required)* – The new message content. *(Must be sent by @TiesBot.)*
- `is_id: bool = False` *(Optional, defaults to False)* – Whether `old_message` is a message ID.
- `delete_origin: bool = False` *(Optional, defaults to False)* – Whether to delete the original message to avoid the "(edited)" tag.

---

### Public Commands

#### `/github`

Sends the GitHub link to @meilaleinalainen's source code.

#### `/replit`

Sends the Replit link to @TiesBot's hosting.

---

