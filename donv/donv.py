from . import option
from .base import Docker_Base

class Donv(Docker_Base):
    def __init__(self, opt):
        super(Donv, self).__init__(opt)
        self.set_cmd()

    def set_cmd(self):
        self.add_option('cat README.md')

def main():
    opt = option.Options().get_option()
    docker = Donv(opt)
    docker.print_cmd()
    docker.do_cmd()

if __name__ == '__main__':
    main()
