import analizador_lexico as a_lex


matrizPredictiva = (
    (601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,0   ,601 ,0   ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601 ,601),
    (602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,2   ,602 ,1   ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602 ,602),
    (603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,4   ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,603 ,3   ,603 ,603 ,603),
    (604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,604 ,6   ,5   ,7   ,604 ,604 ,604 ,604 ,604),
    (605 ,605 ,605 ,605 ,605 ,605 ,605 ,605 ,605 ,605 ,605 ,605 ,605 ,605 ,605 ,605 ,605 ,605 ,605 ,605 ,9   ,605 ,605 ,605 ,8   ,605 ,605 ,605 ,605 ,605 ,605 ,605 ,605 ,605 ,605 ,605 ,605 ,605 ,605 ,605 ,605 ,605 ,605 ,605 ,605 ,605 ,605 ,605 ,605 ,9   ,605 ,605 ,605 ,605 ,605 ,605 ,605 ,605 ,605 ,605 ,605),
    (606 ,606 ,606 ,606 ,606 ,606 ,606 ,606 ,606 ,606 ,606 ,606 ,606 ,606 ,606 ,606 ,606 ,606 ,606 ,606 ,606 ,606 ,606 ,606 ,606 ,606 ,606 ,606 ,606 ,606 ,606 ,606 ,606 ,606 ,11  ,11  ,11  ,11  ,11  ,606 ,606 ,606 ,606 ,606 ,606 ,606 ,606 ,606 ,606 ,606 ,606 ,10  ,606 ,606 ,606 ,606 ,606 ,606 ,606 ,606 ,606),
    (607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,12  ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607 ,607),
    (608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,14  ,608 ,13  ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608 ,608),
    (609 ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,15  ,16  ,17  ,19  ,18  ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,609 ,609),
    (610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,610 ,20  ,610 ,610 ,610),
    (611 ,22  ,611 ,611 ,611 ,611 ,611 ,611 ,611 ,611 ,611 ,611 ,611 ,611 ,611 ,611 ,611 ,611 ,611 ,611 ,611 ,611 ,611 ,611 ,611 ,611 ,611 ,611 ,611 ,611 ,611 ,611 ,611 ,611 ,611 ,611 ,611 ,611 ,611 ,25  ,21  ,21  ,27  ,21  ,611 ,26  ,23  ,24  ,611 ,611 ,611 ,611 ,611 ,611 ,611 ,611 ,611 ,611 ,21  ,21  ,21 ),
    (612 ,28  ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612),
    (612 ,29  ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612 ,612),
    (613 ,613 ,613 ,613 ,613 ,30  ,30  ,30  ,30  ,30  ,30  ,30  ,30  ,30  ,30  ,30  ,613 ,30  ,30  ,613 ,30  ,31  ,30  ,30  ,30  ,613 ,613 ,613 ,30  ,613 ,613 ,613 ,613 ,613 ,613 ,613 ,613 ,613 ,613 ,613 ,613 ,613 ,613 ,613 ,613 ,613 ,613 ,613 ,613 ,613 ,613 ,613 ,613 ,613 ,613 ,613 ,613 ,613 ,613 ,613 ,613),
    (614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,32  ,614 ,32  ,614 ,33  ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614),
    (615 ,34  ,34  ,34  ,34  ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,34  ,615 ,615 ,34  ,615 ,615 ,615 ,615 ,615 ,34  ,34  ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615),
    (616 ,616 ,616 ,616 ,616 ,616 ,616 ,616 ,616 ,616 ,616 ,616 ,616 ,616 ,616 ,616 ,616 ,616 ,36  ,616 ,35  ,616 ,35  ,35  ,35  ,616 ,616 ,616 ,616 ,616 ,616 ,616 ,616 ,616 ,616 ,616 ,616 ,616 ,616 ,616 ,616 ,616 ,616 ,616 ,616 ,616 ,616 ,616 ,616 ,616 ,616 ,616 ,616 ,616 ,616 ,616 ,616 ,616 ,616 ,616 ,616),
    (617 ,37  ,37  ,37  ,37  ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,37  ,617 ,617 ,37  ,617 ,617 ,617 ,617 ,617 ,37  ,37  ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617),
    (617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,39  ,38  ,617 ,38  ,617 ,38  ,38  ,38  ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617 ,617),
    (615 ,41  ,41  ,41  ,41  ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,40  ,615 ,615 ,41  ,615 ,615 ,615 ,615 ,615 ,41  ,41  ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615),
    (615 ,42  ,42  ,42  ,42  ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,42  ,615 ,615 ,615 ,615 ,615 ,42  ,42  ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615),
    (618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,44  ,44  ,44  ,44  ,44  ,44  ,618 ,43  ,43  ,618 ,43  ,618 ,43  ,43  ,43  ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618),
    (618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,45  ,47  ,48  ,49  ,50  ,46  ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618 ,618),
    (615 ,51  ,51  ,51  ,51  ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,51  ,615 ,615 ,615 ,615 ,615 ,51  ,51  ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615),
    (619 ,619 ,619 ,619 ,619 ,53  ,54  ,619 ,619 ,619 ,52  ,52  ,52  ,52  ,52  ,52  ,619 ,52  ,52  ,619 ,52  ,619 ,52  ,52  ,52  ,619 ,619 ,619 ,619 ,619 ,619 ,619 ,619 ,619 ,619 ,619 ,619 ,619 ,619 ,619 ,619 ,619 ,619 ,619 ,619 ,619 ,619 ,619 ,619 ,619 ,619 ,619 ,619 ,619 ,619 ,619 ,619 ,619 ,619 ,619 ,619),
    (615 ,55  ,55  ,55  ,55  ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,55  ,615 ,615 ,615 ,615 ,615 ,55  ,55  ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615),
    (620 ,620 ,620 ,620 ,620 ,59  ,59  ,56  ,57  ,620 ,59  ,59  ,59  ,59  ,59  ,59  ,620 ,59  ,59  ,620 ,59  ,620 ,59  ,59  ,59  ,620 ,620 ,620 ,58  ,620 ,620 ,620 ,620 ,620 ,620 ,620 ,620 ,620 ,620 ,620 ,620 ,620 ,620 ,620 ,620 ,620 ,620 ,620 ,620 ,620 ,620 ,620 ,620 ,620 ,620 ,620 ,620 ,620 ,620 ,620 ,620),
    (615 ,66  ,60  ,61  ,62  ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,65  ,615 ,615 ,615 ,615 ,615 ,63  ,64  ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615 ,615),
    (621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,67  ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621 ,621),
    (622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,68  ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622 ,622),
    (623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,69  ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623),
    (624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,70  ,71  ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,624 ,70  ,624),
    (625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,72  ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,625 ,73  ,625),
    (626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,74  ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626 ,626),
    (627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,75  ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627 ,627)
)

