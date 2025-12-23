class HTML:
    def __init__(self):
        self._code = []
        self._context = []

    def __getattr__(self, tag_name):
        return Tag(tag_name, self)

    def add_line(self, line, indent_level=0):
        indent = '  ' * indent_level
        self._code.append(f"{indent}{line}")

    def get_code(self):
        return '\n'.join(self._code)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class Tag:
    def __init__(self, tag_name, html_instance):
        self.tag_name = tag_name
        self.html = html_instance

    def __enter__(self):
        self.html.add_line(f"<{self.tag_name}>", len(self.html._context))
        self.html._context.append(self.tag_name)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.html._context.pop()
        self.html.add_line(f"</{self.tag_name}>", len(self.html._context))

    def __call__(self, text=None):
        if text is not None:
            indent_level = len(self.html._context)
            self.html.add_line(f"<{self.tag_name}>{text}</{self.tag_name}>", indent_level)
        return self

html = HTML()
with html.body():
    with html.div():
        with html.div():
            html.h1('Первая строка.')
            html.p('Вторая строка.')
        with html.div():
            html.p('Третья строка.')

print(html.get_code())