from googletrans import Translator
sentence = str(input("Sentence:"));
translator = Translator();
translated_sentence = translator.translate(sentence,src='en',dest='language to be which the sentence should be translated');
print(translated_sentence.text);
