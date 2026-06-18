from fastapi import FastAPI
app=FastAPI()
tasks=[]
@app.get("/tasks")
def get_all_tasks():
    return {"tasks":tasks}
@app.post("/tasks/add")
def add_task(task:str):
    tasks.append({"task":task,"completed":False})
    return {"message":"Task added succesfully!","task":task}
@app.put("/tasks/complete/{task_id}")
def complete_task(task_id:int):
    if(task_id>len(tasks)):
        return {"Error id not found!"}
    tasks[task_id]["completed"]=True
    return {"meassage":"Task marked completed!","task":tasks[task_id]}
@app.delete("/tasks/delete/{task_id}")
def delete_task(task_id:int):
    if(task_id>len(tasks)):
        return {"Error ID not found!"}
    removed=tasks.pop(task_id)
    return {"message":"Task deleted successfully","Task":removed}