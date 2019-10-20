const app = require('express')();
const http = require('http').Server(app);
const io = require('socket.io')(http);
const throttle = require('lodash/throttle');
const { spawn } = require('child_process')

const commands = ['command', 'battery?', 'time?']

const drone = spawn('python', ['./src/controller/main.py'])

drone.stdout.pipe(process.stdout)
