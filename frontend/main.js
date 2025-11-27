async function getRecommendations() {
    const res = await fetch('/api/recommend', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ query: "lumini inteligente" })
    });
    const data = await res.json();
    document.getElementById("recommendations").innerText = JSON.stringify(data);
}
getRecommendations();