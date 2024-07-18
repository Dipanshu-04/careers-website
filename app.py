from flask import Flask, json, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
}, {
    'id': 2,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': 'Rs. 12,00,000'
}, {
    'id': 3,
    'title': 'Data Scientist',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 13,00,000'
}, {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 13,00,000'
}, {
    'id': 5,
    'title': 'Backend Engineer',
    'location': 'Pune, India',
    'salary': 'Rs. 13,00,000'
}, {
    'id': 6,
    'title': 'Frontend Engineer',
    'location': 'Hyderabad, India',
    'salary': 'Rs. 10,00,000'
}, {
    'id': 7,
    'title': 'HR Manager',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 15,00,000'
}, {
    'id': 8,
    'title': 'Content Writer',
    'location': 'Kolkata, India',
    'salary': 'Rs. 7,00,000'
}]


@app.route('/')
def hello_world():
    return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
