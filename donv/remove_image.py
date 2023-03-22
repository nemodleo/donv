from . import option
from .base import Docker_Base

class Docker_Remove_Image(Docker_Base):
    def __init__(self, opt):
        super(Docker_Remove_Image, self).__init__(opt)
        self.set_cmd()

    def set_cmd(self):
        self.add_option(f'docker rmi')
        self.add_remain_option(' \\')  
        self.add_option(f'{self.opt.name}', ' \\')

def main():
    opt = option.Options().get_option()
    docker = Docker_Remove_Image(opt)
    docker.print_cmd()
    docker.do_cmd()

if __name__ == '__main__':
    main()