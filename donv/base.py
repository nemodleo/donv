import os
from . import option
from . import version



class Docker_Base:
    def __init__(self, opt):
        super(Docker_Base, self).__init__()
        self.opt = opt
        self.init_cmd()
        self.set_cmd()

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

    def do_cmd(self):
        try:
            os.system(self.format)
        except:
            print('[!] wrong command')

    def print_cmd(self):
        LINE = '--------------------------------------------------------------------------------'
        print(LINE)
        print(version.DONV.format(version.VERSION))
        print(LINE)
        print(self.format.strip())
        print(LINE)

    @property
    def cmd(self):
        return self.format

def main():
    opt = option.Options().get_option()
    docker = Docker_Base(opt)
    docker.print_cmd()
    docker.do_cmd()

if __name__ == '__main__':
    main()