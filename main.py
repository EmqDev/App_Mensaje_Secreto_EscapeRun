import flet as ft
import subprocess


def main(page: ft.Page):

    #propiedades de la pagina
    page.title = "Password Secret App"
    page.window_center()
    page.window_height=800
    page.window_width=600
    
    
    
    dlg = ft.AlertDialog(
        title=ft.Text(""),
        content=ft.Text("")
    )

    
    password = ft.TextField(password=True,hint_text="Ingrese la Contraseña")

    text_custom = ft.Text(  
                            spans=[
                                
                                ft.TextSpan(
                                    "Rio Labs",
                                    
                                    ft.TextStyle(
                                        size=40,
                                        weight=ft.FontWeight.BOLD,
                                        foreground=ft.Paint(
                                            gradient=ft.PaintLinearGradient(
                                                (0, 20), (150, 20), [ft.colors.BLUE, ft.colors.GREEN]
                                            )
                                        ),
                                    ),
                                ),
                            ],
                            text_align = ft.TextAlign.CENTER,
                            
                        )

    def close_dlg(e):
        dlg_modal.open = False
        page.update()

    def open_dlg(e):
        page.dialog = dlg
        if password.value != "hola":
            dlg.open = True
            seconds = 5
            dlg.title = ft.Text("Contraseña incorrecta")
            dlg.content = ft.Text("por seguridad el sistema se reiniciara en %d segundos." % seconds)
            dlg.icon = ft.Icon(ft.icons.NO_ENCRYPTION_GMAILERRORRED, color=ft.colors.RED, size=40)
            #subprocess.run("shutdown -r -t %d" % seconds)
        else:
            dlg.open = True
            dlg.title = ft.Text("Contraseña correcta")

            dlg.content = ft.Text("El mensaje secreto es: ")
            dlg.icon = ft.Icon(ft.icons.LOCK_OPEN_OUTLINED, color=ft.colors.GREEN, size=40)
        password.value = ""
        page.update()


    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Info"),
        content=ft.Text("tendras tres intentos para resolver, luego se reiniciara la pc"),
        actions=[
            ft.TextButton("cerrar", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END
    )

    def open_dlg_modal(e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()

    

    page.add(
        ft.Rive(
            "lab.riv",
            placeholder=ft.ProgressBar(),
            width=600,
            height=400,
            alignment=ft.alignment.center,
        ),
        text_custom,password,
        ft.ElevatedButton("Confirmar", on_click=open_dlg), 
        ft.FloatingActionButton(icon=ft.icons.HELP, on_click=open_dlg_modal),
        )
    
    

ft.app(target=main)