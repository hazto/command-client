import express from 'express';
import path from 'path'; // have to do something to normalize pathing
import { harvest } from './harvest';

const port = 3034;
const app = express();



harvest();
