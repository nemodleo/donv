from . import option
from .base import Docker_Base

class Docker_Remove(Docker_Base):
    def __init__(self, opt):
        super(Docker_Remove, self).__init__(opt)
        self.set_cmd()

    def set_cmd(self):
        self.add_option(f'docker rm {self.opt.name}')

def main():
    opt = option.Options('name').get_option()
    docker = Docker_Remove(opt)
    docker.print_cmd()
    docker.do_cmd()

if __name__ == '__main__':
    main()