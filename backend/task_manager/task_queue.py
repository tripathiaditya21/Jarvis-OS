from collections import deque


class TaskQueue:

    def __init__(self):

        self.queue = deque()

    def add(self, task):

        self.queue.append(task)

    def pop(self):

        if self.queue:
            return self.queue.popleft()

        return None

    def empty(self):

        return len(self.queue) == 0

    def clear(self):

        self.queue.clear()

    def size(self):

        return len(self.queue)