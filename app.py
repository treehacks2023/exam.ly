from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import openai
from functions import *
from dotenv import dotenv_values

app = Flask(__name__)
config = dotenv_values(".env")

openai.api_key = config['API-KEY']

model_engine = "text-davinci-003"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/upload',methods=['post'])
def upload():
    if request.method == 'POST':
        img = request.files.getlist('file')

        if img:
            filenames=[]
            for elem in img:
                filenames.append(secure_filename(elem.filename))
                elem.save(secure_filename(elem.filename))
            # filename = secure_filename(img.filename)
            # img.save(filename)
            filename='merged'
            merge_files(filenames,filename)
            
            page_content = textify(filename+'.pdf')
            page_with_everything = add_prompt(page_content)
            
            # Generate questions using class functions
            question_generator = QuestionGenerator(model_engine, openai.api_key)
            page_with_everything = add_prompt(page_content)
            # feed into model
            response = question_generator.generate_questions(page_with_everything, 2048, 0.5, 1, 0, 0)
            
            response_with_endlines=add_newlines(response)

    return render_template("index.html",response = response_with_endlines)

# Run the app
if __name__ == "__main__":

    app.run(debug=True)