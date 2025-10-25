from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)
candidates = {
    "charles": 0,
    "babu": 0,
    "Alice": 0,
    "NOTA":0
}

DATA_FILE = "votes.csv"


@app.route('/')
def index():
    return render_template('index.html', candidates=candidates)

@app.route('/vote', methods=['POST'])
def vote():
    selected_candidate = request.form.get('candidate')
    if selected_candidate in candidates:
        candidates[selected_candidate] += 1
    save_candidates(candidates)
    return redirect(url_for('success'))
@app.route('/success')
def success():
    return redirect(url_for('index'))

@app.route('/results')
def results():
    return render_template('results.html', candidates=candidates)

def save_candidates(candidates):
    """Save candidates to the CSV file."""
    with open(DATA_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        for candidate, votes in candidates.items():
            writer.writerow([candidate, votes])


if __name__ == '__main__':
    app.run(debug=True)



