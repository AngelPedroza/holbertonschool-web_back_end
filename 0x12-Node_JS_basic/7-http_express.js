const express = require('express');
const countStudents = require('./3-read_file_async');

const args = process.argv.slice(2);

const app = express();
const PORT = 1245;

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  res.setHeader('Content-Type', 'text/plain');
  res.write('This is the list of our students\n');
  countStudents(args[0])
    .then((value) => {
      res.end(`${value.join('\n')}`);
    })
    .catch((error) => {
      res.end(error.message);
    });
});

app.listen(PORT, () => {
  console.log(`Example app listening at http://localhost:${PORT}`);
});

module.exports = app;
