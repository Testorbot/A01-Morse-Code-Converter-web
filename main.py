from flask import Flask, render_template, request
app = Flask(__name__)


morse_code = {
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-",
  ":":"---...",
  ";":"-.-.-.",
  "'":".----.",
  "&":".--...",
  "_":"..--.-",
  "=":"-...-",
  "+":".-.-.",
  "-":"-....-",
  "/":"-..-.",
  '"':'.-..-.',
  "$":"...-..-",
  " ":".......",
}


def encode_to_morse_code(words):
    words_morse = ""
    for letter in words.lower():
      words_morse += f"{morse_code[letter]} "
    return words_morse


def decode_from_morse_code(codes):
    code_words = ""
    for indv_code in codes.split():
      for letter, m_code in morse_code.items():
        if m_code == indv_code:
          code_words += letter
    return code_words.capitalize()


@app.route('/morse', methods=["GET","POST"])
def morse():
  words = request.form["words"]
  words_to_morse = encode_to_morse_code(words)
  return render_template('index.html',words_to_morse=words_to_morse)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
