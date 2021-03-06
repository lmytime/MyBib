# MyBib
Tool to optimize citekey of bibtex to Author+Year.

## Hello
This webpage is designed to optimize citekeys of bibtex file. <br>
The citekey of bibtex file generated by <a href="https://ui.adsabs.harvard.edu/">NASA/ADS</a> is its bibcode. <br>
But I think maybe "Author+Year" is better, at least for myself. <br>
For example, the citekey of the paper `Zur Elektrodynamik bewegter Körper` is `1905AnP...322..891E`. <br>
And I prefer to use `Einstein1905` or `Einstein:1905`. <br>
This pushed me to build this webpage. <br>
And please give me a <a href="https://github.com/lmytime/MyBib">star</a> if you think this webpage is helpful. <br><br>
Online version for this app: https://preview.lmytime.com/mybib

## Python environment
This app requires python package: `flask`, `flask_cors`, `pybtex`.

You can install them using pip: `pip install flask flask_cors pybtex`.

Then run the script typing `python app.py`.

<h2>Usage for webpage</h2>
<ol>
    <li>
        <p>
            <b> Paste your bibtex file into the left textarea. You can get the bibtex file from <a href="https://ui.adsabs.harvard.edu/">NASA/ADS</a>.</b>
        </p>
    </li>
    <li>
        <p>
            <b>Click the button "Go!" to optimize the citekey.</b>
        </p>
    </li>
    <li>
        <p>
            <b>Copy the optimized bibtex file by clicking the "Copy" button.</b>
        </p>
    </li>
</div>
