from googletrans import Translator

translator = Translator()


des = input('choose a language: ')
txt = '''Hello my name is Edwin, how are you?'''

out = translator.translate(txt, dest=des)
print(out.text)
