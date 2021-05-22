TASK №1


1. Ability to create:
agent: http://127.0.0.1:8000/api/v1/agent/agent/create
transactions: http://127.0.0.1:8000/api/v1/transactions/transaction/create

2.Ability to view 
agent: http://127.0.0.1:8000/api/v1/agent/agent/all
transactions: http://127.0.0.1:8000/api/v1/transactions/transaction/all

3. Ability edit / delete information:
agent: http://127.0.0.1:8000/api/v1/agent/agent/detail/<int:pk>/
transactions: http://127.0.0.1:8000/api/v1/transactions/transaction/etail/<int:pk>/

<int:pk> - object id.

4.Ability to view all user’s payments:

http://127.0.0.1:8000/api/v1/transactions/transaction/all/?adent=id1,id2

Swagger does not work


TASK №2

In the utils.p file and implemented a function that returns the n-th number of the Fibonacci sequence.

Example:

print(fibonacci(15))
>>>610

print(fibonacci(9))
>>>34

"# akvelon_python_internship_3_Dmitrey_Malykhin"  
