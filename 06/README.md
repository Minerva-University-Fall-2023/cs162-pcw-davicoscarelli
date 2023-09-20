1. **Flask and Microframework**: Flask is a small web framework in Python. It's called a "microframework" because it's lightweight and doesn't come with all the bells and whistles like some other frameworks. It's simple and gets the job done.

2. **Roles in a Flask app**:
   - **templates**: Where you put your HTML files. Helps in dynamic content rendering.
   - **static files**: Stuff like CSS, JS, and images. They don't change.
   - **requirements.txt**: A list of all the Python libraries your app needs.
   - **virtual environment (venv)**: Keeps your project's libraries separate from other projects. Avoids mess-ups.
   - **render_template**: Function to show an HTML template.
   - **redirect**: Sends the user to a different endpoint.
   - **url_for**: Helps in generating URLs for routes.
   - **session**: Stores data between requests, like user info.

3. **Commands**:
   - **pip3 install -r requirements.txt**: Installs the libraries your app needs.
   - **export FLASK_APP=app**: Tells Flask where your app is.
   - **python3 -m flask run**: Starts your app.

4. **Ways to run Flask**:
   - **export FLASK_APP=app.py & python3 -m flask run**: The "official" way to start Flask.
   - **python3 app.py**: A quick and dirty way to start Flask if you have an `if __name__ == '__main__':` block in your app.py.
   Use the first when you're being proper, and the second when you're being lazy.

5. **requirements.txt**: You specify versions to make sure your app doesn't break if a library updates. Use `pip freeze` to see what versions you're using.

6. **@app.route**: It tells Flask what URL should trigger the function below it. We put it before the function to link them. By default, it's set to `['GET']`.

7. **Decorator**: It's like a wrapper for functions. Adds extra functionality without changing the function itself. In Flask, it helps with routing and other stuff.

8. **config attribute**: It's where you set up settings for your Flask app. You can do `app.config['TESTING'] = True` or `app.config['SECRET_KEY'] = 'abc'`.

9. **JSON**: Stands for JavaScript Object Notation. It's a way to send data that both humans and machines can read. We use it because it's standard and easy to work with.

10. **Default host and port**: By default, Flask runs on `127.0.0.1` (localhost) and port `5000`. You can change it with `app.run(host='0.0.0.0', port=8080)` or something similar.

