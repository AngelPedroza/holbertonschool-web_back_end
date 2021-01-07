const readDatabase = require('../utils');

export default class StudentsController {
    
    static getAllStudents(request, response, DB) {
        readDatabase(DB)
        .then((data) => {
            const msg = 'This is the list of our students\n';
            data = msg + data;
            response.send(200, data);
          })
          .catch((error) => {
            response.send(500, error.message);
          });
    }

    static getAllStudentsByMajor(request, response, DB) {
        const { major } = request.params;
    
        if (major !== 'CS' && major !== 'SWE') {
          response.send(500, 'Major parameter must be CS or SWE');
        } else {
          readDatabase(DB)
            .then((fields) => {
              const list = fields.split('\n');
              let students;
              if (major === 'CS') {
                students = list[1];
              } else {
                students = list[2];
              }
              students = students.split('. ');
              console.log(students);
    
              response.send(200, `${students[1]}`);
            })
            .catch(() => response.send(500, 'Cannot load the database'));
        }
      }
}