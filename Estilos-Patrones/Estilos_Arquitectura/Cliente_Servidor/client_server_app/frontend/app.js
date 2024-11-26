const apiUrl = "http://localhost:8000/products";

async function fetchProducts() {
    const response = await fetch(apiUrl);
    const products = await response.json();
    const list = document.getElementById("product-list");
    list.innerHTML = "";
    products.forEach(product => {
        const item = document.createElement("div");
        item.textContent = `${product.name}: ${product.description}`;
        list.appendChild(item);
    });
}

document.getElementById("product-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    const name = document.getElementById("name").value;
    const description = document.getElementById("description").value;

    await fetch(apiUrl, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, description })
    });
    fetchProducts();
});

fetchProducts();
