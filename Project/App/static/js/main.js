// vehicle elements
const vehicleModelFilter = document.querySelector("#vehicle_model");
const vehicleModelRowName = document.querySelector("#vehicleModelRowName");
const vehicleModelRow = document.querySelectorAll(".vehicleModelRow");

// engine elements
const engineModelFilter = document.querySelector("#engine_model");
const engineModelRowName = document.querySelector("#engineModelRowName");
const engineModelRow = document.querySelectorAll(".engineModelRow");

// transmission elements
const transmissionModelFilter = document.querySelector("#transmission_model");
const transmissionModelRowName = document.querySelector("#transmissionModelRowName");
const transmissionModelRow = document.querySelectorAll(".transmissionModelRow");

// driveAxle elements
const driveAxleModelFilter = document.querySelector("#driveAxle_model");
const driveAxleModelRowName = document.querySelector("#driveAxleModelRowName");
const driveAxleModelRow = document.querySelectorAll(".driveAxleModelRow");

// steeringAxle elements
const steeringAxleModelFilter = document.querySelector("#steeringAxle_model");
const steeringAxleModelRowName = document.querySelector("#steeringAxleModelRowName");
const steeringAxleModelRow = document.querySelectorAll(".steeringAxleModelRow");

// buttons elements
const resetButtonFilterMain = document.querySelector("#resetButtonFilterMain");
const buttonApplyFilterMain = document.querySelector("#buttonApplyFilterMain");
const closeInfoPanelButton = document.querySelector("#closeInfoPanel");

// reset button handler
resetButtonFilterMain.addEventListener("click", function() {
    vehicleModelFilter.value = ''
    engineModelFilter.value = ''
    transmissionModelFilter.value = ''
    driveAxleModelFilter.value = ''
    steeringAxleModelFilter.value = ''
    buttonApplyFilterMain.click()
});

// highlight elements if filters have been set
// vehicle filter
if (vehicleModelFilter.value !== '') {
    // row name
    vehicleModelRowName.style.border = '2px solid #D20A11';
    // each element in the row
    vehicleModelRow.forEach((element) => {
        element.style.border = '2px solid #D20A11';
    });
}
// engine filter
if (engineModelFilter.value !== '') {

    engineModelRowName.style.border = '2px solid #D20A11';

    engineModelRow.forEach((element) => {
        element.style.border = '2px solid #D20A11';
    });
}
// transmission filter
if (transmissionModelFilter.value !== '') {

    transmissionModelRowName.style.border = '2px solid #D20A11';

    transmissionModelRow.forEach((element) => {
        element.style.border = '2px solid #D20A11';
    });
}
// driveAxle filter
if (driveAxleModelFilter.value !== '') {

    driveAxleModelRowName.style.border = '2px solid #D20A11';

    driveAxleModelRow.forEach((element) => {
        element.style.border = '2px solid #D20A11';
    });
}
// steeringAxle filter
if (steeringAxleModelFilter.value !== '') {

    steeringAxleModelRowName.style.border = '2px solid #D20A11';

    steeringAxleModelRow.forEach((element) => {
        element.style.border = '2px solid #D20A11';
    });
}

function on(nameInfo, urlInfo, tableName) {
    //show the block
    document.querySelector('#tableName').textContent = `'${tableName}'`;
    //show the block
    document.querySelector('.vehicleModelRowInfo').style.display = "block";
    //
    const url = `http://127.0.0.1:8000/api/catalog/${urlInfo}/`
    // API handler
    fetch(url)
    .then((response) => {
        const result = response.json()
        return result;
    })
    .then((data) => {
        // console.log('data.results',data.results)
        data.results.map((item) => {
            if (item.name === nameInfo.toString().trim()) {
                // fill the table
                document.querySelector(".vehicleModelRowInfo_Id").textContent = item.id;
                document.querySelector(".vehicleModelRowInfo_Name").textContent = item.name;
                document.querySelector(".vehicleModelRowInfo_Description").textContent = item.description;
            }
            }
        )
    })
    .catch(() => { console.log('error') })

}

// closePanel button handler
closeInfoPanelButton.addEventListener("click", function() {
    //hide the block
    document.querySelector('.vehicleModelRowInfo').style.display = "none";
});