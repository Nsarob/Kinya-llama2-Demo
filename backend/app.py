from flask import Flask, render_template, request, jsonify
import text_generation_model

app = Flask(__name__)

# Load your text generation model
model = text_generation_model.load_model()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prompt = request.form.get('prompt')
        if prompt:
            try:
                generated_text = model.generate_text(prompt)
                return render_template('index.html', prompt=prompt, generated_text=generated_text)
            except Exception as e:
                return render_template('index.html', error=str(e))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)