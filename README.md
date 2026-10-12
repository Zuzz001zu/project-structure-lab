# Text Stats - анализатор текста

Небольшой Python-скрипт командной строки, который считает статистику по текстовому файлу:
количество строк, слов, символов и самые частые слова.

Учебный проект для практического занятия «Создание структуры проекта».

## Структура проекта

```
project-structure-lab/
├── README.md              # описание проекта
├── .gitignore             # исключения для Git
├── LICENSE                # лицензия MIT
├── requirements.txt       # зависимости
├── src/                   # исходный код
│   ├── README.md
│   ├── main.py            # точка входа (CLI)
│   └── text\_stats.py      # логика подсчёта статистики
├── tests/                 # автотесты
│   ├── README.md
│   └── test\_text\_stats.py
├── docs/                  # документация
│   ├── README.md
│   └── architecture.md    # обоснование структуры
├── assets/                # статика
│   ├── README.md
│   └── sample.txt         # пример входного файла
└── .github/
    ├── README.md
    └── workflows/
        ├── README.md
        └── tests.yml      # CI: запуск тестов
```

Схема работы:

```
 assets/sample.txt ──► src/main.py ──► src/text\_stats.py ──► отчёт в консоли
                         (CLI)            (подсчёт)
```

## Установка

Требуется Python 3.9+.

```bash
git clone https://github.com/Zuzz001zu/project-structure-lab.git
cd project-structure-lab
pip install -r requirements.txt
```

## Запуск

```bash
python src/main.py assets/sample.txt
python src/main.py assets/sample.txt --top 3
```

Пример вывода:

```
Строк:    4
Слов:     29
Символов: 202
Топ-5 слов:
  git — 3
  это — 2
  github — 2
  система — 1
  контроля — 1
```

## Тесты

```bash
pytest
```

## Лицензия

Проект распространяется под лицензией MIT — см. файл [LICENSE](LICENSE).

## Контакты

Автор: Zara Gadzhieva
GitHub: https://github.com/Zuzz001zu

