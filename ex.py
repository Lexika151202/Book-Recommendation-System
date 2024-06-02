import pickle

path = "artifacts/book_pivot.pkl"

with open(path, "rb") as file:
    data = pickle.load(file)

print(data)
