from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/analyze_attendance', methods=['POST'])
def analyze():
    data = request.get_json()
    results = []

    for record in data.get('attendance', []):
        name = record.get('name')
        present = record.get('days_present')
        total = record.get('total_days')
        percent = (present / total) * 100 if total else 0
        status = "✅ Good" if percent >= 75 else "❌ Low Attendance"
        
        results.append({
            "name": name,
            "days_present": present,
            "total_days": total,
            "percentage": round(percent, 2),
            "status": status
        })

    return jsonify({"analysis": results})
