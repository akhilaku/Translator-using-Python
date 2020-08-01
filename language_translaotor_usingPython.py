#importing Translator from googletrans.
from googletrans import Translator
#giving the input sentence which need to be translated.
sentence = str(input("Sentence:"));
#translator
translator = Translator();
#translating a sentence
translated_sentence = translator.translate(sentence,src='en',dest='language to be which the sentence should be translated');
#to print the translated sentence.
print(translated_sentence.text);
