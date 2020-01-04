require('dotenv').config();
const app = require('express')();
const http = require('http').Server(app);
const io = require('socket.io')(http);
const throttle = require('lodash/throttle');
const { PORT } = process.env;
const { sendMessage } = require('./src/fly');

// Setup IO for server
io.on('connection', socket => {
  socket.on('command', command => {
    // console.log('command Sent from browser =>', command);
    sendMessage('command')
    sendMessage(command)
    // drone.send(command, 0, command.length, PORT, HOST, handleError);

    // socket.on('disconnect', () => console.log('client disconnected'))
  });

  socket.emit('status', 'CONNECTED');
});

// Setup server
http.listen(PORT, () => console.log(`server running on http://localhost:${PORT}`));