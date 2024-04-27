import flet
from flet import Page, colors
from calculator import create_app

def main(page: Page):
    page.title = "Calculator"
    page.window_height = 340
    page.window_width = 385
    page.bgcolor = colors.WHITE
    calc_app = create_app()
    page.add(calc_app)

flet.app(target=main)
