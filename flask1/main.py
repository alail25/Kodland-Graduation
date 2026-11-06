from flask import Flask, render_template, send_file
import random
import os

app = Flask(__name__)

# Home/1st page
@app.route("/")
def pertama():
    # <a> anchor tag with its attribute
    return "<h1>Hello, World!</h1><br><p>Nice to see you</p><p>please check</p><a href='/random_fact'>View a random fact!</a><br><a href='/modern_fact'>View a modern fact!</a> <br><a href='/random_photo'>View a random photo!</a>"
# 2nd page
@app.route("/random_fact")
def kedua():
    txt_name = random.choice(os.listdir("fact_list"))
    # formatted string
    with open(f'fact_list/{txt_name}', 'r') as f:
        document = f.read()
    return f'{document}'

# 3rd page
@app.route('/modern_fact')
def index():
    return render_template('dasar.html')  # folder templates

# 4th page
@app.route("/random_photo")
def ketiga():
    images = [name for name in os.listdir("static") if name.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]
    img_name = random.choice(images)
    return send_file(os.path.join("static", img_name))

if __name__ == '__main__':
    app.run(debug=True)