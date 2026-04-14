def parse_line(line):
        parts = line.split('|')
        return [parts[0], parts[1], parts[2], int(parts[3]), float(parts[4])]


def get_books(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.strip().split('\n')

    return list(map(parse_line, lines[1:]))

get_books("books.csv")

def filtered_books(books, keyword):
    matches = filter(lambda b: keyword.lower() in b[1].lower(), books)
    return list(map(
        lambda b: [b[0], f"{b[1]}, {b[2]}", b[3], b[4]],
        matches
    ))

books = get_books("books.csv")
result = filtered_books(books, "python")
print(result)
def books_total(books):
    return list(map(
        lambda b: (b[0], b[3] * b[4]),
        books
    ))

books = get_books("books.csv")
totals = books_total(books)
print(totals)
