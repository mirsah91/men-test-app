from flask import Flask
import logging, random
import time

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    if random.random() < 0.2:
        app.logger.error('Simulated random error!')
        return 'Error!', 500
    app.logger.info('Normal request processed')
    return 'Hello from Mend Test App!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
