from flet import App, Page, Text

# Birinci form (page)
form1 = Page(
    title="Form 1",
    content=Text("Bu birinci formun içeriği")
)

# İkinci form (page)
form2 = Page(
    title="Form 2",
    content=Text("Bu ikinci formun içeriği")
)

# Uygulamayı başlat
App(form1).run()
