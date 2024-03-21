import dataclass
from typing import Dict, List, Optional
from pydantic import BaseModel


@dataclass  # could change this class to be a sub class of BaseModel
class Task:

    body: str
    name: str
    id: str
    deleted: bool


class AddResponse(BaseModel):
    success: bool
    problem_details: Optional[Dict]


class TaskService:

    def __init__(self):

        self.store: Dict[Task] = {}  # key as id , value = task object
        # self.deleted_store : Dict[Task] = {} # key as id , value = task object

    def add(self, body: str) -> AddResponse:

        self.store.append(Task(body))

    def delete(self, user_token,  id: str) -> DeleteResponse:
        if not is_user_token_valid(user_token):
            return #responseindicating not authed #auth for deleiton,  

        if  id in self.store:
            item_to_delete = self.store[id]
        
            if item_to_delete.deleted:
                #return response iondicating already deleted
            else:
                #return response indicating deleted
        else:
            #return response idnicating never existed


INSTANCE = TaskService()



