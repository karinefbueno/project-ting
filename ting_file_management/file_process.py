from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue
import sys


def process(path_file, instance: Queue):
    for item in instance.queue:
        if item["nome_do_arquivo"] == path_file:
            return

    linhas = txt_importer(path_file)

    dicionario = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(linhas),
        "linhas_do_arquivo": linhas,
    }

    instance.enqueue(dicionario)
    print(dicionario)


def remove(instance: Queue):
    if len(instance.queue) == 0:
        return print("Não há elementos", file=sys.stdout)
    else:
        removed_file = instance.dequeue()
        return print(
            f"Arquivo {removed_file['nome_do_arquivo']} removido com sucesso",
            file=sys.stdout,
        )


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        print(file)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
