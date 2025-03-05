import discord, logging, asyncio
from discord.ext import commands
from discord import app_commands

from transformers import LlamaForCausalLM, LlamaTokenizer
import torch

class TiesBotAi(commands.Cog):
    def __init__(self, client):
        self.client = client
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
        
        self.model_path = r"H:\.llama\Llama3.2-3B"
        self.tokenizer = LlamaTokenizer.from_pretrained(self.model_path)
        self.model = LlamaForCausalLM.from_pretrained(self.model_path, torch_dtype=torch.float16).cuda()
        self.model.config.pad_token_id = self.tokenizer.pad_token_id or self.tokenizer.eos_token_id
        self.conversation_history = []

    def update_conversation_history(self, role, content):
        self.conversation_history.append({"role": role, "content": content})
        if len(self.conversation_history) > 10:
            self.conversation_history.pop(0)

    def chat_with_llama(self, user_input, max_length=200):
        prompt = f"User: {user_input}\nBot:"
        input_ids = self.tokenizer(prompt, return_tensors="pt", padding=True, truncation=True).input_ids.cuda()

        output = self.model.generate(
            input_ids,
            max_length=max_length,
            num_return_sequences=1,
            temperature=0.7,
            top_p=0.95,
            top_k=60,
            do_sample=True
        )

        response = self.tokenizer.decode(output[0], skip_special_tokens=True)
        response = response[len(prompt):].strip()
        return response

    @app_commands.command(name="ask", description="Ask TiesBot-Ai something")
    @app_commands.describe(message="What do you want to say to TiesBotAi")
    async def ask_ai(self, interaction: discord.Interaction, message: str):
        try:
            await interaction.response.defer()
            self.update_conversation_history("User", message)
            
            loop = asyncio.get_running_loop()
            response = await loop.run_in_executor(None, self.chat_with_llama, message)

            self.update_conversation_history("Bot", response)
            await interaction.followup.send(response)
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            await interaction.followup.send("An error occurred while generating the response.")

