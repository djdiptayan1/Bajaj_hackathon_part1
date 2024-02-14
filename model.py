from transformers import T5Tokenizer, T5ForConditionalGeneration

model = T5ForConditionalGeneration.from_pretrained("Voicelab/vlt5-base-keywords")
tokenizer = T5Tokenizer.from_pretrained("Voicelab/vlt5-base-keywords")

task_prefix = "Keywords: "
inputs = [
    """
    # TEXT GOES HERE
""",
]

for sample in inputs:
    input_sequences = [task_prefix + sample]
    input_ids = tokenizer(
        input_sequences, return_tensors="pt", truncation=True
    ).input_ids
    output = model.generate(input_ids, no_repeat_ngram_size=3, num_beams=4)
    predicted = tokenizer.decode(output[0], skip_special_tokens=True)
    print(sample, "\n --->", predicted)
