"""Blueprint for the index route."""

index = Blueprint('index', __name__)

@index.route('/')
async def home():
    return '<h1>Hello, World!</h1>'