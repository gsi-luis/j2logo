# -*- coding: iso-8859-15 -*-

substrings = lambda string: [string[i:len(string)] for i in range(len(string))]

def final_comun_mayor(str1, str2):
    try:
        result = max(set(substrings(str1)) & set(substrings(str2)), key=len)
    except ValueError:
        result = ''
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
    def show_result(str1, str2, result):
        print(console.HEADER + "Execute: final_comun_mayor("+str(str1)+","+str(str2)+" )" + console.ENDC)
        print(final_comun_mayor(str1, str2))
        print(console.OKGREEN + "Right answer: " + str(result == final_comun_mayor(str1, str2)) + console.ENDC)

        print("")
        print("")


console.show_result('camión', 'ración', 'ión')

console.show_result('Python', 'PyCon', 'on')

console.show_result('Teclado', 'Mezclado', 'clado')

console.show_result('Harina', 'Arroz', '')
