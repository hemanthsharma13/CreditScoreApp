
function generateDynamicTable(){
let displayName=document.querySelector("#name")
let getName=sessionStorage.getItem("name")
 console.log(getName)
displayName.textContent=getName
let displaymodelData=sessionStorage.getItem("driverInsertedData")
let data=JSON.parse(displaymodelData)
console.log(data)
// let psiTRNData=data.psitrn
// let psiOOTData=data.psioot
let binsData=data.bins
console.log(binsData)
let goodTRNData=data.goodtrn
console.log(goodTRNData)
let badTRNData=data.badtrn
console.log(badTRNData)
let goodOOTData=data.goodoot
console.log(goodOOTData)
let badOOTData=data.badoot
console.log(badOOTData)
let getNooflength=Object.entries(goodTRNData)
let getBins=Object.keys(goodTRNData)
// let getNooflength=Object.entries(psiTRNData)
// console.log(getNooflength)
// let getBins=Object.keys(psiTRNData)
// console.log(getBins)

var tbl = document.createElement('table');
var thead = document.createElement("thead");
var tbody = document.createElement("tbody")

var tr_head = document.createElement("tr");
var th_name = document.createElement("th");
var th_goodtrn = document.createElement("th");
var th_badtrn = document.createElement("th");
var th_goodoot = document.createElement("th");
var th_badoot = document.createElement("th");

th_name.textContent = "BINS";
th_goodtrn.textContent="GOOD TRN";
th_badtrn.textContent="BAD TRN";
th_goodoot.textContent="GOOD OOT";
th_badoot.textContent="BAD OOT"

tr_head.appendChild(th_name);
tr_head.appendChild(th_goodtrn)
tr_head.appendChild(th_badtrn);
tr_head.appendChild(th_goodoot);
tr_head.appendChild(th_badoot);




thead.appendChild(tr_head);

for(var i = 0, j =getNooflength.length; i < j; i++) {
    console.log("for loop is working")
    var tr_body = document.createElement("tr");

  //var td_id = document.createElement("td");
    var td_name = document.createElement("td");
var td_goodtrn = document.createElement("td");
var td_badtrn = document.createElement("td");
var td_goodoot = document.createElement("td");
var td_badoot = document.createElement("td");

   // td_id.textContent = i;
	//Get Object keys values

    td_name.textContent = binsData[getBins[i]];
    console.log(binsData[getBins[i]])
    td_goodtrn.textContent=goodTRNData[getBins[i]]
    console.log(goodTRNData[getBins[i]])
    td_badtrn.textContent=badTRNData[getBins[i]]
    console.log(badTRNData[getBins[i]])
    td_goodoot.textContent=goodOOTData[getBins[i]]
    console.log(goodOOTData[getBins[i]])
    console.log(badOOTData[getBins[i]])
    td_badoot.textContent=badOOTData[getBins[i]]
	

 //  tr_body.appendChild(td_id);
    tr_body.appendChild(td_name);
    tr_body.appendChild(td_goodtrn);
    tr_body.appendChild(td_badtrn);
    tr_body.appendChild(td_goodoot);
    tr_body.appendChild(td_badoot);

    tbody.appendChild(tr_body);
   
}
tbl.appendChild(thead);
tbl.appendChild(tbody);
console.log(tbl)
var divContainer = document.getElementById("myContacts");
// divContainer.innerHTML = "";
 divContainer.appendChild(tbl);
}
