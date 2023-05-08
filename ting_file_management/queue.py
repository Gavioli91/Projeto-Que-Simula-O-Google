from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.content = list()

    def __len__(self):
        return len(self.content)

    def enqueue(self, value):
        self.content.append(value)

    def dequeue(self):
        if len(self.content) == 0:
            return None
        return self.content.pop(0)

    def search(self, index):
        if index < 0 or index >= len(self.content):
            raise IndexError("Índice Inválido ou Inexistente")
        return self.content[index]
