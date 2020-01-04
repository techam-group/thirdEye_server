// const app = require('express')();
// const http = require('http').Server(app);
// const io = require('socket.io')(http);
// const throttle = require('lodash/throttle');
// const { spawn, exec } = require('child_process');
// const path = require('path');
//
// const filename = path.join(__dirname + '/controller/main.py');
//
// const commands = ['command', 'battery?', 'time?'];
//
// const drone = spawn('python', [filename], {
//   detached: true,
//   cwd: __dirname,
//   stdio: [null, null, null, "pipe"]
// });

// drone.stdout.pipe(process.stdout);
// drone.stdout.on('data', (data) => console.log('data: ', data.toString()))
// drone.stdout.on('end', () => console.log('ended'))

const { PythonShell } = require('python-shell');
const pyshell = new PythonShell(__dirname + "/controller/main.py")


pyshell.on('message', function (message) {
  // received a message sent from the Python script (a simple "print" statement)
  console.log(message);
});