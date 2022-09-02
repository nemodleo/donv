from . import option
from .base import Docker_Base

class Docker_Build(Docker_Base):
    def __init__(self, opt):
        super(Docker_Build, self).__init__(opt)
        self.set_cmd()

    def set_cmd(self):
        self.add_option('docker build')
        self.add_option(f'-t {self.opt.image}', ' \\')
        self.add_option(f'--build-arg passwd="$(cat /etc/passwd)"', ' \\')
        self.add_option(f'--build-arg requirements="$(cat {self.opt.requirements})"', ' \\')
        self.add_option(f'--build-arg dockerfilesh="$(cat {self.opt.dockerfilesh})"', ' \\')
        self.add_option(f'-f {self.opt.dockerfile} .', ' \\')

def main():
    opt = option.Options().get_option()
    docker = Docker_Build(opt)
    docker.print_cmd()
    docker.do_cmd()

if __name__ == '__main__':
    main()
