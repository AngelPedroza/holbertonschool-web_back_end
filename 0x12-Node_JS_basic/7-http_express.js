const express = require('express');
const countStudents = require('./3-read_file_async');

const args = process.argv.slice(2);

const app = express();
const PORT = 1245;

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  const msg = 'This is the list of our students\n';
  try {
    const students = await countStudents(args[0]);
    res.send(`${msg}${students.join('\n')}`);
  } catch (error) {
    res.send(`${msg}${error.message}`);
  }
});

app.listen(PORT, () => {
  //   console.log(`Example app listening at http://localhost:${port}`);
});

module.exports = app;
