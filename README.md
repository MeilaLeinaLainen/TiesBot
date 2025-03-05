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

`/edit (old_message: str, new_message: str, is_id: bool = False, delete_origin: bool = False)` - Edit a message sent by @TiesBot
**Args:**
`old_message: str` - Required. The message to edit to. If `is_id` is True, this shouldbe a message ID.
`new_message: str` - Required. The message ID to edit. (HAS TO BE SENT BY @TiesBot)
`is_id: bool = False` - Optional, defaults to False. Whether `new_message` is a message ID or not.
`delete_origin: bool = False` - Optional, defaults to False. Whether to delete the original message to avoid the "(edited)

### Public Commands
`/github`  - Send the GitHub link to @meilaleinalainen's source-code.