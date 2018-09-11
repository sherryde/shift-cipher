from flask import Flask, request
from caesar import rotate_string


app = Flask(__name__)
app.config['DEBUG'] = True


form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            body {{
                display: block;
                margin: 8px;
            }}
            form {{               
	            background: linear-gradient(15deg, #fcf8c4c2, #6fa059);
                -moz-box-shadow: 3px 3px 3px 0px rgba(27,43,63,0.64);
                box-shadow: 2px 2px 3px 0px rgba(27,43,63,0.64);
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 8px;
                text-align: left;             
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
                overflow: auto;
                resize: none;
            }}
            p .error {{
                color: red;
            }}

        </style>
    </head>
    <body>
     <form method='POST'>
      <h1>Web Caesar</h1>
            <p>A Caesar encryption cipher rotates the alphabet letters
            by a specific NUMBER referred to as the key.</p>

        <div>
            <label type"rot_label">Rotate by:</label>
            <input type="number" name="rot" value="0"/>
            <p class="error"></p> 
        </div>
        <textarea placeholder="Text, to encrypt!" type="text" name="text">{0}</textarea>
        <br>
        <input type="submit" value="Encrypt the Text"/>
      </form>   
    </body>
</html>"""


@app.route("/")
def index():
    return form.format("") 

@app.route("/", methods=['POST'])   
def encrypt():
    rotation_key = int(request.form['rot'])
    string = request.form['text']
    encrypted = rotate_string(string, rotation_key) 

    return form.format(encrypted)
           

app.run()