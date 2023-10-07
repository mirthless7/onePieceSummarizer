import os
import pysrt

def srt_to_txt_folder(input_folder, output_folder):
    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".srt"):
            srt_file_path = os.path.join(input_folder, filename)

            # Generate corresponding output file path with .txt extension
            txt_file_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.txt")

            # Convert SRT to TXT
            srt_to_txt(srt_file_path, txt_file_path)

def srt_to_txt(srt_file_path, txt_file_path):
    # Load the SRT file
    subs = pysrt.open(srt_file_path, encoding='utf-8')

    # Create a text file and write subtitles to it
    with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
        for sub in subs:
            txt_file.write(sub.text + '\n')

if __name__ == "__main__":
    input_folder = "onePiece_ep"
    output_folder = "onePiece_ep_trans"

    srt_to_txt_folder(input_folder, output_folder)