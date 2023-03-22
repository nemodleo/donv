import os
from . import option
from . import version

class Docker_Base:
    def __init__(self, opt):
        super(Docker_Base, self).__init__()
        self.opt = opt
        self.init_cmd()

    def init_cmd(self):
        self.format = f''

    def set_cmd(self):
        self.add_option('echo [DOCKER INFO]')
        self.add_option('echo')
        self.add_option('echo [IMAGE]')
        self.add_option('docker images')
        self.add_option('echo')
        self.add_option('echo [CONTAINER]')
        self.add_option('docker ps -a')

    def add_option(self, arg: str, parser=''):
        self.format += f'{parser}\n'
        self.format += arg
    
    def add_remain_option(self, parser=''):
        for arg in self.opt.remain_opt:
            self.format += f'{parser}\n'
            self.format += arg

    def do_cmd(self):
        try:
            os.system(self.format)
        except:
            self.print_line()
            print('[!] wrong command')
        self.print_line(line='=')

    def clean_format(self, parser='\\'):
        for f in self.format.split(';'):
            if f.count(parser + '\n') == 1:
                f_replace = f.replace(parser + '\n', '')
                self.format = self.format.replace(f, f_replace)

    def print_cmd(self):
        self.print_line(line='=')
        print(version.DONV.format(version.VERSION))
        self.print_line('[CMD]')
        self.clean_format()
        print(self.format.strip())
        self.print_line('[LOG]')

    def print_line(self, label: str = '', num: int = os.get_terminal_size().columns, line: str = '-', direciton='r'):
        just = {
            'r': label.rjust,
            'l': label.ljust,
        }
        print(just[direciton](num,line))

    @property
    def cmd(self):
        return self.format

def main():
    opt = option.Options().get_option()
    docker = Docker_Base(opt)
    docker.set_cmd()
    docker.print_cmd()
    docker.do_cmd()

if __name__ == '__main__':
    main()