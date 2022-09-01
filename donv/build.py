from . import option
from .base import Docker_Base

class Docker_Build(Docker_Base):
    def __init__(self, opt):
        super(Docker_Build, self).__init__(opt)
        self.format = 'docker build -t {} --build-arg passwd="$(cat /etc/passwd)" -f ./docker/Dockerfile .'
        self.set_cmd()

    def set_cmd(self):
        self.format = self.format.format(self.opt.image)

def main():
    opt = option.Options().get_option()
    docker = Docker_Build(opt)
    docker.print_cmd()
    docker.do_cmd()

if __name__ == '__main__':
    main()
