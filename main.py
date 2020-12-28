def main():
    inFile = open("/Users/stahl/Desktop/Projects/Advent Of Code 2020/AdventOfCode2020Day2/AdventOfCode2020Day2/data.txt")

    valid1 = 0
    valid2 = 0

    def part1(password, min, max, check):
        if password.count(check) >= min and password.count(check) <= max:
            return 1
        else:
            return 0

    def part2(password, min, max, check):


    for line in inFile:
            checkPos = line.find(':')
            minPos = line.find('-')
            maxPos = line.find(' ')
            count = 0
            min = int(line[0:minPos])
            max = int(line[minPos+1:maxPos])
            check = line[maxPos+1:checkPos]
            password = line[checkPos+2:]
            valid1 += part1(password, min, max, check)
            valid2 += part2(password, min, max, check)

    print(valid1)
    print(valid2)

if __name__ == "__main__":
    main()
