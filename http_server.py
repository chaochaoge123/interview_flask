from core import app
from api_info import *



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8002, debug=app.debug)
