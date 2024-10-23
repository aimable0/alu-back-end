#!/usr/bin/python3
"""
    python script that returns TODO list progress for a given employee ID
"""
import sys
import requests
from rich import print_json

def get_data(id):

    try:
        """The first attempt to get name of the provided userid"""
        url1 = "https://jsonplaceholder.typicode.com/users"
        params = {
        "id": id
        }
        response = requests.get(url1, params=params)
        user_data = response.json()
        employee_name = user_data[0]["name"]

        """second attempt to get the todo of a user with the specified id"""
        url2 = "https://jsonplaceholder.typicode.com/todos"
        params_1 = {
        "userId": id
        }
        response = requests.get(url2, params=params_1)
        todos = response.json()
        
        total = len(todos)
        trues = 0
        for item in todos:
            if item['completed'] == True:
                trues += 1

        tasks = f"({trues}/{total})"

        print(f"Employee {employee_name} is done with {tasks}:")
        for item in todos:
            if item['completed'] == True:
                print(f"\t {item['title']}")

    except requests.RequestException as error:
        print(f"Failed to retrieve data. \nError message:{error}")
    except Exception:
        print("Request Failed, Be sure the provided id is with the range and try again")

def main():
    """check if an argument is passed at the command-line"""
    if len(sys.argv) > 1:
        id = sys.argv[1]
        get_data(id)
    else:   
        print('Please provide an id') 
        sys.exit(1)  

"""make sure the code doesn't work when imported"""
if __name__ == "__main__":
    main()