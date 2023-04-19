list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]


def merge_lists(list_1, list_2) -> list:
    dup = set()   #this is used to store elements with same "id"
    list_3 = []
    for dict_ele_1 in list_1:
        for dict_ele_2 in list_2:
            if dict_ele_1['id'] == dict_ele_2['id']:  #updating or merging elements with same id
                dict_ele_1.update(dict_ele_2)
                list_3.append(dict_ele_1.copy())
                dup.add(dict_ele_1['id'])
                break
    #print(dup)
    for ele in list_1:    # these two for loop used for adding uncommon / non overlapping elements
        if ele["id"] not in dup:
            list_3.append(ele)

    for ele in list_2:
        if ele["id"] not in dup:
            list_3.append(ele)

    return list_3


list_3 = merge_lists(list_1, list_2)
