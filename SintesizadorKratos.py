# Analizador Kratos con semantico
import analizador_lexico as a_lex
import pprint

# usada en Sintactico
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

# usada en Sintactico, modificado para semantico
vecProduccion = [
[152, 9, 2, 101, 133, 1],
[],
[1, 123, 101, 131],
[],
[2, 123, 8, 5,149, 4, 101, 3, 148],
[154],
[153],
[155],
[4, 101, 1001, 124],
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
[1009, 15, 109, 1002, 12, 1001],
[13, 101],
[],
[122, 14, 15, 121],
[],
[14, 15, 124],
[16, 1004, 17],
[],
[15, 118, 1006],
[18, 1003, 19],
[],
[17, 117, 1005],
[116, 20],
[20],
[21, 23],
[],
[1010, 23, 22],
[110, 1011],
[115, 1011],
[111, 1011],
[112, 1011],
[113, 1011],
[114, 1011],
[24, 1004,  25],
[],
[23, 105, 1006],
[23, 106, 1006],
[26, 1003, 27],
[25, 107, 1005],
[25, 108, 1005],
[25, 128, 1005],
[],
[102, 1001],
[103, 1001],
[104, 1001],
[125, 1001],
[126, 1001],
[120, 1008,  15, 119, 1007],
[12, 1001],
[1402, 120, 4, 101, 1001,  119, 1401, 146],
[1403, 120, 14, 15, 119, 1401, 147],
[1107, 159, 32, 31, 10, 1106, 1012, 120, 15, 119, 1105, 139],
[],
[31, 1111, 10, 1110 ,1012, 120, 15, 119, 1108, 141],
[1109, 10, 1108, 140],
[],
[1208, 160, 10, 1207, 1012, 120, 15, 119, 1205, 145],
[1306, 144, 1012, 120, 15, 119, 143, 10, 1305, 142],
]

