# Автотесты для Яндекс Самокат

## Стек технологий

- Python 3.13
- Selenium 4
- pytest
- Firefox + GeckoDriver
- Allure Reports
- Page Object Model (POM)

## Структура проекта

```
Sprint_6/
├── tests/
│   ├── conftest.py
│   ├── test_accordion_panel_button_text.py
│   └── test_create_order_rent_scooter.py
├── pages/
│   ├── base_page.py
│   └── create_order_page.py
├── data.py
├── urls.py
├── .gitignore
└── README.md
```

## Установка и запуск

### 1. Установи зависимости

```bash
pip install selenium pytest allure-pytest
```

### 2. Запусти все тесты

```bash
cd Sprint_6
pytest tests/ -v
```

### 3. Запусти конкретный файл

```bash
pytest tests/test_accordion_panel_button_text.py -v
```

### 4. Запусти с выводом в консоль

```bash
pytest tests/ -v -s
```

### 5. Запусти с Allure-отчётом

```bash
pytest tests/ -v --alluredir=allure-results
allure serve allure-results
```
