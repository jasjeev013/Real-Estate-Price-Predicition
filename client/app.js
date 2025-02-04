// app.js
document.addEventListener("DOMContentLoaded", function () {
    fetch("http://127.0.0.1:5000/get_location_names")
        .then(response => response.json())
        .then(data => {
            let locationSelect = document.getElementById("location");
            data.locations.forEach(location => {
                let option = document.createElement("option");
                option.value = location;
                option.textContent = location;
                locationSelect.appendChild(option);
            });
        })
        .catch(error => console.error("Error fetching locations:", error));

    document.getElementById("prediction-form").addEventListener("submit", function (event) {
        event.preventDefault();



        /*let formData = {
            total_sqft: parseFloat(document.getElementById("total_sqft").value),
            bath: parseInt(document.getElementById("bath").value),
            balcony: parseInt(document.getElementById("balcony").value),
            availability_day: parseInt(document.getElementById("availability_day").value),
            availability_month: parseInt(document.getElementById("availability_month").value),
            size_bhk: parseInt(document.getElementById("size_bhk").value),
            area_type: parseInt(document.getElementById("area_type").value),
            location: document.getElementById("location").value
        };*/

        let formdData = new FormData();

        // Append the data from the 'formData' object to the FormData object
        formdData.append("total_sqft", parseFloat(document.getElementById("total_sqft").value));
        formdData.append("bath", parseInt(document.getElementById("bath").value));
        formdData.append("balcony", parseInt(document.getElementById("balcony").value));
        formdData.append("availability_day", parseInt(document.getElementById("availability_day").value));
        formdData.append("availability_month", parseInt(document.getElementById("availability_month").value));
        formdData.append("size_bhk", parseInt(document.getElementById("size_bhk").value));
        formdData.append("area_type", parseInt(document.getElementById("area_type").value));
        formdData.append("location", document.getElementById("location").value);
        fetch("http://127.0.0.1:5000/predict_home_price", {
            method: "POST",
            body: formdData  // Sending the form data as form-data
        })
            .then(response => response.json())
            .then(data => {
                document.getElementById("prediction-result").textContent = "Estimated Price: " + data.estimated_price;
            })
            .catch(error => console.error("Error predicting price:", error));
    });
});