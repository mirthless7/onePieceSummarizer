from googletrans import Translator, constants
from pprint import pprint

translator = Translator()

translation = translator.translate("この世の全てを手に入れた男 海賊王 ゴールド･ロジャー", src = "ja")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")