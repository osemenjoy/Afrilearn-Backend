from app import app, db

def init_db():
    with app.app_context():
        db.create_all()
    print("Database initialized!")

if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == 'initdb':
        init_db()
    else:
        app.run(debug=True)
