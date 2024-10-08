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
[120, 4, 101, 119, 146],
[120, 14, 15, 119, 147],
[159, 32, 31, 10, 1012, 120, 15, 119, 139],
[],
[31, 10, 1012, 120, 15, 119, 141],
[10, 140],
[],
[160, 10, 1012, 120, 15, 119, 145],
[144, 1012, 120, 15, 119, 143, 10, 142],
]

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

dict_constantes_tipos = {
    134: 0, # int
    135: 1, # float
    136: 2, # char
    137: 3, # string
    138: 4, # bool
}

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

def analizador(codigo : str = ''):
    """Analiza el codigo como parametro
    retorna (strTokens, strErrores, __codigo_correcto__, tabla_simbolos, pila_tipos, pila_operadores)"""
    global strErrores 
    global strTokens
    global semantica_correcta
    
    semantica_correcta = True

    list_identificadores = []
    pila_operadores = []
    pila_operadores_estatica = []
    pila_tipos = []
    pila_tipos_estatica = []
    tabla_simbolos = dict()
    ultimo_token = 0 # solo lo usamos para aculumar el ultimo token analizado antes de una acción

    codigo = codigo.replace('\n', ' ')
    #print('CODIGO: ', codigo)
    strTokens = ''
    strErrores =  ''  



    def get_add_error_sintaxix(n_error = 0):
        msg_error = dict_errores_sintax.get(n_error, 'DESCONOCIDO: ERROR DE SINTAXIS\n')
        return msg_error

    def agregar_prod(n_prod: int):
        """Agrega produccion numero n en la pila de producciones
        """
        
        n = n_prod
        #for elemento in vecProduccion[n]:
        #    pila_prod.append(elemento)
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
                print(f'agregando {nombre} como {tipo_temp}')
            else:
                strErrores += f'ERROR SEM. Duplicidad de variable {nombre}\n'
                semantica_correcta = False
                pass
    
    def verificar_tipos_compatibles(tipo1: int, tipo2: int, operador: int):
        """ verifica la compatiblidad de dos tipos sobre un operador
        retorna el resultado, sino exite retorna float (1) y llama el error
        """
        global strErrores, semantica_correcta
        renglon = (tipo1 * 5) + tipo2

        columna = 0

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
    
    def ejecutar_operacion():
        tipo_temp = verificar_tipos_compatibles(pila_tipos[-2], pila_tipos[-1],pila_operadores[-1])

        pila_tipos.pop()
        pila_tipos.pop()
        pila_tipos.append(tipo_temp)
        pila_tipos_estatica.append(tipo_temp)

        pila_operadores.pop()

    def ejecutar_accion(n_accion: int):
        global strErrores, semantica_correcta
        
        # accion 1
        if n_accion == 1001:
            variable = token[1]
            if token[0] in dict_constantes_tipos: # si lo que llega es una constante, añadimos el tipo
                pila_tipos.append(dict_constantes_tipos[token[0]])
                pila_tipos_estatica.append(dict_constantes_tipos[token[0]])

            elif variable in tabla_simbolos: # si lo que llega es una variable que si esta en la tabla de simbolos
                pila_tipos.append(tabla_simbolos[variable])
                pila_tipos_estatica.append(tabla_simbolos[variable])

            else: # si no es constante y es una variable sin declarar
                strErrores += f'ERROR SEM. Variable "{variable}" no declarada, añadida como float\n'
                semantica_correcta = False
                agregar_identificador(variable)
                pila_tipos.append(tabla_simbolos[variable])
                pila_tipos_estatica.append(tabla_simbolos[variable])
        
        # accion 2
        elif n_accion == 1002 and token[1] == '=':
            pila_operadores.append(token[0])
            pila_operadores_estatica.append(token[0])

        # accion 3
        elif n_accion == 1003:
            if not len(pila_operadores) == 0: 
                if pila_operadores[-1] in {107, 108, 128, 118}: # si se trata de un { *, /, %, AND }
                    
                    tipo_temp = verificar_tipos_compatibles(pila_tipos[-2], pila_tipos[-1],pila_operadores[-1])

                    pila_tipos.pop()
                    pila_tipos.pop()
                    pila_tipos.append(tipo_temp)
                    pila_tipos_estatica.append(tipo_temp)

                    pila_operadores.pop()

        # accion 4
        elif n_accion == 1004:
            if not len(pila_operadores) == 0: 
                if pila_operadores[-1] in {105, 106, 117}: # si se trata de un { +, -, OR }
                    
                    tipo_temp = verificar_tipos_compatibles(pila_tipos[-2], pila_tipos[-1],pila_operadores[-1])

                    pila_tipos.pop()
                    pila_tipos.pop()
                    pila_tipos.append(tipo_temp)
                    pila_tipos_estatica.append(tipo_temp)

                    pila_operadores.pop()
        # accion 5
        elif n_accion == 1005 and token[1] in {'*', '/', '%'}:
            pila_operadores.append(token[0])
            pila_operadores_estatica.append(token[0])

        # accion 6
        elif n_accion == 1006 and token[1] in {'+', '-',}:
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
                
                if pila_tipos[-2] != pila_tipos[-1]:
                    strErrores += f'ERROR SEM. entre tipos en "=" con {tipos_to_strig[pila_tipos[-2]]} y {tipos_to_strig[pila_tipos[-1]]}\n'
                    semantica_correcta = False

                pila_tipos.pop()
                pila_tipos.pop()
                pila_operadores.pop()
        # accion 10
        elif n_accion == 1010:
            if not len(pila_operadores) == 0: 
                if pila_operadores[-1] in {110, 114, 112, 115, 113, 111}: # si se trata de un { +, -, OR }
                    
                    tipo_temp = verificar_tipos_compatibles(pila_tipos[-2], pila_tipos[-1],pila_operadores[-1])

                    pila_tipos.pop()
                    pila_tipos.pop()
                    pila_tipos.append(tipo_temp)
                    pila_tipos_estatica.append(tipo_temp)

                    pila_operadores.pop()


        # accion 11
        elif n_accion == 1011 and token[1] in {'==', '>=', '<=', '!=', '>', '<'}:
            pila_operadores.append(token[0])
            pila_operadores_estatica.append(token[0])

        elif n_accion == 1012:
            if not pila_tipos[-1] == 4:
                strErrores += 'ERROR SEM. expresión condicional no booleana.\n'
                semantica_correcta= False,

            pila_tipos.pop()





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

        # cacheo de acciones semanticas
        

        # analizador SINTACTICO
        if tope_pila >= 100: # si se trata de un elemento terminal
            if tope_pila == 100 and token[0] == 100: # si ambos sin finales de cadena $
                #print('SINTAXIS CORRECTA')
                strTokens = f'SINTAXIS CORRECTA\n {strTokens} SINTAXIS CORRECTA\n'
                sintaxis_correcta = True
                break

            elif tope_pila == token[0]: # si son iguales
                ultimo_token = token



                if token[0] == 148: # cuando nos llega un _def_, cambiamos a modo agregar variables
                    agregando_identificadores = True

                if token[0] == 101 and agregando_identificadores: # si el token es un identificador
                    list_identificadores.append(token[1])
                    

                if token[0] in {134, 135, 136, 137, 138} and agregando_identificadores:
                    agregar_identificador(*list_identificadores, tipo=token[0])
                    list_identificadores = []
                    agregando_identificadores = False
                    

                

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

        while pila_prod[-1] >= 1000:
            # print(pila_prod)
            # print( f"ACCAccion semantica encontrada {pila_prod[-1]} con {token[2]}\n")
            strTokens += f"Accion semantica encontrada {pila_prod[-1]} con {token[1]}\n"
            # aqui invocamos la accion
            ejecutar_accion(pila_prod[-1])

            pila_prod.pop()
            tope_pila= pila_prod[-1]





    
    
    


    #print(strTokens, strTokens)  
    print(tabla_simbolos)
    #strTokens += f'{token[1]}:\t {token[2]}\n'
    codigo_correcto = sintaxis_correcta and semantica_correcta

    return (strTokens , strErrores, codigo_correcto, tabla_simbolos, pila_tipos_estatica, pila_operadores_estatica)


if(__name__ == '__main__'):

    codigo_prueba = """
class mi_program
def public A,B, res as float;
def private X as char;
def private nombre as string;
def public bandera as bool;



main()

    # bandera = A == B ;

end

endclass

"""

    strTokens , strErrores, codigo_correcto, tabla_simbolos, pila_tipos, pila_operadores = analizador(codigo=codigo_prueba)
    print(strTokens, strErrores)
    print(f'Codigo correcto: {codigo_correcto}')

    pass