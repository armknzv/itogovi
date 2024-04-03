// maintenance_type elements
const maintenanceTypeFilter = document.querySelector("#maintenance_type");
const maintenanceTypeRowName = document.querySelector("#maintenanceTypeRowName");
const maintenanceTypeRow = document.querySelectorAll(".maintenanceTypeRow");

// vehicle_number elements
const vehicleNumberFilter = document.querySelector("#vehicle_number");
const vehicleNumberRowName = document.querySelector("#vehicleNumberRowName");
const vehicleNumberRow = document.querySelectorAll(".vehicleNumberRow");

// service_company elements
const serviceCompanylFilter = document.querySelector("#service_company");
const serviceCompanyRowName = document.querySelector("#serviceCompanyRowName");
const serviceCompanyRow = document.querySelectorAll(".serviceCompanyRow");

// buttons elements
const resetButtonFilterMain = document.querySelector("#resetButtonFilterMain");
const buttonApplyFilterMain = document.querySelector("#buttonApplyFilterMain");
const closeInfoPanelButton = document.querySelector("#closeInfoPanel");


// reset button handler
resetButtonFilterMain.addEventListener("click", function() {
    maintenanceTypeFilter.value = ''
    vehicleNumberFilter.value = ''
    serviceCompanylFilter.value = ''
    buttonApplyFilterMain.click()
});

// highlight elements if filters have been set
// maintenance_type filter
filterHandler (maintenanceTypeFilter, maintenanceTypeRowName, maintenanceTypeRow)

// vehicle_number filter
filterHandler (vehicleNumberFilter, vehicleNumberRowName, vehicleNumberRow)

// service_company filter
filterHandler (serviceCompanylFilter, serviceCompanyRowName, serviceCompanyRow)

//filter handler function
function filterHandler (filter, rowName, row) {
    if (filter.value !== '') {
        // row name
        rowName.style.border = '2px solid #D20A11';
        // each element in the row
        row.forEach((element) => {
            element.style.border = '2px solid #D20A11';
        });
    }
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