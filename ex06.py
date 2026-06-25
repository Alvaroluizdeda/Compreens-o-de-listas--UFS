nome = input()
nomefiltrado = sum([1 for x in nome if x.upper() in "AEIOU"])
print(nomefiltrado)