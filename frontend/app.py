import flet as ft
import httpx

API_URL = "http://127.0.0.1:8000/books"


def main(page: ft.Page):

    lista = ft.Column()

    def cargar_libros(e):
        r = httpx.get(API_URL)
        books = r.json()

        lista.controls.clear()

        for book in books:
            lista.controls.append(ft.Text(book["title"]))

        page.update()

    page.title = "Flet + FastAPI App"

    page.add(ft.ElevatedButton("Cargar libros", on_click=cargar_libros), lista)


ft.app(target=main)
