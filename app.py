from flask import Flask, request, jsonify
from services.itinerary_service import get_user_data, select_destination, generate_itinerary

app = Flask(__name__)

# Default route to handle GET /
@app.route('/')
def home():
    return "Welcome to the Saathiapp Travel Itinerary API!"

@app.route('/generate-itinerary', methods=['POST'])
def generate_itinerary_route():
    try:
        user_id = request.json.get('user_id')
        user_data = get_user_data(user_id)
        if not user_data:
            return jsonify({"error": "User not found"}), 404

        destination = select_destination(user_data)
        itinerary = generate_itinerary(user_data, destination)
        
        return jsonify({
            'destination': destination,
            'itinerary': itinerary
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)

