import google.generativeai as genai
import os
import json

# Configure a API Key do Google
GOOGLE_API_KEY = "AIzaSyDuZI-_BGgqdiKCKOpc7woUQlAKBqY879k"  # Sua chave

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro')

def load_manifest(file_path):
    """Carrega um arquivo JSON (manifesto)."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado: {file_path}")
        return None
    except json.JSONDecodeError as e:
        print(f"Erro ao ler JSON: {e}")
        return None

def format_manifest(manifest_data):
    """Formata o manifesto com sugestões da API Google AI."""
    if manifest_data is None:
        return None

    prompt = f"""
    
    Ajuste a posição dos componentes no manifesto para criar um layout mais visualmente organizado e alinhado.
    O objetivo é garantir que os elementos da interface fiquem bem distribuídos e harmoniosos, com espaçamento adequado
    entre eles, alinhamento consistente e uma estrutura mais agradável esteticamente. Se necessário para melhor visualização, altere as cores dos componentes, botões e cor da fonte. não adicione comentários no código.
    Ajuste todas as screens(telas) do arquivo, preciso que todas sejam ajustadas.
    
    {json.dumps(manifest_data, indent=2)}
    
    
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Erro ao processar com a API: {e}")
        return None

def save_formatted_manifest(file_path, formatted_manifest):
    """Salva o manifesto formatado em um novo arquivo na pasta 'manifestAjustado'."""
    if formatted_manifest is None:
        return

    try:
        adjusted_dir = os.path.join(os.getcwd(), "manifestAjustado")
        if not os.path.exists(adjusted_dir):
            os.makedirs(adjusted_dir)  # Cria a pasta se não existir

        new_file_path = os.path.join(adjusted_dir, os.path.basename(file_path).replace(".json", "_testeUltracongelador3.json"))
        with open(new_file_path, 'w') as file:
            file.write(formatted_manifest)
        print(f"Manifesto formatado salvo em: {new_file_path}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

def process_manifest(file_path):
    """Processa um arquivo de manifesto e salva a versão formatada."""
    print(f"\nProcessando arquivo: {file_path}\n")
    manifest_data = load_manifest(file_path)
    
    if manifest_data:
        formatted_manifest = format_manifest(manifest_data)
        if formatted_manifest:
            save_formatted_manifest(file_path, formatted_manifest)

if __name__ == "__main__":
    manifest_dir = os.path.join(os.getcwd(), "manifests")
    
    if not os.path.exists(manifest_dir):
        os.makedirs(manifest_dir)

    for filename in os.listdir(manifest_dir):
        if filename.endswith(".json"):
            file_path = os.path.join(manifest_dir, filename)
            process_manifest(file_path)
