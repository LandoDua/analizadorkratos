import analizador_lexico as a_lex



def analizador(codigo : str = ''):

    strTokens = ''
    strErrores =  ''

    lex = a_lex.analizador_lex(codigo)

    # primer token a analizar
    token =  lex.get_token()

    while token != 100: # si el token no es $ (fin de programa)
        
        # CACHEO DE TOKEN Y ERRORES LEXICOS
        if token[0] < 500:
            strTokens += f'{token[1]}:\t {token[2]}\n'
        if token[0] >= 500:
            strErrores += f'{token[1]}:\t {token[2]}\n'


        token =  lex.get_token()

    #print(strTokens, strTokens)  


    return (strTokens , strErrores)



if(__name__ == '__main__'):


    print(analizador('my_var = 100- 3.1'))

    pass