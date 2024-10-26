import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_name_out_range(self):
        collector = BooksCollector()
        collector.add_new_book('12345678901234567890123456789012345678901')
        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize('name,genre', [['Гордость и предубеждение и зомби', 'Ужасы']])
    def test_set_book_genre_book_in_dictionary(self,name,genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name,genre)
        assert collector.books_genre[name] == genre

    @pytest.mark.parametrize('name,genre', [['Гордость и предубеждение и зомби', 'Ужасы']])
    def test_get_book_genre_book_in_dictionary_and_has_genre_true(self,name,genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    @pytest.mark.parametrize('name,genre', [['Гордость и предубеждение и зомби', 'Ужасы']])
    def test_get_books_with_specific_genre_book_in_dictionary_and_has_genre_true(self,name,genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_with_specific_genre(genre) == [name]

    def test_get_books_genre_empty_dictionary_true(self):
        collector = BooksCollector()
        assert collector.get_books_genre() == {}

    def test_get_books_for_children_book_in_dictionary_and_has_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('Я Пони')
        collector.set_book_genre('Я Пони', 'Фантастика')
        assert collector.get_books_for_children() == ['Я Пони']

    @pytest.mark.parametrize('name', ['Гордость и предубеждение и зомби'])
    def test_add_book_in_favorites_add_one_book_and_book_in_dictionary(self,name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert len(collector.favorites) == 1

    @pytest.mark.parametrize('name', ['Гордость и предубеждение и зомби'])
    def test_delete_book_from_favorites_book_in_list(self,name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert len(collector.favorites) == 0

    def test_get_list_of_favorites_books_empty_list_true(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []