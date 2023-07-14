from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = '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'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_form', methods=['GET', 'POST'])
def process_form():
    if request.method == 'POST':
        prompt = request.form['prompt'] + "Give me one word answer. What kind of specialist should I consult for my symptopms. If its not symtomp then say its not a symptom"

        # Make an API call to OpenAI
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100
        )

        # Extract the generated text from the API response
        generated_text = response.choices[0].text.strip()

        # Render the template with the generated text
        return render_template('index.html', generated_text=generated_text)

    return "This route only supports POST requests"

if __name__ == '__main__':
    app.run(debug=True)



