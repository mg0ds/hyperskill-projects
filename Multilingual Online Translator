import requests
import argparse

from bs4 import BeautifulSoup


def nmb_to_lang(nmb):
    if nmb == "1":
        return "arabic", 1
    elif nmb == "2":
        return "german", 1
    elif nmb == "3":
        return "english", 1
    elif nmb == "4":
        return "spanish", 1
    elif nmb == "5":
        return "french", 1
    elif nmb == "6":
        return "hebrew", 1
    elif nmb == "7":
        return "japanese", 1
    elif nmb == "8":
        return "dutch", 1
    elif nmb == "9":
        return "polish", 1
    elif nmb == "10":
        return "portuguese", 1
    elif nmb == "11":
        return "romanian", 1
    elif nmb == "12":
        return "russian", 1
    elif nmb == "13":
        return "turkish", 1
    elif nmb == "0":
        return ["arabic", "german", "english", "spanish", "french", "hebrew", "japanese", "dutch", "polish", "portuguese", "romanian", "russian", "turkish"], 13


def translations(src_lang, trg_lang, lang_no, word, src_lang_nmb):
    #src_lang_nmb is used in not-argparse version
    i = 0
    if lang_no == 1: # how many example lines there will be
        exmpl_no = 5
        aaa = 1
    else:
        exmpl_no = 1
        aaa = 12

    for ln in range(aaa):
        word_translation = []  # single word translation
        sentence_src_list = []  # source language sentence example
        sentence_trg_list = []  # target language sentence example
        sentences_comb = []  # source > target sentence example

        """if i == (int(src_lang_nmb) - 1): #this if is used for not-argparse version
            i += 1"""

        if lang_no == 1:
            bbb = trg_lang
        else:
            bbb = trg_lang[i]

        url = "http://context.reverso.net/translation/" + src_lang + "-" + bbb + "/" + word
        r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        """if r.status_code == 200: #this if prints only 200 status code for connection
            print("200 OK")
        else:
            print("Something wrong, status:" + str(r.status_code))"""

        soup = BeautifulSoup(r.content, 'html.parser')
        translations = soup.find_all('div', {"id": "translations-content"})  # single word translation
        sentences_src = soup.find_all("div", {"class": "src ltr"})  # source language sentence example
        if bbb == "arabic":
            sentences_trg = soup.find_all("div", {"class": "trg rtl arabic"})  # target language sentence example
        elif bbb == "hebrew":
            sentences_trg = soup.find_all("div", {"class": "trg rtl"})  # target language sentence example
        else:
            sentences_trg = soup.find_all("div", {"class": "trg ltr"})  # target language sentence example

        for poz in translations:
            t = poz.text
            word_translation = t.split()

        for poz in sentences_src:
            a = poz.text
            b = a.replace("\n", "")
            sentence_src_list.append(b.lstrip(" "))

        for poz in sentences_trg:
            a = poz.text
            b = a.replace("\n", "")
            sentence_trg_list.append(b.lstrip(" "))

        for poz in range(len(sentence_src_list)):
            sentences_comb.append(sentence_src_list[poz])
            sentences_comb.append(sentence_trg_list[poz])

        f.write("\n")
        print()
        f.write("\n{} Translations:".format(bbb.capitalize()))
        print("{} Translations:".format(bbb.capitalize()))
        for row in range(exmpl_no):
            f.write("\n")
            f.write(word_translation[row])
            print(word_translation[row])
        f.write("\n")
        print()
        f.write("\n{} Examples:".format(bbb.capitalize()))
        print("{} Examples:".format(bbb.capitalize()))
        for row in range(exmpl_no):
            f.write("\n")
            f.write(sentence_src_list[row])
            print(sentence_src_list[row])
            f.write("\n")
            f.write(sentence_trg_list[row])
            print(sentence_trg_list[row])
            f.write("\n")
            print()
        i += 1


parser = argparse.ArgumentParser(description="Multilanguage translator")
#argparse with choice parameter
"""
parser.add_argument("src_lang", choices=["arabic", "german", "english", "spanish", "french", "hebrew", "japanese",
                                         "dutch", "polish", "portuguese", "romanian", "russian", "turkish"],
                    help="Source language")
parser.add_argument("trg_lang", choices=["arabic", "german", "english", "spanish", "french", "hebrew", "japanese",
                                         "dutch", "polish", "portuguese", "romanian", "russian", "turkish", "all"],
                    help="Target language")
"""


parser.add_argument("src_lang", help="Source language")
parser.add_argument("trg_lang", help="Target language")
parser.add_argument("word", help="Word to translate.")
args = parser.parse_args()

#version without argparse, need to input source language, terget language and word manualy after program starts
"""
print(Hello, you're welcome to the translator. Translator supports: 
1. Arabic
2. German
3. English
4. Spanish
5. French
6. Hebrew
7. Japanese
8. Dutch
9. Polish
10. Portuguese
11. Romanian
12. Russian
13. Turkish
Type the number of your language: )
src_lang_nmb = input()
src_lang = nmb_to_lang(src_lang_nmb)

print("Type the number of a language you want to translate to or '0' to translate to all languages:")
trg_lang_nmb = input()
trg_lang = nmb_to_lang(trg_lang_nmb)

print("Type the word you want to translate:")
word = input()


file_name = word + ".txt"
f = open(file_name, "a", encoding="utf-8")
translations(src_lang[0], trg_lang[0], trg_lang[1], word, src_lang_nmb)
f.close()
"""


#argparse version
all_l = ["arabic", "german", "english", "spanish", "french", "hebrew", "japanese", "dutch", "polish", "portuguese",
         "romanian", "russian", "turkish"]
try:
    file_name = args.word + ".txt"
    f = open(file_name, "a", encoding="utf-8")
    if args.trg_lang == "all":
        all_l.pop(all_l.index(args.src_lang))
        translations(args.src_lang, all_l, 12, args.word, 6) # 6 as the last argument is only placeholder for argparse version, can be any number
    else:
        translations(args.src_lang, args.trg_lang, 1, args.word, 6) # 6 as the last argument is only placeholder for argparse version, can be any number
    f.close()

except IndexError:
    #print(e)
    #print(args.src_lang)
    #print(args.trg_lang)
    #print(args.word)
    if args.src_lang != "all" and args.trg_lang != "all":
        if args.src_lang not in all_l:
            print("Sorry, the program doesn't support " + args.src_lang)
        elif args.trg_lang not in all_l:
            print("Sorry, the program doesn't support " + args.trg_lang)
    else:
        print("Sorry, unable to find " + args.word)
except requests.exceptions.ConnectionError:
        print("Something wrong with your internet connection")
