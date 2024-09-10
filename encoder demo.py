from langchain_community.embeddings import HuggingFaceEmbeddings

encoder = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L12-v2",
    model_kwargs = {'device':'cpu'}
)

embeddings = encoder.embed_query("the dog and the man are happy today")

print(sorted(embeddings))

print(len(embeddings))

