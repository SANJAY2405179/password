import math

password = input("Enter a your password: ")
length = len(password)
if length >=8:
    upper = any(char.isupper() for char in password)
    lower = any(char.islower() for char in password)
    digit = any(char.isdigit() for char in password)
    scharacter = any(not char.isalnum() for char in password)

    pool_size = 0
    if upper:
        pool_size += 26
    if lower:
        pool_size += 26
    if digit:
        pool_size += 10
    if scharacter:
        pool_size +=32

    entropy = length*math.log2(pool_size)
    score = min(100, round((entropy / 128) * 100))
    print("Password entropy: ",entropy)
    print("Score of password: ",score)

    if entropy < 36:
        print("Strength: weak")
    elif 36 <= entropy < 60:
        print("Strength: Reasonable for online brute-force protection")
    elif 60 <= entropy < 128:
        print("Strength: Strong")
    else:
        print("Strength: Very Strong (Resistant to offline cracking)")
    print("(Note: Longer passwords with varied character types are exponentially more secure.)")
else:
    print("Your password required at least 8 character")