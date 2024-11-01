# Bot_parsing
**Telegram Бот для Парсинга Данных с IEC
**
Этот проект представляет собой Telegram-бота, который позволяет пользователям парсить данные с веб-страниц Международной электротехнической комиссии (IEC). Бот предоставляет удобный интерфейс для выбора необходимых элементов для парсинга и возвращает результаты в формате CSV-файлов, готовых для скачивания.
Функциональные возможности

    Парсинг отдельных элементов: Пользователь может выбрать отдельный элемент, такой как "Титул", "Наименование", "Описание", "Проект" и т.д., для парсинга с указанной страницы.
    Парсинг всех элементов: Также доступна функция парсинга всех доступных элементов сразу для каждого URL, что позволяет собрать более полные данные.
    Генерация отчётов в CSV: Результаты парсинга отправляются пользователю в виде CSV-файлов, которые можно легко скачать и использовать для анализа.

Структура проекта

Проект состоит из следующих файлов:

    main.py — основной скрипт для запуска бота.
    parser.py — модуль, содержащий функции для парсинга данных с указанных веб-страниц.
    requirements.txt — список зависимостей для установки необходимых библиотек.

Основные технологии

    Python — основной язык программирования.
    python-telegram-bot — библиотека для работы с Telegram API.
    BeautifulSoup и Requests — используются для парсинга HTML и обработки HTTP-запросов.
