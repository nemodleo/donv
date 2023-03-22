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
    donv-build --dockerfile ./donvdonv/Dockerfile --image donv/donv:{version}
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
    ```
    donvr noname -r -bla bla:bla
    ```
    ```
    donvr noname -r
    ```

3. Docker restart

    ```
    donv-restart noname 
    ```
    ```
    donvre noname 
    ```

4. Docker attach

    ```
    donv-attach noname 
    ```
    ```
    donva noname 
    ```

5. Docker restart and attach

    ```
    donv-restart-attach noname 
    ```
    ```
    donvra noname 
    ```

6. Docker stop

    ```
    donv-stop noname 
    ```
    ```
    donvs noname 
    ```

7. Docker remove

    ```
    donv-remove noname 
    ```
    ```
    donvrm noname 
    ```

8. Docker remove image

    ```
    donv-remove-image noname 
    ```
    ```
    donvrmi noname 
    ```
