
function generateDynamicTable(){
    let getDataNameId=document.querySelector("#getDataNameId")
   let statusElement=document.querySelector("#status")
let dataName=sessionStorage.getItem("dataName")
let name=sessionStorage.getItem("modelOrDriver")
let getCurrentName=document.querySelector("#getCurrentName")
let guidelines=document.querySelector("#guidelines")
let getName=sessionStorage.getItem("currentDisplayedData")
let status=document.createElement("div")
console.log(getName)
getCurrentName.textContent=getName

// if(name=="Driver"){
//   getName.textContent="Driver"
// }
console.log(name)
console.log(dataName)
getDataNameId.textContent=dataName

    console.log("working")
    var data=sessionStorage.getItem("modelData")
var getmodelData=JSON.parse(data)
console.log(getmodelData)
var dataTRN=getmodelData.TRNValues
console.log(dataTRN)
console.log(dataTRN)
 var dataOOT=getmodelData.OOTValues
   // var gerBadData=Object.entries(badData)
var dataOOTKeys=Object.keys(dataOOT)
let total=dataTRN['Total']
console.log(total)
    var displayData=Object.entries(dataTRN)
    console.log(displayData)
    var dataTRNKeys=Object.keys(dataTRN)
    console.log(dataTRNKeys)
    var noOfData = displayData.length;
    console.log(noOfData)
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
th_name.textContent = "BINS";
th_trn.textContent = "TRN";
th_oot.textContent="OOT"

//tr_head.appendChild(th_id);
tr_head.appendChild(th_name);
tr_head.appendChild(th_trn);
tr_head.appendChild(th_oot)

thead.appendChild(tr_head);

for(var i = 0, j =noOfData; i < j; i++) {
    console.log("for loop is working")
    var tr_body = document.createElement("tr");

  //var td_id = document.createElement("td");
    var td_name = document.createElement("td");
	var td_trn = document.createElement("td");
	var td_oot = document.createElement("td");

   // td_id.textContent = i;
	//Get Object keys values

    td_name.textContent = dataTRNKeys[i];
    console.log(dataTRNKeys[i])
    td_trn.textContent = dataTRN[dataTRNKeys[i]]+"%";
    console.log(dataTRN[dataTRNKeys[i]])
    td_oot.textContent=dataOOT[dataOOTKeys[i]]+"%"
    console.log(dataOOT[dataOOTKeys[i]])
	

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
 if(name=="Model"){
   console.log("this model is working")
 if(dataName=="GINI"){
   guidelines.textContent="30%:green,15% to 30%:amber,< 15%-Red"
    if(total>30){
      status.textContent="GREEN"
      status.setAttribute("style","background-color:green;")
    }
    else if(total>=15 && total<=30){
      status.textContent="AMBER"
        status.setAttribute("style","background-color:orangered;")
      }
    else{
      status.textContent="RED"
        status.setAttribute("style","background-color:red;")
    }
 }
 if(dataName=="KS"){
   guidelines.textContent=">25% :Green  15% to 25% Moderate <=15% Low   "
    if(total>25){
      status.textContent="GREEN"
      status.setAttribute("style","background-color:green;")
    }
    else if(total>=15 && total<=25){
      status.textContent="MODERATE"
        status.setAttribute("style","background-color:orangered;")
      }
    else{
      status.textContent="RED"
        status.setAttribute("style","background-color:red;")
    }
 }
 if(dataName=="RISKRANKING"){
  guidelines.textContent="<10% of total bands: Green , 10% to 20% bands : Amber , >20% red  "
    if(total<10){
      status.textContent="GREEN"
      status.setAttribute("style","background-color:green;")
    }
    else if(total>=10 && total<=20){
      status.textContent="AMBER"
        status.setAttribute("style","background-color:orangered;")
      }
    else{
      status.textContent="RED"
        status.setAttribute("style","background-color:red;")
    }
 }
 if(dataName=="PSI"){
  guidelines.textContent="<=10%: Good , 10% to 25%: Amber, >25% :Red  "
    if(total<10){
      status.textContent="GREEN"
      status.setAttribute("style","background-color:green;")
    }
    else if(total>=10 && total<=25){
      status.textContent="AMBER"
        status.setAttribute("style","background-color:orangered;")
      }
    else{
      status.textContent="RED"
        status.setAttribute("style","background-color:red;")
    }
 }
 if(dataName=="BADRATE"){
  guidelines.textContent="<10 Good, >=10 to <=30 Amber, >30 Red"
    if(total<10){
      status.textContent="GREEN"
      status.setAttribute("style","background-color:green;")
    }
    else if(total>=10 && total<=30){
      status.textContent="AMBER"
        status.setAttribute("style","background-color:orangered;")
      }
    else{
      status.textContent="RED"
        status.setAttribute("style","background-color:red;")
    }
 }
}
if(name=="Driver"){
  console.log("this driver comparision is working")
  guidelines.textContent=">7% : Green, 5% to 7% : Amber, <5%: Red  "
  if(dataName=="GINI"){
     if(total>7){
      status.textContent="GREEN"
       status.setAttribute("style","background-color:green;")
     }
     else if(total>=5 && total<=7){
      status.textContent="AMBER"
         status.setAttribute("style","background-color:orangered;")
       }
     else{
      status.textContent="RED"
         status.setAttribute("style","background-color:red;")
     }
  }
  if(dataName=="KS"){
    guidelines.textContent=">25% :Green  15% to 25% Moderate <=15% Low   "
     if(total>25){
      status.textContent="GREEN"
       status.setAttribute("style","background-color:green;")
     }
     else if(total>=15 && total<=25){
      status.textContent="MODERATE"
         status.setAttribute("style","background-color:orangered;")
       }
     else{
      status.textContent="RED"
         status.setAttribute("style","background-color:red;")
     }
  }
  if(dataName=="RISKRANKING"){
    guidelines.textContent="<10% of total bands: Green , 10% to 20% bands : Amber , >20% red  "
     if(total<10){
      status.textContent="GREEN"
       status.setAttribute("style","background-color:green;")
     }
     else if(total>=10 && total<=20){
      status.textContent="AMBER"
         status.setAttribute("style","background-color:orangered;")
       }
     else{
      status.textContent="RED"
         status.setAttribute("style","background-color:red;")
     }
  }
  if(dataName=="BADRATE"){
    guidelines.textContent="<10 Good, >=10 to <=30 Amber, >30 Red"
     if(total<10){
      status.textContent="GREEN"
      console.log("less")
       status.setAttribute("style","background-color:green;")
     }
     else if(total>=10 && total<=30){
      status.textContent="AMBER"
      console.log("medium")
         status.setAttribute("style","background-color:orangered;")
       }
     else{
      status.textContent="RED"
      console.log("High")
         status.setAttribute("style","background-color:red;")
     }
  }
  if(dataName=="PSI"){
    guidelines.textContent="<=10%: Good , 10% to 25%: Amber, >25% :Red  "
    if(total<10){
      status.textContent="GREEN"
      console.log("less")
      status.setAttribute("style","background-color:green;")
    }
    else if(total>=10 && total<=25){
      status.textContent="AMBER"
      console.log("medium")
        status.setAttribute("style","background-color:orangered;")
      }
    else{
      status.textContent="RED"
      console.log("High")
        status.setAttribute("style","background-color:red;")
    }
 }
  if(dataName=="VOI"){
    guidelines.textContent=">30% : Good, 10% to 30%: Amber <10%: Red    "
     if(total>30){
      status.textContent="GREEN"
       console.log("<10")
       status.setAttribute("style","background-color:green;")
     }
     else if(total>=10 && total<=30){
      status.textContent="AMBER"
      console.log(">10")
         status.setAttribute("style","background-color:orangered;")
       }
     else{
      status.textContent="RED"
      console.log(">30")
         status.setAttribute("style","background-color:red;")
     }
  } 
 }
 statusElement.appendChild(status)

}	

function exportToExcel(tableID){
  console.log("This function is working")
  var downloadurl;
  var dataFileType = 'application/vnd.ms-excel';
  var tableSelect = document.getElementById(tableID);
  var tableHTMLData = tableSelect.outerHTML.replace(/ /g, '%20');
  
  // Specify file name
  filename = filename?filename+'.xls':'export_excel_data.xls';
  console.log(filename)
  
  // Create download link element
  downloadurl = document.createElement("a");
  
  document.body.appendChild(downloadurl);
  
  if(navigator.msSaveOrOpenBlob){
      var blob = new Blob(['\ufeff', tableHTMLData], {
          type: dataFileType
      });
      navigator.msSaveOrOpenBlob( blob, filename);
  }else{
      // Create a link to the file
      downloadurl.href = 'data:' + dataFileType + ', ' + tableHTMLData;
  
      // Setting the file name
      downloadurl.download = filename;
      
      //triggering the function
      downloadurl.click();
  }
}



    
    
       
