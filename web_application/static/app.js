function updateData() {
    fetch('/weight')
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                console.error('Error:', data.error);
                return;
            }
            
            // Update weight
            document.getElementById('weight-value').textContent = `${data.weight} kg`;
            
            // Update voltage readings
            const voltageContainer = document.getElementById('voltage-readings');
            voltageContainer.innerHTML = ''; // Clear previous readings
            
            data.voltages.forEach((voltage, index) => {
                const voltageElement = document.createElement('div');
                voltageElement.className = 'voltage-reading';
                voltageElement.innerHTML = `
                    <span class="voltage-label">Voltage ${index + 1}</span>
                    <span class="voltage-value">${voltage.toFixed(2)}V</span>
                `;
                voltageContainer.appendChild(voltageElement);
            });
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
}

// Update data every second
setInterval(updateData, 1000);


// Initial update
updateData();
