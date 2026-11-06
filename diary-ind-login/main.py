# Mengimpor library
from flask import Flask, render_template, request, redirect, session
# Menghubungkan library database
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# Mengatur secret key untuk session
app.secret_key = 'my_top_secret_123'
# Menjalankan koneksi SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Membuat database
db = SQLAlchemy(app)
# Membuat tabel

class Card(db.Model):
    # Menentukan field entri
    # id
    id = db.Column(db.Integer, primary_key=True)
    # Judul
    title = db.Column(db.String(100), nullable=False)
    # Subjudul
    subtitle = db.Column(db.String(300), nullable=False)
    # Teks isi
    text = db.Column(db.Text, nullable=False)
    # Email pemilik card
    user_email = db.Column(db.String(100), nullable=False)

    # Menampilkan objek dan ID-nya
    def __repr__(self):
        return f'<Card {self.id}>'
    

# Tugas #1. Buat tabel User


# Menjalankan halaman konten
@app.route('/', methods=['GET','POST'])
def login():
    error = ''
    if request.method == 'POST':
        form_login = request.form['email']
        form_password = request.form['password']
            
        # Tugas #4. Implementasikan verifikasi pengguna

     
    else:
        return render_template('login.html')



@app.route('/reg', methods=['GET','POST'])
def reg():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Tugas #3. Implementasikan penyimpanan data pengguna


        
        return redirect('/')
    
    else:    
        return render_template('registration.html')


# Menjalankan halaman konten
@app.route('/index')
def index():
    # Tugas #4. Pastikan pengguna hanya melihat card miliknya sendiri
    cards = Card.query.order_by(Card.id).all()
    return render_template('index.html', cards=cards)

# Menjalankan halaman card
@app.route('/card/<int:id>')
def card(id):
    card = Card.query.get(id)

    return render_template('card.html', card=card)

# Menjalankan halaman pembuatan card
@app.route('/create')
def create():
    return render_template('create_card.html')

# Form card
@app.route('/form_create', methods=['GET','POST'])
def form_create():
    if request.method == 'POST':
        title =  request.form['title']
        subtitle =  request.form['subtitle']
        text =  request.form['text']

        # Tugas #4. Pastikan pembuatan card dilakukan atas nama pengguna
        card = Card(title=title, subtitle=subtitle, text=text)

        db.session.add(card)
        db.session.commit()
        return redirect('/index')
    else:
        return render_template('create_card.html')

if __name__ == "__main__":
    app.run(debug=True)
