require('dotenv').config();
const app = require('express')();
const http = require('http').Server(app);
const io = require('socket.io')(http);
const throttle = require('lodash/throttle');
const { PORT } = process.env;
const { sendMessage } = require('./src/fly');

// Setup IO for server
io.on('connection', socket => {
  socket.emit('status', 'CONNECTED');

  socket.on('command', async command => {
    await sendMessage('command');
    const data = await sendMessage(command);
    console.log('data: ', data);

    socket.emit('data', data);
  });

  socket.on('disconnect', () => console.log('client disconnected'))
});

// Setup server
http.listen(PORT, () => console.log(`server running on http://localhost:${PORT}`));
