from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for item in range(len(instance)):
        if instance.search(item)['nome_do_arquivo'] == path_file:
            return None
    if txt_importer(path_file):
        data = {
            'nome_do_arquivo': path_file,
            'qtd_linhas': len(txt_importer(path_file)),
            'linhas_do_arquivo': txt_importer(path_file)
        }
    instance.enqueue(data)
    print(data)


def remove(instance):
    instance = instance.dequeue()
    if len(instance) > 0:
        return print(
            f"Arquivo {instance['nome_do_arquivo']} removido com sucesso")
    return print('Não há elementos')


def file_metadata(instance, position):
    try:
        instance = instance.search(position)
        return print(instance)
    except IndexError:
        return print('Posição inválida', instance = sys.stderr)
