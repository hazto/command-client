const express = require('express');
const app = express();
const port = 3030;
const path = require('path')

app.get('/', (req, res) => {
  doShit()
  console.log('path.basename', path.basename('./'))
})


function doShit() {
  const spawn = require('child_process').spawn;

  const py = spawn('python', ['./test.py']); // relative to working directory of the command execution, not the file

  py.stdout.on('data', data => console.log('stdout', data.toString()));

  py.stderr.on('data', error => console.log('an error', error.toString()))

  py.on('close', exitCode => console.log('close with code ', exitCode ))
}

app.listen(port, () => console.log('running...'))
