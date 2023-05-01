from app import app

if __name__ == '__main__':
    app.run(debug=True,port=8000)
    print(f"Flask app running at http://localhost:8000/")

