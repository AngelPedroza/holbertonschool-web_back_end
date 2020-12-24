export default function getListStudents() {
  const set = new Array();

  set.push({ id: 1, firstName: 'Guillaume', location: 'San Francisco' });
  set.push({ id: 2, firstName: 'James', location: 'Columbia' });
  set.push({ id: 5, firstName: 'Serena', location: 'San Francisco' });

  return set;
}
