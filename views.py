from flask import Flask, render_template, request

import random
import get_cats

app = Flask(__name__)
app.debug = True
cssdata = open('static/css/my_css.css').read()


@app.route('/')
def hello():
    return 'hello, wrodl!'


@app.route('/cats', methods=['GET', 'POST'])
def cats():
    name = 'Mr. Andersen'
    if 'love_cats?' in request.form:
        if request.form.get('love_cats?') == 'I<3Cats':
            name = 'Cat Lover Mc. Cat'
        elif request.form.get('love_cats?') == 'I<3Birds':
            name = 'Birdy Lover Mc. Bird'
        result = get_cats.download_random_animal_list(
            request.form.get('love_cats?', 'I<3Birds'))
        
        random.shuffle(result.ids)
        random.shuffle(result.names)

        lines = ["%s - %s" % (id, name) for id, name in
                 zip(result.ids, result.names)]

        return render_template('youtube_cats.html', name=name, lines=lines,
                               ids=result.ids, names=result.names,
                               cssdata=cssdata)

    return render_template('simple_cats.html', name=name,
                           cssdata=cssdata)
    

if __name__ == '__main__':
    app.run()
