'''
Input: an integer
Returns: an integer
1 2 4 7 13 24
'''
def eating_cookies(n):
    derp = [1, 1, 2]
    while len(derp) <= n:
        derp.append(sum(derp[-3:]))

    return derp[abs(n)]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
