import time


def title_with_spaces(name):
    return f'      {name}      '


def higher_name_in(names):
    higher_value = 0
    for name in names:
        name_length = len(name)
        if name_length > higher_value:
            higher_value = name_length
    return higher_value


def print_formated(line, old='.', new=' '):
    formated_line = line[-1::-1].replace(old, new, 1)
    print(formated_line[-1::-1].replace(old, new, 1))


def print_formated_line_in(index, length, layout):
    line = f'{layout} {index[1]:.<{length}}...[{index[0]:>}] {layout}'
    print_formated(line)


class Menu:
    def __init__(self, title, *args):
        self.title = title_with_spaces(title)
        self.options = [arg for arg in args]
        self.length = higher_name_in(self.options)
        self.base = self.return_base(self.length)
        self.diference = len(self.title) - len(self.base)
        self.exit_position = 0
        self.layoutx = '-'
        self.layouty = '|'
        self.key = 0

    def print_title(self):
        if self.title_size_is_lower_than_option_size():
            print(f'\n{self.fixed_separator(self.layoutx)}\n'
                  f'{self.fixed_top()}\n'
                  f'{self.fixed_separator(self.layoutx)}')
        else:
            print(f'\n{self.separator(self.layoutx)}\n'
                  f'{self.centralized_top()}\n'
                  f'{self.separator(self.layoutx)}')

    def title_size_is_lower_than_option_size(self):
        if self.diference < 0:
            return True

    def centralized_top(self):
        return f'{self.title:^}'

    def separator(self, simbol):
        title_length = len(self.centralized_top())
        return simbol * title_length

    def fixed_separator(self, simbol):
        title_bar = self.separator(simbol)
        exceding_bars = self.diference
        bars_left = simbol * (exceding_bars * - 1)
        return f'{title_bar}' + bars_left

    def fixed_top(self):
        exceding_in_each_side = self.diference // 2
        missing_in_each_side = exceding_in_each_side * -1
        return " " * missing_in_each_side + self.centralized_top()

    def return_base(self, size):
        line = str()
        for option in enumerate(self.options, 1):
            line = f'| [{option[0]}]  {"."}{option[1]:.>{size}} |'
        return line

    def print_options(self):
        option_length = higher_name_in(self.options)
        for option in enumerate(self.options, 1):
            if self.title_size_is_lower_than_option_size():
                print_formated_line_in(option, option_length, self.layouty)
            else:
                self.print_formated_line_with_is_missing_in(option, option_length, self.layouty)

    def print_formated_line_with_is_missing_in(self, index, length, layout):
        missing_length = self.diference
        line = f'{layout} {index[1]:.<{length + missing_length}}...[{index[0]:>}] {layout}'
        print_formated(line)

    def set_interface(self, *args, x='-', y='|', close=-1):
        self.options += args
        self.layoutx = x
        self.layouty = y
        self.base = self.return_base(higher_name_in(self.options))
        self.diference = len(self.title) - len(self.base)
        self.exit_position = self.options.index(self.options[close]) + 1

    def user_input(self, txt):
        try:
            self.key = int(input(txt))
        except ValueError:
            option_list = f'{[*enumerate(self.options, 1)]}'.strip('[]')
            print('Por favor digite um número dentro das opções diponíveis:')
            print(option_list.replace("'", ""))
        except EOFError:
            print('Programa finalizado pelo usuário')
            quit()
        except KeyboardInterrupt:
            print('\nPrograma finalizado pelo usuário.')
            quit()
        else:
            if self.key in range(1, len(self.options) + 1):
                return self.key
            else:
                print('Opção inválida')
                time.sleep(2)


if __name__ == '__main__':
    menu = Menu('Grande Conversor de bytes')
    menu.set_interface('Converter bytes', 'Sair')
    while menu.key != menu.exit_position:
        menu.print_title()
        menu.print_options()
        menu.user_input('\nOpção: ')
    print('Fim do programa.')
