import { uploadPhoto, createUser } from "./utils"

async function asyncUploadUser() {
  const json = {
    photo: null,
    user: null,
  };

  try {
    const r1 = await uploadPhoto().then(values => values)
    json.photo = r1
  } catch (err) {
    json.user = null;
    json.photo = null;
    return json;
  };

  try {
    const r2 = await createUser().then(values => values)
    json.user = r2
  } catch (err) {
    json.user = null;
    json.photo = null;
    return json;
  };

  return json;
}

export default asyncUploadUser;