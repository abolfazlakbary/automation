import os

def create_files_from_string(input_string):

    api_path = "app/api/v1"
    directory_path = os.path.join(api_path, input_string)
    os.makedirs(directory_path, exist_ok=True)

    schema_path = os.path.join(directory_path, "schema")
    os.makedirs(schema_path, exist_ok=True)

    router_path = (os.path.join(directory_path, 'router.py'))
    with open(router_path, 'w') as new_router:
        pass

    controller_path = (os.path.join(directory_path, 'controller.py'))
    with open(controller_path, 'w') as new_controller:
        pass
    
    request_path = (os.path.join(schema_path, 'request.py'))
    with open(request_path, 'w') as new_request:
        pass

    response_path = (os.path.join(schema_path, 'response.py'))
    with open(response_path, 'w') as new_responbse:
        pass

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    create_files_from_string(input_string)