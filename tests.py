from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    @pytest.fixture(autouse=True)
    def collector(self):
        self.collector= BooksCollector()

    @pytest.mark.parametrize("name", ['Война и мир', 'Братья Карамазовы'])     # Тест на добавление 2 книг
    def test_positive_add_new_book_add_two_books(self, name):
        self.collector.add_new_book(name)
        result = name in self.collector.get_books_genre()
        assert result == True

    def test_negative_add_new_book(self):                                       # Негативный тест что книга больше 41 символа не добавится
        name = 'a' * 50
        self.collector.add_new_book(name)
        result = name in self.collector.get_books_genre()
        assert result == False

    @pytest.mark.parametrize('name, genre', [('Дюна', 'Фантастика'), ('Оно', 'Ужасы')])
    def test_set_book_genre_set_two_books(self, name, genre):                   # Тест на установку жанра книге
        self.collector.add_new_book(name)
        self.collector.set_book_genre(name, genre)
        result = self.collector.get_book_genre(name) == genre
        assert result == True

    def test_get_book_genre(self):                                              # Тест на получение жанра добавленной книги
        self.collector.add_new_book("Дюна")
        self.collector.set_book_genre("Дюна", 'Фантастика')
        assert self.collector.get_book_genre('Дюна') == 'Фантастика'

    def test_get_books_with_specific_genre_two_books(self):                     # Тест на проверку книг по жанрам
        self.collector.add_new_book('Дюна')
        self.collector.set_book_genre('Дюна', 'Фантастика')
        self.collector.add_new_book('Оно')
        self.collector.set_book_genre('Оно', 'Ужасы')
        fantasy_books = self.collector.get_books_with_specific_genre('Фантастика')
        horror_books = self.collector.get_books_with_specific_genre('Ужасы')
        assert fantasy_books == ['Дюна']
        assert horror_books == ['Оно']

    def test_get_books_genre(self):                                             # Тест вывода текущего словаря books_genre
        collector = BooksCollector()
        collector.add_new_book("Дюна")
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_books_genre() == {'Дюна': 'Фантастика'}

    def test_get_books_for_children_two_books(self):                            # Тест книг которые подходят детям
        self.collector.add_new_book("Дюна")
        self.collector.set_book_genre('Дюна', 'Фантастика')
        self.collector.add_new_book("Оно")
        self.collector.set_book_genre('Оно', 'Ужасы')
        children_books = self.collector.get_books_for_children()
        assert "Дюна" in children_books
        assert "Оно" not in children_books

    def test_add_book_in_favorites(self):                                       # Тест добавления книги в избранное
        self.collector.add_new_book("Дюна")
        self.collector.add_book_in_favorites("Дюна")
        assert "Дюна" in self.collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self):                                  # Тест на удаление книги из избранного
        self.collector.add_new_book("Дюна")
        self.collector.add_book_in_favorites("Дюна")
        self.collector.delete_book_from_favorites("Дюна")
        assert "Дюна" not in self.collector.get_list_of_favorites_books()

    @pytest.mark.parametrize("name", ['Война и мир', 'Братья Карамазовы'])
    def test_get_list_of_favorites_books_two_books(self, name):                  # Тест на получение списка избранных книг
        self.collector.add_new_book(name)
        self.collector.add_book_in_favorites(name)
        assert name in self.collector.get_list_of_favorites_books()

