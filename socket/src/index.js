const http = require('http');
const dotEnv = require('dotenv');
dotEnv.config();
const express = require('express');
const cors = require('cors');
const app = express();

app.use(cors({ origin: '*' }));
app.all('/', (req, res) => res.end('This is Hi-Find Socket Proxy'));

const PORT = process.env['PORT'] || 3000;
const server = http.createServer(app);
const socket = require('./socket');
socket.config(server);

server.listen(PORT, () => console.log(`Socket Server running at http://localhost:${PORT}`));