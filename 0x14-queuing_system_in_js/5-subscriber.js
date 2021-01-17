import redis from "redis"

const subscriber = redis.createClient();


subscriber.once("connect", function() {
    console.log("Redis client connected to the server")
})
subscriber.on("error", function(error) {
    console.log("Redis client not connected to the server:", error.message);
});

subscriber.on("message", function(channel, message) {
    console.log(message);
    if (message === "KILL_SERVER") {
        subscriber.unsubscribe();
        subscriber.quit();
    }
});

subscriber.subscribe("holberton school channel");

