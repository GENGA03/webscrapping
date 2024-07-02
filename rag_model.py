from transformers import pipeline

class RAGModel:
    def __init__(self):
        self.qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
    
    def generate_answer(self, context, question):
        return self.qa_pipeline(question=question, context=context)

rag_model = RAGModel()