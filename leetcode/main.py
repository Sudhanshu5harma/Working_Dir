nums = 123456
res = [int(x) for x in str(nums)]
min_b = min(res)


def replace(li: list, num1: int, num2: int):
    for i, n in enumerate(li):
        if li == num1:
            li.remove(li)
            print(li)
            li.insert(n, num2)
    return li


new_list = replace(res, min_b, 0)







'''res_min = res[0:len(res)//2]
min_b = min(i for i in res_min if i > 0)
max_a = max(res_min)
#[sub.replace('4', '1') for sub in test_list]
if min_b==res[0]:
    min_val = 0
    repalce_val = min()
    rep = [sub.replace(repalce_val,min_val) for sub in res]
else
'''


