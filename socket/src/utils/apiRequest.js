const axios = require('axios');

const BASE_URL = `${process.env['HI_FIND_API_URL']}/api/chat`;

module.exports = axios.default.create({ 
    baseURL: BASE_URL, 
    headers: { "Content-Type": "application/json" } 
});