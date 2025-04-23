import streamlit as st
st.set_page_config(
    page_title="YouTube AI Summarizer",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

import sys
import os
import youtube_utils
import gemini_utils
from streamlit_lottie import st_lottie
import json

# Adiciona o diretorio 'src' ao caminho do Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Configuração de página com visual moderno

# Carregar animações Lottie
def load_lottie(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# CSS 
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
    
    .main-title {
        background: linear-gradient(90deg, #9C27B0, #BA68C8, #E1BEE7, #BA68C8, #9C27B0);
        background-size: 300%;
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        text-align: center;
        font-size: 2.8rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.1);
        animation: gradient 5s ease infinite, fadeIn 2s;
    }
    
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    .subheader {
        color: #7B1FA2;
        font-size: 1.5rem;
        font-weight: 600;
        margin-top: 1.5rem;
        border-bottom: 2px solid #E1BEE7;
        padding-bottom: 0.5rem;
        animation: slideIn 1s;
    }
    
    @keyframes slideIn {
        from { transform: translateX(-20px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #7B1FA2 0%, #4A148C 100%);
        color: white;
        padding: 2rem 1rem;
    }
    
    .sidebar .sidebar-content .sidebar-section {
        margin-bottom: 2rem;
    }
    
    .stTextInput>div>div>input {
        border-radius: 12px;
        padding: 12px;
        box-shadow: 0 2px 4px rgba(156, 39, 176, 0.1);
        border: 1px solid #BA68C8;
    }
    
    .stButton>button {
        background: linear-gradient(90deg, #9C27B0 0%, #BA68C8 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px 24px;
        font-weight: 600;
        font-size: 1rem;
        box-shadow: 0 4px 6px rgba(156, 39, 176, 0.1);
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(156, 39, 176, 0.15);
        background: linear-gradient(90deg, #8E24AA 0%, #AB47BC 100%);
    }
    
    .stTextArea textarea {
        border-radius: 12px;
        padding: 15px;
        box-shadow: 0 2px 4px rgba(156, 39, 176, 0.1);
        border: 1px solid #BA68C8;
    }
    
    .error-message {
        color: #D32F2F;
        background-color: #FFEBEE;
        padding: 1rem;
        border-radius: 12px;
        border-left: 4px solid #D32F2F;
        animation: shake 0.5s;
    }
    
    @keyframes shake {
        0%, 100% { transform: translateX(0); }
        20%, 60% { transform: translateX(-5px); }
        40%, 80% { transform: translateX(5px); }
    }
    
    .success-message {
        color: #388E3C;
        background-color: #E8F5E9;
        padding: 1rem;
        border-radius: 12px;
        border-left: 4px solid #388E3C;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.01); }
        100% { transform: scale(1); }
    }
    
    .spinner-container {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 2rem;
    }
    
    .lottie-animation {
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Título principal animado
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown('<h1 class="main-title">🎥 Transcrição de Videos do Youtube usando IA</h1>', unsafe_allow_html=True)
    with col2:
        st_lottie(
            "https://assets9.lottiefiles.com/packages/lf20_gn0tojcq.json",
            speed=1,
            height=100,
            key="title_animation",
        )
    
    # Sidebar estilizada
    with st.sidebar:

        
        st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
        st.markdown('### ⚙️ CONFIGURAÇÕES')
        max_chars = st.slider(
            "🔠 Máximo de caracteres para exibir", 
            500, 1000000, 2000,
            help="Controla quantos caracteres da transcrição serão mostrados"
        )
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
        st.markdown('### ℹ️ COMO USAR')
        st.markdown("""
        1. 🔗 Cole a URL do vídeo  
        2. 📝 Veja a transcrição  
        3. ✨ Gere o resumo automático  
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("Desenvolvido com ❤️ usando:")
        st.markdown("- 🚀 Streamlit")
        st.markdown("- 🤖 Gemini AI")
        st.markdown("- 🎬 Pytube")

    # Área principal do aplicativo
    col1, col2 = st.columns([3, 1])
    
    with col1:
        video_url = st.text_input(
            "🔍 Insira a URL do vídeo do YouTube:",
            "",
            help="Cole o link completo do vídeo que deseja analisar",
            key="unique_video_url_input"
        )
        
        if video_url:
            try:
                with st.spinner("🔍 Analisando o vídeo, por favor aguarde..."):
                    video_id = youtube_utils.extract_video_id(video_url)
                    video_title = youtube_utils.get_video_title(video_url)
                    transcript = youtube_utils.get_transcript(video_id)

                    if video_title:
                        st.markdown(f'<div class="subheader">📺 {video_title}</div>', unsafe_allow_html=True)

                    if transcript:
                        st.markdown('<div class="subheader">📜 TRANSCRIÇÃO</div>', unsafe_allow_html=True)
                        with st.expander("Visualizar Transcrição Completa", expanded=True):
                            st.text_area(
                                "Transcrição",
                                value=transcript[:max_chars] + ("..." if len(transcript) > max_chars else ""),
                                height=300,
                                label_visibility="collapsed"
                            )

                        if st.button("✨ GERAR RESUMO AUTOMÁTICO", type="primary"):
                            with st.spinner("🧠 Processando com inteligência artificial..."):
                                gemini_utils.configure_gemini()
                                summary = gemini_utils.generate_summary(transcript)

                                if summary:
                                    st.markdown('<div class="subheader">📝 RESUMO GERADO</div>', unsafe_allow_html=True)
                                    st.markdown('<div class="success-message">✅ Resumo criado com sucesso!</div>', unsafe_allow_html=True)
                                    st.markdown(summary)
                                else:
                                    st.markdown('<div class="error-message">❌ Falha ao gerar o resumo</div>', unsafe_allow_html=True)
                    else:
                        st.markdown('<div class="error-message">⚠️ Transcrição não disponível para este vídeo</div>', unsafe_allow_html=True)
                        
            except Exception as e:
                st.markdown(f'<div class="error-message">🚨 Erro: {str(e)}</div>', unsafe_allow_html=True)

    with col2:
        st_lottie(
            "https://assets6.lottiefiles.com/packages/lf20_soCRuE.json",
            speed=1,
            height=200,
            key="stats_animation",
        )
        st.markdown("### 📊 ESTATÍSTICAS")
        if 'transcript' in locals():
            transcript_length = len(transcript) if transcript else 0
            word_count = len(transcript.split()) if transcript else 0
            st.metric("🔠 Caracteres", f"{transcript_length:,}")
            st.metric("📝 Palavras", f"{word_count:,}")
            st.metric("📊 Tamanho", f"{transcript_length/max_chars*100:.1f}% do máximo")
        else:
            st.info("ℹ️ Insira uma URL para ver as estatísticas")

if __name__ == "__main__":
    main()