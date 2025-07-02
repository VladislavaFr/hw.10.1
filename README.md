# Обработка и фильтрация данных

## Описание проекта

Данный проект предназначен для практики работы с GitFlow, GitHub и основами обработки данных в Python. В рамках проекта реализованы функции фильтрации и сортировки данных, представленных в виде списка словарей.

## Структура проекта

```
├── src/
│   └── processing.py       # Модуль с функциями обработки данных
├── README.md               # Документация проекта
```

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/your-username/your-repo-name.git
```

2. Перейдите в папку проекта:
```bash
cd your-repo-name
```

3. Убедитесь, что у вас установлен Python 3.7+.

## Использование

### Функция `filter_by_state(data, state='EXECUTED')`

Фильтрует список словарей по значению ключа `state`.

**Параметры:**
- `data` — список словарей
- `state` — значение для фильтрации по ключу `state` (по умолчанию `'EXECUTED'`)

**Пример входных данных:**

```python
data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}
]
```

**Пример использования:**

```python
from src.processing import filter_by_state

executed_data = filter_by_state(data)
canceled_data = filter_by_state(data, state='CANCELED')
```

**Результат:**

```python
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}]
```

---

### Функция `sort_by_date(data, reverse=True)`

Сортирует список словарей по значению ключа `date`.

**Параметры:**
- `data` — список словарей
- `reverse` — порядок сортировки (по умолчанию `True` — по убыванию)

**Пример использования:**

```python
from src.processing import sort_by_date

sorted_data = sort_by_date(data)
```

**Результат:**

```python
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
```

## Контрибьюция

1. Сделайте форк проекта.
2. Создайте новую ветку: `git checkout -b feature/имя-фичи`
3. Сделайте коммиты: `git commit -m 'Описание изменений'`
4. Отправьте изменения: `git push origin feature/имя-фичи`
5. Создайте Pull Request.

## Лицензия

Проект предназначен для учебных целей.
