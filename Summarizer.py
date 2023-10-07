import requests
from transformers import BartForConditionalGeneration, BartTokenizer

# Function to fetch text from a URL
def fetch_text_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from URL: {e}")
        return None

# Function to summarize text
def summarize_text(input_text, max_length=150):
    try:
        # Initialize the model and tokenizer
        model_name = "facebook/bart-large-cnn"
        tokenizer = BartTokenizer.from_pretrained(model_name)
        model = BartForConditionalGeneration.from_pretrained(model_name)

        # Tokenize the input text
        inputs = tokenizer(input_text, return_tensors="pt", max_length=max_length, truncation=True)

        # Generate the summary
        summary_ids = model.generate(inputs["input_ids"], max_length=50, min_length=10, length_penalty=2.0, num_beams=4, early_stopping=True)

        # Decode the summary
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary
    except Exception as e:
        print(f"Error summarizing text: {e}")
        return None

if __name__ == "__main__":
    url = input("Enter the URL of the text you want to summarize: ")
    text = fetch_text_from_url(url)

    if text:
        summary = summarize_text(text)

        if summary:
            print("Summary:")
            print(summary)