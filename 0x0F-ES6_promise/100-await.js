import { uploadPhoto, createUser } from "./utils"

async function asyncUploadUser() {
  const json = {};

  try {
    json.photo = await uploadPhoto();
    json.user = await createUser();
  } catch (err) {
    json.photo = null;
    json.user = null;
  }

  return json;
}

export default asyncUploadUser;
