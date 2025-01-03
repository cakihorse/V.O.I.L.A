from transformers import BartTokenizer
from datasets import load_dataset


dataset = load_dataset('csv', data_files={
    'train': 'fine_tunning_summerizer/data/train.csv',
    'validation': 'fine_tunning_summerizer/data/test.csv'
})
print(dataset)






import argparse
from datasets import load_dataset
from transformers import BartTokenizer, BartForConditionalGeneration, Trainer, TrainingArguments, DataCollatorForSeq2Seq

# 📝 1. Parser les arguments
parser = argparse.ArgumentParser()
parser.add_argument('--model_name_or_path', type=str, required=True)
parser.add_argument('--train_file', type=str, required=True)
parser.add_argument('--validation_file', type=str, required=True)
parser.add_argument('--text_column', type=str, default='text')
parser.add_argument('--summary_column', type=str, default='summary')
parser.add_argument('--output_dir', type=str, required=True)
parser.add_argument('--per_device_train_batch_size', type=int, default=4)
parser.add_argument('--per_device_eval_batch_size', type=int, default=4)
parser.add_argument('--overwrite_output_dir', action='store_true')
parser.add_argument('--predict_with_generate', action='store_true')
parser.add_argument('--num_train_epochs', type=int, default=3)
parser.add_argument('--evaluation_strategy', type=str, default='epoch')
args = parser.parse_args()

# 📊 2. Charger les données
dataset = load_dataset('csv', data_files={
    'train': args.train_file,
    'validation': args.validation_file
})

# 🔄 3. Prétraitement avec le tokenizer
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
def preprocess_function(examples):
    inputs = [doc for doc in examples['text']]
    targets = [doc for doc in examples['summary']]
    model_inputs = tokenizer(inputs, max_length=1024, truncation=True)
    labels = tokenizer(targets, max_length=128, truncation=True)
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

tokenized_datasets = dataset.map(preprocess_function, batched=True)

# 🤖 4. Charger le modèle BART
model = BartForConditionalGeneration.from_pretrained(args.model_name_or_path)

# 📦 5. Configurer le Data Collator
data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)

# ⚙️ 6. Définir les arguments d'entraînement
training_args = TrainingArguments(
    output_dir=args.output_dir,
    evaluation_strategy=args.evaluation_strategy,
    learning_rate=2e-5,
    per_device_train_batch_size=args.per_device_train_batch_size,
    per_device_eval_batch_size=args.per_device_eval_batch_size,
    num_train_epochs=args.num_train_epochs,
    weight_decay=0.01,
    overwrite_output_dir=args.overwrite_output_dir,
    save_total_limit=1,
    save_strategy='epoch'
)

# 🚀 7. Initialiser Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets['train'],
    eval_dataset=tokenized_datasets['validation'],
    tokenizer=tokenizer,
    data_collator=data_collator
)

# 🏋️‍♂️ 8. Lancer l'entraînement
trainer.train()

# 💾 9. Sauvegarder le modèle fine-tuné
trainer.save_model(args.output_dir)
tokenizer.save_pretrained(args.output_dir)



