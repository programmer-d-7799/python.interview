# import dataclass

# need comments
Id = int


@dataclass
class Task:
    id: Id
    body: str
    priority: int
    to_do_by: TimeStamp
    created: TimeStamp
    modified: TimeStamp
    created_by: User
    modified_by: User
    deleted: bool
    name: str
    status: str  # IN_PROGRESS, DELETED, COMPLETE, NOT_STARTED, FAILURE
    user: str  # source of task creation
    team: str  # team of user
    tags: Set


class SubTask(Task):
    parent_id: Id


class MainTask(Task):
    subtasks: list[SubTask]  # dict?


class TaskService:

    def __init__(self):
        self._id_counter = 0
        self._all_tasks: dict[Id, Task] = {}
        self._priority_tracker: Dict[Dict[Id]] = {}

    def _generate_task_id(self) -> Id:
        task_id = self._id_counter
        self._id_counter += 1
        return task_id

    def add(self, body: str) -> Id:
        task_id = self._generate_task_id()

        task = MainTask(id=task_id, body=body, priority=0, subtasks=[])
        self._all_tasks[task_id] = task
        # may be try except if expect possible task_id collision
        return task_id

    def add_subtask(self, body: str, parent_id: Id) -> Id:
        sub_task_id = self._generate_task_id()

        subtask = SubTask(id=sub_task_id, body=body, priority=0)
        self._all_tasks[sub_task_id] = task
        if parent_id not in self._all_tasks:
            raise KeyError("Cound not find parent task")
        parent_task = self._all_tasks[parent_id]
        parent_task.subtasks.append(subtask)
        return sub_task_id

    def increase_priority(self, task_id: Id) -> None:
        self._all_tasks[task_id].priority += 1
        current_priority = self._all_tasks[task_id].priority

    def edit(self, task_id: Id, new_body: str) -> None:
        self._all_tasks[task_id].body = new_body

    def delete(self, task_id: Id) -> None:
        del self._all_tasks[task_id]

    def get_all(self) -> list[Task]:
        return list(self._all_tasks.values())

    # get specific task

    # get high priotiy tasks


# dictionary that captures all top level tasks,

# root tasks, list of them , paginating. generate list of ids to return them from.
