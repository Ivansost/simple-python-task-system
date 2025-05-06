from Service.task_service import Task_Service
from Service.user_service import User_Service

def main():
    task_Service = Task_Service()
    user_Service = User_Service()

    user_Service.add_user(123, "John Doe", "ifjasd@gmail.com")

    task_Service.create_task(1, "Task 1", "Description for Task 1")
    task_Service.create_task(2, "Task 2", "Description for Task 2") 
    task_Service.create_task(3, "Task 3", "Description for Task 3")
    task_Service.create_task(4, "Task 4", "Description for Task 4")

    print(task_Service.complete_task())
    print(task_Service.complete_task())
    print(task_Service.complete_task())
    print(task_Service.complete_task())


if __name__ == "__main__":
    main()