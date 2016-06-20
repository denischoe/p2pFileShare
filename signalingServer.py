
import  json,sys
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit


app = Flask(__name__)

socketio = SocketIO(app)
url='';
### when there is IP address coming from cmd
if len(sys.argv) > 1:
        url = sys.argv[1]

globalList = [];
###########router############
@app.route('/')
def main():
        if url:
                return render_template('index.html',url=url)
        else:
                return render_template('index.html')
##########socketio handlers########
@socketio.on('connect')
def ws_conn():
	pass
        
@socketio.on('disconnect')
def ws_conn():
        print('disconnect', request.sid)

@socketio.on('message')
def ws_message(message):

        data = json.loads(message);

        print(data)

        if data['type'] == "offer":
                socketio.send(json.dumps({'offer': data['offer'], 'type':data['type']}))
        elif data['type'] == "answer":
                socketio.send(json.dumps({'answer': data['answer'], 'type': data['type']}))
	elif data['type'] == "file":
		socketio.send(json.dumps({'file': data['file'], 'type': data['type']}))
        else:
                socketio.send(json.dumps({'candidate': data['candidate'],'type':data['type']}))


if __name__ == "__main__":
        socketio.run(app, host=url)
        



