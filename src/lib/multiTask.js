const { spawn, exec } = require('child_process')
const fs = require('fs')

// Main message to screen
// process.stdout.write('Hello Hackr' + '\n')

// fs.createReadStream(__filename).pipe(process.stdout)

// exec('cat src/lib/multiTask.js', function (err, stdout, stderr) {
//   if (err) throw stderr
//   process.stdout.write('Your output: ' + stdout)
// })

/* if (process.argv[2] === 'child') {
  process.stdout.write("I'm the child process now")
} else {
  var child = spawn(process.execPath, [__filename, 'child'])
  // child.stdout.on('data', function (data) {
  //   process.stdout.write('from child: ' + data.toString())
  // })

  // We can pipe the data as well
  child.stdout.pipe(process.stdout)
} */

const ls = spawn('ls', [__dirname + '/']);

ls.stdout.on('data', (data) => {
  console.log(`stdout: ${data}`);
});

ls.stderr.on('data', (data) => {
  console.error(`stderr: ${data}`);
});

ls.on('close', (code) => {
  console.log(`child process exited with code ${code}`);
});
// runScript.stdout.pipe(process.stdout)
