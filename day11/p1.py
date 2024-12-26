import time

inp_test="""125 17"""
inp_real="""8793800 1629 65 5 960 0 138983 85629"""

inp = inp_real

vals = [int(el) for el in inp.split(" ")]

def blink_once(vals):
    res = []
    for el in vals:
        if el == 0:
            res.append(1)
        elif len(str(el)) % 2 == 0:
            left_half = int(str(el)[:len(str(el))//2])
            right_half = int(str(el)[len(str(el))//2:])
            res.append(left_half)
            res.append(right_half)
        else:
            res.append(2024*el)
    return res

def blink_n_times(start_vals, n=75):
    BLINK_TOTAL = n
    blink_curr = 0
    curr_vals = start_vals
    # curr_time = time.time()
    while blink_curr < BLINK_TOTAL:
        # now_time = time.time()
        # passed_time = now_time - curr_time
        # print("Passed time", passed_time)
        # curr_time = now_time
        blink_curr += 1
        # print(blink_curr)
        this_vals = blink_once(curr_vals)
        curr_vals = this_vals
    return curr_vals

def main():
    blink_n_times(vals,25)


if __name__ == "__main__":
    main()