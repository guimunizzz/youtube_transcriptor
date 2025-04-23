📝 YouTube Transcript & Summary Generator
✨ Um aplicativo que extrai transcrições de vídeos do YouTube e gera resumos automáticos usando IA (Gemini 2.0-flash)

🚀 Recursos
✅ Extrai transcrições em português ou inglês
✅ Gera resumos automáticos com IA
✅ Interface amigável com Streamlit
✅ Estatísticas do vídeo (palavras, caracteres)
✅ Tradução automática (se necessário)

🛠️ Tecnologias
Python 3.10+

Streamlit (interface web)

Pytube (download de metadados do YouTube)

YouTube Transcript API (extração de legendas)

Google Gemini 2.0 Flash (IA para resumos)

⚡ Como Usar
Instale as dependências:

bash
pip install -r requirements.txt
Configure sua API Key do Gemini:
Crie um arquivo .env e adicione:

env
GOOGLE_API_KEY=sua_chave_aqui
Execute o app:

bash
streamlit run main.py
No navegador:

Cole a URL de um vídeo do YouTube

Veja a transcrição

Clique em "✨ GERAR RESUMO AUTOMÁTICO"

📋 Estrutura do Projeto
.
├── main.py              # Aplicação principal
├── youtube_utils.py     # Extração de transcrições
├── gemini_utils.py      # Integração com a IA
├── requirements.txt     # Dependências
├── .env.example         # Modelo para variáveis de ambiente
└── README.md            # Este arquivo
🌟 Exemplo de Uso
Demonstração
(Substitua por um screenshot real depois)

📌 Notas
Requer conexão com internet

Vídeos com restrição de idade podem não funcionar

Limite de caracteres para resumos: ~30k tokens

📄 Licença
MIT © [Seu Nome]

🔗 Disponível no GitHub: github.com/seu-usuario/youtube-ai-summarizer

✨ Contribuições são bem-vindas! Envie um PR ou abra uma issue.
