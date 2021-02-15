# import os
import csv

import flask


app = flask.Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/<page_name>')
def display_page(page_name=None):
    if page_name == 'components.html':
        return flask.Response(status=404)
    else:
        return flask.render_template(page_name)


# @app.route('/favicon.ico')
# def favicon():
#     path = os.path.join(app.root_path, 'static')
#     return flask.send_from_directory(
#         'path',
#         'favicon.ico',
#         mimetype='image/vnd.microsoft.icon'
#     )


def write_to_file(data):
    with open('database.txt', mode='a') as db:
        email = data['email']
        subject = data['subject']
        message = data['message']
        db.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a') as db2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(db2, delimiter=',')
        csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if flask.request.method == 'POST':
        data = flask.request.form.to_dict()
        write_to_csv(data)
        return flask.redirect('/thank_you.html')
    else:
        return 'something went wrong, try again'


if __name__ == '__main__':
    app.run(port=5000, debug=True)
