# 🎥 Transcrição de Vídeos do YouTube com Resumo por IA

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Gemini](https://img.shields.io/badge/Google_Gemini-2.0_Flash-4285F4?logo=google&logoColor=white)

Ferramenta que extrai transcrições de vídeos do YouTube e gera resumos automáticos usando a inteligência artificial do Google Gemini Pro.

## 🌟 Funcionalidades

- 🎬 **Extrai transcrições automaticamente** - Legendas em português ou inglês
- ✨ **Gera resumos com IA** - Utiliza o Gemini 2.0 flash para criar resumos
- 🌍 **Tradução integrada** - Opção de tradução para português
- 📊 **Estatísticas do vídeo** - Contagem de caracteres e palavras
- 🖥️ **Interface simples** - Aplicação web fácil de usar com Streamlit

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python 3.10+
- **Interface Web**: Streamlit
- **Integração com YouTube**: Pytube, youtube-transcript-api
- **Processamento de IA**: Google Generative AI (Gemini 2.0 flash)
- **Ambiente**: python-dotenv

## 🚀 Começando Rápido

### Pré-requisitos
- Python 3.10+
- Chave de API do Google (para Gemini)

### Instalação
1. Clone o repositório:
```bash
git clone https://github.com/seuusuario/transcritor-youtube.git
cd transcritor-youtube
```
Instale as dependências:
```
pip install -r requirements.txt
```
Crie o arquivo .env:
```
GOOGLE_API_KEY=sua_chave_aqui
```
### Como Usar
Execute a aplicação:
```
streamlit run main.py
```
Depois:

Cole a URL de um vídeo do YouTube

Veja a transcrição extraída

Clique em "✨ GERAR RESUMO" para análise por IA
```
📂 Estrutura do Projeto
.
├── main.py                 # Lógica principal
├── youtube_utils.py        # Manipulação de transcrições
├── gemini_utils.py         # Integração com Gemini
├── requirements.txt        # Dependências
├── .env.example            # Modelo de configuração
└── README.md               # Documentação
```

## ⚠️ Limitações
Requer conexão com internet

Pode não funcionar com vídeos restritos

Disponibilidade de legendas depende do vídeo

Versão gratuita da API Gemini tem limites

## 🤝 Como Contribuir
Contribuições são bem-vindas! Siga esses passos:

Faça um fork do projeto

Crie sua branch de feature

Faça commit das mudanças

Envie para a branch

Abra um Pull Request

