import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer
from sentence_transformers import SentenceTransformer, util

# Load the retrieval model
retriever = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Load the generator model
tokenizer = T5Tokenizer.from_pretrained('t5-small')
generator = T5ForConditionalGeneration.from_pretrained('t5-small')

# Example corpus
corpus = [
    "RAG models combine retrieval and generation for better accuracy.",
    "RAG models are scalable and flexible for various NLP tasks.",
    "Using retrieval-augmented generation can enhance the relevance of generated answers."
]

# Encode the corpus
corpus_embeddings = retriever.encode(corpus, convert_to_tensor=True)

def retrieve(query, top_k=1):
    query_embedding = retriever.encode(query, convert_to_tensor=True)
    hits = util.semantic_search(query_embedding, corpus_embeddings, top_k=top_k)
    retrieved_docs = [corpus[hit['corpus_id']] for hit in hits[0]]
    return retrieved_docs

def generate_answer(query, context):
    input_text = f"question: {query} context: {context}"
    input_ids = tokenizer.encode(input_text, return_tensors='pt')
    output_ids = generator.generate(input_ids)
    answer = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return answer
