
# 🧊 Melhoria de manifests de Interface (.json)

Este projeto utiliza a **API Gemini da Google** para formatar e melhorar automaticamente o layout visual de arquivos JSON que representam interfaces gráficas. O script processa todos os arquivos `.json` contidos na pasta `manifests/`, reorganiza os componentes da tela e salva os ajustes na pasta `manifestAjustado/`.

---

## 🚀 Funcionalidades

- Carrega arquivos JSON de manifesto com interfaces de usuário.
- Usa IA (Gemini) para melhorar o layout automaticamente.
- Ajusta posição, alinhamento, cores e espaçamentos dos componentes.
- Salva o resultado formatado em uma nova pasta.

---

## 🧰 Requisitos

### Linguagem
- Python 3.9+

### Extensões recomendadas no VS Code
Instale estas extensões para facilitar o desenvolvimento:

- **Python** (ms-python.python)
- **Pylance** (ms-python.vscode-pylance)
- **JSON Tools** (eriklynd.json-tools)
---

## 📦 Instalação

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Crie um ambiente virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências**
   ```bash
   pip install google-generativeai
   ```

---

## 🔑 Configuração da API Gemini

1. Vá até [Google AI Studio](https://aistudio.google.com/app/apikey) e gere uma chave de API.
2. Substitua a variável `GOOGLE_API_KEY` no código pelo valor da sua chave:
   ```python
   GOOGLE_API_KEY = "SUA_CHAVE_AQUI"
   ```

---

## 📁 Como usar

1. Coloque os arquivos `.json` de manifesto na pasta `manifests/`.
2. Execute o script:
   ```bash
   python seu_script.py
   ```
3. Os arquivos ajustados serão salvos na pasta `manifestAjustado/`.

---

## 📝 Observações

- Certifique-se de que os arquivos `.json` estejam bem formatados.

