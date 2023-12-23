# from colorama import init
# init()
# start = "\033[1;31m"
# end = "\033[0;0m"

# message = 'Hello World!'
# print("\033[1;31mHello World!\033[0;0m")

from colorama import Fore, Back, Style, init

# Inicialize o colorama
init()

# Exemplo de uso
print(f'{Fore.GREEN}{Back.WHITE}Texto{Style.RESET_ALL}')
