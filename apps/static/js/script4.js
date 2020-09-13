function generateDynamicTable(){
    let getDataNameId=document.querySelector("#getDataNameId")
    let status=document.querySelector("#status")
    let name=sessionStorage.getItem("modelOrDriver")
let dataName=sessionStorage.getItem("dataName")
console.log(dataName)
let getCurrentName=document.querySelector("#getCurrentName")
let guidelines=document.querySelector("#guidelines")
let getName=sessionStorage.getItem("currentDisplayedData")
console.log(getName)
getCurrentName.textContent=getName
// if(name=="Driver"){
//   getName.textContent="Driver"
// }
//getDataNameId.textContent=dataName

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
let total=dataOOT['Total']
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
var th_status=document.createElement("th")

//th_id.textContent = "Id";
th_name.textContent = "MONITORING PARAMETERS";
th_trn.textContent = "TRN";
th_oot.textContent="OOT"
th_status.textContent="STATUS"

//tr_head.appendChild(th_id);
tr_head.appendChild(th_name);
tr_head.appendChild(th_trn);
tr_head.appendChild(th_oot)
tr_head.appendChild(th_status)

thead.appendChild(tr_head);

for(var i = 0, j =noOfData; i < j; i++) {
    console.log("for loop is working")
    var tr_body = document.createElement("tr");
  //var td_id = document.createElement("td");
    var td_name = document.createElement("td");
	var td_trn = document.createElement("td");
    var td_oot = document.createElement("td");
    var td_status=document.createElement("td")
    // td_status.setAttribute("style","background:green;")

   // td_id.textContent = i;
	//Get Object keys values

    td_name.textContent = dataTRNKeys[i];
     if(name=="Model"){
       guidelines.innerHTML="<br></br> GINI:30%:green,15% to 30%:amber,< 15%-Red <br></br> KS:>25% :Green  15% to 25% Moderate <=15% Low <br></br> RISKRANKING:<10% of total bands: Green , 10% to 20% bands : Amber , >20% red  <br></br> PSI:<=10%: Good , 10% to 25%: Amber, >25% :Red <br></br> BADRATE:<10 Good, >=10 to <=30 Amber, >30 Red"
      if(dataTRNKeys[i]=="GINI"){
         if(dataTRN[dataTRNKeys[i]]>30){
           td_status.setAttribute("style","background-color:green;")
         }
         else if(dataTRN[dataTRNKeys[i]]>=15 && dataTRN[dataTRNKeys[i]]<=30){
             td_status.setAttribute("style","background-color:orangered;")
           }
         else{
             td_status.setAttribute("style","background-color:red;")
         }
      }
      if(dataTRNKeys[i]=="KS"){
         if(dataTRN[dataTRNKeys[i]]>25){
           td_status.setAttribute("style","background-color:green;")
         }
         else if(dataTRN[dataTRNKeys[i]]>=15 && dataTRN[dataTRNKeys[i]]<=25){
             td_status.setAttribute("style","background-color:orangered;")
           }
         else{
             td_status.setAttribute("style","background-color:red;")
         }
      }
      if(dataTRNKeys[i]=="RISKRANKING"){
         if(dataTRN[dataTRNKeys[i]]<10){
           td_status.setAttribute("style","background-color:green;")
         }
         else if(dataTRN[dataTRNKeys[i]]>=10 && dataTRN[dataTRNKeys[i]]<=20){
             td_status.setAttribute("style","background-color:orangered;")
           }
         else{
             td_status.setAttribute("style","background-color:red;")
         }
      }
      if(dataTRNKeys[i]=="PSI"){
         if(dataTRN[dataTRNKeys[i]]<10){
           console.log(dataTRN[dataTRNKeys[i]])
           td_status.setAttribute("style","background-color:green;")
         }
         else if(dataTRN[dataTRNKeys[i]]>=10 && dataTRN[dataTRNKeys[i]]<=25){
          console.log("10")
             td_status.setAttribute("style","background-color:orangered;")
           }
         else{
          console.log("less")
             td_status.setAttribute("style","background-color:red;")
         }
      }
      if(dataTRNKeys[i]=="BADRATE"){
         if(dataTRN[dataTRNKeys[i]]<10){
           td_status.setAttribute("style","background-color:green;")
         }
         else if(dataTRN[dataTRNKeys[i]]>=10 && dataTRN[dataTRNKeys[i]]<=30){
             td_status.setAttribute("style","background-color:orangered;")
           }
         else{
             td_status.setAttribute("style","background-color:red;")
         }
      }
     }
     if(name=="Driver"){
      guidelines.innerHTML="<br></br> GINI:>7%:green,5% to 7%:amber,< 5%-Red <br></br> KS:>25% :Green  15% to 25% Moderate <=15% Low <br></br> RISKRANKING:<10% of total bands: Green , 10% to 20% bands : Amber , >20% red  <br></br> PSI:<=10%: Good , 10% to 25%: Amber, >25% :Red <br></br> BADRATE:<10 Good, >=10 to <=30 Amber, >30 Red <br></br> VOI:>30% : Good, 10% to 30%: Amber <10%: Red      "
       if(dataTRNKeys[i]=="GINI"){
          if(dataTRN[dataTRNKeys[i]]>7){
            td_status.setAttribute("style","background-color:green;")
          }
          else if(dataTRN[dataTRNKeys[i]]>=5 && dataTRN[dataTRNKeys[i]]<=7){
              td_status.setAttribute("style","background-color:orangered;")
            }
          else{
              td_status.setAttribute("style","background-color:red;")
          }
       }
       if(dataTRNKeys[i]=="KS"){
          if(dataTRN[dataTRNKeys[i]]>25){
            td_status.setAttribute("style","background-color:green;")
          }
          else if(dataTRN[dataTRNKeys[i]]>=15 && dataTRN[dataTRNKeys[i]]<=25){
              td_status.setAttribute("style","background-color:orangered;")
            }
          else{
              td_status.setAttribute("style","background-color:red;")
          }
       }
       if(dataTRNKeys[i]=="RISKRANKING"){
          if(dataTRN[dataTRNKeys[i]]<10){
            td_status.setAttribute("style","background-color:green;")
          }
          else if(dataTRN[dataTRNKeys[i]]>=10 && dataTRN[dataTRNKeys[i]]<=20){
              td_status.setAttribute("style","background-color:orangered;")
            }
          else{
              td_status.setAttribute("style","background-color:red;")
          }
       }
       if(dataTRNKeys[i]=="PSI"){
        if(dataTRN[dataTRNKeys[i]]<10){
          console.log("less")
          td_status.setAttribute("style","background-color:green;")
        }
        else if(dataTRN[dataTRNKeys[i]]>=10 && dataTRN[dataTRNKeys[i]]<=25){
          console.log("medium")
            td_status.setAttribute("style","background-color:orangered;")
          }
        else{
          console.log("High")
            td_status.setAttribute("style","background-color:red;")
        }
     }
       if(dataTRNKeys[i]=="BADRATE"){
          if(dataTRN[dataTRNKeys[i]]<10){
            td_status.setAttribute("style","background-color:green;")
          }
          else if(dataTRN[dataTRNKeys[i]]>=10 && dataTRN[dataTRNKeys[i]]<=30){
              td_status.setAttribute("style","background-color:orangered;")
            }
          else{
              td_status.setAttribute("style","background-color:red;")
          }
       }
       if(dataTRNKeys[i]=="VOI"){
          if(dataTRN[dataTRNKeys[i]]>30){
            td_status.setAttribute("style","background-color:green;")
          }
          else if(dataTRN[dataTRNKeys[i]]>=10 && dataTRN[dataTRNKeys[i]]<=30){
              td_status.setAttribute("style","background-color:orangered;")
            }
          else{
              td_status.setAttribute("style","background-color:red;")
          }
       } 
      }
    //  if(dataTRNKeys[i]="VOI"){
    //     if(dataTRN[dataTRNKeys[i]]>30){
    //       td_status.setAttribute("style","background-color:green;")
    //     }
    //     else if(dataTRN[dataTRNKeys[i]]>=10 && dataTRN[dataTRNKeys[i]]<=30){
    //         td_status.setAttribute("style","background-color:orangered;")
    //       }
    //     else{
    //         td_status.setAttribute("style","background-color:red;")
    //     }
    //  }
    console.log(dataTRNKeys[i])
    td_trn.textContent = dataTRN[dataTRNKeys[i]]+"%";
    console.log(dataTRN[dataTRNKeys[i]])
    td_oot.textContent=dataOOT[dataOOTKeys[i]]+"%"
    console.log(dataOOT[dataOOTKeys[i]])
	

 //  tr_body.appendChild(td_id);
    tr_body.appendChild(td_name);
	tr_body.appendChild(td_trn);
    tr_body.appendChild(td_oot);
    tr_body.appendChild(td_status)

    tbody.appendChild(tr_body);
   
}
tbl.appendChild(thead);
tbl.appendChild(tbody);
console.log(tbl)
var divContainer = document.getElementById("myContacts");
// divContainer.innerHTML = "";
 divContainer.appendChild(tbl);
}