vecProduccion = [
    [152, 9, 2, 101, 133, 1],
    [],
    [1, 123, 101, 131],
    [],
    [2, 123, 8, 5,149, 4, 101, 3, 148],
    [154],
    [153],
    [155],
    [4, 101, 124],
    [],
    [6, 151],
    [],
    [122, 7, 102, 121],
    [7, 102, 124],
    [],
    [134],
    [135],
    [136],
    [138],
    [137],
    [158, 10, 120, 119, 157],
    [],
    [10, 123, 11],
    [10, 123, 28],
    [10, 123, 29],
    [10, 30],
    [10, 33],
    [10, 34],
    [15, 109, 12],
    [13, 101],
    [],
    [122, 14, 15, 121],
    [],
    [14, 15, 124],
    [16, 17],
    [],
    [15, 118],
    [18, 19],
    [],
    [17, 117],
    [116, 20],
    [20],
    [21, 23],
    [],
    [23, 22],
    [110],
    [115],
    [111],
    [112],
    [113],
    [114],
    [24, 25],
    [],
    [23, 105],
    [23, 106],
    [26, 27],
    [25, 107],
    [25, 108],
    [25, 128],
    [],
    [102],
    [103],
    [104],
    [125],
    [126],
    [120, 15, 119],
    [12],
    [120, 4, 101, 119, 146],
    [120, 14, 15, 119, 147],
    [159, 32, 31, 10, 120, 15, 119, 139],
    [],
    [31, 10, 120, 15, 119, 141],
    [10, 140],
    [],
    [160, 10, 120, 15, 119, 145],
    [144, 120, 15, 119, 143, 10, 142]
]

