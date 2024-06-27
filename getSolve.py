from flask import Flask, jsonify, request
import Solve

app = Flask(__name__)

@app.route('/solve_recaptcha', methods=['POST'])
def solve_recaptcha():
    data = request.get_json()

    if 'site_key' not in data or 'url' not in data:
        return jsonify({'error': 'Missing site_key or url in request body'}), 400

    site_key = data['site_key']
    url = data['url']

    result = Solve.ReCaptcha(site_key, url)

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
