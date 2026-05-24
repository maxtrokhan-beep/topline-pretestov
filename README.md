# Генератор HTML-отчета по пре-тесту рекламы

Веб-сервис на `Streamlit`, который:
- принимает Excel-файл `.xlsx` со стандартной структурой;
- принимает текстовые выводы пользователя;
- генерирует автономный HTML-отчет (все стили встроены в файл);
- отдает готовый HTML для скачивания.

## 1) Локальный запуск

1. Перейдите в папку проекта:
   ```bash
   cd topline-pretest
   ```
2. Создайте и активируйте виртуальное окружение:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
4. Запустите приложение:
   ```bash
   streamlit run app.py
   ```
5. Откройте URL, который покажет Streamlit (обычно `http://localhost:8501`).

## 2) Загрузка на GitHub

1. Инициализируйте git (если еще не инициализирован):
   ```bash
   git init
   ```
2. Добавьте файлы и сделайте первый коммит:
   ```bash
   git add .
   git commit -m "Initial version of pretest HTML report generator"
   ```
3. Создайте пустой репозиторий на GitHub и подключите удаленный origin:
   ```bash
   git remote add origin <YOUR_GITHUB_REPO_URL>
   git branch -M main
   git push -u origin main
   ```

## 3) Настройки Render

Создайте новый **Web Service** из GitHub-репозитория и укажите:

- **Environment**: `Python`
- **Build Command**:
  ```bash
  pip install -r requirements.txt
  ```
- **Start Command**:
  ```bash
  streamlit run app.py --server.port $PORT --server.address 0.0.0.0
  ```

Render автоматически подставит переменную окружения `PORT`.

## Структура проекта

- `app.py` — Streamlit UI и скачивание HTML;
- `report_generator.py` — чтение Excel, нормализация данных, выбор цветов, рендер Jinja2;
- `templates/report_template.html` — HTML/CSS шаблон отчета (структура блоков как в PPTX);
- `templates/assets/report_bg.png` — декоративный фон (полосы и логотип), экспорт из `topline pre test_ background.pdf`;
- `requirements.txt` — зависимости;
- `README.md` — инструкция по запуску и деплою.
