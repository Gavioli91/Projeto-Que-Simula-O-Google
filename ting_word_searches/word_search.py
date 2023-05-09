def exists_word(word, instance):
    index_of_words = []

    for content in instance.content:
        for index in range(len(content['linhas_do_arquivo'])):
            if word.lower() in content['linhas_do_arquivo'][index].lower():
                index_of_words.append({'linha': index + 1})

        if len(index_of_words) > 0:
            return [{
                'palavra': word,
                'arquivo': content['nome_do_arquivo'],
                'ocorrencias': index_of_words
                }]

        return []


def search_by_word(word, instance):
    index_of_words = []

    for content in instance.content:
        dict = {
                'palavra': word,
                'arquivo': content['nome_do_arquivo'],
                'ocorrencias': []
                }
        count = 1
        for index in content['linhas_do_arquivo']:
            if word.lower() in index.lower():
                dict['ocorrencias'].append({
                    'linha': count, 'conteudo': index
                })
            count += 1
        if len(dict['ocorrencias']) != 0:
            index_of_words.append(dict)
        dict['ocorrencias'] == []

        return index_of_words
