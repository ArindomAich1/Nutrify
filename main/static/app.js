const content = document.querySelector("#content");

fetch("https://api.spoonacular.com/food/news?apiKey=aa5ed93c89954d76a8bf235bfdc9d699")
  .then(response => response.json())
  .then(data => {
    const news = data.articles;

    news.forEach(article => {
      const newsCard = document.createElement("div");
      newsCard.classList.add("news-card");

      newsCard.innerHTML = `
        <h2>${article.title}</h2>
        <p>${article.description}</p>
        <a href="${article.url}" target="_blank">Read more</a>
      `;

      content.appendChild(newsCard);
    });
  })
  .catch(error => {
    console.error(error);
  });
