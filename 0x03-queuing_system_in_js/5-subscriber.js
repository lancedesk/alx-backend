import { createClient } from 'redis';

// Create a Redis client
const client = createClient();

// Handle successful connection
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

// Handle connection errors
client.on('error', (err) => {
    console.log('Redis client not connected to the server:', err.message);
});

// Subscribe to the channel 'holberton school channel'
client.subscribe('holberton school channel');

// Handle messages received
client.on('message', (channel, message) => {
    console.log(message);

    // Check if message is KILL_SERVER
    if (message === 'KILL_SERVER') {
        client.unsubscribe();
        client.quit();
    }
});
