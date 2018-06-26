terminado.apply(Terminal);

var term = new Terminal(),
    protocol = (location.protocol === 'https:') ? 'wss://' : 'ws://',
    socketURL = protocol + location.hostname + ((location.port) ? (':' + location.port) : '') + "/websocket";
sock = new WebSocket(socketURL);

sock.addEventListener('open', function () {
    term.terminadoAttach(sock);
});

term.open(document.getElementById('terminal-container'));