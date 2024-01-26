import math
import flet
import flet.canvas


def main(page: flet.Page):
    stroke_paint = flet.Paint(stroke_width=2, style=flet.PaintingStyle.STROKE)
    fill_paint = flet.Paint(style=flet.PaintingStyle.FILL)
    flet_canvas = flet.canvas.Canvas(
        [
            ## Face
            flet.canvas.Circle(100, 100, 50, stroke_paint),  # x, y, radius, paint
            ## Eyes
            flet.canvas.Circle(80, 90, 5, stroke_paint),
            flet.canvas.Circle(80, 90, 4, fill_paint),
            flet.canvas.Circle(120, 90, 5, stroke_paint),
            flet.canvas.Circle(120, 90, 4, fill_paint),
            ## Smile
            flet.canvas.Arc(
                70, 98, 60, 36, 0, math.pi, paint=stroke_paint
            ),  # x, y, width, height, start_angle, sweep_angle, paint
        ],
        width=float("inf"),
        expand=True,
    )

    page.title = "Smiley"
    page.window_width = 250
    page.window_height = 275
    page.theme_mode = flet.ThemeMode.LIGHT

    page.add(flet_canvas)


flet.app(main)
