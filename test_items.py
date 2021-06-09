# Строка в терминал: pytest -s -v --language=es --browser_name=chrome test_items.py

import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_of_add_to_basket(browser):
    browser.get(link)
    time.sleep(30)  # Пауза для проверки выбора языка
    n = browser.find_elements_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")  # n - искомые элементы
    assert len(n) > 0, "Кнопка не найдена"  # ошибка, если количество искомых элементов == 0
