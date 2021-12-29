from flask import Flask, request

from agent import Agent

app = Flask(__name__)
agent = Agent()


@app.route('/move-motor', methods=['GET'])
def move_motor():
    leg = int(request.args.get('leg'))
    angle1 = request.args.get('angle1')
    angle2 = request.args.get('angle2')
    angle3 = request.args.get('angle3')

    angle1 = float(angle1) if angle1 is not None else None
    angle2 = float(angle2) if angle2 is not None else None
    angle3 = float(angle3) if angle3 is not None else None
    agent.set_angles(leg, [angle1, angle2, angle3])
    return 'Thank you!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)