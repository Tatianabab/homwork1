text ="Пример текста для подсчета гласных букв"
b="а,е,о,и,я"
a=0
for c in text:
    if c in b:
        a+=1
print(a)