const updateInterval = 5000;
let destinationIpChart;
let sourceIpChart;
function removeLegend(chart) {
    chart.legend.options.display = false;
    chart.legend.draw();
}

function createDestinationIpChart(data) {
    const destinationIpChartCanvas = document.getElementById('destinationIpChart').getContext('2d');
    if (destinationIpChart) {
        destinationIpChart.destroy();  // Destrói o gráfico existente
    }
    // Crie um array para armazenar os IPs e suas contagens
    const ipCounts = {};

    data.forEach(item => {
        const ip = item.destination_ip;
        ipCounts[ip] = ipCounts[ip] ? ipCounts[ip] + 1 : 1;
    });

    const labels = Object.keys(ipCounts);
    const counts = Object.values(ipCounts);

    
    destinationIpChart = new Chart(destinationIpChartCanvas, {
        type: 'doughnut',
        data: {
            labels: labels,
            datasets: [{
                data: counts,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.7)',
                    'rgba(54, 162, 235, 0.7)',
                    'rgba(255, 206, 86, 0.7)',
                    'rgba(75, 192, 192, 0.7)',
                    'rgba(153, 102, 255, 0.7)',
                ],
            }],
        },
        options: {
            layout: {
                padding:{
                    bottom: 45,
                    right: 50
                }
            }
        }
    });
    removeLegend(destinationIpChart);
}

function createSourceIpChart(data) {
    const sourceIpChartCanvas = document.getElementById('sourceIpChart').getContext('2d');
    if (sourceIpChart) {
        sourceIpChart.destroy();
    }
    const ipCounts = {};

    data.forEach(item => {
        const ip = item.source_ip;
        ipCounts[ip] = ipCounts[ip] ? ipCounts[ip] + 1 : 1;
    });

    const labels = Object.keys(ipCounts);
    const counts = Object.values(ipCounts);
    sourceIpChart = new Chart(sourceIpChartCanvas, {
        type: 'doughnut',
        data: {
            labels: labels,
            datasets: [{
                data: counts,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.7)',
                    'rgba(54, 162, 235, 0.7)',
                    'rgba(255, 206, 86, 0.7)',
                    'rgba(75, 192, 192, 0.7)',
                    'rgba(153, 102, 255, 0.7)',
                ],
            }],
        },
        options: {
            layout: {
                padding:{
                    bottom: 45,
                    right: 50
                }
            }
        }
    });

}
function fetchDataAndUpdate() {
    fetch('js-desktop/dados.json')
        .then(response => {
            if (!response.ok) {
                throw new Error('Erro ao obter os dados.');
            }
            return response.json();
        })
        .then(data => {
            const tableBody = document.getElementById('table-body');
            const tableBody2 = document.getElementById('table-body2');
            const malwareCountElement = document.getElementById('malware-count');
            const totalFilesCheckedElement = document.getElementById('total-files-checked');
            const totalHostsAffectedElement = document.getElementById('total-hosts-affected');

            tableBody.innerHTML = '';  // Limpar a tabela antes de adicionar os novos dados
            tableBody2.innerHTML = '';

            let malwareCount = 0;
            let totalFilesChecked = data.length;
            const uniqueAffectedHosts = new Set();

            for (let i = 0; i < data.length; i++) {
                const item = data[i];
                if (item.malware_detected) {
                    malwareCount++;
                    uniqueAffectedHosts.add(item.destination_ip);
                    const malwareRow = document.createElement('tr');
                    malwareRow.innerHTML = `
                        <td>${item.filename}</td>
                        <td>${item.malware_detected ? 'Sim' : 'Não'}</td>
                    `;
            
                    tableBody2.appendChild(malwareRow);
                }
            }

            // Adicionar apenas os últimos 4 registros
            for (let i = Math.max(0, data.length - 4); i < data.length; i++) {
                const item = data[i];
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${item.filename}</td>
                    <td>${item.source_ip}</td>
                    <td>${item.destination_ip}</td>
                `;
                tableBody.appendChild(row);
            }
            
            malwareCountElement.textContent = `${malwareCount}`;
            totalFilesCheckedElement.textContent = `${totalFilesChecked}`
            totalHostsAffectedElement.textContent = `${uniqueAffectedHosts.size}`;

            createDestinationIpChart(data);
            createSourceIpChart(data);

            return data;
        })
        .catch(error => console.error('Erro:', error));
}
// Chamar a função inicialmente para exibir os dados
fetchDataAndUpdate();

// Atualizar os dados periodicamente
setInterval(fetchDataAndUpdate, updateInterval);

  

