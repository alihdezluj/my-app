import os

import flet as ft
import httpx

API_URL = "https://my-app-t2fs.onrender.com/books"


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


if __name__ == "__main__":
    ft.run(
        main,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000)),
        web_renderer=ft.WebRenderer.HTML,
    )
