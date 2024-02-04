from flask import Flask, rendertemplate

app = Flask(name)

Список книг і їхні дані (назва, опис, зображення тощо)
books = [
    {
        'id': 1,
        'title': 'Книга 1',
        'description': 'Опис для Книги 1',
        'image': 'book1.jpg',  
    },
{
        'id': 2,
        'title': 'Книга 1',
        'description': 'Опис для Книги 1',
        'image': 'book1.jpg',  
    },
{
        'id': 3,
        'title': 'Книга 1',
        'description': 'Опис для Книги 1',
        'image': 'book1.jpg',  
    },
{
        'id': 4,
        'title': 'Книга 1',
        'description': 'Опис для Книги 1',
        'image': 'book1.jpg',  
    },
{
        'id': 5,
        'title': 'Книга 1',
        'description': 'Опис для Книги 1',
        'image': 'book1.jpg', 
    },
{
        'id': 6,
        'title': 'Книга 1',
        'description': 'Опис для Книги 1',
        'image': 'book1.jpg',  
    },
{
        'id': 7,
        'title': 'Книга 1',
        'description': 'Опис для Книги 1',
        'image': 'book1.jpg',  
    },
{
        'id': 8,
        'title': 'Книга 1',
        'description': 'Опис для Книги 1',
        'image': 'book1.jpg',
    },
{
        'id': 9,
        'title': 'Книга 1',
        'description': 'Опис для Книги 1',
        'image': 'book1.jpg',
    },
{
        'id': 10,
        'title': 'Книга 1',
        'description': 'Опис для Книги 1',
        'image': 'book1.jpg',
    }
]

@app.route('/')
def index():
    return rendertemplate('index.html', books=books)

@app.route('/book/<int:bookid>')
def book(bookid):
    book_data = next((b for b in books if b['id'] == book_id), None)
    if book_data:
        return render_template('book.html', book=book_data)
    else:
        return "Книга не знайдена", 404

if __name == '__main':
    app.run(debug=True)
