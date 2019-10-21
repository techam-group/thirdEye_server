const app = require('express')();
const http = require('http').Server(app);
const io = require('socket.io')(http);
const throttle = require('lodash/throttle');
const { spawn, exec } = require('child_process')
const path = require('path')

const filename = path.join(__dirname + '/controller/main.py')

const commands = ['command', 'battery?', 'time?']

const drone = spawn('python', [filename], { 
  detached: true,
  cwd: __dirname,
  stdio: [null, null, null, "pipe"]
})

drone.stdout.pipe(process.stdout)
// drone.stdout.on('data', (data) => console.log('data: ', data.toString()))
// drone.stdout.on('end', () => console.log('ended'))
