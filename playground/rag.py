import os

# Set database host to localhost since we're connecting to it outside of docker
os.environ["DATABASE_HOST"] = "localhost"
from services.vector_store import VectorStore


vec = VectorStore()

# --------------------------------------------------------------
# Test semantic search
# --------------------------------------------------------------

result = vec.semantic_search("What's the working from home policy?")

# --------------------------------------------------------------
# Test keyword search
# --------------------------------------------------------------

result = vec.keyword_search("Policy")
