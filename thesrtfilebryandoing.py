import pysrt

srt_path='M:\Python\onePieceSummarizer\onePiece_ep'
def srt_to_txt(srt_path, txt_file_path'):
    # Load the SRT file
    subs = pysrt.open(srt_file_path, encoding='utf-8')

    # Create a text file and write subtitles to it
    with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
        for sub in subs:
            txt_file.write(sub.text + '\n')

if name == "main":
    srt_file_path = "path/to/your/input_file.srt"
    txt_file_path = "path/to/your/output_file.txt"

    srt_to_txt(srt_file_path, txt_file_path)