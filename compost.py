import docker
from flask import Flask, request, jsonify
# from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app)
dockerMachine = docker.from_env()


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route('/projects', methods=['GET'])
def getInstances():
    projects={}
    for container in dockerMachine.containers.list(all=True,filters={"label":"com.docker.compose.project"}):
        projectName = str(container.attrs['Config']['Labels']['com.docker.compose.project'])
        dockerContainer = {'id': container.id, 'name': container.name, 'status': container.status}
        project = projects.get(projectName, {'name':projectName, 'containers':[]})
        project['containers'].append(dockerContainer)
        projects[projectName] = project
    return jsonify(projects.values())


@app.route('/projects/<name>/<version>', methods=['PUT'])
def put_project(name, version):
    dockerCompose = request.data.decode("utf-8")
    return 'TODO'


@app.route('/projects/<name>/<version>', methods=['DELETE'])
def delete_project(name, version):
    return 'TODO'


# @socketio.on('logs_open')
# def open_logs(json):
#     emit('my response', 'TODO')
#
#
# @socketio.on('logs_close')
# def close_logs(json):
#     emit('my response', 'TODO')
#
#
# @socketio.on('logs_open')
# def open_console(json):
#     for line in dockerMachine.logs(json.container, stream=True, timestamps=True, tail='all'):
#         emit('logs', line)
#
#
# @socketio.on('logs_close')
# def close_console(json):
#     emit('my response', 'TODO')


if __name__ == '__main__':
    app.run(debug = True)
