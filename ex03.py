def achatar(xs):
    if xs == []:
        return []
    
    primeiro = xs[0]
    resto = xs[1:]

    if type(primeiro) == list:
        return achatar(primeiro) + achatar(resto)
    else:
        return [primeiro] + achatar(resto)
    

def achatar_compreensao(xs):
    if xs == []:
        return []
    
    return[b for a in xs for b in (achatar_compreensao(a) if type(a) == list else [a])]