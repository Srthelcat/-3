import os

def parse_line(line):
    parts = line.split('|')
    return [parts[0], parts[1], parts[2], int(parts[3]), float(parts[4])]


def get_books(file_name):
    # Получаем путь к текущей директории скрипта
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, file_name)

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.strip().split('\n')

    return list(map(parse_line, lines[1:]))


def filtered_books(books, keyword):
    matches = filter(lambda b: keyword.lower() in b[1].lower(), books)
    return list(map(
        lambda b: [b[0], f"{b[1]}, {b[2]}", b[3], b[4]],
        matches
    ))


books = get_books("books.csv")
result = filtered_books(books, "python")

def books_total(books):
    return tuple(list(map(
        lambda b: (b[0], b[3] * b[4]),
        books
    )))

print(books)
print('--------------------------')
print(result)
print('--------------------------')
totals = books_total(books)
print(totals)

input('Нажмите Enter, чтобы продолжить...')
