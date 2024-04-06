

1. Create a new folder and move into the newly created folder by using the command:
    ```
    cd your-folder-name
    ```

2. Create a virtual environment by using the following command:
    * for windows
        ```
        python -m venv env
        ```
    * for mac
        ```
        python3 -m venv env
        ```
    
3. Next you need to activate the virtual environment as:
    * for windows
        ```
        env\Scripts\activate
        ```
    * for mac
        ```
        source env/bin/activate
        ```

4. Unzip the code in this folder

5. We  now need to move into our project folder. Do this by running the following command:
    ```
    cd stock-screener
    ```

6. Now we need to install all the dependencies of the project. This can be done using the following command:
    ```
    pip install -r requirements.txt
    ```

7. Next you need to run the following command to setup our database:
    ```
    python manage.py makemigrations app
    ```

8. Then we simply need to apply these migrations by running:
    ```
    python manage.py migrate
    ```

9. Next we need to create a super user to acess the database and all its tables:
    ```
    python manage.py createsuperuser
    ```

10. Now finally to run the development server as follows:
    ```
    python manage.py runserver
    ```

## Now you have setup the project successfully!!

