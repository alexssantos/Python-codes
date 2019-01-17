from app import app     
# do modulo(pasta) app, importe (do __init__.py) a variavel 'app'   // modulo + variavel


@app.route("/")
def index():
    return "Hollo, World!"
