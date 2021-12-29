from flask import Flask, request

from agent import Agent

app = Flask(__name__)
agent = Agent()


@app.route('/move-motor', methods=['GET'])
def move_motor():
    leg = int(request.args.get('leg'))
    angle = float(request.args.get('angle'))
    agent.point(angle, leg_index=leg)
    return 'Thank you!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)