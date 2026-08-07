fh = open('books-languages.txt') #warning: ugly coding for educational purposes
content = fh.readlines()
unique = []
for lang in content:
    lang = lang.strip()
    if not lang in unique:
        unique.append(lang)
print(unique)
fh.close()
fh = open('books-languages.txt')
content = fh.readlines()
langdict = {}
for lang in content:
    lang = lang.strip()
    if lang in langdict:
        langdict[lang] += 1
    else:
        langdict[lang] = 1
print(repr(langdict))
fh.close()

#improve this code
#first step: deduplication of code
#second step: make it pythonic
#third step: create functions
#fourth step: make printing more user-friendly and create comments
