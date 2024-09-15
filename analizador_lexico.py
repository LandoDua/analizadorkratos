


class analizador_lex():
    def __init__(self, palabra = '') -> None:
        self.matrizLexico = (
        (1  , 2  , 3  , 506, 506, 1  , 2  , 106, 105, 107, 128, 108, 15 , 17 , 19 , 129, 130, 121, 122, 119, 120, 10 , 11 , 9  , 14 , 13 , 12 , 124, 123, 0  , 0  , 0  , 506, 0  ),
        (1  , 2  , 2  , 2  , 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100),
        (2  , 2  , 2  , 2  , 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101),
        (102, 102, 3  , 102, 4  , 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102),
        (500, 500, 5  , 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500),
        (103, 103, 5  , 103, 103, 6  , 6  , 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103),
        (501, 501, 8  , 501, 501, 501, 501, 7  , 7  , 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501),
        (502, 502, 8  , 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502),
        (104, 104, 8  , 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104, 104),
        (109, 109, 109, 109, 109, 109, 109, 109, 109, 109, 109, 109, 109, 109, 109, 109, 109, 109, 109, 109, 109, 109, 109, 110, 109, 109, 109, 109, 109, 109, 109, 109, 109, 109),
        (111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 112, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111),
        (113, 113, 113, 113, 113, 113, 113, 113, 113, 113, 113, 113, 113, 113, 113, 113, 113, 113, 113, 113, 113, 113, 113, 114, 113, 113, 113, 113, 113, 113, 113, 113, 113, 113),
        (116, 116, 116, 116, 116, 116, 116, 116, 116, 116, 116, 116, 116, 116, 116, 116, 116, 116, 116, 116, 116, 116, 116, 115, 116, 116, 116, 116, 116, 116, 116, 116, 116, 116),
        (503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 117, 503, 503, 503, 503, 503, 503, 503, 503),
        (504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 504, 118, 504, 504, 504, 504, 504, 504, 504, 504, 504),
        (16 , 16 , 16 , 16 , 16 , 16 , 16 , 16 , 16 , 16 , 16 , 16 , 505, 16 , 16 , 16 , 16 , 16 , 16 , 16 , 16 , 16 , 16 , 16 , 16 , 16 , 16 , 16 , 16 , 16 , 16 , 16 , 16 , 16 ),
        (507, 507, 507, 507, 507, 507, 507, 507, 507, 507, 507, 507, 125, 507, 507, 507, 507, 507, 507, 507, 507, 507, 507, 507, 507, 507, 507, 507, 507, 507, 507, 507, 507, 507),
        (17 , 17 , 17 , 17 , 17 , 17 , 17 , 17 , 17 , 17 , 17 , 17 , 17 , 18 , 17 , 17 , 17 , 17 , 17 , 17 , 17 , 17 , 17 , 17 , 17 , 17 , 17 , 17 , 17 , 508, 17 , 17 , 17 , 17 ),
        (126, 126, 126, 126, 126, 126, 126, 126, 126, 126, 126, 126, 126, 17 , 126, 126, 126, 126, 126, 126, 126, 126, 126, 126, 126, 126, 126, 126, 126, 126, 126, 126, 126, 126),
        (19 , 19 , 19 , 19 , 19 , 19 , 19 , 19 , 19 , 19 , 19 , 19 , 19 , 19 , 19 , 19 , 19 , 19 , 19 , 19 , 19 , 19 , 19 , 19 , 19 , 19 , 19 , 19 , 19 , 127 , 19, 19 , 19 , 19 )
        )

        self.caracteres = {
            '_':3,
            r'.':4,
            'e':5,
            'E':6,
            '-':7,
            '+':8,
            '*':9,
            '%':10,
            '/':11,
            r"'":12,
            r'"':13,
            '#':14,
            '}':15,
            '{':16,
            '[':17,
            ']':18,
            '(':19,
            ')':20,
            '<':21,
            '>':22,
            '=':23,
            '|':24,
            '&':25,
            '!':26,
            ',':27,
            r';':28,
            '\n':29,
            '\t':30,
            '\b':31,
            ' ':33,
        }

        self.reservadas = {
            "lib":  131,
            "library":  132,
            "class":    133,
            "int":  134,
            "float":    135,
            "char": 136,
            "string":   137,
            "bool": 138,
            "if":   139,
            "else": 140,
            "elseif":   141,
            "do":   142,
            "dowhile":  143,
            "enddo":    144,
            "while":    145,
            "input":    146,
            "output":   147,
            "def":  148,
            "as":   149,
            "cons": 150,
            "array":    151,
            "endclass": 152,
            "private":  153,
            "public":   154,
            "protected":155,
            "list": 156,
            "main": 157,
            "end":  158,
            "endif":159,
            "endwhile": 160,
        }

        self.token_regresivos = {102, 103, 104, 109, 111, 113, 116, 126, 500, 501, 503, 504, 505, 507,}

        self.tokem_to_msj = {
            100:  "Reservada" ,
            101:  "Identificador" ,
            102:  "Entero" ,
            103:  "Real" ,
            104:  "Not Cient." ,
            105:  "Suma" ,
            106:  "Resta" ,
            107:  "Multi" ,
            108:  "Division" ,
            109:  "Asignacion" ,
            110:  "Igual" ,
            111:  "Menor" ,
            112:  "Menor igual" ,
            113:  "Mayor" ,
            114:  "Mayor igual" ,
            115:  "Diferente" ,
            116:  "NOT" ,
            117:  "AND" ,
            118:  "OR" ,
            119:  "Abre parent." ,
            120:  "Cierra parent." ,
            121:  "Abre corch." ,
            122:  "Cierra corch." ,
            123:  "Punto y coma" ,
            124:  "Coma" ,
            125:  "Caracter" ,
            126:  "String" ,
            127:  "Coment. linea" ,
            128:  "Modulo" ,
            129:  "Cierra llave" ,
            130:  "Abre llave" ,
            131:  "_lib_" ,
            132:  "_library_" ,
            133:  "_class_" ,
            134:  "_int_" ,
            135:  "_float_" ,
            136:  "_char_" ,
            137:  "_string_" ,
            138:  "_bool_" ,
            139:  "_if_" ,
            140:  "_else_" ,
            141:  "_elseif_" ,
            142:  "_do_" ,
            143:  "_dowhile_" ,
            144:  "_enddo_" ,
            145:  "_while_" ,
            146:  "_input_" ,
            147:  "_output_" ,
            148:  "_def_" ,
            149:  "_as_" ,
            150:  "_cons_" ,
            151:  "_array_" ,
            152:  "_endclass_" ,
            153:  "_private_" ,
            154:  "_public_" ,
            155:  "_protected_" ,
            156:  "_list_" ,
            157:  "_main_" ,
            158:  "_end_" ,
            159:  "_endif_" ,
            160:  "_endwhile_" ,
            500: "e500: real espera digito",
            501: "e501: se esperaba digito, + o -",
            502: "e502: se esperaba digito",
            503: "e503: se esperaba &",
            504: "e504: se esperaba |",
            505: "e505: error al declarar caracter",
            506: "e506: . o _ invalidos, caractert desconocido",
            507: "e507: solo un caracter entre comillas",
            508: "e508: comillas esperan ser cerradas",
        }

        self.lexema = ' '
        self.lexema_simple = ' '
        self.caracter = ''
        self.posicion = 0
        self.edo = 0
        self.palabra = palabra + ' '
        self.col = 0

    def relaciona(self, c):
        if c>='a' and c<='z':
            if(self.lexema[0] >= '0' and self.lexema[0] <= '9' and c == 'e'):
                return 5
            return 0
        
        if c>='A' and c<='Z':
            if(self.lexema[0] >= '0' and self.lexema[0] <= '9' and c == 'e'):
                return 5
            return 0
        
        if(c>='0' and c<='9'):
            return 2
        
        return self.caracteres.get(c,32)
        
    def ajustar_puntero(self):
        
        self.lexema_simple = self.lexema_simple[:-1]
        self.lexema_simple = self.lexema_simple.strip()

        self.lexema = self.lexema[:-1]

        self.posicion -= 1


    def get_token(self):
        """
        Retorna un token de la cadena analizada paso por paso en forma de tupla
        ej: (109, '=', 'Asignacion')
        """
        self.lexema = ' '
        self.lexema_simple = ' '
        self.edo = 0
        
        while self.posicion < len(self.palabra):
            self.caracter = self.palabra[self.posicion]
            self.col = self.relaciona(self.caracter)
            #print('EDO = ', self.edo)
            self.edo = self.matrizLexico[self.edo][self.col]

            if(self.caracter != '\n' and self.caracter != ' '):
                self.lexema += self.caracter
            
            self.lexema_simple += self.caracter

            if (self.edo == 101): # si es un identificador
                self.ajustar_puntero()

            if self.edo == 100: # evaluar reservadas() # para identificadores que parecen reservadas
                self.ajustar_puntero()
                self.edo = self.reservadas.get(self.lexema_simple, 101)
            
            if self.edo >= 50:

                if self.edo >= 500: # ERROR
                    pass


                if self.edo >= 100 and self.edo < 500: # TOKEN VALIDO
                    pass
                
                if self.edo in self.token_regresivos:
                    self.ajustar_puntero()

                # guardamos un temporal del lexema 
                cadena_temp = self.lexema_simple.strip()

                #reiniciamos variables
                self.lexema = ''
                self.lexema_simple = ''
                self.posicion += 1

                #retornamos la tupla del token
                return self.edo, cadena_temp, self.tokem_to_msj[self.edo]
            
            self.posicion += 1

        return 100, '$', 'final de cadena' # $ # fin de la cadena

if(__name__ == '__main__'):

    cadena = '. myvar = 5+ 4.1 !if == _d , ; .'

    lex = analizador_lex(cadena)
    
    token = lex.get_token()

    while token[0] != 100:
        print(token)
        token = lex.get_token()
    



