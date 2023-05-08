import sys
from ting_file_management.file_management import txt_importer


def process(path_file, archive):
    directory = txt_importer(path_file)
    create_file = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(directory),
        'linhas_do_arquivo': directory,
    }

    for content in archive.data:
        if content['nome_do_arquivo'] == path_file:
            return False

    archive.enqueue(create_file)

    return sys.stdout.write(str
                            (create_file)
                            )


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
