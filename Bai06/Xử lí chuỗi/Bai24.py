def dem_so_lan(a = str()):
    a = a.lower()
    chu = []
    chu = a.split()
    dest = {}
    for i in chu:
        if "a" <= i <= "z":
            if i not in dest:
                dest[i] = 1
            else:
                dest[i] += 1
    return dest
def main():
    a = input()
    print(dem_so_lan(a))
main()