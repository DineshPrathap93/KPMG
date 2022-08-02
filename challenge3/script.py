import json

def getValue(obj, key):

    if isinstance(obj, str):
        try:
            obj = json.loads(obj)
        except ValueError as err:
            return("Invalid object passed")

    keys = key.split("/")
    value = obj
    try:
        for key in keys:
            value= value[key]
    except KeyError:
        return("Invalid key passed")

    return(value)



# obj = '{"a":{"b":{"c":"d"}}}'
# obj = {"x":{"y":{"z":{"a":"1"}}}}
obj = "{hai}"

# key = "x/y/z/a"
key = "a/b/c"

print(getValue(obj, key))