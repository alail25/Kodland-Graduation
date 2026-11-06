# Import
from flask import Flask, render_template, request, redirect, session
# Menghubungkan perpustakaan database
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
# Menghubungkan SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '@strong_secret_key'

# Membuat sebuah DB
db = SQLAlchemy(app)

# Membuat sebuah tabel card
class Card(db.Model):
    # Membuat kolom-kolom
    # id(kolom #1)
    id = db.Column(db.Integer, primary_key=True)
    # Judul
    title = db.Column(db.String(100), nullable=False)
    # Deskripsi
    subtitle = db.Column(db.String(300), nullable=False)
    # Teks up to 30 000 char
    text = db.Column(db.Text, nullable=False)
    # User ID as foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # Relationship to User model
    user = db.relationship('User', backref=db.backref('cards', lazy=True))

    #Parameterized Constructor accepts additional arguments
    def __init__(self, title, subtitle, text, user_id):
        self.title = title
        self.subtitle = subtitle
        self.text = text
        self.user_id = user_id

    # Menampilkan objek dan id
    # The __repr__ method is a special method in Python that defines how an object
    # should be represented as a string.
    # It is used to provide a human-readable representation of the object, typically
    # for debugging purposes.
    def __repr__(self):
        return f'<Card {self.id}>'

# Tugas #1. Membuat tabel Pengguna
class User(db.Model):
    # Membuat kolom
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    #Parameterized Constructor accepts additional arguments
    def __init__(self, login, password_hash):
        self.login = login
        self.password_hash = password_hash

# Menjalankan halaman utama
@app.route('/', methods=['GET','POST'])
def login():
    error = ''
    if request.method == 'POST':
        form_login = request.form['email']
        form_password = request.form['password']

        # Tugas #2. Menerapkan otorisasi
        users_db = User.query.all()
        for user in users_db:
            if form_login == user.login and check_password_hash(user.password_hash, form_password):
                # Store user ID in session
                session['user_id'] = user.id
                return redirect('/index')
        error = 'Login atau kata sandi tidak tepat'
    return render_template('login.html', error=error)

# Halaman sign up
@app.route('/reg', methods=['GET','POST'])
def reg():
    if request.method == 'POST':
        login= request.form['email']
        password = request.form['password']
        hashed_pw = generate_password_hash(password)
        #Tugas #3. Buat agar data pengguna direkam ke dalam database
        user = User(login=login, password_hash=hashed_pw)
        db.session.add(user)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('registration.html')


# Menjalankan halaman konten
@app.route('/index')
def index():
    # Check if user is logged in
    if 'user_id' not in session:
        return redirect('/')

    # Get the logged-in user's ID
    user_id = session['user_id']

    # Add datetime.now()
    from datetime import datetime
    now = datetime.now()

    # Menampilkan catatan-catatan dari database for the logged-in user
    cards = Card.query.filter_by(user_id=user_id).order_by(Card.id).all()
    return render_template('index.html', cards=cards, now=now)

# Menjalankan halaman dengan entri tersebut
@app.route('/card/<int:id>')
def card(id):
    if 'user_id' not in session:
        return redirect('/')

    card = Card.query.get_or_404(id)

    if card.user_id == session['user_id']:
        return render_template('card.html', card=card, now=datetime.now())
    return "Unauthorized", 403

# Menjalankan halaman pembuatan entri
@app.route('/create')
def create():
    # Check if user is logged in
    if 'user_id' not in session:
        return redirect('/')

    return render_template('create_card.html')

# Formulir entri
@app.route('/form_create', methods=['GET','POST'])
def form_create():
    # Check if user is logged in
    if 'user_id' not in session:
        return redirect('/')

    if request.method == 'POST':
        title =  request.form['title']
        subtitle =  request.form['subtitle']
        text =  request.form['text']

        # Get the logged-in user's ID
        user_id = session['user_id']

        # Membuat objek yang akan dikirim ke DB
        card = Card(title=title, subtitle=subtitle, text=text, user_id=user_id)
        db.session.add(card)
        db.session.commit()
        return redirect('/index')
    else:
        return render_template('create_card.html')

@app.route('/delete/<int:id>')
def delete(id):
    # Check if user is logged in
    if 'user_id' not in session:
        return redirect('/')

    card = Card.query.get_or_404(id)

    # Check if the card belongs to the logged-in user
    if card.user_id == session['user_id']:
        try:
            db.session.delete(card)
            db.session.commit()
            return redirect('/index')
        except:
            return 'Terjadi kesalahan saat menghapus entri'
    else:
        return "Unauthorized", 403

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect('/')

@app.route('/edit/<int:id>', methods=['GET'])
def edit(id):
    # Check if user is logged in
    if 'user_id' not in session:
        return redirect('/')

    # Get the card or return 404 if not found
    card = Card.query.get_or_404(id)

    # Check if the card belongs to the logged-in user
    if card.user_id == session['user_id']:
        return render_template('edit_card.html', card=card)
    else:
        return "Unauthorized", 403

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    # Check if user is logged in
    if 'user_id' not in session:
        return redirect('/')

    card = Card.query.get_or_404(id)

    # Check if the card belongs to the logged-in user
    if card.user_id == session['user_id']:
        try:
            card.title = request.form['title']
            card.subtitle = request.form['subtitle']
            card.text = request.form['text']

            db.session.commit()
            return redirect('/index')
        except:
            return 'Terjadi kesalahan saat memperbarui entri'
    else:
        return "Unauthorized", 403

# if __name__ == "__main__":
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)
@app.after_request
def set_security_headers(response):
    response.headers["Strict-Transport-Security"] = "max-age=63072000; includeSubDomains; preload"
    response.headers["Content-Security-Policy"] = "default-src 'self'; script-src 'self'; object-src 'none'; base-uri 'self'; frame-ancestors 'none';"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Referrer-Policy"] = "no-referrer"
    response.headers["Permissions-Policy"] = "camera=(), geolocation=(), microphone=()"
    return response

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)