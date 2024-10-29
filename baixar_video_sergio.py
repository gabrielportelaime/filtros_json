import os
import requests


def baixar_videos(arquivo_urls, pasta):
    os.mkdir(pasta)
    with open(arquivo_urls, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            url = linha.strip()
            if url:
                try:
                    nome_original = os.path.basename(url)
                    nome_novo = os.path.splitext(nome_original)[0] + "_novo.mp4"
                    resposta = requests.get(url, verify=False, stream=True)
                    resposta.raise_for_status()
                    with open(pasta + '/' + nome_novo, "wb") as arquivo_video:
                        for parte in resposta.iter_content(chunk_size=8192):
                            arquivo_video.write(parte)
                    print(f"Download de '{nome_original}' concluído. Salvo como '{nome_novo}'")
                except requests.exceptions.RequestException as erro:
                    print(f"Erro ao baixar '{url}': {erro}")

if __name__ == "__main__":
    materias = ['portugues', 'dir_adm', 'sist_op', 'dev_sist', 'redes_seg', 'eng_soft', 'gestao', 'banco_dados']
    for materia in materias:
        caminho_arquivo_urls = materia + ".txt"
        baixar_videos(caminho_arquivo_urls, materia)
