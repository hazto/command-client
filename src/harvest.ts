import { pythonPath } from './constants';
const spawn = require('child_process').spawn;
const path = require('path');

// default 13-plot harvest
export function harvest() {
  console.log('calling harvest')
  // call the python file
  const python = spawn('python', ['test.py']); // path to python dir somewhere...
  

  python.stdout.on('data', (data) => {
    console.log('from stdout:  ', data)
  });

  python.on('close', (shit) => console.log('shit?', shit))
}
