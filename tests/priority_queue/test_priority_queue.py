import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    queue = PriorityQueue()
    file1 = {
        "nome_do_arquivo": "file01.txt",
        "qtd_linhas": 5,
        "linhas_do_arquivo": [
            "Fundamentos",
            "Front-end",
            "Back-end",
            "CS",
            "Eletiva",
        ],
    }
    file2 = {
        "nome_do_arquivo": "file02.txt",
        "qtd_linhas": 3,
        "linhas_do_arquivo": ["Fundamentos", "Front-end", "Back-end"],
    }
    file3 = {
        "nome_do_arquivo": "file03.txt",
        "qtd_linhas": 4,
        "linhas_do_arquivo": ["Fundamentos", "Front-end", "Back-end", "CS"],
    }

    # Teste de enqueue
    queue.enqueue(file1)
    assert len(queue) == 1
    assert len(queue.regular_priority) == 1
    assert len(queue.high_priority) == 0

    queue.enqueue(file2)
    assert len(queue) == 2
    assert len(queue.regular_priority) == 1
    assert len(queue.high_priority) == 1

    queue.enqueue(file3)
    assert len(queue) == 3
    assert len(queue.regular_priority) == 1
    assert len(queue.high_priority) == 2

    # Teste de search
    assert queue.search(0) == file2
    assert queue.search(1) == file3
    assert queue.search(2) == file1

    # Teste para índice inválido em search
    with pytest.raises(IndexError):
        queue.search(3)

    # Teste de dequeue
    assert queue.dequeue() == file2
    assert queue.dequeue() == file3
    assert queue.dequeue() == file1
