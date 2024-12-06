import { createClient } from "redis";

const client = createClient();

client.on("connect", () => {
  console.log("Redis client connect to the server");
});

client.on("error", (err) => {
  console.log(`Redis client not connected to the server, ${err.message}`);
});

// Subscribe to the ALXchannel
client.subscribe("ALXchannel", (err, count) => {
  if (err) {
    console.log(`Error subscribing: ${err.message}`);
  } else {
    console.log(`Subcribed to ${count} channel(s)`);
  }
});

// Event listener for receiving messages
client.on("message", (channel, message) => {
  console.log(`Message received on channel ${channel}: ${message}`);

  // check for KILL_SERVEER message and unsubscribe if received
  if (message === "KILL_SERVER") {
    console.log("Unsubscribing and quitting...");
    client.unsubscribe("ALXchannel");
    client.quit();
  }
});
