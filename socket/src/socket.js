const socketIO = require('socket.io');
const { handleSocketEvent } = require('./socket-controller');

exports.config = (server) => {
    const io = socketIO(server, {
        cors: {
          origin: "*",
          methods: "*"
        }
    });

    handleSocketEvent(io);
}