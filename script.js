document.getElementById('climaForm').onsubmit = function(event) {
  event.preventDefault();
  const cidade = document.getElementById('cidade').value;
  buscarClima(cidade);
};

function buscarClima(cidade) {
  fetch(`http://api.openweathermap.org/data/2.5/weather?q=${cidade}&appid=3bf3970635a7027ba5113229f9179e3d`)
    .then(response => response.json())
    .then(data => {
      const temperaturaCelcius = (data.main.temp - 273.15).toFixed(0);
      const descricao = data.weather[0].description;
      const umidade = data.main.humidity;
      const vento = data.wind.speed;

      document.getElementById('resultado').innerHTML = `
        <h2>Tempo em ${cidade.charAt(0).toUpperCase() + cidade.slice(1)}</h2>
        <p>Temperatura: ${temperaturaCelcius}°C</p>
        <p>Condição: ${descricao.charAt(0).toUpperCase() + descricao.slice(1)}</p>
        <p>Umidade: ${umidade}%</p>
        <p>Vento: ${vento} m/s</p>
      `;
    })
    .catch(error => {
      console.error('Erro ao buscar dados da API', error);
      document.getElementById('resultado').innerHTML = `Não foi possível obter os dados.`;
    });
}
