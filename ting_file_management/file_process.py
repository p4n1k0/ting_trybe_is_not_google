from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for item in range(len(instance)):
        if instance.search(item)['nome_do_arquivo'] == path_file:
            return None
    file = txt_importer(path_file)
    if file:
        data = {
            'nome_do_arquivo': path_file,
            'qtd_linhas': len(file),
            'linhas_do_arquivo': file
        }
    instance.enqueue(data)
    print(data)


def remove(instance):
    instance = instance.dequeue()
    if len(instance) > 0:
        return print(f"Arquivo {instance['nome_do_arquivo']} removido com sucesso")
    return print('Não há elementos')

def file_metadata(instance, position):
    """Aqui irá sua implementação"""
