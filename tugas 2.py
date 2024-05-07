def print_nilai_kuadrat(n):
    for i in range(n):
        print(i**2)

def print_nilai_kuadrat_ganjil(n):
    for i in range(n):
        if i % 2 != 0:
            print(i**2)

def main():
    n = int(input("Masukkan nilai n: "))
    print("Part A:")
    print_nilai_kuadrat(n)
    print("Part B Ganjil Genap:")
    print_nilai_kuadrat_ganjil(n)

if __name__ == "__main__":
    main()