import express from 'express';
import path from 'path'; // have to do something to normalize pathing
import { harvest } from './harvest';

const port = 3034;
const app = express();

// may need to break goblin challenges into a grid
// take stock of each image in each slot, make best guess on what might be a goblin and what might not be a goblin
// 2 strikes then bail
// law of averages it will guess right
// need to define what constitutes 'gobliness'
// use machine learning?  teach it what's a goblin and what isn't?  oh... sounds like fun!!!

harvest();
