import { createClient, print } from 'redis';

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

/**
 * setHashValues - Set multiple fields in a hash in Redis
 */
function setHashValues()
{
    client.hset('HolbertonSchools', 'Portland', 50, print);
    client.hset('HolbertonSchools', 'Seattle', 80, print);
    client.hset('HolbertonSchools', 'New York', 20, print);
    client.hset('HolbertonSchools', 'Bogota', 20, print);
    client.hset('HolbertonSchools', 'Cali', 40, print);
    client.hset('HolbertonSchools', 'Paris', 2, print);
}

/**
 * displayHashValues - Get and log all fields and values in a hash in Redis
 */
function displayHashValues()
{
    client.hgetall('HolbertonSchools', (err, obj) => {
        if (err) throw err;
        console.log(obj);
    });
}

// Call the functions
setHashValues();
displayHashValues();
