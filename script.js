let soilMoisture = 50; // Example value
let temperature = 22;  // Example value in °C
let humidity = 60;     // Example value in %

function updateSensorData() {
    // Simulating data update after a certain interval (e.g., 5 seconds)
    soilMoisture = Math.random() * 100;
    temperature = Math.random() * (35 - 15) + 15;
    humidity = Math.random() * (80 - 40) + 40;

    document.getElementById('soil-moisture').textContent = `Soil Moisture: ${soilMoisture.toFixed(2)}%`;
    document.getElementById('temperature').textContent = `Temperature: ${temperature.toFixed(2)} °C`;
    document.getElementById('humidity').textContent = `Humidity: ${humidity.toFixed(2)}%`;
}

function predictIrrigationNeed() {
    const result = calculateIrrigationNeed(soilMoisture, temperature, humidity);
    document.getElementById('irrigation-result').textContent = `Irrigation Prediction: ${result}`;
}

function calculateIrrigationNeed(soilMoisture, temperature, humidity) {
    if (soilMoisture < 30 && temperature > 25 && humidity < 50) {
        return "High"; // High irrigation needed
    } else if (soilMoisture >= 30 && temperature > 20 && humidity >= 50) {
        return "Medium"; // Medium irrigation needed
    } else {
        return "Low"; // Low irrigation needed
    }
}

// Event listener for the "Predict Irrigation Need" button
document.getElementById('predict-btn').addEventListener('click', function() {
    predictIrrigationNeed();
});

// Update sensor data every 5 seconds
setInterval(updateSensorData, 5000);

// Initial data load
updateSensorData();
