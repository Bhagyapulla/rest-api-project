from flask import Flask, request, jsonify

app = Flask(__name__)


subscriptions = {}


@app.route('/subscription/<int:subscription_id>', methods=['POST'])
def add_subscription(subscription_id):
    if subscription_id in subscriptions:
        return jsonify({"error": "Subscription ID already exists"}), 400

    data = request.get_json()
    required_fields = ['reader_name', 'magazine_title', 'duration_months', 'active']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    subscriptions[subscription_id] = {
        "reader_name": data['reader_name'],
        "magazine_title": data['magazine_title'],
        "duration_months": data['duration_months'],
        "active": data['active']
    }

    return jsonify({"message": "Subscription added", "subscription": subscriptions[subscription_id]}), 201


@app.route('/subscription/<int:subscription_id>', methods=['PUT'])
def update_subscription(subscription_id):
    if subscription_id not in subscriptions:
        return jsonify({"error": "Subscription not found"}), 404

    data = request.get_json()
    for key in ['reader_name', 'magazine_title', 'duration_months', 'active']:
        if key in data:
            subscriptions[subscription_id][key] = data[key]

    return jsonify({"message": "Subscription updated", "subscription": subscriptions[subscription_id]})


@app.route('/subscription/<int:subscription_id>', methods=['DELETE'])
def delete_subscription(subscription_id):
    if subscription_id not in subscriptions:
        return jsonify({"error": "Subscription not found"}), 404

    del subscriptions[subscription_id]
    return jsonify({"message": "Subscription deleted"})


@app.route('/subscription/<int:subscription_id>', methods=['GET'])
def get_subscription(subscription_id):
    if subscription_id not in subscriptions:
        return jsonify({"error": "Subscription not found"}), 404

    return jsonify(subscriptions[subscription_id])

@app.route('/subscriptions', methods=['GET'])
def get_all_subscriptions():
    return jsonify(subscriptions)


if __name__ == '__main__':
    app.run(debug=True)