import flet as ft
import AnalizadorKratos


def main(page: ft.Page):
    page.title = 'Analizador Kratos'
    #page.window.width = 1100
    #page.window.height = 600
    page.fonts = {
        'JetBrains' : 'fonts/JetBrainsMono-VariableFont_wght.ttf'
    }
    page.theme = ft.Theme(
        color_scheme_seed=ft.colors.PINK,
        font_family='JetBrains'
    )
    page.theme_mode = ft.ThemeMode.LIGHT
    #page.add(ft.SafeArea(ft.Text("Analizador Kratos1", text_align='center', expand=True),))

    def clic_analizar(e = None):
        codigo = str(txt_codigo.value)
        codigo = codigo.replace('\n', r' ')
        
        #print('CODIGO: ', codigo[0], type(codigo[0]))

        strTokens = ''
        strTokens, strErrores = AnalizadorKratos.analizador(codigo)

        strErrores = '\n' + strErrores
        strErrores = strErrores.replace('\n:	 e506: . o _ invalidos, caractert desconocido', '')

        txt_tokens.value = strTokens
        txt_errores.value = strErrores

        page.update()

    def limpiar_campos(e=None):
        txt_codigo.value = ''
        txt_tokens.value = ''
        txt_errores.value = ''
        page.update()

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

    txt_codigo = ft.TextField(
        label="// Código",
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
        expand_loose=True,
    )

    txt_tokens = ft.TextField(
        label="// Token",
        multiline=True,
        min_lines=30,
        max_lines=30,
        hint_text='// Tu código',
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
        hint_text='// Tu código',
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
        expand_loose=True,
    )

    btnAbrir = ft.ElevatedButton(
        text='Abrir',
        icon=ft.icons.FILE_OPEN,
    )

    btnGuardar = ft.ElevatedButton(
        text='Guardar',     
        icon=ft.icons.SAVE,
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

    botones = ft.Row(
        controls=[
            btnAbrir,btnGuardar, btnLimpiar, btnAnalizar
        ],
        #expand=True,
        alignment=ft.MainAxisAlignment.START,
        scroll=ft.ScrollMode.ALWAYS,
        wrap=True,
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
                botones
            ]
        )
    )
    
    page.add(
        ft.Column(
            controls=[
                ft.Text(
                    value='Analizador Kratos 2.0',
                    size=24,
                    ),
                contenedor_principal,
            ],
            expand=True,
            horizontal_alignment= ft.CrossAxisAlignment.CENTER
        )
    )
    


    txt_codigo.value = prueba_cod

ft.app(main)
