from setuptools import setup, find_packages

version = '0.0.4'

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
            "donv-info = donv.base:main",
            "donv-run = donv.run:main",
            "donv-build = donv.build:main",
            "donvi = donv.base:main",
            "donvr = donv.run:main",
            "donvb = donv.build:main"
        ],
    },
    classifiers=[
        'License :: OSI Approved :: MIT License'
    ]
)