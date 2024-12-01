
from app import create_app

app = create_app()

if __name__ == '__main__':
    print("STARTING APP")
    app.run(debug=True)
