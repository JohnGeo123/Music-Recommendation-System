from flask import Flask, request, jsonify
from recommendation_engine import get_recommendations

app = Flask(__name__)

@app.route('/recommendations', methods=['POST'])
def recommend_music():
    user_profile = request.json
    recommendations = get_recommendations(user_profile)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
