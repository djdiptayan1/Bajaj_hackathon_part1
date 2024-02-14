from transformers import T5Tokenizer, T5ForConditionalGeneration

model = T5ForConditionalGeneration.from_pretrained("Voicelab/vlt5-base-keywords")
tokenizer = T5Tokenizer.from_pretrained("Voicelab/vlt5-base-keywords")

task_prefix = "Keywords: "
inputs = [
    """
Education Loan - How to get Student Loan for Abroad Study | Bajaj Finserv
How to get an Education Loan
How to get an education loan?
How to apply for an education loan against property?
Related videos
Loan of up to Rs. 3 crores against property in just 4 days
Things You Need to Know Before Applying for a Loan Against Property
Calculate your EMIs : Loan Against Property EMI Calculator
How to apply for a Loan Against Property?
Please wait
Application Forms
Products Portfolio
Loans
Insurance
Finance for Professionals
Investments
Pocket Subscription
Bajaj Mall
Services
Wallets & Cards
Value Added Services
Bills & Recharges
Calculators
Legal
Reach Us
Corporate Office
Bajaj Finance Limited Regd. Office
Corporate Identity Number (CIN)
IRDAI Corporate Agency (Composite) Regn No.
URN - WEB/BFL/23-24/1/V1
Bajaj Finserv Limited Regd. Office
Corporate Identity Number (CIN)
Our Companies
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
