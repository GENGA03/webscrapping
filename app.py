from flask import Flask, request, jsonify
from scraper import fetch_content
from rag_model import RAGModel

app = Flask(__name__)
content_db = {}
rag_model = RAGModel()

@app.route('/load', methods=['POST'])
def load_content():
    url = request.json.get('url')
    content = fetch_content(url)
    if content:
        content_db[url] = content
        return jsonify({"message": "Content loaded successfully."}), 200
    else:
        return jsonify({"message": "Failed to load content."}), 400

@app.route('/query', methods=['POST'])
def query_content():
    url = request.json.get('url')
    question = request.json.get('question')
    context = content_db.get(url)
    if context:
        answer = rag_model.generate_answer(context, question)
        return jsonify({"answer": answer['answer']}), 200
    else:
        return jsonify({"message": "Content not found for the given URL."}), 404

if __name__ == '__main__':
    app.run(debug=True)