# usada en Sintactico
dict_errores_sintax = {
    600:"e600: ERROR DE SINTAXIS",
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

# usada en Semantico
# usamos un nuevo codigo para los tipos durante las operaciones del semantico
dict_constantes_tipos = {
    134: 0, # int
    102: 0, # cte-int
    135: 1, # float
    103: 1, # cte-float
    136: 2, # char
    125: 2, # cte-char
    137: 3, # string
    126: 3, # cte-string
    138: 4, # bool
}

dict_valores_defecto = {
    0: 0,
    1: 0.0,
    2: '',
    3: "",
    4: False
}
# usada en Semantico
# convierte tokens numericos a string para mostrarlos
tipos_to_strig = {
	0: 'int',
	1: 'float',
	2: 'char',
	3: 'string',
	4: 'bool',
    105: '+',
    106: '-',
    107: '*',
    108: '/',
    109: '=',
    128: '%',
    117: 'and',
    118: 'or',
    110: '==',
    114: '>=',
    112: '<=',
    115: '!=',
    -1:  'MFF',
}
# usada en Semantico
# taba de tipos compatibles en operaciones
tabla_tipos = [
    #105, 106, 107, 108, 128, 117, 118, 110, 114, 112,	115  113  111
    #  +,   -,   *,   /,   %,  &&,  ||,  ==,  >=,  <=,  !=,   >,    <, 
    (  0,   0,   0,   1,   0,  -1,  -1,   4,   4,   4,   4,   4,   4), # int-int
    (  1,   1,   1,   1,   1,  -1,  -1,   4,   4,   4,   4,   4,   4), # int-float
    ( -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1), # int-char
    ( -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1), # int-string
    ( -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1), # int-bool
    (  1,   1,   1,   1,   1,  -1,  -1,   4,   4,   4,   4,   4,   4), # float-int
    (  1,   1,   1,   1,   1,  -1,  -1,   4,   4,   4,   4,   4,   4), # float-float
    ( -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1), # float-char
    ( -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1), # float-string
    ( -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1), # float-bool
    ( -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1), # char-int
    ( -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1), # char-float
    (  3,  -1,  -1,  -1,  -1,  -1,  -1,   4,  -1,  -1,   4,  -1,  -1), # char-char
    (  3,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1), # char-string
    ( -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1), # char-bool
    ( -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1), # string-int
    ( -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1), # string-float
    (  3,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1), # string-char
    (  3,  -1,  -1,  -1,  -1,  -1,  -1,   4,  -1,  -1,   4,  -1,  -1), # string-string
    ( -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1), # string-bool
    ( -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1), # bool-int
    ( -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1), # bool-float
    ( -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1), # bool-char
    ( -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1), # bool-string
    ( -1,  -1,  -1,  -1,  -1,   4,   4,   4,  -1,  -1,   4,  -1,  -1), # bool-bool
]



strErrores = ''
strTokens = ''
semantica_correcta = False

contador_cuatruplo = 1

code_to_strig = {
	0: 'int',
	1: 'float',
	2: 'char',
	3: 'string',
	4: 'bool',
    105: '+',
    106: '-',
    107: '*',
    108: '/',
    109: '=',
    128: '%',
    117: 'and',
    118: 'or',
    110: '==',
    114: '>=',
    112: '<=',
    115: '!=',
    111: '<',
    113: '>',
    -1: 'MFF',
}

class contador_r():
    def __init__(self) -> None:
        self.contador = 0

    def getR(self):
        self.contador +=1

        return(f'__R{self.contador}')


generador_temps = contador_r()



def analizador(codigo : str = ''):
    """Analiza el codigo como parametro
    retorna (strTokens, strErrores, __codigo_correcto__, tabla_simbolos, pila_tipos, pila_operadores)"""
    global strErrores 
    global strTokens
    global semantica_correcta
    global contador_cuatruplo
    
    semantica_correcta = True

    list_identificadores = []
    pila_operadores = []
    pila_operadores_estatica = []
    pila_tipos = []
    pila_tipos_estatica = []
    tabla_simbolos = dict()
    ultimo_token = 0 # solo lo usamos para aculumar el ultimo token analizado antes de una acción

    strTokens = ''
    strErrores =  ''  

########################################### VARIABLES DE CODIGO INTERMEDIO ###########################################
    cuatruplos = [
        [None, None, None, None, None]
    ] 
    pila_saltos = []
    pila_saltos_estatica = []
    pila_operandos = []

    tabla_variables = {}
    tabla_simbolos_temporales = {}



#######################################################################################################################


    def get_add_error_sintaxix(n_error = 0):
        """Invoca el error de sintaxis necesario"""
        msg_error = dict_errores_sintax.get(n_error, 'DESCONOCIDO: ERROR DE SINTAXIS\n')
        return msg_error

    def agregar_prod(n_prod: int):
        """Agrega produccion numero n en la pila de producciones
        """
        
        n = n_prod
        pila_prod.extend(vecProduccion[n])
        

    ########### METODOS DE SEMANTICO ###########      
    def agregar_identificador(*nombres, tipo = 135):
        """"
        verificar tabla de identificadores
        agrega el nuevo identificador con tipo si no existe
        retorna el error si si existe
        
        """  
        global strErrores, semantica_correcta
        for nombre in nombres:
            
            if nombre not in tabla_simbolos:
                tipo_temp = dict_constantes_tipos[tipo]
                tabla_simbolos[nombre] = tipo_temp
                # print(f'agregando {nombre} como {tipo_temp}')

                tabla_variables[nombre] = dict_valores_defecto[tipo_temp]

            else:
                strErrores += f'ERROR SEM. Duplicidad de variable {nombre}\n'
                semantica_correcta = False
                pass
    
    def verificar_tipos_compatibles(tipo1: int, tipo2: int, operador: int):
        """ verifica la compatiblidad de dos tipos sobre un operador
        retorna el resultado, sino exite retorna float (1) y llama el error
        """
        global strErrores, semantica_correcta
        # global contador_cuatruplo

        renglon = (tipo1 * 5) + tipo2

        columna = 0
        # asi determinamos la columana de la tabla de tipos
        if operador == 105:   # +
            columna = 0
        elif operador == 106: # -
            columna = 1
        elif operador == 107: # *
            columna = 2
        elif operador == 108: # /
            columna = 3
        elif operador == 128: # %
            columna = 4
        elif operador == 117: # and
            columna = 5
        elif operador == 118: # or
            columna = 6
        elif operador == 110: # ==
            columna = 7
        elif operador == 114: # >=
            columna = 8
        elif operador == 112: # <=
            columna = 9
        elif operador == 115: # !=
            columna = 10
        elif operador == 113: # >
            columna = 11
        elif operador == 111: # <
            columna = 12
        
        
        tipo_resultado = tabla_tipos[renglon][columna]

        if tipo_resultado == -1: # error entre tipos
            strErrores += f"ERROR SEM. entre tipos entre {tipos_to_strig[tipo1]} y {tipos_to_strig[tipo2]} en {tipos_to_strig[operador]}\n" # marcamos el error
            semantica_correcta = False
            return 1 # parchamos con float (1)

        return tipo_resultado
    
    def ejecutar_operacion(): # en desuso
        tipo_temp = verificar_tipos_compatibles(pila_tipos[-2], pila_tipos[-1],pila_operadores[-1])

        pila_tipos.pop()
        pila_tipos.pop()
        pila_tipos.append(tipo_temp)
        pila_tipos_estatica.append(tipo_temp)

        pila_operadores.pop()

    def ejecutar_accion(n_accion: int):
        '''Ejecuta la accion semantica correspondiente en el tope de pila de operadores
        (1000 -> accion 01)'''
        global strErrores, semantica_correcta, contador_cuatruplo
        
        # accion 1
        if n_accion == 1001:
            variable = token[1]
            if token[0] in dict_constantes_tipos: # si lo que llega es una constante, añadimos el tipo
                pila_tipos.append(dict_constantes_tipos[token[0]])
                pila_tipos_estatica.append(dict_constantes_tipos[token[0]])

                pila_operandos.append(token[1])

            elif variable in tabla_simbolos: # si lo que llega es una variable que si esta en la tabla de simbolos
                pila_tipos.append(tabla_simbolos[variable])
                pila_tipos_estatica.append(tabla_simbolos[variable])

                pila_operandos.append(token[1])


            else: # si no es constante y es una variable sin declarar
                strErrores += f'ERROR SEM. Variable "{variable}" no declarada, añadida como float\n'
                semantica_correcta = False
                agregar_identificador(variable)
                pila_tipos.append(tabla_simbolos[variable])
                pila_tipos_estatica.append(tabla_simbolos[variable])
        
                pila_operandos.append(variable)


        # accion 2
        elif n_accion == 1002 and token[1] == '=':
            pila_operadores.append(token[0])
            pila_operadores_estatica.append(token[0])

            


        # accion 3
        elif n_accion == 1003:
            if not len(pila_operadores) == 0: 
                if pila_operadores[-1] in {107, 108, 128, 117}: # si se trata de un { *, /, %, AND }

                    ############## GENERAR CUATRUPLO #####################
                    temp_r = generador_temps.getR()

                    cuatruplos.append([contador_cuatruplo, code_to_strig[pila_operadores[-1]], pila_operandos[-2], pila_operandos[-1], temp_r])
                    contador_cuatruplo += 1

                    pila_operandos.pop()
                    pila_operandos.pop()
                    pila_operandos.append(temp_r)
                    
                    tipo_temp = verificar_tipos_compatibles(pila_tipos[-2], pila_tipos[-1],pila_operadores[-1])
                    
                    tabla_simbolos_temporales[temp_r] = tipo_temp
                    ########################################################
                    

                    pila_tipos.pop()
                    pila_tipos.pop()
                    pila_tipos.append(tipo_temp)
                    pila_tipos_estatica.append(tipo_temp)

                    pila_operadores.pop()

        # accion 4
        elif n_accion == 1004:
            if not len(pila_operadores) == 0: 
                if pila_operadores[-1] in {105, 106, 118}: # si se trata de un { +, -, OR }
                    
                    ############## GENERAR CUATRUPLO #####################
                    temp_r = generador_temps.getR()

                    cuatruplos.append([contador_cuatruplo, code_to_strig[pila_operadores[-1]], pila_operandos[-2], pila_operandos[-1], temp_r])
                    contador_cuatruplo += 1

                    pila_operandos.pop()
                    pila_operandos.pop()
                    pila_operandos.append(temp_r)

                    tipo_temp = verificar_tipos_compatibles(pila_tipos[-2], pila_tipos[-1],pila_operadores[-1])

                    tabla_simbolos_temporales[temp_r] = tipo_temp

                    ########################################################

                    

                    pila_tipos.pop()
                    pila_tipos.pop()
                    pila_tipos.append(tipo_temp)
                    pila_tipos_estatica.append(tipo_temp)

                    pila_operadores.pop()
        # accion 5
        elif n_accion == 1005 and token[1] in {'*', '/', '%', '&&'}:
            pila_operadores.append(token[0])
            pila_operadores_estatica.append(token[0])

        # accion 6
        elif n_accion == 1006 and token[1] in {'+', '-', '||'}:
            pila_operadores.append(token[0])
            pila_operadores_estatica.append(token[0])

        # accion 7
        elif n_accion == 1007: # inserta una marca de fondo falso MFF
            pila_operadores.append(-1)
            pila_operadores_estatica.append(-1)

        # accion 8
        elif n_accion == 1008: # remueve una marca de fondo falso MFF
            if pila_operadores[-1] == -1:
                pila_operadores.pop()
            else:
                print('ERROR LOGICO debimos encontrar un MFF\n\n')
        
        # accion 9
        elif n_accion == 1009:



            if pila_operadores[-1] == 109: # si lo que sigue es una adignasion "="

                cuatruplos.append([contador_cuatruplo, code_to_strig[pila_operadores[-1]], pila_operandos[-2], None, pila_operandos[-1]])
                contador_cuatruplo += 1
                pila_operandos.pop()
                pila_operandos.pop()

                if pila_tipos[-2] != pila_tipos[-1]:
                    strErrores += f'ERROR SEM. entre tipos en "=" con {tipos_to_strig[pila_tipos[-2]]} y {tipos_to_strig[pila_tipos[-1]]}\n'
                    semantica_correcta = False

                pila_tipos.pop()
                pila_tipos.pop()
                pila_operadores.pop()
        # accion 10
        elif n_accion == 1010:
            if not len(pila_operadores) == 0: 
                if pila_operadores[-1] in {110, 114, 112, 115, 113, 111}:

                    ############## GENERAR CUATRUPLO #####################
                    temp_r = generador_temps.getR()

                    cuatruplos.append([contador_cuatruplo, code_to_strig[pila_operadores[-1]], pila_operandos[-2], pila_operandos[-1], temp_r])
                    contador_cuatruplo += 1

                    pila_operandos.pop()
                    pila_operandos.pop()
                    pila_operandos.append(temp_r)
                    
                    tipo_temp = verificar_tipos_compatibles(pila_tipos[-2], pila_tipos[-1],pila_operadores[-1])
                    
                    tabla_simbolos_temporales[temp_r] = tipo_temp
                    ########################################################
                    

                    pila_tipos.pop()
                    pila_tipos.pop()
                    pila_tipos.append(tipo_temp)
                    pila_tipos_estatica.append(tipo_temp)

                    pila_operadores.pop()


        # accion 11
        elif n_accion == 1011 and token[1] in {'==', '>=', '<=', '!=', '>', '<'}:
            pila_operadores.append(token[0])
            pila_operadores_estatica.append(token[0])

        # accion 12, verificar expresion booleana
        elif n_accion == 1012:
            if not pila_tipos[-1] == 4:
                strErrores += 'ERROR SEM. expresión condicional no booleana.\n'
                semantica_correcta= False,

            pila_tipos.pop()


        elif n_accion == 1205:
            pila_saltos.append(contador_cuatruplo)
            pila_saltos_estatica.append(contador_cuatruplo)
            

        elif n_accion == 1207:
            cuatruplos.append([contador_cuatruplo, 'SF', pila_operandos[-1], None, None])
            pila_saltos.append(contador_cuatruplo-1)
            pila_saltos_estatica.append(contador_cuatruplo-1)
            contador_cuatruplo += 1

            # pila_saltos.pop() 
            pila_operandos.pop()

        elif n_accion == 1208:
            cuatruplos.append([contador_cuatruplo, 'SI', None, None, pila_saltos[-1]])

            contador_cuatruplo += 1
            pila_saltos.pop() 

            cuatruplos[pila_saltos[-1]+1][4] = contador_cuatruplo
            pila_saltos.pop()

        ### ACCIONES DOWHILE ###
        elif n_accion == 1305:
            pila_saltos.append(contador_cuatruplo);
            pila_saltos_estatica.append(contador_cuatruplo);
    
        elif n_accion == 1306:
            cuatruplos.append([contador_cuatruplo, 'SV', pila_operandos[-1], None, pila_saltos[-1]])
            contador_cuatruplo += 1
            pila_saltos.pop()
            pila_operandos.pop()

        ### ACCIONES IF ###

        elif n_accion == 1105:
            pila_operadores.append("MFF")
            pila_operadores_estatica.append("MFF")

        elif n_accion == 1106:
            cuatruplos.append([contador_cuatruplo, 'SF', pila_operandos[-1], None, None])
            pila_saltos.append(contador_cuatruplo-1)

            contador_cuatruplo += 1
            # pila_saltos.pop() 
            pila_operandos.pop()

        elif n_accion == 1107:
            cuatruplos[pila_saltos[-1]+1][4] = contador_cuatruplo
            pila_saltos.pop()

            pila_operadores.pop() # quitar marca de fondo falso

        elif n_accion == 1108:
            cuatruplos.append([contador_cuatruplo, 'SI', None, None, None])
            pila_saltos.append(contador_cuatruplo-1)
            pila_saltos_estatica.append(contador_cuatruplo-1)
            contador_cuatruplo += 1

            cuatruplos[pila_saltos[-2]+1][4] = contador_cuatruplo
            pila_saltos.pop(-2)

        elif n_accion == 1110:
            cuatruplos.append([contador_cuatruplo, 'SF', pila_operandos[-1], None, None])
            pila_saltos.append(contador_cuatruplo-1)
            pila_saltos_estatica.append(contador_cuatruplo-1)
            contador_cuatruplo += 1

        elif n_accion == 1111:
            cuatruplos[pila_saltos[-2]+1][4] = contador_cuatruplo
            pila_saltos.pop(-2)

            # cuatruplos.append([contador_cuatruplo, 'SI', None, None, None])
            # pila_saltos.append(contador_cuatruplo-1)
            # contador_cuatruplo += 1

            # cuatruplos[pila_saltos[-2]+1][4] = contador_cuatruplo
            # pila_saltos.pop(-2)
            

        elif n_accion == 1401:
            pila_operandos.append("MFF")
            print('1401:::::', pila_operandos[-1])

        elif n_accion == 1402:
            
            pila_temp =  []
            print('1402:::::', pila_operandos)
            while not pila_operandos[-1] == 'MFF':

                
                pila_temp.append(pila_operandos[-1])
                pila_operandos.pop()

            pila_temp.reverse()

            for id_temp in pila_temp:
                cuatruplos.append([contador_cuatruplo, 'Input', None, None, id_temp])
                contador_cuatruplo += 1

            pila_operandos.pop()

        elif n_accion == 1403:
            pila_temp =  []
            while not pila_operandos[-1] == 'MFF':
                pila_temp.append(pila_operandos[-1])
                pila_operandos.pop()

            pila_temp.reverse()

            for id_temp in pila_temp:
                cuatruplos.append([contador_cuatruplo, 'Output', None, None, id_temp])
                contador_cuatruplo += 1

            pila_operandos.pop()



    # inicializamos nuestro analizador
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

    
    # esta bandera cambia al modo agregar variables
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


        ####################### analizador SINTACTICO #######################
        if tope_pila >= 100: # si se trata de un elemento terminal
            if tope_pila == 100 and token[0] == 100: # si ambos sin finales de cadena $
                strTokens = f'SINTAXIS CORRECTA\n {strTokens} SINTAXIS CORRECTA\n'
                sintaxis_correcta = True
                break

            elif tope_pila == token[0]: # si son iguales
                
                ########################################### bloque agregar variables (SEMANTICO) ###########################################
                if token[0] == 148: # cuando nos llega un _def_, cambiamos a modo agregar variables
                    agregando_identificadores = True

                if token[0] == 101 and agregando_identificadores: # si el token es un identificador
                    list_identificadores.append(token[1])
                    

                if token[0] in {134, 135, 136, 137, 138} and agregando_identificadores: # declaramos las variables 
                    agregar_identificador(*list_identificadores, tipo=token[0])
                    list_identificadores = [] # limpiamos la pila de identificadores
                    agregando_identificadores = False
                
                ######################################## fin bloque agregar variables (SEMANTICO) ###########################################    

                

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


        
        ########################################### bloque Cachear acciones (SEMANTICO) ########################################### 
        while pila_prod[-1] >= 1000:
            # aqui invocamos la accion
            ejecutar_accion(pila_prod[-1])

            pila_prod.pop()
            tope_pila= pila_prod[-1]
        ######################################## fin bloque Cachear acciones (SEMANTICO) ########################################### 

 
    # print(tabla_simbolos)
    #  por ultimo determinamos si el codigo en su totalidad es correcto
    codigo_correcto = sintaxis_correcta and semantica_correcta


    generador_temps.contador = 0
    contador_cuatruplo = 1
    return (tabla_variables, cuatruplos, tabla_simbolos_temporales, pila_saltos_estatica)



########################################### bloque pruebas ########################################### 
if(__name__ == '__main__'):

    codigo_prueba = """
class mi_program
def public A,B, res as int;
def private X as char;
def private nombre as string;
def public bandera as bool;



main()

    nombre = "lico";
    B = 5 * 10;
    A = B + 10;

    res = 1 - (A * B) ;

    bandera = (A > B) || (A == B);

    while(A > B)

        B = B + 1; 


    endwhile

    
    if(A==1)
        B = 1;
    elseif (A == 2)
        nombre = "orlande";
    else
        A = 3;
    endif

    input(A, B);
    output(X, A+1);

end



endclass

"""

    tabla_variables, lista_cuatruplos, tabla_temporales, pila_saltos = analizador(codigo=codigo_prueba)
    print(tabla_variables)
    for cuatruplo in lista_cuatruplos:
        print('[', end=' ')

        for dato in cuatruplo:
            print(dato, end='\t')
        
        print(']')

    print(tabla_temporales)
    print(pila_saltos)


    # pprint.pprint(tabla_variables)


    