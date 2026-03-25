'''JSON(JavaScript Object Notation) 
Unflattened JSON: {'user' :{'Rachel':{'UserID':1717171717, 'Email': 'rachel1999@gmail.com', 'friends': ['John', 'Jeremy', 'Emily']}}} 
Flattened JSON = {'user_Rachel_friends_2': 'Emily', 'user_Rachel_friends_0': 'John', 'user_Rachel_UserID': 1717171717, 'user_Rachel_Email': 'rachel1999@gmail.com', 'user_Rachel_friends_1': 'Jeremy'}
'''

unflattened = {'user' :{'Rachel':{'UserID':1717171717, 'Email': 'rachel1999@gmail.com', 'friends': ['John', 'Jeremy', 'Emily']}}} 

## Flattening JSON
# import json
# # Pretty-print the formatted/prettified JSON with indentation
# print("\n\nFormatted (Prettified) JSON:")
# print(json.dumps(unflattened, indent=4))

##Naming convention for flattened keys: parent_child or parent_child_index for lists
def flatten_json(data, parent_key='', sep='_'):
    items = {}
    
    if type(data) == dict:
        for k, v in data.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if type(v) == dict:
                items.update(flatten_json(v, new_key, sep=sep))
            elif type(v) == list:
                # Flatten list items with index
                for i, el in enumerate(v):
                    list_key = f"{new_key}{sep}{i}"
                    if type(el) == dict:
                        items.update(flatten_json(el, list_key, sep=sep))
                    else:
                        items[list_key] = el
            else:
                items[new_key] = v
    
    return items

flattened_names = flatten_json(unflattened)
print("Flattened JSON:/n", flattened_names)
print()

unflattened = {'user' :{'Rachel':{'UserID':1717171717, 'Email': 'rachel1999@gmail.com', 'friends': ['John', 'Jeremy', 'Emily']}}} 
def print_json(data,indent=0):
    space = ' ' * indent

    if type(data)==dict:
        print(space + '{')
        keys = list(data.keys())

        for i in range(len(keys)):
            key = keys[i]
            print(space + ' ' + '"'+ key + '": ', end="")

            print_json(data[key], indent + 4)

            if i < len(keys) - 1:
                print(',')  # Add comma between key-value pairs
            else:
                print()  # Newline after the last key-value pair
        print(space + '}',end="")

    elif type(data)==list:
        print('[')
        for i in range(len(data)):
            print(space + ' ' * 4, end="")  # Add indentation for list items
            print_json(data[i], indent + 4)

            if i < len(data) - 1:
                print(',')  # Add comma between list items
            else:
                print()  # Newline after the last item

        print(space + ']', end="")

    elif type(data)==str:
        print('"' + data + '"', end="")

    else:
        print(data, end="")
    
print("Flattened JSON:")
print_json(unflattened)