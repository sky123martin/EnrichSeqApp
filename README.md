# EnrichSeqApp

1. Install pip (package manager)

    ```unix
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py
    rm get-pip.py
    ```

2. Create and Activate Virtual Enviorment

    ```
    conda install anaconda

    conda create -n enrichseq python=3

    conda activate enrichseq_env
    ```

4. Install Requirements

    ```unix
    pip3 install -r requirements.txt
    ```

5. Run Application
    ```unix
    flask run
    ```

6. Exit Enviorment
    ```unix
    conda deactivate
    ```

