from flask import Flask

app = Flask(__name__)

### route dari html-nya nanti
@app.route('/', methods=['POST'])
def translator():
    ### disini tempat source code dari machine learningnya
    print('dicoba dulu')
    return ('Hello, World!')
