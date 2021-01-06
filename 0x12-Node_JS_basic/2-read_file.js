const fs = require('fs');

function countStudents(path) {
  let content;
  try {
    content = fs.readFileSync(`${path}`, { encoding: 'utf8' });
    const chainStudents = content.split('\n');
    const students = chainStudents.slice(1);
    console.log(`Number of students: ${students.length}`);

    const dict = {};
    students.forEach((element) => {
      const list = element.split(',');
      const key = list[3];
      if (!(key in dict)) {
        dict[key] = [];
      }
      dict[key].push(`${list[0]}`);
    });
    for (const i in dict) {
      if (i) {
        console.log(`Number of students in ${i}: ${dict[i].length}. List: ${dict[i].join(', ')}`);
      }
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}
module.exports = countStudents;
