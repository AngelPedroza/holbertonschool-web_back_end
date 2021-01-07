const express = require('express');

const app = express();
const PORT = 1245;

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.listen(PORT, () => {
  //   console.log(`Example app listening at http://localhost:${port}`);
});

module.exports = app;
