# donv: docker-env
Easy setup for docker env.

## How to install

```
pip install docker-env
```

## How to donv use

0. Docker Info

    ```
    donv-info
    ```
    ```
    donvi
    ```

1. Docker Build

    ```
    donv-build
    ```
    ```
    donvb
    ```

2. Docker Run

    ```
    donv run --gpus 0,1,2,3,4,5,6,7 --name noname --rm
    ```
    ```
    donvr -g 0,1,2,3,4,5,6,7 -n noname -r
    ```

## How to build package.

```
python setup.py bdist_wheel && pip install -e .
twine upload dist/{generated dist file path}
```