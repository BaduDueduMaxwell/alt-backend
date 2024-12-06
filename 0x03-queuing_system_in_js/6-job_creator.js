import kue from "kue";

const queue = kue.createQueue();

const jobData = {
  phoneNumber: "+1234567890",
  message: "Chikibom completed!",
};

const job = queue.create("push_notification_code", jobData).save((err) => {
  if (err) {
    console.log("Error creating job", err);
  } else {
    console.log(`Notification job created ${job.id}`);
  }
});

// Job completion handler
job.on("complete", () => {
  console.log("Notification job completed");
});

// Job failure handler
job.on("failed", (err) => {
  console.log(`Notification job failed: ${err}`);
});
