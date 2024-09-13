import flet as ft
import AnalizadorKratos


def main(page: ft.Page):
    page.title = 'Analizador Kratos'
    #page.window.width = 1100
    #page.window.height = 600
    page.theme = ft.Theme(
        color_scheme_seed=ft.colors.PINK
    )
    page.theme_mode = ft.ThemeMode.LIGHT
    #page.add(ft.SafeArea(ft.Text("Analizador Kratos1", text_align='center', expand=True),))

    def clic_analizar(e = None):

        strTokens, strErrores = AnalizadorKratos.analizador(txt_codigo.value)
        txt_tokens.value = strTokens
        txt_errores.value = strErrores

        page.update()

        pass

    txt_codigo = ft.TextField(
        label="// Código",
        multiline=True,
        min_lines=50,
        max_lines=50,
        hint_text='// Tu código',
        expand=True,
        expand_loose=True,
        bgcolor=ft.colors.SURFACE,
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
        value=' ',
        read_only=True,
        bgcolor=ft.colors.SURFACE,
    )

    txt_errores = ft.TextField(
        label="// Errores",
        multiline=True,
        min_lines=30,
        max_lines=30,
        hint_text='// Tu código',
        expand=True,
        expand_loose=True,
        value=' ',
        read_only=True,
        bgcolor=ft.colors.SURFACE,
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
        ]
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
                    ),
                contenedor_principal,
            ],
            expand=True,
            horizontal_alignment= ft.CrossAxisAlignment.CENTER
        )
    )
    

ft.app(main)
