
import time

inp_test="""125 17"""
inp_real="""8793800 1629 65 5 960 0 138983 85629"""
inp_test_two = """4048 4048 2 1"""

inp = inp_real

vals = [int(el) for el in inp.split(" ")]

def blink_once(vals):
    res = []
    for el in vals:
        str_el = str(el)
        if el == 0:
            res.append(1)
        elif len(str_el) % 2 == 0:
            left_half = int(str_el[:len(str_el)//2])
            right_half = int(str_el[len(str_el)//2:])
            res.append(left_half)
            res.append(right_half)
        else:
            res.append(2024*el)
    return res

def blink_recursive(counted_vals, n):
    if n == 0:
        return counted_vals
    print(f"n = {n}")
    # first dedupe and sum up counts
    vals = [c[0] for c in counted_vals]
    unique_vals = list(set(vals))
    deduped_counted_vals = []
    for unique_val in unique_vals:
        count = 0
        for counted_val in counted_vals:
            if counted_val[0] == unique_val:
                count += counted_val[1]
        deduped_counted_vals.append((unique_val, count))
    
    res = []
    for (val, count) in deduped_counted_vals:
        blinked_once = blink_once([val])
        res.extend([(new_val,count) for new_val in blinked_once])
    return blink_recursive(res,n-1)



counted_vals = [(val, 1) for val in vals]
print(counted_vals)

res = blink_recursive(counted_vals,75)
# print("res",res)
print(f"stones {sum([el[1] for el in res])}")