from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

query = input("Введите свой запрос на сайте Wikipedia: ")
def main():
    browser = webdriver.Chrome()
    browser.get('https://ru.wikipedia.org')
    search_box = browser.find_element(By.CLASS_NAME, "vector-search-box-input")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

    time.sleep(3)

    a = browser.find_element(By.LINK_TEXT, query)
    a.click()

    time.sleep(3)


    while True:
        query2 = input(
            "Если вы хотите, чтобы информация выводилась по параграфам, нажмите 1; если хотите перейти на связанную страницу, нажмите 2; если нужно выйти из программы, нажмите 3: ")
        if query2 == "1":
            paragraphs = browser.find_elements(By.TAG_NAME, "p")
            for paragraph in paragraphs:
                print(paragraph.text)
                input()

        elif query2 == "2":
            links = browser.find_elements(By.CSS_SELECTOR, 'p a')
            if links:
                print("Выберите ссылку для перехода:")
                for index, link in enumerate(links):
                    print(f"{index + 1}: {link.text}")
                link_choice = input("Введите номер ссылки: ")
                try:
                    link_index = int(link_choice) - 1
                    if 0 <= link_index < len(links):
                        links[link_index].click()
                    else:
                        print("Неверный выбор ссылки.")
                except ValueError:
                    print("Введите числовое значение.")
            else:
                print("Ссылки не найдены.")
        elif query2 == "3":
            print("Спасибо за использование программы!")
            break

        else:
            print("Неверный ввод. Пожалуйста, выберите 1, 2 или 3.")

    browser.quit()

main()