dict_errores_sintax = {
    600: "e600: ERROR DE SINTAXIS",
    601:"e601: ERROR DE SINTAXIS: Se esperaba lib o class",
    602:"e602: ERROR DE SINTAXIS: Se esperaba lib",
    603:"e603: ERROR DE SINTAXIS: Se esperaba def",
    604:"e604: ERROR DE SINTAXIS: Se esperaba private,, public o protected",
    605:"e605: ERROR DE SINTAXIS: Se esperaba , o ), o continuar con as",
    606:"e606: ERROR DE SINTAXIS: Se esperaba array con continuar con tipo de dato",
    607:"e607: ERROR DE SINTAXIS: Se esperaba [",
    608:"e608: ERROR DE SINTAXIS: Se esperaba , o continuar con ]",
    609:"e609: ERROR DE SINTAXIS: Se esperaba tipo de dato",
    610:"e610: ERROR DE SINTAXIS: Se esperaba declarar main()",
    611:"e611: ERROR DE SINTAXIS: Se esperaba empezar o terminar estatuto",
    612:"e612: ERROR DE SINTAXIS: Se esperaba id",
    613:"e613: ERROR DE SINTAXIS: Se esperaba [",
    614:"e614: ERROR DE SINTAXIS: Se esperaba , o continuar expresion",
    615:"e615: ERROR DE SINTAXIS: Se esperaba una constante, id u otra expresion",
    616:"e616: ERROR DE SINTAXIS: Se esperaba || o continuar expresion",
    617:"e617: ERROR DE SINTAXIS: Se esperaba && o continuar expresion",
    618:"e618: ERROR DE SINTAXIS: Se esperaba operador relacional",
    619:"e619: ERROR DE SINTAXIS: Se esperaba + o -",
    620:"e620: ERROR DE SINTAXIS: Se esperaba *, / o %",
    621:"e621: ERROR DE SINTAXIS: Se esperaba input",
    622:"e622: ERROR DE SINTAXIS: Se esperaba output",
    623:"e623: ERROR DE SINTAXIS: Se esperaba if",
    624:"e624: ERROR DE SINTAXIS: Se esperaba elif",
    625:"e625: ERROR DE SINTAXIS: Se esperaba else o terminar con endif",
    626:"e626: ERROR DE SINTAXIS: Se esperaba while",
    627:"e627: ERROR DE SINTAXIS: Se esperaba do",
}

dict_conversion_tipos = {
    134: 0,
    135: 1,
    136: 2,
    137: 3,
    138: 4,
}

tipos_to_strig = {
	0: 'int',
	1: 'float',
	2: 'char',
	3: 'string',
	4: 'bool', 
}

strErrores = ''
strTokens = ''  

