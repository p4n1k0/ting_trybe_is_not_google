def exists_word(word, instance):
    occurrences = list()
    for item in instance.queue:
        for index, linha in enumerate(item['linhas_do_arquivo']):
            if word.lower() in linha.lower():
                occurrences.append({'linha': index + 1})
    if occurrences:
        occurrences = [{
            'palavra': word,
            'arquivo': item['nome_do_arquivo'],
            'ocorrencias': occurrences
        }]
    return occurrences

def search_by_word(word, instance):
    """Aqui irá sua implementação"""
