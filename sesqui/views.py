

from inertia import inertia


@inertia('Index.html')
def index(req):
    return {"name": "World"}


@inertia('Test.html')
def test(req):
    return {"foo": "bar"}

