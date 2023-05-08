import sys
from ting_file_management.file_management import txt_importer


def process(path_file, archive):
    directory = txt_importer(path_file)
    create_file = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(directory),
        'linhas_do_arquivo': directory
    }

    for content in archive.content:
        if content['nome_do_arquivo'] == path_file:
            return None

    archive.enqueue(create_file)
    return sys.stdout.write(str(create_file))


def remove(instance):
    if len(instance) > 0:
        directory = instance.dequeue()
        path_file = directory['nome_do_arquivo']
        return sys.stdout.write(
            str(f'Arquivo {path_file} removido com sucesso\n'))
    return sys.stdout.write(str('Não há elementos\n'))


def file_metadata(instance, position):
    try:
        return sys.stdout.write(
            str(instance.search(position)
                ))
    except IndexError:
        return sys.stderr.write('Posição inválida')
