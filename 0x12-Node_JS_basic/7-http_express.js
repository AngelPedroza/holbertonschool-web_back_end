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
    await countStudents(args[0]).then((value) => {
      res.send(`${value.join('\n')}`);
    }).catch((error) => {
      res.send(`${error}`);
    });
});

app.listen(PORT, () => {
  //   console.log(`Example app listening at http://localhost:${port}`);
});

module.exports = app;
