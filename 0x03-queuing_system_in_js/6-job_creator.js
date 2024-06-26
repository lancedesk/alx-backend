import kue from 'kue';
import redis from 'redis';

// Connect to Redis
const client = redis.createClient();

// Create a Kue queue
const queue = kue.createQueue({ redis: client });

// Define the job data
const jobData = {
    phoneNumber: '1234567890',
    message: 'Hello, this is a notification!'
};

// Create a job in the queue
const job = queue.create('push_notification_code', jobData);

// Handle successful job creation
job.on('enqueue', () => {
    console.log(`Notification job created: ${job.id}`);
});

// Handle job completion
job.on('complete', () => {
    console.log('Notification job completed');
    // Remove completed job from Redis
    job.remove(() => {
        console.log(`Removed completed job ${job.id} from queue`);
        // Close Redis client connection
        client.quit();
    });
});

// Handle job failure
job.on('failed', (err) => {
    console.log(`Notification job failed with error: ${err}`);
});

// Save the job to the queue
job.save();

// Log a message indicating the script is waiting for job processing
console.log(`Nothing else will happen - to process the job, go to the next task!
