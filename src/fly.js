const path = require('path');
const { PythonShell } = require('python-shell');

const filePath = path.join(__dirname, '../pyDrone/main.py');
// const options = {
//   mode: 'text',
//   pythonOptions: ['-u'], // get print results in real-time
//   // pythonPath: 'path/to/python',
//   // scriptPath: 'path/to/my/scripts',
//   args: ['value1', 'value2', 'value3']
// };

// const pyShell = new PythonShell(filePath, options);

// pyShell.on('message', function (message) {
//   // received a message sent from the Python script (a simple "print" statement)
//   console.log(message);
// });

function sendMessages(command) {
  const options = {
    mode: 'text',
    pythonOptions: ['-u'], // get print results in real-time
    args: [command]
  };

  const pyShell = new PythonShell(filePath, options);

  return pyShell.on('message', msg => console.log(msg))
}


function sendMessage(command) {
  return new Promise(async function (resolve, reject) {
    let options = {
      mode: 'text',
      pythonOptions: ['-u'],
      args: [command]
    };

    const pyShell = new PythonShell(filePath, options);

    await pyShell.on('message', function (msg) {

      console.log('from flyJs: ', msg);
      resolve(msg)
    });
  })
}

module.exports = { sendMessage }