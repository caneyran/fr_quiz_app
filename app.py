import streamlit as st
import random

st.set_page_config(page_title="Fransızca-Türkçe Quiz", layout="centered")

# Senin öğrendiğin kelimeler
words = {
    "école": "okul", "maison": "ev", "travail": "iş", "famille": "aile",
    "ami": "arkadaş", "livre": "kitap", "chat": "kedi", "chien": "köpek",
    "voiture": "araba", "ville": "şehir", "pays": "ülke", "heure": "saat",
    "jour": "gün", "nuit": "gece", "matin": "sabah", "soir": "akşam",
    "bien": "iyi", "mal": "kötü", "beau": "güzel", "froid": "soğuk",
    "chaud": "sıcak", "faim": "açlık", "soif": "susuzluk", "content": "mutlu",
    "triste": "üzgün", "fatigué": "yorgun", "facile": "kolay", "difficile": "zor",
    "petit": "küçük", "grand": "büyük"
}

# Oturum bilgileri (soru ve skor için)
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.question = None
    st.session_state.correct_answer = None

# Başlık
st.title("📚 Fransızca - Türkçe Quiz")
st.markdown("Her seferinde farklı bir kelime gelir. Cevabını yaz, kontrol et!")

# Yeni soru oluşturma fonksiyonu
def get_new_question():
    word, meaning = random.choice(list(words.items()))
    if random.choice([True, False]):
        question = f"Bu kelimenin Türkçe anlamı nedir? 👉 **{word}**"
        correct = meaning
    else:
        question = f"Bu kelimenin Fransızca karşılığı nedir? 👉 **{meaning}**"
        correct = word
    return question, correct

# Yeni Soru Butonu
if st.button("🎲 Yeni Soru"):
    q, a = get_new_question()
    st.session_state.question = q
    st.session_state.correct_answer = a.lower()

# Soru göster ve cevap al
if st.session_state.question:
    st.markdown(st.session_state.question)
    user_answer = st.text_input("Cevabınızı yazın").strip().lower()

    if st.button("Cevabı Kontrol Et"):
        if user_answer == st.session_state.correct_answer:
            st.success("✅ Doğru!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Yanlış. Doğru cevap: {st.session_state.correct_answer}")

# Skor göster
st.markdown(f"### 🔢 Skor: {st.session_state.score}")