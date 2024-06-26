import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const app = express();
const port = 1245;

// Data: List of products
const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 }
];

// Function to get a product by its ID
const getItemById = (id) => {
  return listProducts.find(product => product.itemId === id);
};

// Express middleware to parse JSON bodies
app.use(express.json());

// Redis client setup
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Function to reserve stock in Redis
const reserveStockById = async (itemId, stock) => {
  await setAsync(`item.${itemId}`, stock.toString());
};

// Async function to get current reserved stock from Redis
const getCurrentReservedStockById = async (itemId) => {
  const reservedStock = await getAsync(`item.${itemId}`);
  return reservedStock ? parseInt(reservedStock) : 0;
};

// Route: GET /list_products
app.get('/list_products', (req, res) => {
  res.json(listProducts.map(product => ({
    itemId: product.itemId,
    itemName: product.itemName,
    price: product.price,
    initialAvailableQuantity: product.initialAvailableQuantity
  })));
});

// Route: GET /list_products/:itemId
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);

  if (!product) {
    res.json({ status: 'Product not found' });
  } else {
    const currentQuantity = await getCurrentReservedStockById(itemId);
    res.json({
      itemId: product.itemId,
      itemName: product.itemName,
      price: product.price,
      initialAvailableQuantity: product.initialAvailableQuantity,
      currentQuantity: currentQuantity
    });
  }
});

// Route: GET /reserve_product/:itemId
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);

  if (!product) {
    res.json({ status: 'Product not found' });
  } else {
    const currentStock = product.initialAvailableQuantity;
    const reservedStock = await getCurrentReservedStockById(itemId);

    if (reservedStock >= currentStock) {
      res.json({ status: 'Not enough stock available', itemId: itemId });
    } else {
      await reserveStockById(itemId, reservedStock + 1);
      res.json({ status: 'Reservation confirmed', itemId: itemId });
    }
  }
});

// Start the Express server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
