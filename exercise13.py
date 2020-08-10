sum_list = lambda list_sub_numbers, start, end: sum(list_sub_numbers[start:end])


def acumulado(list_numbers: list):
    result = []
    for i in range(len(list_numbers)):
        result.append(sum_list(list_numbers, 0, i+1))
    return result


class bcolors:
    HEADER = '\033[95m' + '\033[1m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(bcolors.HEADER + "Execute: acumulado([1, 5, 7])" + bcolors.ENDC)
print(acumulado([1, 5, 7]))
print(bcolors.OKGREEN + "Right answer: " + str([1, 6, 13] == acumulado([1, 5, 7])) + bcolors.ENDC)

print("")
print("")

print(bcolors.HEADER + "Execute: acumulado([1, 0, 1, 0, 1])" + bcolors.ENDC)
print(acumulado([1, 0, 1, 0, 1]))
print(bcolors.OKGREEN + "Right answer: " + str([1, 1, 2, 2, 3] == acumulado([1, 0, 1, 0, 1])) + bcolors.ENDC)

print("")
print("")

print(bcolors.HEADER + "Execute: acumulado([])" + bcolors.ENDC)
print(acumulado([]))
print(bcolors.OKGREEN + "Right answer: " + str([] == acumulado([])) + bcolors.ENDC)
