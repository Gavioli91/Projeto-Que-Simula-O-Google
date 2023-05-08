from ting_file_management.priority_queue import PriorityQueue
import pytest


mock = {'qtd_linhas': 2}
mock1 = {'qtd_linhas': 5}


def test_basic_priority_queueing():
    directory = PriorityQueue()

    directory.enqueue(mock)
    directory.enqueue(mock1)

    assert len(directory) == 1
    assert directory.search(0) == mock
    directory.dequeue()
    assert len(directory) == 2

    with pytest.raises(IndexError):
        directory.search(3)
