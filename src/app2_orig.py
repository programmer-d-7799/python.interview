Id = int


@dataclasses.dataclass
class Task:
    id: Id
    body: str
    priority: int
    subtasks: list[Task]


class TaskService:

    def __init__(self):
        self._id_counter = 0
        self._all_tasks: dict[Id, Task] = {}

    def add(self, body: str) -> Id:
        task_id = self._id_counter
        self._id_counter += 1

        task = Task(id=task_id, body=body, priority=0, subtasks=[])
        self._all_tasks[task_id] = task
        return task_id

    def add_subtask(self, body: str, parent_id: Id) -> Id:
        task_id = self._id_counter
        self._id_counter += 1

        task = Task(id=task_id, body=body, priority=0, subtasks=[])
        self._all_tasks[task_id] = task
        if parent_id not in self._all_tasks:
            raise KeyError("Cound not find parent task")
        self._all_tasks[parent_id].subtasks.append(task)
        return task_id

    def increase_priority(self, task_id: Id) -> None:
        self._all_tasks[task_id].priority += 1

    def edit(self, task_id: Id, new_body: str) -> None:
        self._all_tasks[task_id].body = new_body

    def delete(self, task_id: Id) -> None:
        del self._all_tasks[task_id]

    def get_all(self) -> list[Task]:
        return list(self._all_tasks.values())
