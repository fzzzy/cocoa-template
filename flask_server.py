

from flask import Flask, request, Response
from flask_inertia import Inertia, render_inertia

import json

from lambda_api_gateway_hello import lambda_handler


SECRET_KEY = "alsjdfal;osudfgha;lsuehgf;alsuegha;sliegh1;lo3u5yto923yg!"
INERTIA_TEMPLATE = "base.html"

app = Flask(__name__)
app.config.from_object(__name__)

inertia = Inertia(app)


def flask_to_lambda_event(req):
    headers = {k: v for k, v in req.headers}

    return {
        'body': req.data if req.data else json.dumps(req.json) if req.json else None,
        'headers': headers,
        'httpMethod': req.method,
        'isBase64Encoded': False,
        'path': req.path,
        'pathParameters': req.view_args,
        'queryStringParameters': req.args,
        'stageVariables': {},
        'requestContext': {},
        'resource': ''
    }


def lambda_to_flask_response(result):
    status_code = result['statusCode']
    headers = result['headers']
    body = result['body']

    flask_response = Response(body, status=status_code, headers=headers)
    return flask_response


@app.route("/")
def index():
    return render_inertia("Index", {"name": "orldW!1ss"})


@app.route("/test/")
def test():
    return render_inertia("Test", {"foo": "bar"})

