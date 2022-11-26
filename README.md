# qa_python
Проверки для конструктора:
    Проверка что books_rating - словарь. `test_books_rating_is_dictionary`
    Проверка что favorites - список. `test_favorites_is_list`

Проверки методов:
    Проверка что дефолтный рейтинг у только что добавленой книги =1. `test_add_new_book_default_rating`
    Проверка что рейтинг от 1 до 10 устанавливается. `test_set_book_rating_set_rating8_true`
    Проверка что рейтинг больше 10 не устанавливается. `test_set_book_rating_rating11_false`
    Проверка получения рейтинга по имени книги. `test_get_book_rating_added_book_true`
    Проверка получения книг с определенным рейтингом рейтингом. `test_get_books_whith_specific_rating_raiting8_true`
    Проверка получения книг с определенным рейтингом из пустого списка. `test_get_books_whith_specific_rating_list_empty`
    Проверка получения списка из трех книг. `test_get_books_rating_three_books_true`
    Проверка добавления в Избранное книги которая есть в общем списке. `test_add_book_in_favorites_book_in_rating_true`
    Проверка добавления в избранное книги которой нет в общем списке. `test_add_book_in_favorites_book_not_from_rating_false`
    Проверка добавления в Избранное книги которая уже есть в списке Избранного. `test_add_book_in_favorites_book_already_in_favorites_false`
    Проверка удаления книги из Избранного. `test_delete_book_from_favorites_book_in_favirites_true`
    Проверка удаления из Избранного книги которой нет в Избранном. `test_delete_book_from_favorites_book_not_from_favorites_false`
    Проверка получения Избранного. `test_get_list_of_favorites_books_two_books_true`