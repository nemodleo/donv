import os
import argparse
from pathlib import Path
from glob import glob

class Options:
    """Argument for Docker-ENV.
    """
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-g', '--gpus', default='all', type=str,
                            help='[ all | 0 | 0,1,2,3,4 ]')
        parser.add_argument('-w', '--workspace', default='~/Lion', type=str,
                            help='server workspace - code')
        parser.add_argument('-p', '--port', default=None, type=int,
                            help='port number')
        parser.add_argument('-i', '--image', default='lionrocket/lr_vision:0.9.6', type=str,
                            help='docker image')
        parser.add_argument('-n', '--name', default='noname', type=str,
                            help='docker name')
        parser.add_argument('-r', '--rm', action='store_true',
                            help='docker --rm option')
        parser.add_argument('-f', '--dockerfile', default=None, type=str,
                            help='docker file')
        self.opt = parser.parse_args()
        self.opt.workspace_docker = f'/{Path(self.opt.workspace).stem}'
        self.opt.datas = glob('/data*/')
        if self.opt.dockerfile is None:
            try:
                import donv
                donv_dir = os.path.dirname(donv.__file__)
                self.opt.dockerfile = os.path.join(donv_dir, 'docker', 'Dockerfile')
            except:
                self.opt.dockerfileDockerfile

    def get_option(self):
        """get_option
        """
        return self.opt

if __name__ == '__main__':
    opt = Options().get_option()
    print(opt)