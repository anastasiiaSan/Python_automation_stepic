# Python_automation_stepic
This is repository for homework of automation course on stepic: https://stepik.org/course/575/syllabus

1. Создайте GitHub-репозиторий, в котором будут лежать файлы conftest.py и test_items.py.
2. Добавьте в файл conftest.py обработчик, который считывает из командной строки параметр language.
3. Реализуйте в файле conftest.py логику запуска браузера с указанным языком пользователя. Браузер должен объявляться в фикстуре browser и передаваться в тест как параметр.
4. В файл test_items.py напишите тест, который проверяет, что страница товара на сайте содержит кнопку добавления в корзину. Например, можно проверять товар, доступный по http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.
5 Тест должен запускаться с параметром language следующей командой:
pytest --language=es test_items.py
и проходить успешно. Достаточно, чтобы код работал только для браузера Сhrome.
6. Отправить ссылку на данный репозиторий в качестве ответа на данное задание.
