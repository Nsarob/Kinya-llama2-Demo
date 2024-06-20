from flask import Flask, request, jsonify
import your_text_generation_model

app = Flask(__name__)

# Load your text generation model
model = your_text_generation_model.load_model()

@app.route('/api/generate-text', methods=['POST'])
def generate_text():
    # Get the prompt from the request payload
    prompt = request.json.get('prompt')

    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    try:
        # Generate text using your model
        generated_text = model.generate_text(prompt)
        return jsonify({'text': generated_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)