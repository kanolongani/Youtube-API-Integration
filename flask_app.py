
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request


from api import fetch_data

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def fetch_input():
    if request.method == 'POST':
        input = request.form['input']
        print("------------------------------------------------------")
        v_ip = request.remote_addr
        s_n = request.form['nnn']
        print(f"ip {v_ip} ::::::::::::::: {input} {s_n}")
        print("#######################################################")
        return process_input(input)
    return '''
    <html>
    <head>
    <style>
    /* Form styles */
    form {
        max-width: 600px;
        margin: 0 auto;
        padding: 20px;
        text-align: center;
    }
    /* Label styles */
    label {
        display: block;
        font-size: 1.2em;
        margin-bottom: 10px;
    }
    /* Input styles */
    input[type="text"], input[type="submit"] {
        width: 100%;
        padding: 12px 20px;
        margin-bottom: 20px;
        box-sizing: border-box;
        border: 2px solid #ccc;
        border-radius: 4px;
        font-size: 1.2em;
    }
    /* Submit button styles */
    input[type="submit"] {
        background-color: #4CAF50;
        color: white;
        border: none;
        cursor: pointer;
    }
    /* Media query for responsive design */
    @media (max-width: 600px) {
        form {
            padding: 10px;
        }
        label {
            font-size: 1em;
        }
        input[type="text"], input[type="submit"] {
            font-size: 1em;
            padding: 8px;
        }
    }

    body {
  background-image: url('https://static.toiimg.com/thumb/resizemode-4,msid-64590538,imgsize-318552,width-720/64590538.jpg');
  background-size: cover;
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-position: center;
}
</style>

</head>
<body>
        <form action="/" method="POST">
            <label for="input">Enter your Name</label>
            <input type="text" id="nnn" name="nnn">
            <label for="input">Enter your video search </label>
            <input type="text" id="input" name="input">
            <input type="submit" value="Submit">
        </form>

                <form action="/kano">

            <input type="submit" value="About Me">
        </form>
    </body>
    </html>
    '''
@app.route('/kano')
def kk():
    return '''
    <h1> Created by Karan Longani</h1>

    '''
def process_input(i):
    # do something with the input
    df = fetch_data(i)
    s = """
<style>
    table {
        color: #333; /* Lighten up font color */
        font-family: Helvetica, Arial, sans-serif; /* Nicer font */
        width: 100%;
        border-collapse: collapse;
    }

    td, th {
        border: 5px solid #800080; /* Light grey border */
        padding: 10px; /* So text is centered */
    }

    /* Alternating background colors */
    tr:nth-child(even) td {
        background: #cf9b0e;
    }
    tr:nth-child(odd) td {
        background: #cf0eaf;
    }

    /* Add some hover effects */
    td:hover {
        background-color: #F5F5F5;
    }
</style>
"""
    # html_table = df.to_html(table_id='data_table', classes='table', escape=False, index=False,  style=style)
    return """<html><head>{1}</head><body><div>{0}</div></body></html>""".format(df.to_html(escape=False),s)
    # return df.to_html(table_id='data_table', classes='table', escape=False, index=False)




