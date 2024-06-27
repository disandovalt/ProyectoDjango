let cartItems = [];

function addToCart(itemName) {
    cartItems.push(itemName);
    updateCart();
}

function removeFromCart(index) {
    cartItems.splice(index, 1);
    updateCart();
}

function updateCart() {
    const cartItemsElement = document.getElementById('cart-items');
    cartItemsElement.innerHTML = '';
    if (cartItems.length === 0) {
        cartItemsElement.innerHTML = '<p>El carrito está vacío</p>';
    } else {
        cartItems.forEach((item, index) => {
            const itemElement = document.createElement('div');
            itemElement.classList.add('cart-item');
            itemElement.innerHTML = `
                <p>${item}</p>
                <button class="btn btn-danger btn-sm" onclick="removeFromCart(${index})">Eliminar</button>
            `;
            cartItemsElement.appendChild(itemElement);
        });
        document.querySelector('.btn-checkout').style.display = 'block';
    }
}

function checkout() {
    cartItems = [];
    updateCart();
    alert('¡Pedido realizado con éxito!');
    window.location.reload();
}
