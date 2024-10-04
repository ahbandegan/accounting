from flet import *
import flet as ft


def main(page: Page):
    def add(e):
        if _price.value != "":
            if _for.value == "": _for.value = "None"
            _price.error_text = None
            id.value = str(int(id.value)+1)
            if _price.value[0] == "-":
                table.rows.append(
                    DataRow(
                        cells=[
                            DataCell(Text(f"{id.value}:", size=20, color="#000000")),
                            DataCell(Text(f"{_for.value}", size=20, color="#000000")),
                            DataCell(Text(f"${_price.value}", size=20, color="#660000")),
                        ],
                    )
                )
                money.value = str(int(_price.value) + int(money.value))
                _price.value = ""
                _for.value = ""

            else:
                table.rows.append(
                    DataRow(
                        cells=[
                            DataCell(Text(f"{id.value}:", size=20, color="#000000")),
                            DataCell(Text(f"{_for.value}", size=20, color="#000000")),
                            DataCell(Text(f"${_price.value}", size=20, color="#006600")),
                        ],
                    )
                )
                money.value = str(int(_price.value) + int(money.value))
                _price.value = ""
                _for.value = ""
            page.update()

        elif _price.value == "":
            _price.error_text = "filling fild"
            page.update()

    def clear(e):
        table.rows.clear()
        id.value = "0"
        money.value = "0"
        page.update()


    page.appbar = AppBar(
        title=ft.Row(
            [
                Text(f"money:$", size=25),
                money := Text("0", size=25)
            ]
        ),
        actions=[
            FloatingActionButton(icon=icons.DELETE, on_click=clear),
            Container(width=8)
        ]
    )
    table = DataTable(
        columns=[
            DataColumn(Text("id", size=20, color="#000000")),
            DataColumn(Text("for", size=20, color="#000000")),
            DataColumn(Text("price", size=20, color="#000000")),
        ],
    )
    id = Text("0")
    main_page = Column(
        [
            Divider(height=5),
            ft.Row(
                [
                    _for := TextField(
                        hint_text="for",
                        width=200,
                        border_width=2,
                        border_radius=20
                    ),
                    _price := TextField(
                        hint_text="price",
                        width=200,
                        border_width=2,
                        border_radius=20,
                        max_length=19
                    ),
                    FloatingActionButton(
                        icon=icons.ADD,
                        on_click=add
                    )
                ]
            ),
            ft.Row(
                [
                    Card(
                        content=Column(
                            [
                                table
                            ],
                            scroll=ScrollMode.AUTO,
                            height=280,
                            width=465,
                        ),
                        color="#ffffff",
                    )
                ]
            )
        ]
    )


    page.title = "accounting"
    page.window.width = 510
    page.window.height = 500
    page.add(
        main_page,
    )


app(main)