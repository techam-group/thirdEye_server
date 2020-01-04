const { PythonShell } = require('python-shell');
const pyshell = new PythonShell(__dirname + "/main.py")


// let options = {
//   mode: 'text',
//   // pythonPath: './controller',
//   pythonOptions: ['-u'], // get print results in real-time
//   scriptPath: './controller',
//   // args: ['value1', 'value2', 'value3']
// };


pyshell.on('message', function (message) {
  // received a message sent from the Python script (a simple "print" statement)
  console.log(message);
});