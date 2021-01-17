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

const keys = ['Portland', 'Seattle', 'New York', 'Bogota', 'Cali', 'Paris'];
const values = [50, 80, 20, 20, 40, 2];

keys.forEach((key, index) => {
    client.hset('HolbertonSchools', key, values[index], redis.print);
});

client.hgetall('HolbertonSchools', (err, value) => {
    console.log(value);
});
