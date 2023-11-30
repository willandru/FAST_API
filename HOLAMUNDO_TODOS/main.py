from fastapi import FastAPI, HTTPException
from models import Todo

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

todos = []


# GEt all todos

@app.get("/todos")
async def get_todos():
    return {"todos": todos}

#GEt single todo
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return{"todo":todo}
    return {"message": "No todos found"}


#Create a todo
@app.post("/todos")
async def create_item(todo: Todo):
    todos.append(todo)
    return {"message": "Todo has been added"}



# UPDATE A todo
@app.put("/todos")
async def update_todo( newTodo: Todo):

    for i in todos:
        if(i.id==newTodo.id):
            i.item = newTodo.item
    return{"message":"todo has been UPDATED"}

    raise HTTPException(status_code=404, detail="Todo ID not found")


#DELETE A todo
@app.delete("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return{"message":"todo has been removed¡"}
    raise HTTPException(status_code=404, detail="Todo ID not found")



