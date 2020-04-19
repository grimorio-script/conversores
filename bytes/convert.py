from bytes import calc, cli
import time


def main():
    menu = cli.Menu('Conversor de bytes')
    menu.set_interface('Converter bytes',
                       'Converter Kilobytes',
                       'Converter Megabytes',
                       'Converter Gygabytes',
                       'Sair')
    mainloop(menu)


def mainloop(self):
    while self.key != self.exit_position:
        print_interface(self)
        show_options(self)
    print('Fim do Programa.')


def print_interface(self):
    self.print_title()
    self.print_options()
    self.user_input('\nOpção: ')


def show_options(self):
    option(self, 1, 'B')
    option(self, 2, 'KB')
    option(self, 3, 'MB')
    option(self, 4, 'GB')


def option(self, num, user_value):
    if self.key == num:
        solve_problem(num, user_value)
        time.sleep(3)


def solve_problem(num=0, pattern='B'):
    user_value = num
    byte = int(input(f'Digite o número de {pattern}ytes: '))
    converted = calc.convert_size(byte, size=pattern)
    print(f'{byte} {pattern} equivale a {converted}')
    return user_value


main()
