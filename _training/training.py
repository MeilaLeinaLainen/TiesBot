from transformers import LlamaForCausalLM, LlamaTokenizer, Trainer, TrainingArguments
from datasets import Dataset
import torch
from os import getcwd

name = "altered"
txt_file_path = f'{getcwd()}\\_training\\data-{name}.txt'

print("hello?")
model_name = r"H:\.llama\Llama3.2-3B"

model = LlamaForCausalLM.from_pretrained(model_name)
tokenizer = LlamaTokenizer.from_pretrained(model_name, use_fast=False)
tokenizer.pad_token = tokenizer.eos_token 

with open(txt_file_path, 'r', encoding='utf-8') as file:
    text = file.read()

print("hi?")
def tokenize_function(examples):
    return tokenizer(examples['text'], truncation=True, padding="longest", max_length=512)

dataset = Dataset.from_dict({"text": [text]})
dataset = dataset.map(tokenize_function, batched=True, remove_columns=["text"])

training_args = TrainingArguments(
    output_dir="./llama-finetuned-models",
    overwrite_output_dir=True,
    num_train_epochs=10,
    per_device_train_batch_size=1, 
    save_steps=500,
    logging_dir="./logs",
    logging_steps=100,
    do_train=True,
    prediction_loss_only=True,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
)

print("train")
trainer.train()

trainer.save_model(f"./llama-finetuned-models/llama-3.2-{name}")
tokenizer.save_pretrained(f"./llama-finetuned-models/llama-3.2-{name}")
