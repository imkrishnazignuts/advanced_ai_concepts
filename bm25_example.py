from rank_bm25 import BM25Okapi

docs = [
    "Hello i am krishna working intern at zignuts technolab",
    "i krishna doing internship in field of AI,ML",
    "what i learn is beyond the GTU syllabus"
]

tokenized_docs = [doc.lower().split() for doc in docs]

bm25 = BM25Okapi(tokenized_docs)

query = "krishna"

tokenized_query = query.lower().split()

score = bm25.get_scores(tokenized_query)

print(score)



