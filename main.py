import os
import shutil

# Diretório de origem
origem = "D:/marcia/"

# Diretórios de destino
destino_imagens = "D:/filtro/fotos/"
destino_documentos = "D:/filtro/documentos/"
destino_videos = "D:/filtro/video/"
destino_musicas = "D:/filtro/musica/"
destino_compactado = "D:/filtro/compactado/"

# Criar os diretórios de destino se não existirem
os.makedirs(destino_imagens, exist_ok=True)
os.makedirs(destino_documentos, exist_ok=True)
os.makedirs(destino_videos, exist_ok=True)
os.makedirs(destino_musicas, exist_ok=True)
os.makedirs(destino_compactado, exist_ok=True)

def gerar_novo_nome(destino, nome_original):
    base, extensao = os.path.splitext(nome_original)
    contador = 1
    novo_nome = os.path.join(destino, f"{base}_{contador}{extensao}")
    while os.path.exists(novo_nome):
        contador += 1
        novo_nome = os.path.join(destino, f"{base}_{contador}{extensao}")
    return novo_nome

def mover_e_limpar_arquivos(diretorio):
    esta_vazio = True

    for item in os.listdir(diretorio):
        path_completo = os.path.join(diretorio, item)
        
        if os.path.isdir(path_completo):
            if not mover_e_limpar_arquivos(path_completo):
                os.rmdir(path_completo)
                print(f"Pasta removida: {path_completo}")
            else:
                esta_vazio = False
        else:
            destino_final = None
            extensao = os.path.splitext(item)[1].lower()
            if extensao in ['.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff']:
                destino_final = destino_imagens
            elif extensao in ['.docx', '.doc', '.xlsx', '.xls', '.pptx', '.ppt', '.pdf', '.csv', '.rtf', '.odt']:
                destino_final = destino_documentos
            elif extensao in ['.mp4', '.mov', '.wmv', '.avi', '.mkv', '.flv', '.webm', '.3gp']:
                destino_final = destino_videos
            elif extensao in ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a', '.wma', '.mpg']:
                destino_final = destino_musicas
            elif extensao in ['.gz', '.zip', '.rar', '.7z']:
                destino_final = destino_compactado

            # Se um destino foi definido, move o arquivo
            if destino_final:
                destino_path = os.path.join(destino_final, os.path.basename(path_completo))
                if os.path.exists(destino_path):
                    novo_nome = gerar_novo_nome(destino_final, os.path.basename(path_completo))
                    shutil.move(path_completo, novo_nome)
                    print(f"Arquivo movido para {novo_nome}")
                else:
                    shutil.move(path_completo, destino_path)
                    print(f"Arquivo movido para {destino_path}")
            # Se não for para mover, verifique se deve ser deletado
            elif extensao in ['.sxw', '.iso', '.py', '.woff', '.prproj', '.ani', '.dat', '.jsp', '.java', '.exe', '.dll', '.lnk', '.ttf', '.cab', '.txt', '.reg', '.xml', '.ico', '.h', '.sqlite', '.ini', '.edb', '.html', '.elf', '.jar', '.webp', '.apk', '.svg', '.bat', '.wpd', '.f', '.c', '.db'] or extensao == '':
                os.remove(path_completo)
                print(f"Arquivo removido: {path_completo}")
            else:
                esta_vazio = False

    return not esta_vazio

# Iniciar o processo
mover_e_limpar_arquivos(origem)

print("Processo de movimentação e limpeza de arquivos concluído com sucesso!")
