import json
import threading

import time

import logging

import paramiko
from django.http import HttpResponse
from django.shortcuts import render


from dwebsocket import require_websocket, accept_websocket


LOG = logging.getLogger(__name__)

# Create your views here.
def websocket(request):
    return render(request, 'websocket.html')


def webssh(request):
    return render(request, 'webssh.html')

def scripts(request):
    pass



clients = []

@accept_websocket
def echo(request):
    if request.is_websocket:
        lock = threading.RLock()
        try:
            lock.acquire()
            clients.append(request.websocket)
            for message in request.websocket:
                if not message:
                    break
                for client in clients:
                    client.send(message)
        finally:
            clients.remove(request.websocket)
            lock.release()

@accept_websocket
def ws(request):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    if request.is_websocket:
        lock = threading.RLock()
        try:
            lock.acquire()
            clients.append(request.websocket)
            while not request.websocket.has_messages():
                LOG.debug("Wait for websocket message...")
                time.sleep(0.1)
            message = request.websocket.wait().decode("utf-8")
            data = json.loads(message)
            host = data['data']['host']
            port = data['data']['port']
            username = data['data']['username']
            if data['data'].get('ispwd') == 'true':
                password = data['data']['secret']
            ssh.connect(host, port, username, password, timeout=5)
            for cmd in request.websocket:
                if cmd.lower() == 'exit':
                    break
                for client in clients:
                    stdin, stdout, stderr = ssh.exec_command(cmd)
                    client.send(stdout.read())
        finally:
            ssh.close()
            clients.remove(request.websocket)
            lock.release()