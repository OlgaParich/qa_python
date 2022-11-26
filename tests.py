from main import BooksCollector

class TestBooksCollector:

    # пример теста:
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        assert len(collector.get_books_rating()) == 2

    #Проверяем что books_rating - словарь
    def test_books_rating_is_dictionary(self):
        collector = BooksCollector()
        assert collector.books_rating == {}

    #Проверяем что favorites - список
    def test_favorites_is_list(self):
        collector = BooksCollector()
        assert collector.favorites == []

    #Проверяем что при добавлении новой книги её дефолтный рейтинг =1
    def test_add_new_book_default_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Зов кукушки')
        assert collector.get_books_rating()['Зов кукушки'] == 1

    #Проверяем установку корректного рейтинга
    def test_set_book_rating_set_rating8_true(self):
        collector = BooksCollector()
        collector.add_new_book('Война и Мир')
        collector.set_book_rating('Война и Мир', 8)
        assert collector.get_books_rating()['Война и Мир'] == 8

    #Проверяем установки не корректного рейтинга книге
    def test_set_book_rating_rating11_false(self):
        collector = BooksCollector()
        collector.add_new_book('Война и Мир')
        collector.set_book_rating('Война и Мир', 11)
        assert collector.get_books_rating()['Война и Мир'] == 1

    #Проверяем получение рейтинга по имени книги
    def test_get_book_rating_added_book_true(self):
        collector = BooksCollector()
        collector.add_new_book('Повелитель мух')
        collector.set_book_rating('Повелитель мух', 5)
        assert collector.get_book_rating('Повелитель мух') == 5

    # Проверяем получение книг с рейтингом 8
    def test_get_books_whith_specific_rating_raiting8_true(self):
        collector = BooksCollector()
        collector.add_new_book('Хоббит')
        collector.set_book_rating('Хоббит', 7)
        collector.add_new_book('Властелин колец')
        collector.set_book_rating('Властелин колец', 8)
        books_with_specific_rating = collector.get_books_with_specific_rating(8)
        assert len(books_with_specific_rating) == 1

    # Проверяем получение книг из пустого списка
    def test_get_books_whith_specific_rating_list_empty(self):
        collector = BooksCollector()
        books_with_specific_rating = collector.get_books_with_specific_rating(8)
        assert books_with_specific_rating == []

    # Проверяем получение списка из трех книг
    def test_get_books_rating_three_books_true(self):
        collector = BooksCollector()
        collector.add_new_book('Игра престолов')
        collector.add_new_book('Пир стервятников')
        collector.add_new_book('Битва королей')
        assert len(collector.get_books_rating()) == 3

    #Проверяем добавление книги которая есть в общем списке в избранное
    def test_add_book_in_favorites_book_in_rating_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        assert len(collector.get_list_of_favorites_books()) == 1

    #Проверяем добавление в избранное книги которой нет в общем списке
    def test_add_book_in_favorites_book_not_from_rating_false(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Властелин колец')
        assert len(collector.get_list_of_favorites_books()) == 0

    #Проверяем добавление книги которая уже есть в списке избранного
    def test_add_book_in_favorites_book_already_in_favorites_false(self):
        collector = BooksCollector()
        collector.add_new_book('Сияние')
        collector.add_book_in_favorites('Сияние')
        collector.add_book_in_favorites('Сияние')
        assert len(collector.get_list_of_favorites_books()) == 1

    #Проверяем удаление книги из избранного
    def test_delete_book_from_favorites_book_in_favirites_true(self):
        collector = BooksCollector()
        collector.add_new_book('Миссия шута')
        collector.add_new_book('Судьба шута')
        collector.add_book_in_favorites('Миссия шута')
        collector.add_book_in_favorites('Судьба шута')
        collector.delete_book_from_favorites('Судьба шута')
        assert len(collector.get_list_of_favorites_books()) == 1

    #Проверяем удаление книги которой нет в избранном
    def test_delete_book_from_favorites_book_not_from_favorites_false(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Оно')
        collector.delete_book_from_favorites('Кэри')
        assert len(collector.get_list_of_favorites_books()) == 1

    #Проверяем получение Избранного
    def test_get_list_of_favorites_books_two_books_true(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Оно')
        collector.add_new_book('Сияние')
        collector.add_book_in_favorites('Сияние')
        assert len(collector.get_list_of_favorites_books()) == 2
