from flask import Flask, request, jsonify
import addressrec

app = Flask(__name__)

@app.route('/smart_address', methods=['POST'])
def handle_smart_address():
    data = request.get_json()

    # 获取请求数据 
    text = data.get('text', '')
    town_village = data.get('town_village', True)
    change2new = data.get('change2new', False)
    
    # 运行地址解析 
    result = addressrec.run(text, town_village, change2new)

    if result:
        return jsonify(result)
    else:
        return jsonify({"error": "Failed to process the request"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)