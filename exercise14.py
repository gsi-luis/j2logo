from numpy import array, sort

def siguiente_mayor(list_numbers):
    result = []
    list_numbers = array(list_numbers)
    for i in range(len(list_numbers)-1):
        num_g_than = sort(list_numbers[list_numbers > list_numbers[i]])
        num_g_than = -1 if len(num_g_than) == 0 else num_g_than[0]
        result.append(num_g_than)
    result.append(-1)
    return result


class console:
    HEADER = '\033[95m' + '\033[1m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def show_result(list_numbers, result):
        print(console.HEADER + "Execute: acumulado("+str(list_numbers)+")" + console.ENDC)
        print(siguiente_mayor(list_numbers))
        print(console.OKGREEN + "Right answer: " + str(result == siguiente_mayor(list_numbers)) + console.ENDC)

        print("")
        print("")


console.show_result([5, 7, 3, 2, 8], [7, 8, 5, 3, -1])

console.show_result([2, 3, 4, 5], [3, 4, 5, -1])

console.show_result([1, 0, -1, 8, -72], [8, 1, 0, -1, -1])
