const dgram = require('dgram');
const wait = require('waait');
const app = require('express')();
const http = require('http').Server(app);
const io = require('socket.io')(http);
const throttle = require('lodash/throttle');
const commandDelays = require('./lib/commandDelays');

const PORT = 8889;
const HOST = '192.168.10.1';
const DS_PORT = 8890;

const drone = dgram.createSocket('udp4');
const droneState = dgram.createSocket('udp4');

drone.bind(PORT);
droneState.bind(DS_PORT);

drone.on('message', message => {
  console.log(`🤖 : ${message}`);
});

function handleError(err) {
  if (err) {
    console.log('=== ERROR ===');
    console.log(err);
  }
}

// drone.send('command', 0, 7, PORT, HOST, handleError)
// drone.send('battery?', 0, 8, PORT, HOST, handleError)

const commands = ['command', 'battery?']

let i = 0;

async function go() {
  const command = commands[i]
  const delay = commandDelays[command]

  console.log(`running command: ${command}`)

  drone.send(command, 0, command.length, PORT, HOST, handleError)

  await wait(delay)
  i++

  if (i < commands.length) {
    return go()
  }

  console.log('done!')
  console.log('3rdEye has landed')
}

go()