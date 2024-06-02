from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

"""
@app.get('/', status_code=HTTPStatus.OK, response_model=Message, response_class=HTMLResponse)
def read_root():
    return {'message': 'Olá mundo através do FastApi'}
"""


@app.get('/', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def read_dot():
    return """
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>"""
