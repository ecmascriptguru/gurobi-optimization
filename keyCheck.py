#default value in dictionary
def keyCheck(key, arr, default):
    if key in arr.keys():
        return arr[key]
    else:
        return 0