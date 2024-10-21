from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# Load configuration from a JSON file or create a default one
config_file = 'config.json'
default_config = {
    "city": "Your City",
    "state": "Your State",
    "country": "Your Country",
    "azan_url": "https://icyongit.github.io/AzanCastPy/azan.mp3",
    "prayer_times": {
        "Fajr": "05:00",
        "Dhuhr": "12:00",
        "Asr": "15:30",
        "Maghrib": "18:00",
        "Isha": "19:30"
    }
}

try:
    with open(config_file, 'r') as f:
        config = json.load(f)
except FileNotFoundError:
    with open(config_file, 'w') as f:
        json.dump(default_config, f)
    config = default_config

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Update configuration from form
        config['city'] = request.form['city']
        config['state'] = request.form['state']
        config['country'] = request.form['country']
        config['azan_url'] = request.form['azan_url']
        for prayer in config['prayer_times']:
            config['prayer_times'][prayer] = request.form[prayer]
        
        # Save updated configuration
        with open(config_file, 'w') as f:
            json.dump(config, f)

        return redirect(url_for('index'))

    return render_template('index.html', config=config)

if __name__ == '__main__':
    app.run(debug=True)
