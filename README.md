# Introducing TiesBot
**Multi-Use Discord Bot specifically for TiesKey's FreeBuild Server.**
Developed by @meilaleinalainen ;)

## Hosting
Currently TiesBot is not being hosted 24/7, instead it is hosted whenever @meilaleinalainen is working on it, or just idling. This will change in the future however when there are more features.

## Usage
### Manager-Only Commands
| `/echo (message: str, channel: discord.TextChannel, copy: bool = False, delete_origin: bool = False)` | Send a message with @TiesBot |
|----------|----------|----------|
| `message: str` | Required. The message to send. If `copy` is True, input the message ID here. |
| `channel: discord.TextChannel` | Optional, defaults to the channel the command is used in. Use #channel format. |
| `copy: bool = False` | Optional, defaults to False. Whether to copy an already sent message. |
| `delete_origin: bool = False` | Optional, defaults to False. Whether to delete the message to copy. |


`/edit (old_message: str, new_message: str, is_id: bool = False, delete_origin: bool = False)` - Edit a message sent by @TiesBot
**Args:**
- `old_message: str` - Required. The message to edit to. If `is_id` is True, this shouldbe a message ID.
- `new_message: str` - Required. The message ID to edit. (HAS TO BE SENT BY @TiesBot)
- `is_id: bool = False` - Optional, defaults to False. Whether `new_message` is a message ID or not.
- `delete_origin: bool = False` - Optional, defaults to False. Whether to delete the original message to avoid the "(edited)

### Public Commands
`/github`  - Send the GitHub link to @meilaleinalainen's source-code.
