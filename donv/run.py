from . import option
from .base import Docker_Base

class Docker_Run(Docker_Base):
    def __init__(self, opt):
        super(Docker_Run, self).__init__(opt)
        self.set_cmd()

    def set_cmd(self):
        self.format = 'docker run -it'
        self.add_option(f"""--gpus '"{f'device={self.opt.gpus}'}"'""", ' \\')
        self.add_option('--ipc=host --ulimit memlock=-1 --ulimit stack=67108864', ' \\')
        self.add_option(f'--name {self.opt.name}', ' \\')
        if self.opt.rm:
            self.add_option('--rm', ' \\')
        self.add_option('-u `id -u`:`id -g`', ' \\')
        self.add_option(f'-v {self.opt.workspace}:{self.opt.workspace_docker}', ' \\')
        for data in self.opt.datas:
            self.add_option(f'-v {data}:{data}', ' \\')
        if self.opt.port:
            self.add_option(f'-p {self.opt.port}:{self.opt.port}', ' \\')
        self.add_option(f'{self.opt.image}', ' \\')

def main():
    opt = option.Options().get_option()
    docker = Docker_Run(opt)
    docker.print_cmd()
    docker.do_cmd()

if __name__ == '__main__':
    main()