let getUserName=document.querySelector("#uname")
// let  addAddress=document.querySelector("#addAddress");
let uname= sessionStorage.getItem("uname")
let id=0;
let check=uname.indexOf("@")
let display=uname.slice(0,check)
getUserName.textContent='\xa0\xa0\xa0'+ `${display.toUpperCase()}`;

//Add inputs for drivers dynamically
function addDrivers(){
    console.log("working")
    const position="beforeend";
let getDrivers=document.querySelector("#drivers").value;

while(getDrivers>0){
let item= `<div class="mt-4 col-13 d-flex justify-content-center align-items-center"> 
<form action="#" method="POST">
    <div class="d-flex col-11 form-group">
        <input type="text" name="drivername${id}" id="drivername${id}" placeholder="Driver Name" class="form-control col-10 mr-10" autocomplete="off">
        <button type="button" name="${id}" id="${id}" class="ml-5 btn btn-primary .text-white" onclick="addAddress(this.id)">Add Bin</button>
    </div>
    </form>
</div>`

list.insertAdjacentHTML(position,item)
console.log(id)
id++;
getDrivers--;
}    
sessionStorage.setItem("noOfDrivers",id)
}

//Send driver names and path names and get ids
function addAddress(clicked){
console.log("add address is workingss")
let addBinValue=document.getElementById(`${clicked}`).name
console.log(addBinValue)
let driverNameValue=document.getElementById(`drivername${addBinValue}`).value
// let driverPathValue=document.getElementById(`driverpath${addBinValue}`).value
console.log(driverNameValue)
// console.log($("form").serialize())
// let a=$("form").serialize()
// console.log(a)
var url = '/fileDatas?a=' + addBinValue+'&b='+driverNameValue
sessionStorage.setItem("name",driverNameValue)
let getName=sessionStorage.getItem("name")
console.log(getName)
let xhr=new XMLHttpRequest();
xhr.onreadystatechange=function(){
if(xhr.readyState==4 && xhr.status==200){
console.log("inside address is working")
console.log('responseText:' + xhr.responseText)
if(xhr.responseText){
 let data=xhr.responseText
sessionStorage.setItem(`${driverNameValue}`,data)
let getDriverId=sessionStorage.getItem(`${driverNameValue}`)
let getDriverIds=JSON.parse(getDriverId)
sessionStorage.setItem("driverInsertedData",data)
console.log(getDriverId)
console.log(getDriverIds.status.goodtrnid)
window.open('/index3','popup','width=700,height=600'); 
// console.log(getDriverIds.status)
// console.log(getDriverIds.goodootid)
console.log("it is working")
}
else{
console.log("it is not greater")
}
}
};
xhr.open("GET",url,true)
xhr.send();

}

//Next Page
function nextPage(){

let noOfDrivers= sessionStorage.getItem("noOfDrivers")
console.log(noOfDrivers)
let getDrivers=document.querySelector("#drivers").value;
console.log(getDrivers)
//   let get=document.querySelector(`#drivers`.value)
//   console.log(get)
if(getDrivers>0){
while(noOfDrivers>0){
    
sessionStorage.setItem(`driverName${noOfDrivers-1}`,document.querySelector(`#drivername${noOfDrivers-1}`).value)
alert(document.querySelector(`#drivername${noOfDrivers-1}`).value)
noOfDrivers--;

}
window.location="/index2"
}
else{
window.location="/index2"
}
}
//Upload Model Data
$(function() {
console.log("working")
$('#upload').click(function() {
    console.log("Button is working")
var form_data = new FormData($('#upload-file')[0]);
var modelName=document.querySelector("#insertedModelName").value
console.log(modelName)
sessionStorage.setItem("insertedModelName",modelName)
sessionStorage.setItem("name",modelName)
let getName=sessionStorage.getItem("name")
console.log(getName)
console.log(form_data)
$.ajax({
url: '/fileData',
data: form_data,
type: 'POST',
contentType: false,
            cache: false,
            processData: false,
success: function(response) {
    var data=response
    sessionStorage.setItem("modelId",data)
    sessionStorage.setItem("driverInsertedData",data)
    console.log(data)
    window.open('/index3','popup','width=700,height=600'); 
    console.log(response)
    console.log(data.status);
},
error: function(error) {
    console.log(error);
}
});
});
});
//Logout function
let logout=document.querySelector("#logout")
logout.addEventListener("click",function(){
sessionStorage.clear()
window.location.reload(true);
window.location.replace('/');
})

