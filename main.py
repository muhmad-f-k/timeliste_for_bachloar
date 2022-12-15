import streamlit as st

data = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35},
]

# Legg til en kolonne som viser om personen er voksen eller ikke
data_with_is_adult = [
    {"name": row["name"], "age": row["age"], "is_adult": row["age"] >= 18}
    for row in data
]

st.table(data_with_is_adult)