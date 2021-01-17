import redis from "redis"
import { promisify } from "util"

const client = redis.createClient();
const asyncGet = promisify(client.get).bind(client)
const asyncSet = promisify(client.set).bind(client)

client.once("connect", function() {
    console.log("Redis client connected to the server")
})
client.on("error", function(error) {
    console.log("Redis client not connected to the server:", error.message);
});

async function setNewSchool(schoolName, value) {
    //client.set(schoolName, value, redis.print);
    await asyncSet(schoolName, value).then((reply) => redis.print(`Reply: ${reply}`));
}

async function displaySchoolValue(schoolName) {
    const value = await asyncGet(schoolName);
    console.log(value);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
