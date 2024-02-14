from transformers import T5Tokenizer, T5ForConditionalGeneration
import json
import urllib.parse

# Load your JSON file
with open("output.json", "r", encoding="utf-8") as json_file:
    data_list = json.load(json_file)["results"]

# T5 model setup
model = T5ForConditionalGeneration.from_pretrained("Voicelab/vlt5-base-keywords")
tokenizer = T5Tokenizer.from_pretrained("Voicelab/vlt5-base-keywords")

# Iterate over each entry in the JSON file
for data in data_list:
    # Extract title and h_tags from the current entry
    url = data["url"]
    title = data["meta"]["title"]
    h_tags = " ".join(data["meta"]["h_tags"])  # Combine h_tags into a single string

    # Parse the URL
    parsed_url = urllib.parse.urlparse(url)
    # Extract path (everything after base URL)
    path = parsed_url.path.strip("/")
    # Split path by "/" and remove empty elements
    url_keywords = [keyword for keyword in path.split("/") if keyword]

    # Construct input sequence
    task_prefix = "Keywords: "
    # input_text = f"{task_prefix} {title} {h_tags}"
    input_text = f"{task_prefix} {url} {title}"

    # Generate keywords using T5 model
    input_ids = tokenizer(input_text, return_tensors="pt", truncation=True).input_ids
    output = model.generate(input_ids, no_repeat_ngram_size=3, num_beams=4)
    predicted_keywords = tokenizer.decode(output[0], skip_special_tokens=True)

    # Print the original title, h_tags, and predicted keywords for each entry
    print("URL:", data["url"])
    print("Title:", title)
    # print("H Tags:", h_tags)
    print("URL Keywords:", url_keywords)
    print("Predicted Keywords:", predicted_keywords)
    print("------")
