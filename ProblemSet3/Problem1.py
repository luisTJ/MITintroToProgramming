import random

def sim(consecutive = 8):
    count = 0
    while True:
        ok = True
        l = []
        cnt = 0
        for i in range(consecutive):
            tmp = random.choice(range(10))
            l.append(str(tmp))
            if not (tmp == 1):
                ok = False
                break
        if ok:
            print l
            print "ok: " + str(count)
            break
        else:
            count += 1
            print count

sim()