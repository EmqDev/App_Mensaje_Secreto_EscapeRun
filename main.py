import flet
from flet import *
from math import pi
import time
import subprocess


class AnimatedBox(UserControl):
    def __init__(self, border_color, bg_color, rotate_angle):
        self.border_color = border_color
        self.bg_color = bg_color
        self.rotate_angle = rotate_angle
        super().__init__()

    def build(self):
        return Container(
            width=48,
            height=48,
            border=border.all(2.5, self.border_color),
            bgcolor=self.bg_color,
            border_radius=2,
            rotate=transform.Rotate(self.rotate_angle, alignment.center),
            animate_rotation=animation.Animation(700, "easeInOut"),
        )


def main(page: Page):
    page.window_center()
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.padding = padding.only(right=50)
    page.bgcolor = "#0B2D48"


    intentos = Ref
    intentos.current = 3
    
    password = TextField(
                        password=True,
                        hint_text="Ingrese la Contraseña",
                        text_align=TextAlign.CENTER, 
                        border_radius=5,
                        height=100,
                        width=350,
                        border_color=colors.WHITE
                        )

    dlg = AlertDialog(
        title=Text(""),
        content=Text("")
    )

        
    
    def close_dlg(e):
        dlg_modal.open = False
        page.update()

    def open_dlg(e):
        page.dialog = dlg

        if password.value != "1117":
            if intentos.current > 0:
                intentos.current -= 1
            dlg.open = True
            seconds = 5
            dlg.title = Text("Contraseña incorrecta")
            dlg.icon = Icon(icons.NO_ENCRYPTION_GMAILERRORRED, color=colors.RED, size=40)
            if intentos.current == 0:
                dlg.content = Text("por seguridad el sistema se reiniciara en %d segundos." % seconds)
                subprocess.run("shutdown -r -t %d" % seconds)
            else:
                dlg.content = Text(f"Cantidad de intentos restantes: {intentos.current}")
        else:
            dlg.open = True
            dlg.title = Text("Contraseña correcta")

            dlg.content = Text("El mensaje secreto es: ")
            dlg.icon = Icon(icons.LOCK_OPEN_OUTLINED, color=colors.GREEN, size=40)
        password.value = ""
        page.update()


    dlg_modal = AlertDialog(
        modal=True,
        title=Text("Información"),
        content=Text("VaultChest es un programa diseñado para guardar de manera segura las contraseñas de laboratorio.\nLos usuarios pueden intentar ingresar la contraseña hasta tres veces.\nSi se equivocan más de tres veces, por motivos de seguridad, la computadora se reiniciará y deberán probar nuevamente."),
        actions=[
            TextButton("cerrar", on_click=close_dlg),
        ],
        actions_alignment = MainAxisAlignment.END
    )

    def open_dlg_modal(e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()

    def animate_boxes():
        clock_wise_rotate = pi / 4
        counter_clock_wise_rotate = -pi * 2
        red_box = page.controls[0].content.content.controls[1].controls[0].controls[0]
        blue_box = page.controls[0].content.content.controls[1].controls[1].controls[0]
        counter = 0
        while True:
            if counter >= 0 and counter <= 4:
                red_box.rotate = transform.Rotate(
                    counter_clock_wise_rotate, alignment.center
                )
                blue_box.rotate = transform.Rotate(clock_wise_rotate, alignment.center)

                red_box.update()
                blue_box.update()

                clock_wise_rotate += pi / 2
                counter_clock_wise_rotate -= pi / 2

                counter += 1

                time.sleep(0.70)

            if counter >= 5 and counter <= 10:
                clock_wise_rotate -= pi / 2
                counter_clock_wise_rotate += pi / 2

                red_box.rotate = transform.Rotate(
                    counter_clock_wise_rotate, alignment.center
                )
                blue_box.rotate = transform.Rotate(clock_wise_rotate, alignment.center)

                red_box.update()
                blue_box.update()

                counter += 1

                time.sleep(0.70)

            if counter > 10:
                counter = 0

    page.add(
        Card(
            width=408,
            height=612,
            elevation=15,
            
            content=Container(
                
                image_src="asset\laboratorio.jpg",
                image_fit=ImageFit.COVER,
                image_opacity=.2,
                bgcolor="black",
                
                border_radius=6,
                content=Column(
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        
                        Divider(height=60, color="transparent"),
                        Stack(
                            controls=[
                                AnimatedBox("#e9665a", None, 0),
                                AnimatedBox("#7df6dd", None, pi / 4),
                            ]
                        ),
                        
                        Divider(height=60, color="transparent"),
                        Column(
                            alignment=MainAxisAlignment.CENTER,
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            spacing=5,
                            controls=[
                                
                                Text("VaultChest", size=30, weight="bold"),
                                Text(
                                    "VaultChest securely stores laboratory passwords.",
                                    size=13,
                                    weight="bold",
                                ),
                                
                            ],
                        ),
                        Divider(height=1, color="transparent"),
                        password,
                        Divider(height=1, color="transparent"),
                        ElevatedButton("Confirmar", on_click=open_dlg), 
                        Divider(height=5, color="transparent"),
                        FloatingActionButton(icon=icons.HELP, on_click=open_dlg_modal,),
                        Divider(height=8, color="transparent"),
                        Text(
                            "Colegio Rio de la Plata || Escape Room 2024",
                            size=10,
                            color="white54",
                        ),
                    ],
                ),
            ),
        )
    )
    page.update()
    animate_boxes()


if __name__ == "__main__":
    flet.app(target=main)
