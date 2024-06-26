import kue from 'kue';
import redis from 'redis';

// Connect to Redis
const client = redis.createClient();

// Create a Kue queue
const queue = kue.createQueue({ redis: client });

// Function to send notifications
function sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Process jobs in the queue
queue.process('push_notification_code', (job, done) => {
    // Extract job data
    const { phoneNumber, message } = job.data;

    // Call function to send notification
    sendNotification(phoneNumber, message);

    // Simulate completion of job processing
    setTimeout(() => {
        done();
    }, 1000); // Simulate processing time

    // Log job processing
    console.log(`Processed job ${job.id}`);
});

// Log a message indicating the script is waiting for job processing
console.log(`Waiting for jobs to process...`);
