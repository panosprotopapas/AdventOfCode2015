from hashlib import md5

with open("./Day 04/input.txt", encoding="utf-8") as f:
    input = f.read().strip()

def find_i(number_of_zeroes):
    i = 0
    while True:
        val = input + str(i)
        try:
            a = int(md5(val.encode()).hexdigest()[:number_of_zeroes])
            if a == 0:
                break
        except ValueError:
            pass
        i += 1
    return i

print(f"""Part 1: {find_i(5)}""")
print(f"""Part 2: {find_i(6)}""")
