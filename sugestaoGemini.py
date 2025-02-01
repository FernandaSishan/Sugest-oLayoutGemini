import google.generativeai as genai
import os
import json

# Configure a API Key do Google
GOOGLE_API_KEY = "AIzaSyDuZI-_BGgqdiKCKOpc7woUQlAKBqY879k"  # Sua chave

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

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
    
    Por favor, ajuste a posição dos componentes no manifesto para criar um layout mais visualmente organizado e alinhado.
    O objetivo é garantir que os elementos da interface fiquem bem distribuídos e harmoniosos, com espaçamento adequado
    entre eles, alinhamento consistente e uma estrutura mais agradável esteticamente. Mantenha a hierarquia e a funcionalidade do design, 
    mas otimize a disposição dos componentes para melhorar a clareza visual e a fluidez da interface,
    resultando em uma aparência sintaticamente mais bonita e equilibrada.
    
    {json.dumps(manifest_data, indent=2)}
    
    
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Erro ao processar com a API: {e}")
        return None

def save_formatted_manifest(file_path, formatted_manifest):
    """Salva o manifesto formatado em um novo arquivo."""
    if formatted_manifest is None:
        return

    try:
        new_file_path = file_path.replace(".json", "_formatted.json")
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
