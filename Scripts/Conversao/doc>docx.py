import os
import win32com.client

def criar_diretorio(diretorio):
    """Cria o diretório se ele não existir."""
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)

def converter_doc_para_docx(caminho_arquivo, caminho_arquivo_novo, word):
    """Converte um arquivo .doc para .docx."""
    try:
        documento = word.Documents.Open(caminho_arquivo)  # Abre o documento .doc
        documento.SaveAs(caminho_arquivo_novo, FileFormat=16)  # Salva como .docx
        print(f"Convertido: {caminho_arquivo} -> {caminho_arquivo_novo}")
    except Exception as e:
        print(f"Erro ao processar {caminho_arquivo}: {e}")
    finally:
        documento.Close()  # Fecha o documento

def main():
    # Definindo os caminhos das pastas de origem e destino
    pasta_origem = "caminho/para/arquivos/doc"
    pasta_destino = "caminho/para/arquivos/docx"

    # Criar o diretório de destino se não existir
    criar_diretorio(pasta_destino)

    # Inicializando a aplicação Word
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False  # Mantém o Word invisível durante a execução

    # Contador de arquivos convertidos
    contador_convertidos = 0

    # Iterando sobre os arquivos na pasta de origem
    for arquivo in os.listdir(pasta_origem):
        if arquivo.endswith(".doc"):
            caminho_arquivo = os.path.join(pasta_origem, arquivo)  # Caminho completo do arquivo
            nome_arquivo_novo = os.path.splitext(arquivo)[0] + ".docx"
            caminho_arquivo_novo = os.path.join(pasta_destino, nome_arquivo_novo)  # Caminho completo do novo arquivo
            
            # Converte o arquivo
            converter_doc_para_docx(caminho_arquivo, caminho_arquivo_novo, word)
            contador_convertidos += 1

    # Encerra a aplicação Word
    word.Quit()

    # Exibe a quantidade de arquivos convertidos
    print(f"Conversão concluída: {contador_convertidos} arquivos convertidos!")

if __name__ == "__main__":
    main()
