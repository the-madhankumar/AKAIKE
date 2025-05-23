from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import os
from groq import Groq

app = Flask(__name__)
CORS(app)

df = None

groq_api_key = "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" 
client = Groq(api_key=groq_api_key)

@app.route('/upload', methods=['POST'])
def load_csv():
    global df
    data = request.get_json()

    file_path = data.get('file_path').strip() if data else ""

    df = pd.read_csv(file_path)
    return jsonify({"message": "CSV loaded successfully from path"}), 200

@app.route('/query', methods=['POST'])
def ask_query():
    global df
    data = request.get_json()
    question = data.get("question", "").strip() if data else ""

    context = df

    prompt = f"""
        You are a data analyst. Analyze the following CSV data and answer the question.
        -> give the point by point response.
        -> use statistical analysis
        -> do not use the charts or coding in response

        CSV Content:
        {context}

        Question:
        {question}
        """


    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "You are a helpful data assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )
        answer = response.choices[0].message.content.strip()
        return jsonify({"response": answer}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)