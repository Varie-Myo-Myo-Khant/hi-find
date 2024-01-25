const ApiRequest = require('./utils/apiRequest');
const socketEvent = require('./constants/socket-event');

const userSocket = { };

exports.handleSocketEvent = (io) => {
    io.on('connection', (socket) => {
        socket.on(socketEvent.REGISTER, data => registerClient(socket, data));
        socket.on(socketEvent.SEND_MESSAGE, data => sendMessage(socket, data));
    });

    function notifyUser(userId, eventName, data=null) {
        const userSockets = userSocket[userId] || [];
        userSockets.forEach(socketId => {
            io.sockets.to(socketId).emit(eventName, data);
        })
    }

    function registerClient(clientSocket, data) {
        const { user_id } = data;
    
        console.log(`User connected with id: ${user_id} and socket id: ${clientSocket.id}`);
    
        if(userSocket[user_id] && !userSocket[user_id].includes(clientSocket.id)) {
            userSocket[user_id].push(clientSocket.id);
            return;
        }
    
        userSocket[user_id] = [clientSocket.id];
    }

    async function sendMessage (clientSocket, data) {
        const { sender_id, receiver_id, message } = data;

        // Request to store message
        await ApiRequest.post('/messages/send', {
            sender_id,
            receiver_id,
            message
        });
        
        // Send to receiver 
        notifyUser(receiver_id, socketEvent.RECEIVE_MESSAGE, { message: message, sender_id });
    }
}