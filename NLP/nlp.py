import streamlit as st
from googletrans import Translator, LANGUAGES

# Initialize the translator
translator = Translator()

# Define language options
language = {
    "bn": "Bangla",
    "en": "English",
    "ko": "Korean",
    "fr": "French",
    "de": "German",
    "he": "Hebrew",
    "hi": "Hindi",
    "it": "Italian",
    "ja": "Japanese",
    'la': "Latin",
    "ms": "Malay",
    "ne": "Nepali",
    "ru": "Russian",
    "ar": "Arabic",
    "zh": "Chinese",
    "es": "Spanish"
}

# Streamlit title and description
st.title("NLP Language Translation 🌐")
st.write("Translate text into different languages using the Google Translate API.")

# Sidebar with language selection
st.sidebar.header("Language Selection")
target_language_code = st.sidebar.selectbox(
    "Select target language",
    list(language.keys()),
    format_func=lambda x: language[x]
)

# Input text box
input_text = st.text_area("Enter the text you want to translate:")

# Displaying example sentences
st.sidebar.header("Example Sentences")
example_sentences = {
    "en": "Hello, how are you?",
    "fr": "Bonjour, comment ça va?",
    "es": "Hola, ¿cómo estás?",
    "de": "Hallo, wie geht's?",
    "zh": "你好，你怎么样？",
    "hi": "नमस्ते, आप कैसे हैं?"
}
st.sidebar.write("Example:", example_sentences.get(target_language_code, "No example available"))

# History of translations
if "history" not in st.session_state:
    st.session_state.history = []

# Button to perform translation
if st.button("Translate"):
    if input_text:
        try:
            # Translating the text
            translated = translator.translate(input_text, dest=target_language_code)
            translation_result = {
                "input": input_text,
                "output": translated.text,
                "pronunciation": translated.pronunciation,
                "source_language": language.get(translated.src, "Unknown"),
                "target_language": language[target_language_code]
            }
            st.session_state.history.append(translation_result)

            # Display translation result
            st.success(f"Translated text ({language[target_language_code]}): {translated.text}")
            if translated.pronunciation:
                st.info(f"Pronunciation: {translated.pronunciation}")
            st.info(f"Translated from: {language.get(translated.src, 'Unknown')}")

        except Exception as e:
            st.error(f"Translation Error: {e}")
    else:
        st.warning("Please enter some text to translate.")

# Display translation history
st.subheader("Translation History")
for item in st.session_state.history:
    st.write(f"**Input:** {item['input']}")
    st.write(f"**Output ({item['target_language']}):** {item['output']}")
    if item['pronunciation']:
        st.write(f"**Pronunciation:** {item['pronunciation']}")
    st.write(f"**Translated from:** {item['source_language']}")
    st.write("---")

# Footer
st.markdown("""
<style>
    .footer {
        text-align: center;
        padding: 10px;
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        color: black;
    }
</style>
<div class="footer">
    <p>Developed by HitmanJ18</p>
</div>
""", unsafe_allow_html=True)