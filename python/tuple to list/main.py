def test(my_tuple):
    result = []
    for item in my_tuple:
        result[item("name:Tahsin(firs name)Shanil(last name)","age:13","height ;5,5")] = item[1:]
    return result

