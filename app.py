from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from data_structure import QUEUE
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

queue = QUEUE()

@app.route('/add_booking', methods=['POST'])
def add_booking():
    data = request.json
    name = data.get('name')
    people = data.get('people')
    remarks = data.get('remarks')
    vip = data.get('vip', False)
    
    if not name or not people:
        return jsonify({"error": "Invalid input"}), 400
    
    queue.Enqueue(name, people, vip, remarks)
    return jsonify({"message": "You've joined the waitlist!"})

@app.route('/view_bookings', methods=['GET'])
def view_bookings():
    return jsonify({"bookings": queue.Print_test()})

@app.route('/process_booking', methods=['POST'])
def process_booking():
    booking = queue.Dequeue()
    if booking is None:
        return jsonify({"error": "No bookings to process"}), 400
    return jsonify({"message": f"{booking['name']}, your table is ready!"})

@app.route('/cancel_booking', methods=['POST'])
def cancel_booking():
    data = request.json
    booking_id = data.get('id')
    success = queue.Cancel(booking_id)
    if success:
        return jsonify({"message": "Booking canceled successfully!"})
    else:
        return jsonify({"error": "Booking ID not found"}), 404

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

