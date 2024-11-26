import requests
from bs4 import BeautifulSoup


def parse_url(url):
    try:
        # Получение данных с веб-сайта
        response = requests.get(url)
        response.raise_for_status()  # Проверяем наличие ошибок HTTP
        html_content = response.text

        # Парсинг HTML-кода
        soup = BeautifulSoup(html_content, "html.parser")
        return soup
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе: {e}")
        return None


if __name__ == "__main__":
    # Пример использования
    url = "https://gmail.com"
    soup = parse_url(url)

    if soup:
        # Весь текст сайта (урезанный)
        print(soup.text[:500], "\n. . .\n", soup.text[-500:].strip())
