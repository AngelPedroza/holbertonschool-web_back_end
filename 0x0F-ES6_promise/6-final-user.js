import signUpUser from "./4-user-promise";
import uploadPhoto from "./5-photo-reject";

async function handleProfileSignup(firstName, lastName, fileName) {
  const json1 = {
    status: 'pending'
  };

  const json2 = {
    status: 'pending'
  };

  try {
    const promise_sing = await signUpUser(firstName, lastName);
    json1.status = 'fulfilled';
    json1.value = promise_sing;
  } catch (err) {
    json1.status = 'rejected'
    json1.value = err.toString();
  }

  try {
    const up_promise = await uploadPhoto(fileName);
    json2.status = 'fulfilled';
    json2.value = promise_sing;
  } catch (err) {
    json2.status = 'rejected'
    json2.value = err.toString();
  }

  return [json1, json2];
}

export default handleProfileSignup;
