const { spawn } = require('child_process')

const pynia = spawn('python', [__dirname + './lib/python/pynia.py'])
const data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
let dataString = ''

// pynia.stdout.on('data', (data) => dataString += data.toString() )
pynia.stdout.on('data', (data) => {
  console.log('this data: ', data)
  dataString += data.toString()
} )
pynia.stdout.on('end', () => console.log('The total data: ', dataString))

pynia.stdin.write(JSON.stringify(data))
pynia.stdin.end()

const piper = spawn('python', ['./src/lib/python/test_pipe.py', 'George', 'Favour'])
// piper.stdout.on('data', (data) => console.log('data returned', data.toString()))
piper.stdout.pipe(process.stdout)