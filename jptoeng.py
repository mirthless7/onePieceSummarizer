from translate import Translator
import os

def translate_text(input_text, target_language='en'):
    translator = Translator(to_lang=target_language)
    try:
        translation = translator.translate(input_text)
        return translation
    except Exception as e:
        print(f"Translation error: {e}")
        return None

def translate_file(input_file_path, output_file_path, target_language='en'):
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        japanese_text = input_file.read()

    translated_text = translate_text(japanese_text, target_language)

    if translated_text is not None:
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(translated_text)
        print(f"Translation successful: {input_file_path} -> {output_file_path}")
    else:
        print(f"Translation failed for: {input_file_path}")

def translate_folder(input_folder, output_folder, target_language='en'):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            input_file_path = os.path.join(input_folder, filename)
            output_file_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_trans.txt")

            translate_file(input_file_path, output_file_path, target_language)

if __name__ == "__main__":
    input_folder = "onePiece_ep_trans"
    output_folder = "onePiece_ep_eng"

    translate_folder(input_folder, output_folder)