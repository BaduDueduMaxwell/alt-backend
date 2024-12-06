import { createClient } from "redis";

const client = createClient();
const redis = require("redis");

client.on("connect", () => {
  console.log("Redis client connected to the server");
});

client.on("error", (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Create Hash
const key = "ALX";

// Delete the existing key if it exists to avoid WRONGTYPE error
client.del(key, (err, response) => {
  if (err) {
    console.error(`Error deleting key ${key}`, err);
  } else {
    console.log(`Deleted key ${key}: ${response}`);
  }

  client.hset(key, "Portland", 50, redis.print);
  client.hset(key, "Seattle", 80, redis.print);
  client.hset(key, "New York", 20, redis.print);
  client.hset(key, "Bogota", 20, redis.print);
  client.hset(key, "Cali", 40, redis.print);
  client.hset(key, "Paris", 2, redis.print);

  // Display Hash
  client.hgetall(key, (err, result) => {
    if (err) {
      console.error(`Error retrieving hash ${key}:`, err);
    } else {
      console.log(result);
    }

    client.quit();
  });
});
