from app import app
import os

port = int(os.environ.get('PORT', 10000))

if __name__ == "__main__":
    app.run(debug=False, port=port) 

