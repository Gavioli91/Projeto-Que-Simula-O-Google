def exists_word(word, instance):
    letters = []

    for content in instance.content:
        for words in range(len(content['linhas_do_arquivo'])):
            if word.lower() in content['linhas_do_arquivo'][words].lower():
                letters.append({'linha': words + 1})

        if len(letters) > 0:
            return [{
                'palavra': word,
                'arquivo': content['nome_do_arquivo'],
                'ocorrencias': letters
                }]

        return []


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
