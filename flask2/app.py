from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config['UPLOAD_PATH'] = 'static/images'

@app.route('/')
def show_aadhaar_front():
    sample_data = {
        "name": "Pavan Kumar",
        "dob": "01-Jan-2000",
        "gender": "Male",
        "address": "123, MG Road, Bengaluru, Karnataka, India - 560001",
        "aadhaar_number": "1234 5678 9012",
        "photo_url": url_for('static', filename='images/Pavan 194kb.jpg'),
        "aadhaar_logo": url_for('static', filename='images/img.png'),
        "fingerprint_logo": url_for('static', filename='images/fingerprint.png'),
        "emblem_logo": url_for('static', filename='images/emblem.png')
    }

    return render_template('adhar.html', **sample_data)

if __name__ == '__main__':
    app.run(debug=True)