def analizador(codigo : str = ''):
    global strErrores 
    global strTokens

    list_identificadores = []

    tabla_id = dict()

    codigo = codigo.replace('\n', ' ')
    #print('CODIGO: ', codigo)
    strTokens = ''
    strErrores =  ''  

    def get_add_error_sintaxix(n_error = 0):
        msg_error = dict_errores_sintax.get(n_error, 'DESCONOCIDO: ERROR DE SINTAXIS\n')
        return msg_error

    def agregar_prod(n_prod: int):
        
        n = n_prod
        #for elemento in vecProduccion[n]:
        #    pila_prod.append(elemento)
        pila_prod.extend(vecProduccion[n])
        
    def agregar_identificador(*nombres, tipo = 1):
        """"
        verificar tabla de identificadores
        agrega el nuevo identificador con tipo si no existe
        retorna el error si si existe
        
        """
        global strErrores

        for nombre in nombres:
            
            if nombre not in tabla_id:
                tipo_temp = dict_conversion_tipos[tipo]
                tabla_id[nombre] = tipo_temp
                print(f'agregando {nombre} como {tipo_temp}')
            else:
                strErrores += f'\nDUPLICIDAD de variable {nombre}'
                pass
        
    

    pila_prod = [100,0]
    sintaxis_correcta = False

    lex = a_lex.analizador_lex(codigo)

    # primer token a analizar
    token =  lex.get_token()
    if token[0] < 500 and token[0] != 127:
        strTokens += f'{token[1]}:\t {token[2]}\n'
    if token[0] >= 500 and token[0] < 600:
        strErrores += f'{token[1]}:\t {token[2]}\n'
        strTokens += f'{token[1]}:\t {token[2]}\n'

    

    agregando_identificadores = False

    while True:
        #ignoramos los tokens de comentario y pedimos otro token
        if token[0] == 127:
            token = lex.get_token()

            if token[0] < 500 and token[0] != 127:
                strTokens += f'{token[1]}:\t {token[2]}\n'
            if token[0] >= 500 and token[0] < 600:
                strErrores += f'{token[1]}:\t {token[2]}\n'
                strTokens += f'{token[1]}:\t {token[2]}\n'

            continue

        # cacheo de tokens y errores LEXICOS
        if token[0] >= 500 and token[0] < 600:
            token = lex.get_token()

            if token[0] < 500 and token[0] != 127:
                strTokens += f'{token[1]}:\t {token[2]}\n'
            if token[0] >= 500 and token[0] < 600:
                strErrores += f'{token[1]}:\t {token[2]}\n'
                strTokens += f'{token[1]}:\t {token[2]}\n'

            continue

        tope_pila = pila_prod[-1]

        # analizador SINTACTICO
        if tope_pila >= 100: # si se trata de un elemento terminal
            if tope_pila == 100 and token[0] == 100: # si ambos sin finales de cadena $
                #print('SINTAXIS CORRECTA')
                strTokens = f'SINTAXIS CORRECTA\n {strTokens} SINTAXIS CORRECTA'
                sintaxis_correcta = True
                break

            elif tope_pila == token[0]: # si son iguales

                if token[0] == 148: # cuando nos llega un _def_, cambiamos a modo agregar variables
                    agregando_identificadores = True

                if token[0] == 101 and agregando_identificadores: # si el token es un identificador
                    list_identificadores.append(token[1])
                    

                if token[0] in {134, 135, 136, 137, 138} and agregando_identificadores:
                    agregar_identificador(*list_identificadores, tipo=token[0])
                    list_identificadores = []
                    agregando_identificadores = False
                    pass

                if not agregando_identificadores:
                    pass

                pila_prod.pop()
                token =  lex.get_token()

                if token[0] < 500 and token[0] != 127:
                    strTokens += f'{token[1]}:\t {token[2]}\n'
                if token[0] >= 500 and token[0] < 600:
                    strErrores += f'{token[1]}:\t {token[2]}\n'
                    strTokens += f'{token[1]}:\t {token[2]}\n'

                

                tope_pila = pila_prod[-1]
                #print(f'nuevo token: {token}')

            else: # si son diferentes
                strErrores += token[1]+ ':\t' + get_add_error_sintaxix(0)
                #print(f'::{token}::')
                #print(f'::{tope_pila}::')
                #print(f'::{pila_prod}::')
                # Aqui va la la explicacion del error
                #
                #
                break

        else: # su es un NO terminal, es una nueva PRODUCCION
            # primero checamos de que produccion se trata
            n_prod = matrizPredictiva[tope_pila][(token[0]-100)]

            if n_prod < 600: # si la produccion no dirige a error
                pila_prod.pop() # hacemos pop
                agregar_prod(n_prod) # agregamos los elementos de la produccion a la pila de producciones
                

            else:
                strErrores += token[1]+ ':\t' + get_add_error_sintaxix(0)
                break







    
    



    #print(strTokens, strTokens)  
    print(tabla_id)
    #strTokens += f'{token[1]}:\t {token[2]}\n'
    return (strTokens , strErrores)



if(__name__ == '__main__'):

    codigo_prueba = """
class mi_program
def public A,B, res as int;
def private X as float;
def private nombre as string;
def public A as char;

main()
   input(A,B);
   res = A+ B;
   
end

endclass

"""

    str1, str2 = analizador(codigo=codigo_prueba)
    print(str1, str2)

    pass