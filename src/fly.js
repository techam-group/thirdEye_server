const path = require('path');
const { PythonShell } = require('python-shell');

const filePath = path.join(__dirname, '../pyDrone/main.py');

function sendMessage(command) {
  return new Promise(async function (resolve, reject) {
    let options = {
      mode: 'text',
      pythonOptions: ['-u'],
      args: [command]
    };

    const pyShell = new PythonShell(filePath, options);

    await pyShell.on('message', function (msg) {
      return resolve(msg)
    });
  })
}

module.exports = { sendMessage };
