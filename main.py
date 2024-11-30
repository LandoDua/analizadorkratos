import flet as ft
import AnalizadorKratos
import SintesizadorKratos

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

modo_compilado = False

def main(page: ft.Page):
    global modo_compilado
    

    page.title = 'Analizador Kratos'
    #page.window.width = 1500
    page.window.height = '900'
    page.fonts = {
        'JetBrains' : 'fonts/JetBrainsMono-VariableFont_wght.ttf'
    }
    page.theme = ft.Theme(
        color_scheme_seed=ft.colors.AMBER_600,
        font_family='JetBrains'
    )
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding= 15


    def click_analizar(e = None):
        cambiar_modo_analizador()
        codigo = str(txt_codigo.value)
        # codigo = codigo.replace('\n', r' ') 

        strTokens = ''
        strTokens , strErrores, codigo_correcto, tabla_simbolos, pila_tipos, pila_operadores = AnalizadorKratos.analizador(codigo)
        strErrores = '\n' + strErrores
        strErrores = strErrores.replace('\n:	 e506: . o _ invalidos, caractert desconocido', '')

        # txt_tokens.value = strTokens
        txt_errores.value = strErrores
        
        if codigo_correcto:
            btnCompilar.disabled = not codigo_correcto
            page.open(dlg_codigo_correcto)
            contenedor_principal.bgcolor = ft.colors.TERTIARY_CONTAINER
        else:
            desplegar_error('Errores de código encontrados')
        
        txt_tokens.value = strTokens

        renglon_tabla_simbolos = ''

        txt_tabla_simbolos.value = ''
        for variable in tabla_simbolos:
            tipo = tabla_simbolos[variable]
            renglon_tabla_simbolos = f'{variable}:\t {code_to_strig[tipo]}\n'
            txt_tabla_simbolos.value += renglon_tabla_simbolos

        txt_pila_tipos.value = ''
        for tipo in pila_tipos:
            txt_pila_tipos.value += f'{code_to_strig[tipo]}, '

        txt_pila_operadores.value = ''
        for operador in pila_operadores:
            txt_pila_operadores.value += f'{code_to_strig[operador]}, '


        # print(f'Codigo Correcto {codigo_correcto}')

        page.update()

    def click_compilar(e = None):
        cambiar_modo_compilador()

        
        codigo = str(txt_codigo.value)

        tabla_variables, lista_cuatruplos, tabla_temporales, pila_saltos = SintesizadorKratos.analizador(codigo=codigo)
        txt_cuatruplos.value = str(lista_cuatruplos)
        txt_pila_saltos.value = ''


        for salto in pila_saltos:
            txt_pila_saltos.value += str(salto) + ', '

        tabla_cautruplos.rows.clear()
        for cuatruplo in lista_cuatruplos:
            tabla_cautruplos.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(cuatruplo[0]))),
                        ft.DataCell(ft.Text(str(cuatruplo[1]))),
                        ft.DataCell(ft.Text(str(cuatruplo[2]))),
                        ft.DataCell(ft.Text(str(cuatruplo[3]))),
                        ft.DataCell(ft.Text(str(cuatruplo[4]))),
                    ]
                )
            )

        txt_tabla_variables.value = ''

        for variable_temp in tabla_temporales:
            strtemp= f'{variable_temp}:\t{str(code_to_strig[tabla_temporales[variable_temp]])}\n'
            txt_tabla_variables.value  += strtemp


        page.update()
        pass

    def desactivar_btn_compilador(e = None):
        cambiar_modo_analizador()

        if not btnCompilar.disabled:
            btnCompilar.disabled = True
            page.update()
        pass

    def limpiar_campos(e=None):
        cambiar_modo_analizador()
        txt_codigo.value = ''
        txt_tokens.value = ''
        txt_tabla_simbolos.value = ''
        txt_errores.value = ''
        txt_pila_tipos.value = ''
        txt_pila_operadores.value = ''

        page.title = 'Analizador Kratos'  
        txt_codigo.label = 'Codigo'

        page.update()
    
    def desplegar_error(error : str):
        page.snack_bar = ft.SnackBar(
            ft.Text(error, color=ft.colors.ON_ERROR),
            bgcolor=ft.colors.ERROR
        )

        page.snack_bar.open = True
        page.update()

    def abrir_archivo(e: ft.FilePickerResultEvent):
        cambiar_modo_analizador()

        if not file_picker.result.files == None:
            path_codigo =  file_picker.result.files[0].path
 
            limpiar_campos()

            page.title = path_codigo
            txt_codigo.label = file_picker.result.files[0].name

            txt_codigo.value = open(path_codigo, 'r').read()
            page.update()

    def guarda_archivo(e: ft.FilePickerResultEvent):
        try:
            print('Nombre: ', e.name)
            print('Ruta: ', e.path)

            archivo_temp = open(e.path + '.kcod', 'w')
            archivo_temp.write(txt_codigo.value)
            
            page.title = e.path
            txt_codigo.label = archivo_temp.name.split('\\')[-1]


            archivo_temp.close()

            page.snack_bar = ft.SnackBar(
            ft.Text(f"Guardado en: {e.path}", color=ft.colors.ON_ERROR),
            bgcolor=ft.colors.ERROR
            )
 
            page.snack_bar.open = True

            page.update()


        except:
            desplegar_error('Error al guardar archivo')

    




    prueba_cod = """class mi_program
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
    

end
endclass
    """

    def change_theme_mode(e: None):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            btn_mode_theme.icon = ft.icons.DARK_MODE
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            btn_mode_theme.icon = ft.icons.LIGHT_MODE
        page.update()

    def cambiar_modo_compilador():
        global modo_compilado

        if not modo_compilado:
            contenedor_animado.content = contenedor_sintetizador 
            contenedor_principal.bgcolor = ft.colors.with_opacity(.4, ft.colors.BLUE_300)
            modo_compilado = True


    def cambiar_modo_analizador():
        global modo_compilado

        contenedor_animado.content = contenedor_analizador 
        contenedor_principal.bgcolor = ft.colors.PRIMARY_CONTAINER
        modo_compilado = False


    btn_mode_theme = ft.IconButton(
        icon=ft.icons.LIGHT_MODE if page.theme_mode == ft.ThemeMode.LIGHT else ft.icons.DARK_MODE,
        icon_size=24,
        on_click= change_theme_mode

    )
    
    page.appbar = ft.AppBar(
        title=ft.Text('Analizador Kratos 2.0', size=24),
        # bgcolor=ft.colors.PRIMARY,
        center_title=True,
        actions=[btn_mode_theme, ft.Container(width=15)], 
        

    )

    file_picker = ft.FilePicker(on_result=abrir_archivo)
    page.overlay.append(file_picker)
    file_picker_saver = ft.FilePicker(on_result=guarda_archivo)
    page.overlay.append(file_picker_saver)
    page.update()

    dlg_codigo_correcto = ft.AlertDialog(
        title=ft.Text('Código correcto', ),
        content=ft.Text('El codigo fue analizado y está listo para ser compilado.'),
        actions=[
            ft.TextButton(
                text='Aceptar',
                on_click= lambda _: page.close(dlg_codigo_correcto),
            )
        ]
    )

    
     

    txt_codigo = ft.TextField(
        label="Codigo",
        multiline=True,
        min_lines=50,
        max_lines=50,
        hint_text='// Tu código',
        expand=True,
        expand_loose=True,
        bgcolor=ft.colors.SURFACE,
        value= prueba_cod   ,
        on_change=desactivar_btn_compilador,
        
    )

    columna_izq = ft.Column(
        controls=[txt_codigo],
        expand=True,
        col={"md": 6},
        height=700
    )
    
     

    txt_tabla_simbolos = ft.TextField(
        label="// Tabla de Simbolos",
        multiline=True,
        min_lines=30,
        max_lines=30,
        expand=True,
        expand_loose=True,
        value='',
        read_only=True,
        bgcolor=ft.colors.SURFACE,
        text_style= ft.TextStyle(
            ft.colors.LIGHT_BLUE_800,
        ),
        border_color=ft.colors.LIGHT_BLUE_700,
        border_width=2,
        height=400,
        
    )

    txt_tokens = ft.TextField(
        label="// Tokens",
        multiline=True,
        min_lines=30,
        max_lines=30,
        expand=True,
        expand_loose=True,
        value='',
        read_only=True,
        bgcolor=ft.colors.SURFACE,
        text_style= ft.TextStyle(
            ft.colors.LIGHT_BLUE_800,
        ),
        border_color=ft.colors.LIGHT_BLUE_700,
        border_width=2,
        height=400,
    )

    txt_errores = ft.TextField(
        label="// Errores",
        multiline=True,
        min_lines=30,
        max_lines=30,
        expand=True,
        expand_loose=True,
        value='',
        read_only=True,
        bgcolor=ft.colors.SURFACE, 
        border_color=ft.colors.RED_700,
        border_width=2,
    )

    columna_der = ft.Column(
        controls=[
            ft.Row([txt_tokens,txt_tabla_simbolos]), 
            txt_errores
            ],
        expand=True,
        height=700,
        
    )

    contenedor_analizador = ft.Container(
        content= columna_der,
        col={"md": 6},
        
    )

    txt_cuatruplos = ft.TextField(
        label="Codigo Intermedio",
        multiline=True,
        min_lines=50,
        max_lines=50,
        hint_text='// Cuatruplos',
        expand=True,
        expand_loose=True,
        bgcolor=ft.colors.SURFACE,
        read_only=True,
        
    )

    renglones_prueba = []

    for i in range(45):
        renglones_prueba.append(ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(value=str(i)),),
                    ft.DataCell(ft.Text(value='SV'),),
                    ft.DataCell(ft.Text(value='__R2'),),
                    ft.DataCell(ft.Text(value='None'),),
                    ft.DataCell(ft.Text(value='2'),),
                ]
            ))

    tabla_cautruplos = ft.DataTable(

        columns=[
            ft.DataColumn(label=ft.Text('#'), numeric=True),
            ft.DataColumn(label=ft.Text('OPE')),
            ft.DataColumn(label=ft.Text('OP1')),
            ft.DataColumn(label=ft.Text('OP2')),
            ft.DataColumn(label=ft.Text('RES')),
            
        ],
        # rows=renglones_prueba,
        bgcolor=ft.colors.SURFACE,
        border_radius=3,
        # expand=True,
        data_row_max_height=18,
        column_spacing=12,
        vertical_lines= ft.BorderSide(1, ft.colors.BLUE_300),

    )

    contendedor_tabla_cuatruplos = ft.Container(
        content=ft.Column(
            controls=[tabla_cautruplos],
            scroll=ft.ScrollMode.ALWAYS,
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        expand=True,
        border= ft.border.all(2),
        border_radius=3,
        bgcolor=ft.colors.SURFACE,
        expand_loose=True,
        width=800,
        height=630,
        margin= ft.margin.only(left=10,),
        col={"xs": 8}

    )

    
    txt_pila_saltos = ft.TextField(
        label="Pila de Saltos",
        #expand=True,
        #expand_loose=True,
        # value='',
        read_only=True,
        bgcolor=ft.colors.SURFACE,
        text_style= ft.TextStyle(
            ft.colors.BLACK87,
        ),
        border_color=ft.colors.BLACK87,
        
        border_width=2,

    )

    txt_tabla_variables = ft.TextField(
        label="// Tabla de variables",
        multiline=True,
        min_lines=25,
        max_lines=25,
        expand=True,
        expand_loose=True,
        value='',
        read_only=True,
        bgcolor=ft.colors.SURFACE,
        text_style= ft.TextStyle(
            ft.colors.LIGHT_BLUE_800,
        ),
        border_color=ft.colors.LIGHT_BLUE_700,
        border_width=2,
        height=800,
        col={"xs": 4}
    )


    columna_cuatruplos = ft.Column(
        controls=[txt_pila_saltos, 
        ft.ResponsiveRow(
            controls=[txt_tabla_variables,contendedor_tabla_cuatruplos],
            alignment= ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.START,
            spacing=4,
        )],
        expand=True,
        height=700,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    contenedor_sintetizador = ft.Container(
        content=columna_cuatruplos,
        # bgcolor=ft.colors.TERTIARY_CONTAINER,
        col={'md': 6}, 
        
    )

    btnAbrir = ft.ElevatedButton(
        text='Abrir',
        icon=ft.icons.FILE_OPEN,
        on_click= lambda _: file_picker.pick_files(allowed_extensions=['txt', 'kcod'],allow_multiple=False)
    
    )

    btnGuardar = ft.ElevatedButton(
        text='Guardar',     
        icon=ft.icons.SAVE,
        on_click= lambda _: file_picker_saver.save_file(dialog_title='Guardar archivo como: ', allowed_extensions=['kcod', 'txt'], file_name=txt_codigo.label)
    )

    btnLimpiar = ft.ElevatedButton(
        text='Limpiar',
        icon=ft.icons.CLEANING_SERVICES,
        on_click=limpiar_campos
    )

    btnAnalizar = ft.ElevatedButton(
        text='Analizar',
        icon=ft.icons.SEARCH_SHARP,
        color=ft.colors.AMBER_700,
        on_click= click_analizar,
    )

    btnCompilar = ft.ElevatedButton(
        text='Compilar',
        icon=ft.icons.BUILD_CIRCLE,
        color=ft.colors.BLUE_300,
        on_click= click_compilar,
        disabled=True
    )

    botones = ft.Row(
        controls=[
            ft.Container(ft.Row([btnAbrir,btnGuardar, btnLimpiar,], wrap=True,)) ,
            ft.Container(ft.Row([btnAnalizar, btnCompilar], wrap=True,alignment=ft.MainAxisAlignment.END))
        ],
        #expand=True,
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        scroll=ft.ScrollMode.ALWAYS,
        wrap=True,
        width=10000
        
    )

    txt_pila_operadores = ft.TextField(
        label="Pila de Operadores",
        #expand=True,
        #expand_loose=True,
        # value='', 
        read_only=True,
        bgcolor=ft.colors.SURFACE,
        text_style= ft.TextStyle(
            ft.colors.BLACK87,
        ),
        border_color=ft.colors.BLACK87,
        border_width=2,
    )

    txt_pila_tipos = ft.TextField(
        label="Pila de Tipos",
        #expand=True,
        #expand_loose=True,
        # value='',
        read_only=True,
        bgcolor=ft.colors.SURFACE,
        text_style= ft.TextStyle(
            ft.colors.BLACK87,
        ),
        border_color=ft.colors.BLACK87,
        border_width=2,
    )


    contenedor_animado = ft.AnimatedSwitcher(
        content=contenedor_analizador,
        transition=ft.AnimatedSwitcherTransition.FADE,
        duration=500,
        reverse_duration=400,
        switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
        switch_out_curve=ft.AnimationCurve.BOUNCE_IN,
        col={"md":6},
    )    

    contenedor_principal = ft.Container(
        bgcolor=ft.colors.PRIMARY_CONTAINER,
        padding= 15,
        expand=True,
        border_radius=15,

        content= ft.Column(
            expand=True,

            controls=[
                ft.ResponsiveRow(
                    controls=[columna_izq, contenedor_animado,],
                    expand=True
                ),
            ],
            scroll=ft.ScrollMode.ALWAYS
        )
    )
    
    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    
                    contenedor_principal,
                    
                    txt_pila_operadores,
                    txt_pila_tipos,
                    # txt_pila_saltos,
                    botones
                ],
                expand=True,
                horizontal_alignment= ft.CrossAxisAlignment.CENTER
            ),
            bgcolor=ft.colors.PRIMARY_CONTAINER,
            border_radius=15,
            expand=True,
            padding=10,
        )
    )
    


    txt_codigo.value = prueba_cod


ft.app(main)
