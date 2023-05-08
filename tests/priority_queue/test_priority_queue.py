from ting_file_management.priority_queue import PriorityQueue
import pytest


mock = {
    "nome_do_arquivo": "nome1.txt",
    "qtd_linhas": 10,
}
mock1 = {
    "nome_do_arquivo": "nome2.txt",
    "qtd_linhas": 15,
}


def test_basic_priority_queueing():
    directory = PriorityQueue()
    directory.enqueue(mock)
    directory.enqueue(mock1)
    assert len(directory) == 1
    assert directory.search(0) is mock
    directory.dequeue()
    assert len(directory) == 2
    with pytest.raises(IndexError):
        directory.search(3)
    assert directory.is_priority(mock) is False
