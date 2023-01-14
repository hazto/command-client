import { pythonPath } from './constants';
import path from 'path';
import { spawn } from 'child_process'
// const spawn = require('child_process').spawn;
// const path = require('path');

// default 13-plot harvest
export function harvest() {
  console.log('calling harvest')
  // call the python file
  const py = spawn('python', [path.join(pythonPath, 'harvest.py')]); 
  

  py.stdout.on('data', (data) => {
    console.log('from stdout:  ', data.toString())
  });

  py.stderr.on('data', error => console.log('an error', error.toString()))

  py.on('close', (shit) => console.log('shit?', shit))
}
