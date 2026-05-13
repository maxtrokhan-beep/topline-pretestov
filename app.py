from __future__ import annotations

from pathlib import Path

import streamlit as st

from report_generator import ReportGenerationError, generate_report_html


st.set_page_config(page_title="Генератор HTML-отчета по пре-тесту рекламы", layout="centered")
st.title("Генератор HTML-отчета по пре-тесту рекламы")

uploaded_file = st.file_uploader("Выберите Excel-файл (.xlsx)", type=["xlsx"])
user_insights = st.text_area(
    "Введите текстовые выводы",
    height=220,
    placeholder="Введите ключевые выводы по результатам пре-теста...",
)

if st.button("Сформировать HTML-отчет", type="primary"):
    if uploaded_file is None:
        st.error("Сначала загрузите Excel-файл.")
    else:
        try:
            html_content = generate_report_html(
                file_bytes=uploaded_file.getvalue(),
                user_insights=user_insights,
                template_dir=Path(__file__).parent / "templates",
            )

            report_name = f"topline_report_{Path(uploaded_file.name).stem}.html"
            st.success("Отчет успешно сформирован.")
            st.download_button(
                label="Скачать HTML-файл",
                data=html_content.encode("utf-8"),
                file_name=report_name,
                mime="text/html",
            )
        except ReportGenerationError as exc:
            st.error(str(exc))
        except Exception:
            st.error(
                "Произошла непредвиденная ошибка при формировании отчета. "
                "Проверьте формат входного файла."
            )
