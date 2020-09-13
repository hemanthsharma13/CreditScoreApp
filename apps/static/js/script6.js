function generateDynamicTable(){
    let getDataNameId=document.querySelector("#getDataNameId")
    let status=document.querySelector("#status")
    let guidelines=document.querySelector("#guidelines")
let dataName=sessionStorage.getItem("dataName")
getDataNameId.textContent=dataName
var data=sessionStorage.getItem("modelData")
var getmodelData=JSON.parse(data)
console.log(getmodelData)
var dataTRN=getmodelData.Intercept
console.log(dataTRN)
 var dataOOT=getmodelData.Slope
 console.log(dataOOT)
 var dataPDO=getmodelData.PDOVal
 console.log(dataPDO)
   // var gerBadData=Object.entries(badData)
// var dataOOTKeys=Object.keys(dataOOT)
// console.log(dataOOTKeys)
// var dataPDOKeys=Object.keys(dataPDO)
// console.log(dataPDOKeys)
// //let total=dataTRN['Total']
// //console.log(total)
//     var displayData=Object.entries(dataTRN)
//     console.log(displayData)
//     var dataTRNKeys=Object.keys(dataTRN)
//     console.log(dataTRNKeys)
//     var noOfData = displayData.length;
//     console.log(noOfData)
var tbl = document.createElement('table');
tbl.id="tblexportData"
var thead = document.createElement("thead");
var tbody = document.createElement("tbody")

var tr_head = document.createElement("tr");
//var th_id = document.createElement("th");
var th_name = document.createElement("th");
var th_trn = document.createElement("th");
var th_oot = document.createElement("th");

//th_id.textContent = "Id";
th_name.textContent = "INTERCEPT";
th_trn.textContent = "SLOPE";
th_oot.textContent="PDO_VAL"

//tr_head.appendChild(th_id);
tr_head.appendChild(th_name);
tr_head.appendChild(th_trn);
tr_head.appendChild(th_oot)

thead.appendChild(tr_head);

for(var i = 0, j =1; i < j; i++) {
    console.log("for loop is working")
    var tr_body = document.createElement("tr");

  //var td_id = document.createElement("td");
    var td_name = document.createElement("td");
	var td_trn = document.createElement("td");
	var td_oot = document.createElement("td");

   // td_id.textContent = i;
	//Get Object keys values

    td_name.textContent = dataTRN+"%";
    console.log(dataTRN)
    td_trn.textContent = dataOOT+"%";
    console.log(dataOOT)
    td_oot.textContent=dataPDO+"%"
    console.log(dataPDO)
	

 //  tr_body.appendChild(td_id);
    tr_body.appendChild(td_name);
	tr_body.appendChild(td_trn);
	tr_body.appendChild(td_oot);

    tbody.appendChild(tr_body);
   
}
tbl.appendChild(thead);
tbl.appendChild(tbody);
console.log(tbl)
var divContainer = document.getElementById("myContacts");
// divContainer.innerHTML = "";
 divContainer.appendChild(tbl);
 if(dataPDO >40){
    status.textContent="GREEN"
    status.setAttribute("style","background-color:green;")
}
else if(dataPDO>=20 && dataPDO<40){
    status.textContent="MODERATE"
    status.setAttribute("style","background-color:orangered;")
}
else{
    status.textContent="RED"
    status.setAttribute("style","background-color:red;")
}
guidelines.textContent=">40%	Red  between 20 to 40 	Amber less than 20%	Green"
}


