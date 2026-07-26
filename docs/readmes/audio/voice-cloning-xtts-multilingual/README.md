<!-- source: https://github.com/lauromotta/voice-cloning-xtts-multilingual.git sha: 32a3474f11a0e19eb7d0bd65fe6d1e9fcad09a35 readme: main/README.md -->
# lauromotta/voice-cloning-xtts-multilingual

Professional voice cloning system with 13 languages support using XTTS v2 + Google Gemini AI. Features: voice cloning, multi-language TTS, 17 narration styles, audio transcription with Whisper.

---

# 🎙️ Sistema de Clonagem de Voz Multi-idioma

Clone qualquer voz com apenas 6 segundos de áudio! Sistema profissional com **13 idiomas** e **17 estilos de narração**, usando tecnologia XTTS v2 + Google Gemini AI.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![XTTS](https://img.shields.io/badge/XTTS-v2-green.svg)
![Gemini](https://img.shields.io/badge/Gemini-AI-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 🎯 O que este sistema faz?

Este é um **sistema completo de clonagem e síntese de voz** que permite:

1. **Clonar qualquer voz** usando apenas ~6 segundos de áudio de referência
2. **Gerar narrações em 13 idiomas** diferentes com a voz clonada
3. **Aplicar 17 estilos profissionais** (jornalístico, narrativo, dramático, etc.)
4. **Traduzir automaticamente** textos para qualquer idioma suportado
5. **Transcrever áudios** em 99+ idiomas usando Whisper (offline, sem custo de API)

**Tecnologias principais:**
- **XTTS v2** (Coqui TTS) - Clonagem de voz neural de alta qualidade
- **Google Gemini AI** - Adaptação inteligente de texto e tradução profissional
- **OpenAI Whisper** - Transcrição de áudio local (sem uso de quota)
- **Gradio** - Interface web moderna e intuitiva

---

## ✨ Funcionalidades Resumidas

### 🎵 Clonagem de Voz
- Clone voz com ~6s de áudio de referência
- 13 idiomas: Português, Inglês, Espanhol, Francês, Alemão, Italiano, Japonês, Chinês, Russo, Coreano, Holandês, Polonês, Turco
- 17 estilos profissionais de narração
- Detecção automática do idioma do texto
- Tradução inteligente entre idiomas

### 🎤 Transcrição de Áudio
- Transcrição local com Whisper (99+ idiomas)
- Revisão com Gemini AI para correção de erros
- Tradução integrada do texto transcrito

---

## 🚀 Instalação

### Requisitos
- Python 3.10 ou superior
- FFmpeg instalado no sistema
- GPU NVIDIA com CUDA (opcional, mas recomendado)
- Chaves API do Google Gemini

### 1. Clonar repositório
```bash
git clone https://github.com/lauromotta/voice-cloning-xtts-multilingual.git
cd voice-cloning-xtts-multilingual
```

### 2. Criar ambiente virtual
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

### 3. Executar instalação automática
```bash
python setup.py
```

Ou instalar manualmente:
```bash
pip install -r requirements.txt
```

### 4. Instalar FFmpeg
**Windows:** Baixe em https://ffmpeg.org/download.html
**Linux:** `sudo apt install ffmpeg`
**Mac:** `brew install ffmpeg`

### 5. Configurar chaves Gemini API

#### 🔑 Como obter chaves do Google Gemini:

1. **Acesse o site:** https://aistudio.google.com/api-keys
2. **Clique em "Create API Key"** (ou "Criar chave de API")
3. **Selecione um projeto** (ou crie um novo)
4. **Copie a chave gerada** (formato: `AIzaSy...`)

#### 📝 Como configurar no arquivo .env:

1. **Copie o arquivo de exemplo:**
   ```bash
   # Windows
   copy .env.example .env

   # Linux/Mac
   cp .env.example .env
   ```

2. **Edite o arquivo `.env`** e adicione suas chaves:
   ```env
   # Para MÚLTIPLAS chaves (recomendado - rotação automática)
   GEMINI_API_KEYS=AIzaSyABC123...,AIzaSyDEF456...,AIzaSyGHI789...

   # OU apenas UMA chave
   GEMINI_API_KEY=AIzaSyABC123...
   ```

3. **Salve o arquivo** - pronto! O sistema detectará automaticamente as chaves

**Dica:** Você pode adicionar quantas chaves quiser separadas por vírgula. O sistema fará rotação automática quando uma atingir o limite de quota (~1.500 requisições/dia por chave).

---

## 📖 Uso

### Iniciar aplicação
```bash
python app.py
```

A aplicação abrirá automaticamente no navegador em: **http://127.0.0.1:7860**

### 🎵 Gerar Áudio

1. **Selecione ou faça upload** de um áudio de referência (mínimo ~6s)
2. **Digite ou cole** o texto para narração
3. O sistema **detecta automaticamente** o idioma do texto
4. **Marque "Traduzir"** se quiser gerar em outro idioma
5. **Selecione o estilo** de narração (neutro, jornalístico, etc.)
6. Clique em **"Gerar Áudio"**

### 🎤 Transcrever Áudio

1. Acesse a aba **"📝 Transcrever"**
2. **Faça upload** do áudio para transcrever
3. **Selecione o idioma** do áudio (ou "auto" para detecção)
4. Clique em **"Transcrever"**
5. (Opcional) Use **"Revisar com Gemini"** para corrigir erros
6. (Opcional) Use **"Traduzir"** para converter para outro idioma

---

## 🎨 Estilos de Narração

O sistema oferece **17 estilos profissionais**:

| Estilo | Descrição | Melhor para |
|--------|-----------|-------------|
| **Neutro** | Leitura equilibrada sem ênfases especiais | Uso geral |
| **Jornalístico** | Narração de noticiário profissional | Notícias, reportagens |
| **Narrativo** | História envolvente com variações de tom | Contos, histórias |
| **Documentário** | Tom de autoridade informativa | Documentários, educação |
| **Didático** | Explicativo e claro | Tutoriais, aulas |
| **Motivacional** | Inspirador e energizante | Palestras, coaching |
| **Dramático** | Teatral com alta intensidade | Teatro, performances |
| **Emocional** | Carga emocional profunda | Poesia, textos emotivos |
| **Reflexivo** | Contemplativo e filosófico | Meditações, reflexões |
| **Entusiasmado** | Animado e vibrante | Anúncios, promoções |
| **Institucional** | Corporativo profissional | Empresas, comunicados |
| **Solene** | Cerimonial e majestoso | Cerimônias, homenagens |
| **Suspense** | Cria tensão e mistério | Thrillers, mistério |
| **Explicativo** | Técnico e detalhado | Manuais, tutoriais |
| **Inspirador** | Eleva e motiva | Discursos, mensagens |
| **Lento** | Pausado e deliberado | Relaxamento, calma |
| **Rápido** | Acelerado e dinâmico | Anúncios rápidos |

---

## 🌍 Idiomas Suportados

### Para Clonagem de Voz (XTTS)
✅ Português | ✅ Inglês | ✅ Espanhol | ✅ Francês
✅ Alemão | ✅ Italiano | ✅ Japonês | ✅ Chinês
✅ Russo | ✅ Coreano | ✅ Holandês | ✅ Polonês | ✅ Turco

### Para Transcrição (Whisper)
✅ **99+ idiomas** incluindo todos acima + árabe, hindi, tailandês, sueco, e muitos outros

---

## ⚙️ Configurações Avançadas

### GPU (CUDA)
Para melhor desempenho, instale PyTorch com CUDA:
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Japonês
Para suporte completo ao japonês, as seguintes bibliotecas já estão incluídas:
- `cutlet` - Romanização
- `fugashi` - Tokenização
- `unidic-lite` - Dicionário

---

## 📊 Estrutura do Projeto

```
clonar-voz/
├── app.py                      # Interface Gradio principal
├── src/
│   ├── pipeline.py            # Pipeline de clonagem de voz
│   ├── voice_synthesizer.py   # Síntese com XTTS v2
│   ├── text_adapter.py        # Adaptação de texto com Gemini
│   ├── text_segmenter.py      # Segmentação inteligente
│   ├── style_presets.py       # Estilos de narração
│   ├── audio_cleaner.py       # Limpeza de áudio
│   ├── audio_postprocessor.py # Pós-processamento
│   ├── transcription.py       # Transcrição com Whisper
│   └── gemini_key_manager.py  # Gerenciamento de chaves
├── audio_input/               # Áudios de referência
├── output/                    # Áudios gerados
├── temp/                      # Arquivos temporários
├── requirements.txt           # Dependências Python
├── .env                       # Chaves API (não commitado)
└── README.md                  # Este arquivo
```

---

## 💡 Exemplos de Uso

### Exemplo 1: Narração de notícia em português
```
1. Texto: "O Brasil registrou hoje um aumento de 5% no PIB..."
2. Estilo: Jornalístico
3. Idioma: Português (Original)
4. Traduzir: ❌ Não
```

### Exemplo 2: História infantil em inglês
```
1. Texto: "Era uma vez, em um reino muito distante..."
2. Estilo: Narrativo
3. Idioma: Inglês
4. Traduzir: ✅ Sim
```

### Exemplo 3: Tutorial técnico em japonês
```
1. Texto: "Para configurar o servidor, primeiro abra o terminal..."
2. Estilo: Explicativo
3. Idioma: Japonês
4. Traduzir: ✅ Sim
```

---

## 🐛 Troubleshooting

### Erro: "GEMINI_API_KEY não configurada"
**Solução:** Crie o arquivo `.env` com pelo menos uma chave

### Erro: "FFmpeg não encontrado"
**Solução:** Instale FFmpeg e adicione ao PATH do sistema

### Erro: "CUDA out of memory"
**Solução:** Reduza o tamanho do texto ou use CPU (`device="cpu"`)

### Erro: "No module named 'cutlet'" (Japonês)
**Solução:** Execute `pip install cutlet fugashi unidic-lite`

---

## 📝 Changelog

### v2.0.0 (2025-01-21)
- ✨ Adicionada detecção automática de idioma
- ✨ Suporte a 13 idiomas com templates TTS específicos
- ✨ Checkbox para controlar tradução
- ✨ Dropdown interativo de idioma de saída
- ✨ Suporte completo a japonês
- 🐛 Corrigido: áudio em idiomas estrangeiros com sotaque português
- 📚 Melhorias na documentação

### v1.0.0 (2025-01-20)
- 🎉 Lançamento inicial
- ✨ Clonagem de voz com XTTS v2
- ✨ Transcrição com Whisper
- ✨ 17 estilos de narração
- ✨ Integração com Gemini AI

---

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

## 🙏 Agradecimentos

- [Coqui TTS](https://github.com/coqui-ai/TTS) - XTTS v2
- [Google Gemini](https://ai.google.dev/) - Adaptação de texto
- [OpenAI Whisper](https://github.com/openai/whisper) - Transcrição
- [Gradio](https://gradio.app/) - Interface web

---

## 📧 Contato

Para dúvidas, sugestões ou problemas, abra uma [issue](https://github.com/lauromotta/voice-cloning-xtts-multilingual/issues).

---

<div align="center">
  <strong>Desenvolvido com ❤️ usando Python</strong>
  <br>
  <sub>Sistema de clonagem de voz multi-idioma</sub>
</div>
