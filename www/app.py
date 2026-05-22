from flask import Flask, request, jsonify
from flask_cors import CORS # لضمان سماح المتصفح بالاتصال بأمان

app = Flask(__name__)
CORS(app)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    marks = data.get('marks', [])
    coeffs = data.get('coeffs', [])
    
    total_points = 0.0
    total_coefficients = 0.0
    
    for mark, coeff in zip(marks, coeffs):
        try:
            m = float(mark)
            c = float(coeff)
            total_points += (m * c)
            total_coefficients += c
        except ValueError:
            return jsonify({'error': 'تأكد من إدخال أرقام صحيحة'}), 400

    gpa = total_points / total_coefficients if total_coefficients > 0 else 0.0
    status = "ناجح (Admis) 🎉" if gpa >= 10.0 else "راسب (Ajourné) ⚠️"
    
    return jsonify({
        'gpa': f"{gpa:.2f}",
        'status': status
    })

if __name__ == '__main__':
    app.run(port=5000, debug=True)