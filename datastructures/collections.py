def init_arrays():
    arr_1 = ['zero']
    arr_2 = ['one', 'two', 'three']
    arr_1 += arr_2
    print(arr_1)

    n = 10
    zeros_arr = [0] * n
    print(zeros_arr)


def merging_maps():
    dict_1 = dict({'key1': 1, 'key2': 2})
    dict_2 = {'key1': 4, 'key3': 3}
    dict_1.update(dict_2)
    print(dict_1)  # note the key1 was overwritten


def defaults():
    dict_1 = dict()
    dict_1.setdefault('val1', 0)
    dict_1['val1'] += 1
    print(dict_1)


# dictionary comprehensions
def remove_all():
    t = {'key1': 1, 'key2': 2}
    final_dict = {key: t[key] for key in t if key not in ['key1']}  # omits from final dict all keys mentioned in list
    print(final_dict)


def main():
    init_arrays()
    merging_maps()
    defaults()
    remove_all()


if __name__ == '__main__':
    main()
