from flask import Flask, request, render_template
from flask_cors import CORS


app = Flask(__name__, static_url_path='/', static_folder='.',
            template_folder='./')
cors = CORS(app)

def newbib(bib):
    from pybtex.database import parse_string, BibliographyData
    from time import strptime

    bib_data = parse_string(bib, bib_format='bibtex')

    dates, oldkeys, keys, entries = [], [], [], []
    for index, key in enumerate(bib_data.entries):
        oldkeys.append(key)
        entry = bib_data.entries[key]
        dates.append(strptime(entry.fields['month'],'%B').tm_mon)
        new_key = str(entry.persons['author'][0].rich_last_names[0]) + ":" + entry.fields['year']
        keys.append(new_key)
        entries.append(entry)

    # Trying to avoid same keys
    suffix = "abcdefghijklmnopqrstuvwxyz"
    import numpy as np
    for key in keys:
        mask = np.where(np.array(keys) == key)[0]
        if len(mask) > 1:
            date = np.array(dates)[mask]
            sort = np.argsort(date)
            for suffix_index, key_index in enumerate(mask):
                keys[key_index] += suffix[sort[suffix_index]]

    # Remove space
    keys = [key.replace(" ", "") for key in keys]


    for okey, nkey in zip(oldkeys, keys):
        bib = bib.replace('{'+okey, '{'+nkey)
        # Verbose for debug
        # print(okey, "=>" , nkey)
    return bib

@app.route('/adsbib', methods=['POST'])
def adsbib():
    bib = request.get_json()['input']
    bib = newbib(bib)
    return bib

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=2312)
    # app.run(debug=True, port=2417)
