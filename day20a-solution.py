from beepy import beep

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

print(primes(34000000)[-20:])

exit()

houses = []

house = 800000
presents = 0
elves = []
while sum(elves)*10 < 34000000:
    elves = [i for i in range(1, house + 1) if house % i == 0]
    print(house, sum(elves)*10)
    house += 1




beep(sound=6)

