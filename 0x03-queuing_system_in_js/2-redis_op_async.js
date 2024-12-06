import { createClient } from "redis";

const client = createClient();

client.on("connect", () => {
  console.log("Redis client connected to the server");
});

client.on("error", (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    if (err) {
      console.error(`Error setting key ${schoolName}:`, err);
    } else {
      console.log(`Reply: ${reply}`);
    }
  });
}

async function displaySchoolValue(schoolName) {
  try {
    const value = await client.get(schoolName);
    console.log(`Value for key "${schoolName}": ${value}`);
  } catch (err) {
    console.error(`Error retrieving key ${schoolName}:`, err);
  }
}

displaySchoolValue("ALX");
setNewSchool("ALXSanFrancisco", "100");
displaySchoolValue("ALXSanFrancisco");
