
# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem?h_r=internal-search


def reverseInt(number):
    strToInt = str(number)
    reverse = strToInt[::-1]
    intTostr = int(reverse)
    return intTostr


def beautifulDays(start, end, denominator):
    output = 0

    while start < end:
        nominator = abs(start - reverseInt(start))
        if nominator % denominator == 0:
            output += 1
        start += 1

    return output


start = 20
end = 23
denominator = 6

print(beautifulDays(start, end, denominator))
