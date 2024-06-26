import kue from 'kue';

// Function to create push notification jobs
function createPushNotificationsJobs(jobs, queue) {
  // Check if jobs is an array
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  // Create jobs in the queue
  jobs.forEach((jobData) => {
    const job = queue.create('push_notification_code_3', jobData);

    // On successful creation
    job.on('enqueue', () => {
      console.log(`Notification job created: ${job.id}`);
    });

    // On completion
    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });

    // On failure
    job.on('failed', (err) => {
      console.log(`Notification job ${job.id} failed: ${err}`);
    });

    // On progress
    job.on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });

    // Save the job to the queue
    job.save((err) => {
      if (err) {
        console.error(`Could not save job ${job.id}: ${err}`);
      }
    });
  });
}

export default createPushNotificationsJobs;
import kue from 'kue';

// Function to create push notification jobs
function createPushNotificationsJobs(jobs, queue) {
  // Check if jobs is an array
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  // Create jobs in the queue
  jobs.forEach((jobData) => {
    const job = queue.create('push_notification_code_3', jobData);

    // On successful creation
    job.on('enqueue', () => {
      console.log(`Notification job created: ${job.id}`);
    });

    // On completion
    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });

    // On failure
    job.on('failed', (err) => {
      console.log(`Notification job ${job.id} failed: ${err}`);
    });

    // On progress
    job.on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });

    // Save the job to the queue
    job.save((err) => {
      if (err) {
        console.error(`Could not save job ${job.id}: ${err}`);
      }
    });
  });
}

export default createPushNotificationsJobs;
