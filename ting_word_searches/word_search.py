from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
    occurrences = []
    for file in instance.queue:
        file_occurrences = []
        for line_number, line in enumerate(file["linhas_do_arquivo"]):
            print("linha 9", line)
            if word.lower() in line.lower():
                file_occurrences.append({"linha": line_number+1})
        if len(file_occurrences) > 0:
            occurrences.append(
                {
                    "palavra": word,
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": file_occurrences,
                }
            )
    return occurrences


def search_by_word(word, instance):
    occurrences = []
    for file in instance.queue:
        file_occurrences = []
        for line_number, line in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                file_occurrences.append(
                    {
                        "linha": line_number+1,
                        "conteudo": line
                    }
                )
        if len(file_occurrences) > 0:
            occurrences.append(
                {
                    "palavra": word,
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": file_occurrences,
                }
            )
    return occurrences
