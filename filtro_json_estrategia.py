import json 

materias = ['portugues', 'dir_adm', 'sist_op', 'dev_sist', 'redes_seg', 'eng_soft', 'gestao', 'banco_dados']

for materia in materias:
    with open(materia + '.json', 'r') as arquivo:
        with open(materia + '.txt', 'w') as saida:
            dados = json.load(arquivo)
            for aula in dados['data']['aulas']:
                for video in aula['videos']:
                    print(video['resolucoes']['720p'])
                    saida.write(video['resolucoes']['720p'] + '\n')