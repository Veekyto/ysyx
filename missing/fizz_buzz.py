def fizz_buzz(limit):
    for i in range(limit+1):
        if i % 3 == 0:
            print('fizz')
        if i % 5 == 0:
            print('fizz')
        if i % 3==0 and i % 5==0:
            print(i)

def main():
    fizz_buzz(10)

if name =="__main__":
    main()
