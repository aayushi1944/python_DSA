"""
j
H1) A security researcher is testing a 3-digit lock (digits 1-3 only, no repeats). 
They need to generate every possible combination — a classic backtracking/permutation problem asked in 
Google and Microsoft interviews.
"""

def combination(num, ind):
    if ind == len(num):
        print("".join(num))
        return

    for i in range(ind, len(num)):
        num[ind], num[i] = num[i], num[ind]

        combination(num, ind + 1)

        num[ind], num[i] = num[i], num[ind]   
n=input("Enter 3 digit No:")
combination(list(n), 0)