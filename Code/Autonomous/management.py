from flask import Flask, request

from agent import Agent

app = Flask(__name__)
agent = Agent()


@app.route('/move-motor', methods=['GET'])
def move_motor():
    leg = int(request.args.get('leg'))
    angle1 = float(request.args.get('angle1'))
    angle2 = float(request.args.get('angle2'))
    angle3 = float(request.args.get('angle3'))
    agent.set_angles(leg, [angle1, angle2, angle3])
    return 'Thank you!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)