import kue from 'kue';
import redis from 'redis';

// Array of blacklisted phone numbers
const blacklist = ['4153518780', '4153518781'];

// Connect to Redis
const client = redis.createClient();

// Create a Kue queue
const queue = kue.createQueue({ redis: client });

// Function to send notifications
function sendNotification(phoneNumber, message, job, done) {
  // Track job progress
  job.progress(0, 100);

  // Check if phoneNumber is blacklisted
  if (blacklist.includes(phoneNumber)) {
    // Fail the job with an error
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // Track progress to 50%
  job.progress(50);

  // Log the notification being sent
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  // Simulate sending notification
  setTimeout(() => {
    // Complete the job
    done();
  }, 1000); // Simulating delay
}

// Process jobs from the queue
queue.process('push_notification_code_2', 2, (job, done) => {
  // Extract job data
  const { phoneNumber, message } = job.data;

  // Call sendNotification function
  sendNotification(phoneNumber, message, job, done);
});

// Log a message indicating that jobs are being processed
console.log('Job processor is running...');
