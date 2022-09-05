from setuptools import setup, find_packages
from donv import version
version = version.VERSION

setup(
    name="donv",
    version=version,
    packages=find_packages(),
    description="Easy setup for docker env.",
    keywords='docker build dockerfile run env images ps',
    long_description_content_type="text/markdown",
    long_description=open("README.md").read(),
    package_data={'donv': ['donv']},
    url="https://github.com/nemodleo/donv",
    author='Hyun Park',
    author_email='nemod.leo@snu.ac.kr',
    license='MIT',
    install_requires=[
        'python_version >= "3.5"',
    ],
    include_package_data=True,
    script=["donv"],
    entry_points={
        "console_scripts": [
            "donv = donv.donv:main",
            "donv-info = donv.base:main",
            "donv-run = donv.run:main",
            "donv-build = donv.build:main",
            "donv-restart = donv.restart:main",
            "donv-attach = donv.attach:main",
            "donv-restart-attach = donv.restart_attach:main",
            "donv-stop = donv.stop:main",
            "donv-remove = donv.remove:main",
            "donvi = donv.base:main",
            "donvr = donv.run:main",
            "donvb = donv.build:main",
            "donvrst = donv.restart:main",
            "donva = donv.attach:main",
            "donvra = donv.restart_attach:main",
            "donvs = donv.stop:main",
            "donvrm = donv.remove:main",
        ],
    },
    classifiers=[
        'License :: OSI Approved :: MIT License'
    ]
)