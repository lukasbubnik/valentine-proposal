import streamlit as st
import streamlit.components.v1 as components

# Nastavení stránky
st.set_page_config(page_title="Valentine Proposal", page_icon="❤️")

# CSS pro pěkné pozadí a stylování rámečku
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 99%, #fecfef 100%);
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .main-card {
        background: white;
        padding: 50px;
        border-radius: 20px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.1);
        text-align: center;
        max-width: 500px;
        position: relative;
    }
    .question {
        font-family: 'Pacifico', cursive, sans-serif;
        font-size: 35px;
        color: #d63384;
        margin-bottom: 30px;
    }
    /* Styl pro Yes tlačítko */
    .stButton>button {
        background-color: #28a745 !important;
        color: white !important;
        border-radius: 10px;
        padding: 10px 25px;
        font-weight: bold;
        border: none;
    }
    </style>
    <link href="https://fonts.googleapis.com" rel="stylesheet">
    """, unsafe_allow_html=True)

# Inicializace stavu (aby se po kliknutí na Yes změnil obsah)
if 'accepted' not in st.session_state:
    st.session_state.accepted = False

# Hlavní kontejner (Rámeček)
if not st.session_state.accepted:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.markdown('<p class="question">Will you be my VALENTINE?</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Yes"):
            st.session_state.accepted = True
            st.rerun()

    with col2:
        # JavaScript pro uskakovací tlačítko "No"
        components.html("""
            <style>
                #no-btn {
                    background-color: #dc3545;
                    color: white;
                    border: none;
                    padding: 10px 25px;
                    border-radius: 10px;
                    font-weight: bold;
                    cursor: pointer;
                    position: absolute;
                    transition: 0.2s;
                }
            </style>
            <button id="no-btn">No</button>
            <script>
                const btn = document.getElementById('no-btn');
                btn.addEventListener('mouseover', function() {
                    const x = Math.random() * (window.innerWidth - 100);
                    const y = Math.random() * (window.innerHeight - 50);
                    btn.style.left = x + 'px';
                    btn.style.top = y + 'px';
                });
                btn.addEventListener('click', function() {
                    alert('Nice try! But you have to say Yes! 😉');
                });
            </script>
        """, height=100)
    
    st.markdown('</div>', unsafe_allow_html=True)

else:
    # Co se stane po kliknutí na "Yes"
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    # GIF s emojim s růží (používáme veřejný odkaz)
    st.image("https://media.giphy.com")
    st.markdown('<h2 style="color: #d63384; font-family: sans-serif;">Yeeeeeeey I knew it 🤗</h2>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

