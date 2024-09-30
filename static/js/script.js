/**
 * Removes an item from the cart asynchronously.
 * @param {number} cart_id - The ID of the item in the cart.
 */
function removeFromCart(cart_id) {
    // Make an asynchronous request to the server to update the quantity
    fetch(`/remove_from_cart/${cart_id}`, { method: "POST" })
        .then(response => response.json())
        .then(data => {
            // Fetch and update cart items again after modification
            updateCartTable();
        })
        .catch(error => console.error("Error removing item from cart:", error));
}

/**
 * Increments the quantity of an item in the cart asynchronously.
 * @param {number} cart_id - The ID of the item in the cart.
 */
function incrementQuantity(cart_id) {
    // Make an asynchronous request to the server to increment the quantity
    fetch(`/update_quantity/${cart_id}`, { method: "POST", body: `new_quantity=${currentQuantity + 1}` })
        .then(response => response.json())
        .then(data => {
            // Fetch and update cart items again after modification
            updateCartTable();
        })
        .catch(error => console.error("Error updating quantity:", error));
}

/**
 * Decrements the quantity of an item in the cart asynchronously.
 * @param {number} cart_id 
 * @param {number} currentQuantity - The current quantity of the item.
 */
function decrementQuantity(cart_id, currentQuantity) {
    // Make an asynchronous request to the server to decrement the quantity
    fetch(`/update_quantity/${cart_id}`, { method: "POST", body: `new_quantity=${currentQuantity - 1}` })
        .then(response => response.json())
        .then(data => {
            // Fetch and update cart items again after modification
            updateCartTable();
        })
        .catch(error => console.error("Error updating quantity:", error));
}
