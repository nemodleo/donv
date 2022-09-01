from . import option
from .base import Docker_Base

class Docker_Attach(Docker_Base):
    def __init__(self, opt):
        super(Docker_Attach, self).__init__(opt)
        self.set_cmd()

    def set_cmd(self):
        self.format = f'docker attach {self.opt.name}'

def main():
    opt = option.Options().get_option()
    docker = Docker_Attach(opt)
    docker.print_cmd()
    docker.do_cmd()

if __name__ == '__main__':
    main()