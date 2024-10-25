def apply_all_func(int_list, *functions):
    results = {}
    for i in functions:
        result_0 = i(int_list)
        j = i.__name__
        dict_0 = {f'{j}': result_0}
        results.update(dict_0)
    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))