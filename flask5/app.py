from flask import Flask,render_template
from forms import  HelloForm
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        return render_template('hello.html',name=name)
    return render_template('form.html',form=form)
if __name__ == '__main__':
     app.run(debug= False)
