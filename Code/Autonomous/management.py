from flask import Flask, request

from agent import Agent

app = Flask(__name__)
agent = Agent()


@app.route('/move-motor', methods=['GET'])
def move_motor():
    leg = int(request.args.get('leg'))
    angle = float(request.args.get('angle'))



if __name__ == "__main__":
    app.run(debug=True)