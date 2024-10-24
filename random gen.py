from flask import Flask, render_template, request
import random

app = Flask(__name__)

# List of code snippets
code_snippets = [
    "print('Hello, World!')",
    "def add(a, b):\n    return a + b",
    "class MyClass:\n    def my_method(self):\n        print('Hello from my_method')",
    # ...
]

@app.route('/')
def index():
    # Generate a random code snippet
    random_code = random.choice(code_snippets)
    return render_template('index.html', code=random_code)

if __name__ == '__main__':
    app.run(debug=True)
    <!DOCTYPE html>
<html>
<head>
  <title>Random Code Generator</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
  <h1>Random Code Generator</h1>
  <pre>{{ code | safe }}</pre>

  <button onclick="location.reload()">Generate Random Code</button>

  <script>
    document.querySelector('button').addEventListener('click', function() {
      location.reload();
    });
  </script>
</body>
</html>
body {
  font-family: monospace;
}

pre {
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-bottom: 20px;
}

button {
  background-color: #4CAF50;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #3e8e41;
}