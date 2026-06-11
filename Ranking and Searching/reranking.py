from sentence_transformers import CrossEncoder

model = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)

query = "what is remote work"

documents = [
    "Company gives 12 weeks maternity leave",
    "Salary is credited monthly",
    "Remote work policy available"
]

pairs = [[query,doc] for doc in documents]

score = model.predict(pairs)

print(score)

