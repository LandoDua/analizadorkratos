import flet as ft
import AnalizadorKratos

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
    128: '%',
    117: 'and',
    118: 'or',
    110: '==',
    114: '>=',
    112: '<=',
    115: '!=',
}


def main(page: ft.Page):
    page.title = 'Analizador Kratos'
    #page.window.width = 1100
    #page.window.height = 600
    page.fonts = {
        'JetBrains' : 'fonts/JetBrainsMono-VariableFont_wght.ttf'
    }
    page.theme = ft.Theme(
        color_scheme_seed=ft.colors.CYAN,
        font_family='JetBrains'
    )
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding= 15


    def clic_analizar(e = None):
        codigo = str(txt_codigo.value)
        codigo = codigo.replace('\n', r' ')
        
        #print('CODIGO: ', codigo[0], type(codigo[0]))

        strTokens = ''
        strTokens , strErrores, codigo_correcto, tabla_simbolos, pila_tipos, pila_operadores = AnalizadorKratos.analizador(codigo)
        strErrores = '\n' + strErrores
        strErrores = strErrores.replace('\n:	 e506: . o _ invalidos, caractert desconocido', '')

        # txt_tokens.value = strTokens
        txt_errores.value = strErrores
        
        if codigo_correcto:
            btnCompilar.disabled = False

        renglon_tabla_simbolos = ''

        txt_tokens.value = ''
        for variable in tabla_simbolos:
            tipo = tabla_simbolos[variable]
            renglon_tabla_simbolos = f'{variable}:\t {code_to_strig[tipo]}\n'
            txt_tokens.value += renglon_tabla_simbolos

        txt_pila_tipos.value = ''
        for tipo in pila_tipos:
            txt_pila_tipos.value += f'{code_to_strig[tipo]}, '

        txt_pila_operadores.value = ''
        for operador in pila_operadores:
            txt_pila_operadores.value += f'{code_to_strig[operador]}, '




        page.update()

    def limpiar_campos(e=None):
        txt_codigo.value = ''
        txt_tokens.value = ''
        txt_errores.value = ''
        txt_pila_tipos = ''
        txt_pila_operadores = ''

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
        #print(f'{file_picker.result.files[0].path}')

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
            # print('Error al guardar archivo')
            desplegar_error('Error al guardar archivo')

    




    prueba_cod = """class mi_program
def public A,B, res as int;
def private X as float;

main()
   input(A,B);
   res = A+ B;
   output("El resultado es: ", res);
   input(X);
   if (X == res)
       output ("son iguales");
   else
      input(Y);
      if (X != Y)
         output("no son iguales");
      endif
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

    
     

    txt_codigo = ft.TextField(
        label="Codigo",
        multiline=True,
        min_lines=50,
        max_lines=50,
        hint_text='// Tu código',
        expand=True,
        expand_loose=True,
        bgcolor=ft.colors.SURFACE,
        value= prueba_cod   
    )

    columna_izq = ft.Column(
        controls=[txt_codigo],
        expand=True,
    ) 

    txt_tokens = ft.TextField(
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
        controls=[txt_tokens, txt_errores],
        expand=True,
        
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
        on_click= clic_analizar,
    )

    btnCompilar = ft.ElevatedButton(
        text='Compilar',
        icon=ft.icons.BUILD_CIRCLE,
        color=ft.colors.BLUE_300,
        # on_click= clic_analizar,
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
        #read_only=True,
        bgcolor=ft.colors.SURFACE,
        text_style= ft.TextStyle(
            ft.colors.BLACK87,
        ),
        border_color=ft.colors.BLACK87,
        border_width=2,
    )

    contenedor_principal = ft.Container(
        bgcolor=ft.colors.PRIMARY_CONTAINER,
        padding= 15,
        expand=True,
        border_radius=15,

        content= ft.Column(
            expand=True,

            controls=[
                ft.Row(
                    controls=[columna_izq, columna_der],
                    expand=True
                ),
                txt_pila_operadores,
                txt_pila_tipos,
                botones
            ]
        )
    )
    
    page.add(
        ft.Column(
            controls=[
                
                contenedor_principal,
            ],
            expand=True,
            horizontal_alignment= ft.CrossAxisAlignment.CENTER
        )
    )
    


    txt_codigo.value = prueba_cod

ft.app(main)
