import numpy as np
import pandas as pd

# Mảng suggestion bạn muốn khởi tạo
suggestion = np.array([[1, 2, 3]], dtype=np.int64)
book_pivot = {
    "title": ["A", "B", "C", "D", "E"],
    "Author": [1, 2, 3, 4, 5],
    "Year": [2001, 2002, 2003, 2004, 2005],
}

final_rating = {
    "user_id": [277427, 3363, 11676, 12538, 13552],
    "ISBN": [
        "002542731X",
        "002542732X",
        "002542733X",
        "002542734X",
        "002542735X",
    ],
    "rating": [10, 0, 6, 10, 0],
    "title": [
        "The Lord of the Rings",
        "A",
        "C",
        "B",
        "James Finn Garner",
    ],
    "years": [1994, 1994, 1994, 1994, 1994],
    "pulisher": [
        "John Wiley &amp; Sons Inc",
        "John Wiley &amp; Sons Inc",
        "John Wiley &amp; Sons Inc",
        "John Wiley &amp; Sons Inc",
        "John Wiley &amp; Sons Inc",
    ],
    "image-url": [
        "http://images.amazon.com/images/P/01.LZZZZZZZ.jpg",
        "http://images.amazon.com/images/P/02.LZZZZZZZ.jpg",
        "http://images.amazon.com/images/P/03.LZZZZZZZ.jpg",
        "http://images.amazon.com/images/P/04.LZZZZZZZ.jpg",
        "http://images.amazon.com/images/P/05.LZZZZZZZ.jpg",
    ],
    "num_of_rating": [82, 82, 82, 82, 82],
}

book_pivot = pd.DataFrame(book_pivot)
book_pivot.set_index("title", inplace=True)
# print(book_pivot)

final_rating = pd.DataFrame(final_rating)


# idx = [1, 2]
# url = final_rating.iloc[idx]["image-url"]
# print(url)


def fecth_poster(suggestion):
    book_name = []
    ids_index = []
    poster_url = []

    for book_id in suggestion[0]:
        book_name.append(book_pivot.index[book_id])

    for name in book_name:
        ids = np.where(final_rating["title"] == name)[0]
        ids_index.append(ids)

    for idx in ids_index:
        url = final_rating.iloc[idx]["image-url"]
        poster_url.append(url)
    return poster_url


suggestion = np.array([[0, 1, 2, 3, 4]], dtype=np.int64)
poster_url = fecth_poster(suggestion)
print(poster_url)
