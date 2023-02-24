
# MamaFua - book laundry and cleaning service our call service

## Windows / Linux (Recommended)

  ``` shell
  python -m venv venv
  venv\Scripts\activate
  pip install -r requirements.txt
  ```

- create .env file in the **app** folder with the following variables

  ```text
  USERNAME="your_at_username"
  API_KEY="your_username"
  ```

- start server

  ``` shell
  flask run
  ```

  - start server in debug mode (recommended)

  ``` shell
  flask --debug run
