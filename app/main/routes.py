from app.main import bp

@bp.route('/', methods=['GET'])
def index():
    return 'Hello, World!'