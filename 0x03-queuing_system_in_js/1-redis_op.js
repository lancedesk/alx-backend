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

// Connect the client
client.connect();

/**
 * setNewSchool - Set the value for a given key in Redis
 * @param {string} schoolName - The key name
 * @param {string} value - The value to set
 */
function setNewSchool(schoolName, value)
{
    client.set(schoolName, value, print);
}

/**
 * displaySchoolValue - Get and log the value for a given key in Redis
 * @param {string} schoolName - The key name
 */
function displaySchoolValue(schoolName)
{
    client.get(schoolName, (err, reply) => {
        if (err) throw err;
        console.log(reply);
    });
}

// Call the functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
