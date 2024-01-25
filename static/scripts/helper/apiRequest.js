/**
 * ## ApiRequest
 * @param {String} url 
 * @param {Object} option 
 * @param {("GET"|"POST"|"PUT"|"DELETE")} option.method 
 */
async function ApiRequest(url, { method }, data=null) {
    const option = {
        method,
        headers: { "Conent-Type": "application/json" }
    };
    data && (option['body'] = JSON.stringify(data));

    const res = await fetch(
        url, 
        option
    );
    return res.json();
}

export default ApiRequest;