# donv: docker-env
Easy setup for docker env.

## How to install

```
pip install donv
```

## How to donv use

0. Docker Info

    ```
    donv-info
    ```
    ```
    donvi
    ```
    ```
    donvi --help
    ```

1. Docker Build

    ```
    donv-build --dockerfile ./donvdonv/Dockerfile --image donv/donv:0.0.1
    ```
    ```
    donvb
    ```
    ```
    donvb --help
    ```

2. Docker Run

    ```
    donv run --gpus 0,1,2,3,4,5,6,7 --name noname --rm
    ```
    ```
    donvr -g 0,1,2,3,4,5,6,7 -n noname -r
    ```
    ```
    donvr --help
    ```

## How to build package

```
python setup.py bdist_wheel && pip install -e .
twine upload dist/{generated dist file path}
```
