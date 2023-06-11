

from inertia import inertia


@inertia('inertia.html')
def index(req):
    return {"name": "World"}


