def acimamedia(notas):
    media = sum(notas)/len(notas)
    return len([nota for nota in notas if nota > media])