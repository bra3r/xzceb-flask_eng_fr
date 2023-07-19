'''import the translation function'''
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    #write the code here
    '''english to french translation'''
    french_text=MyMemoryTranslator(source='english',target='french').translate(english_text)
    return french_text

def french_to_english(french_text):
    #write the code here
    '''french to english translation'''
    english_text=MyMemoryTranslator('french','english').translate(french_text)
    return english_text
