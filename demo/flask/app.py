
app = Flask(__name__)


class Webbits:
    def __init__(self, app):
        self.app = app
        self.components = set()

    def register(self, component):
        self.components.add(component)


def component(x):
    return x

@component
class Page:
    pass


webbits = Webbits(app)
webbits.register(Page)

app.run(debug=True)
