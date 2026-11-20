def word_frequency_analyzer(text:str , top=10):
    dictionary = {}
    words_list = text_cleaner(text)
    for word in words_list:
        dictionary[word] = dictionary.get(word,0) + 1
        desc = {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1],reverse=True)}
    print(desc)


def text_cleaner(text:str):
    specials = [".",",","\n","\t"]
    text = text.strip()
    for special in specials :
        if special == "\n":
            text = text.replace(special," ")    
        text = text.replace(special,"")
    return text.lower().split(" ")


if __name__ == "__main__":
    with open("sample.txt","r") as file:
        text  = file.read()
        result  = word_frequency_analyzer(text)
