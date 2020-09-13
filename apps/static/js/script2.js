console.log("new script is working")
let getUserName=document.querySelector("#uname") //Get the tag of username
let uname= sessionStorage.getItem("uname") //Get the username of logged User
let giniButton=document.querySelector("#giniModel") //Get the giniButton
let ksModelButton=document.querySelector("#ksModel") //Get the ksModelButton
let riskRankingButton=document.querySelector("#riskRankingModel") //Get the riskRankingModelButton
let psiButton=document.querySelector("#psiModel") //Get the psiModelButton
let badRateButton=document.querySelector("#badRateModel") //Get the badRateModelButton
let modelSummary=document.querySelector("#modelSummary")
let driverGiniButton=document.querySelector("#giniDriver")
let driverKsButton=document.querySelector("#ksDriver")
let driverRiskButton=document.querySelector("#riskRankingDriver")
let driverPsiButton=document.querySelector("#psiDriver")
let driverBadRateButton=document.querySelector("#badRateDriver")
let voiDriver=document.querySelector("#voiDriver")
let driverSummary=document.querySelector("#driverSummary")
let podModel=document.querySelector("#pod")
let giniDrivers=sessionStorage.getItem("noOfDrivers")
let ksDrivers=sessionStorage.getItem("noOfDrivers")
let riskDrivers=sessionStorage.getItem("noOfDrivers")
let psiDrivers=sessionStorage.getItem("noOfDrivers")
let badDrivers=sessionStorage.getItem("noOfDrivers")
let voiDrivers=sessionStorage.getItem("noOfDrivers")
let summaryDrivers=sessionStorage.getItem("noOfDrivers")
   let check=uname.indexOf("@")
   let display=uname.slice(0,check)
   getUserName.textContent='\xa0\xa0\xa0'+ `${display.toUpperCase()}`;

//Get the giniValue
giniButton.addEventListener("click",function(){
   let getmodelIds=sessionStorage.getItem("modelId")
   let getmodelId=JSON.parse(getmodelIds)
   let url='/api/gini?a='+getmodelId.status.goodtrnid+'&b='+getmodelId.status.badtrnid+'&c='+getmodelId.status.goodootid+'&d='+getmodelId.status.badootid+'&e='+getmodelId.status.binsid   
   console.log(url)
   console.log("the gini button is working")
   let name="Model"
   let fileName="ModelGini"
   let getModelName=sessionStorage.getItem("insertedModelName")
   sessionStorage.setItem("currentDisplayedData",getModelName)
   sessionStorage.setItem("fileName",fileName)
   sessionStorage.setItem("modelOrDriver",name)
   let xhr=new XMLHttpRequest();
   xhr.onreadystatechange=function(){
      if(xhr.readyState==4 && xhr.status==200){
      //   console.log()
         console.log("inside gini is working")
         let data =xhr.responseText;
         let dataName="GINI"
         let convertData=JSON.parse(data)
         console.log(convertData)
         // let giniData=Object.entries(data)
         sessionStorage.setItem("dataName",dataName);
         sessionStorage.setItem("modelData",data);
         let getModelData=sessionStorage.getItem("modelData")
         console.log(getModelData)
      //   let giniModelData=sessionStorage.getItem("giniData")
       //  console.log(giniModelData)
         console.log('responseText:' + data)
         if(xhr.responseText){
            window.open('/index5','popup','width=700,height=600'); 
         }
         else{
            console.log("it is not greater")
         }
      }
   };
   xhr.open("GET",url,true)
   xhr.send();
})

//Get the ksValue
ksModelButton.addEventListener("click",function(){
   let getmodelIds=sessionStorage.getItem("modelId")
   let getmodelId=JSON.parse(getmodelIds)
   let url='/api/ks?a='+getmodelId.status.goodtrnid+'&b='+getmodelId.status.badtrnid+'&c='+getmodelId.status.goodootid+'&d='+getmodelId.status.badootid+'&e='+getmodelId.status.binsid
   let name="Model"
   sessionStorage.setItem("modelOrDriver",name)
   let fileName="ModelKs"
   sessionStorage.setItem("fileName",fileName)
   let getModelName=sessionStorage.getItem("insertedModelName")
   sessionStorage.setItem("currentDisplayedData",getModelName)
   let xhr=new XMLHttpRequest();
   xhr.onreadystatechange=function(){
      if(xhr.readyState==4 && xhr.status==200){
         let data =xhr.responseText;
         let dataName="KS"
         let convertData=JSON.parse(data)
         console.log(convertData)
         sessionStorage.setItem("dataName",dataName);
         sessionStorage.setItem("modelData",data);
       //  let giniModelData=sessionStorage.getItem("ksData")
               console.log('responseText:' + data)
         console.log("inside ks is working")
         console.log('responseText:' + xhr.responseText)
         if(xhr.responseText){
            window.open('/index5','popup','width=700,height=600'); 
         }
         else{
            console.log("it is not greater")
         }
      }
   };
   xhr.open("GET",url,true)
   xhr.send();
})

//Get the riskRankingValue
riskRankingButton.addEventListener("click",function(){
   let getmodelIds=sessionStorage.getItem("modelId")
   let getmodelId=JSON.parse(getmodelIds)
   let url='/api/risk?a='+getmodelId.status.goodtrnid+'&b='+getmodelId.status.badtrnid+'&c='+getmodelId.status.goodootid+'&d='+getmodelId.status.badootid+'&e='+getmodelId.status.binsid
   let name="Model"
   sessionStorage.setItem("modelOrDriver",name)
   let fileName="ModelRiskRanking"
   sessionStorage.setItem("fileName",fileName)
   let getModelName=sessionStorage.getItem("insertedModelName")
   sessionStorage.setItem("currentDisplayedData",getModelName)
   let xhr=new XMLHttpRequest();
   xhr.onreadystatechange=function(){
      if(xhr.readyState==4 && xhr.status==200){
         let data =xhr.responseText;
         let dataName="RISKRANKING"
         let convertData=JSON.parse(data)
         console.log(convertData)
         // let giniData=Object.entries(data)
         sessionStorage.setItem("dataName",dataName);
         sessionStorage.setItem("modelData",data);
     //    let giniModelData=sessionStorage.getItem("riskRankingData")
                  console.log('responseText:' + data)
         console.log('responseText:' + xhr.responseText)
         if(xhr.responseText){
            window.open('/index5','popup','width=700,height=600'); 
         }
         else{
            console.log("it is not greater")
         }
      }
   };
   xhr.open("GET",url,true)
   xhr.send();
})

//Get the psiModelValue
psiButton.addEventListener("click",function(){
   let getmodelIds=sessionStorage.getItem("modelId")
   let getmodelId=JSON.parse(getmodelIds)
   let url='/api/psi?a='+getmodelId.status.psitrnid+'&b='+getmodelId.status.psiootid+'&e='+getmodelId.status.binsid
   console.log(url)
   let name="Model"
   sessionStorage.setItem("modelOrDriver",name)
   let fileName="ModelPsi"
   sessionStorage.setItem("fileName",fileName)
   let getModelName=sessionStorage.getItem("insertedModelName")
   sessionStorage.setItem("currentDisplayedData",getModelName)
   let xhr=new XMLHttpRequest();
   xhr.onreadystatechange=function(){
      if(xhr.readyState==4 && xhr.status==200){
         console.log("inside bad rate is working")
         let data =xhr.responseText;
         let dataName="PSI"
   sessionStorage.setItem("dataName",dataName);
        // let convertData=JSON.parse(data)
       //  console.log(convertData)
         // let giniData=Object.entries(data)
         console.log(dataName)
         sessionStorage.setItem("modelData",data);
        // let giniModelData=sessionStorage.getItem("badRateData")
               console.log('responseText:' + data)
      
       //  console.log('responseText:' + xhr.responseText)
         if(xhr.responseText){
            window.open('/index5','popup','width=700,height=600'); 
         }
         else{
            console.log("it is not greater")
         }
      }
   };
   xhr.open("GET",url,true)
   xhr.send();
  
   
})

//Get the badRateModelValue
badRateButton.addEventListener("click",function(){
   console.log("inside badRateButton is clicked")
   let getmodelIds=sessionStorage.getItem("modelId")
   let getmodelId=JSON.parse(getmodelIds)
   let url='/api/bad?a='+getmodelId.status.goodtrnid+'&b='+getmodelId.status.badtrnid+'&c='+getmodelId.status.goodootid+'&d='+getmodelId.status.badootid+'&e='+getmodelId.status.binsid
   console.log(url)
   let name="Model"
   sessionStorage.setItem("modelOrDriver",name)
   let fileName="ModelBadRate"
   sessionStorage.setItem("fileName",fileName)
   let getModelName=sessionStorage.getItem("insertedModelName")
   sessionStorage.setItem("currentDisplayedData",getModelName)
   let xhr=new XMLHttpRequest();
   xhr.onreadystatechange=function(){
      if(xhr.readyState==4 && xhr.status==200){
         console.log("inside bad rate is working")
         let data =xhr.responseText;
         let dataName="BADRATE";
        // let convertData=JSON.parse(data)
       //  console.log(convertData)
         // let giniData=Object.entries(data)
         sessionStorage.setItem("dataName",dataName);
         console.log(dataName)
         sessionStorage.setItem("modelData",data);
        // let giniModelData=sessionStorage.getItem("badRateData")
               console.log('responseText:' + data)
      
       //  console.log('responseText:' + xhr.responseText)
         if(xhr.responseText){
            window.open('/index5','popup','width=700,height=600'); 
         }
         else{
            console.log("it is not greater")
         }
      }
   };
   xhr.open("GET",url,true)
   xhr.send();
})

//Get the summary of model
modelSummary.addEventListener("click",function(){
   let xhr=new XMLHttpRequest();
   let getmodelIds=sessionStorage.getItem("modelId")
   let getmodelId=JSON.parse(getmodelIds)
   let url='/api/modelsummary?a='+getmodelId.status.goodtrnid+'&b='+getmodelId.status.badtrnid+'&c='+getmodelId.status.goodootid+'&d='+getmodelId.status.badootid+'&e='+getmodelId.status.psitrnid+'&f='+getmodelId.status.psiootid+'&g='+getmodelId.status.binsid
   let name="Model"
   sessionStorage.setItem("modelOrDriver",name)
   let fileName="ModelSummary"
   sessionStorage.setItem("fileName",fileName)
   console.log(url)
   let getModelName=sessionStorage.getItem("insertedModelName")
   sessionStorage.setItem("currentDisplayedData",getModelName)
   xhr.onreadystatechange=function(){
      if(xhr.readyState==4 && xhr.status==200){
         console.log("inside bad rate is working")
         let data =xhr.responseText;
         let dataName="MODELSUMMARY"
                 // let convertData=JSON.parse(data)
       //  console.log(convertData)
         // let giniData=Object.entries(data)
         sessionStorage.setItem("dataName",dataName);
         sessionStorage.setItem("modelData",data);
        // let giniModelData=sessionStorage.getItem("badRateData")
               console.log('responseText:' + data)
      
       //  console.log('responseText:' + xhr.responseText)
         if(xhr.responseText){
            window.open('/index4','popup','width=700,height=600'); 
         }
         else{
            console.log("it is not greater")
         }
      }
   };
   xhr.open("GET",url,true)
   xhr.send();
})

//Get the driverGini Values
driverGiniButton.addEventListener("click",function(){
   let adjustCol=document.querySelector("#adjustCol")
   adjustCol.setAttribute("class","col-7 d-flex justify-content-around")

   let list=document.querySelector("#list")
   const position="beforeend";
   let id=0
   while(giniDrivers>0){
      let getDriverName=sessionStorage.getItem(`driverName${id}`)
      let item= `<div class="col-13 d-flex justify-content-around ">
            <button onclick="displayDriverGiniData(this.id)" name="${getDriverName}" id="${getDriverName}" class="btn btn-outline-light d-inline-block" style="width: 150px;">${getDriverName}</button>
        </div>`
      list.insertAdjacentHTML(position,item)
      id++
      giniDrivers--;
  }
})

function displayDriverGiniData(clicked){
   console.log("the driverGini button is working")
   let getDriverNameValue=document.getElementById(`${clicked}`).name
   let getDriverIds=sessionStorage.getItem(`${getDriverNameValue}`)
   let getDriverId=JSON.parse(getDriverIds)
   let url='/api/gini?a='+getDriverId.status.goodtrnid+'&b='+getDriverId.status.badtrnid+'&c='+getDriverId.status.goodootid+'&d='+getDriverId.status.badootid+'&e='+getDriverId.status.binsid
   console.log(url)
   let name="Driver"
   sessionStorage.setItem("modelOrDriver",name)
   let fileName= getDriverNameValue+"Gini"
   sessionStorage.setItem("fileName",fileName)
   let xhr=new XMLHttpRequest();
   sessionStorage.setItem("currentDisplayedData",getDriverNameValue)
   xhr.onreadystatechange=function(){
      if(xhr.readyState==4 && xhr.status==200){
         console.log("inside gini is working")
         let data =xhr.responseText;
         let dataName="GINI"
         sessionStorage.setItem("dataName",dataName);
         sessionStorage.setItem("modelData",data);
         console.log('responseText:' + data)
         if(xhr.responseText){
            window.open('/index5','popup','width=700,height=600'); 
         }
         else{
            console.log("it is not greater")
         }
      }
   };
   xhr.open("GET",url,true)
   xhr.send();
}

//Get the driverKs Values
driverKsButton.addEventListener("click",function(){
   let list=document.querySelector("#list1")
   const position="beforeend";
   let id=0
   while(ksDrivers>0){
      let getDriverName=sessionStorage.getItem(`driverName${id}`)
      let item= `<div class="col-13 d-flex justify-content-around ">
            <button onclick="displayDriverKsData(this.id)" name="${getDriverName}" id="${getDriverName}" class="btn btn-outline-light d-inline-block" style="width: 150px;">${getDriverName}</button>
        </div>`
      list.insertAdjacentHTML(position,item)
      id++
      ksDrivers--;
  }
})

function displayDriverKsData(clicked){
 console.log("the driverKs button is working")
 let getDriverNameValue=document.getElementById(`${clicked}`).name
   let getDriverIds=sessionStorage.getItem(`${getDriverNameValue}`)
   let getDriverId=JSON.parse(getDriverIds)
   let url='/api/ks?a='+getDriverId.status.goodtrnid+'&b='+getDriverId.status.badtrnid+'&c='+getDriverId.status.goodootid+'&d='+getDriverId.status.badootid+'&e='+getDriverId.status.binsid
   console.log(url)
   let name="Driver"
   sessionStorage.setItem("modelOrDriver",name)
   let fileName= getDriverNameValue+"Ks"
   sessionStorage.setItem("fileName",fileName)
   sessionStorage.setItem("currentDisplayedData",getDriverNameValue)
   let xhr=new XMLHttpRequest();
   xhr.onreadystatechange=function(){
      if(xhr.readyState==4 && xhr.status==200){
         console.log("inside ks is working")
         let data =xhr.responseText;
         let dataName="KS"
         sessionStorage.setItem("dataName",dataName);
         sessionStorage.setItem("modelData",data);
         console.log('responseText:' + data)
         if(xhr.responseText){
            window.open('/index5','popup','width=700,height=600'); 
         }
         else{
            console.log("it is not greater")
         }
      }
   };
   xhr.open("GET",url,true)
   xhr.send();
}

//Get the driverRisk Values
driverRiskButton.addEventListener("click",function(){
   let list=document.querySelector("#list2")
   const position="beforeend";
   let id=0
   while(riskDrivers>0){
      let getDriverName=sessionStorage.getItem(`driverName${id}`)
      let item= `<div class="col-13 d-flex justify-content-around ">
            <button onclick="displayDriverRiskRankingData(this.id)" name="${getDriverName}" id="${getDriverName}" class="btn btn-outline-light d-inline-block" style="width: 150px;">${getDriverName}</button>
        </div>`
      list.insertAdjacentHTML(position,item)
      id++
      riskDrivers--;
  }
})

function displayDriverRiskRankingData(clicked){
console.log("the driverRisk button is working")
let getDriverNameValue=document.getElementById(`${clicked}`).name
   let getDriverIds=sessionStorage.getItem(`${getDriverNameValue}`)
   let getDriverId=JSON.parse(getDriverIds)
   let url='/api/risk?a='+getDriverId.status.goodtrnid+'&b='+getDriverId.status.badtrnid+'&c='+getDriverId.status.goodootid+'&d='+getDriverId.status.badootid+'&e='+getDriverId.status.binsid
   console.log(url)
   let name="Driver"
   sessionStorage.setItem("modelOrDriver",name)
   let fileName= getDriverNameValue+"RiskRanking"
   sessionStorage.setItem("fileName",fileName)
   sessionStorage.setItem("currentDisplayedData",getDriverNameValue)
   let xhr=new XMLHttpRequest();
   xhr.onreadystatechange=function(){
      if(xhr.readyState==4 && xhr.status==200){
         console.log("inside risk is working")
         let data =xhr.responseText;
         let dataName="RISKRANKING"
         sessionStorage.setItem("dataName",dataName);
         sessionStorage.setItem("modelData",data);
         console.log('responseText:' + data)
         if(xhr.responseText){
            window.open('/index5','popup','width=700,height=600'); 
         }
         else{
            console.log("it is not greater")
         }
      }
   };
   xhr.open("GET",url,true)
   xhr.send();
}

//Get the driverPsi Values
driverPsiButton.addEventListener("click",function(){
   let list=document.querySelector("#list3")
   const position="beforeend";
   let id=0
   while(psiDrivers>0){
      let getDriverName=sessionStorage.getItem(`driverName${id}`)
      let item= `<div class="col-13 d-flex justify-content-around ">
            <button onclick="displayDriverPsiData(this.id)" name="${getDriverName}" id="${getDriverName}" class="btn btn-outline-light d-inline-block" style="width: 150px;">${getDriverName}</button>
        </div>`
      list.insertAdjacentHTML(position,item)
      id++
      psiDrivers--;
  }
})

function displayDriverPsiData(clicked){
console.log("the driverPsi button is working")
let getDriverNameValue=document.getElementById(`${clicked}`).name
   let getDriverIds=sessionStorage.getItem(`${getDriverNameValue}`)
   let getDriverId=JSON.parse(getDriverIds)
   let url='/api/psi?a='+getDriverId.status.psitrnid+'&b='+getDriverId.status.psiootid+'&e='+getDriverId.status.binsid
   console.log(url)
   let name="Driver"
   sessionStorage.setItem("modelOrDriver",name)
   let fileName= getDriverNameValue+"Psi"
   sessionStorage.setItem("fileName",fileName)
   sessionStorage.setItem("currentDisplayedData",getDriverNameValue)
   let xhr=new XMLHttpRequest();
   xhr.onreadystatechange=function(){
      if(xhr.readyState==4 && xhr.status==200){
         console.log("inside psi is working")
         let data =xhr.responseText;
         let dataName="PSI"
         sessionStorage.setItem("dataName",dataName);
         sessionStorage.setItem("modelData",data);
         console.log('responseText:' + data)
         if(xhr.responseText){
            window.open('/index5','popup','width=700,height=600'); 
         }
         else{
            console.log("it is not greater")
         }
      }
   };
   xhr.open("GET",url,true)
   xhr.send();
}

//Get the driverBadRate Values
driverBadRateButton.addEventListener("click",function(){
   let list=document.querySelector("#list4")
   const position="beforeend";
   let id=0
   while(badDrivers>0){
      let getDriverName=sessionStorage.getItem(`driverName${id}`)
      let item= `<div class="col-13 d-flex justify-content-around ">
            <button onclick="displayDriverBadRateData(this.id)" name="${getDriverName}" id="${getDriverName}" class="btn btn-outline-light d-inline-block" style="width: 150px;">${getDriverName}</button>
        </div>`
      list.insertAdjacentHTML(position,item)
      id++
      badDrivers--;
  }
})

function displayDriverBadRateData(clicked){
 console.log("the driverBadRate button is working")
 let getDriverNameValue=document.getElementById(`${clicked}`).name
   let getDriverIds=sessionStorage.getItem(`${getDriverNameValue}`)
   let getDriverId=JSON.parse(getDriverIds)
   let url='/api/bad?a='+getDriverId.status.goodtrnid+'&b='+getDriverId.status.badtrnid+'&c='+getDriverId.status.goodootid+'&d='+getDriverId.status.badootid+'&e='+getDriverId.status.binsid
   let name="Driver"
   sessionStorage.setItem("modelOrDriver",name)
   let fileName= getDriverNameValue+"BadRate"
   sessionStorage.setItem("fileName",fileName)
   sessionStorage.setItem("currentDisplayedData",getDriverNameValue)
   let xhr=new XMLHttpRequest();
   xhr.onreadystatechange=function(){
      if(xhr.readyState==4 && xhr.status==200){
         console.log("inside badRate is working")
         let data =xhr.responseText;
         let dataName="BADRATE"
         sessionStorage.setItem("dataName",dataName);
         sessionStorage.setItem("modelData",data);
         console.log('responseText:' + data)
         if(xhr.responseText){
            window.open('/index5','popup','width=700,height=600'); 
         }
         else{
            console.log("it is not greater")
         }
      }
   };
   xhr.open("GET",url,true)
   xhr.send();
}

//Get the voi values
voiDriver.addEventListener("click",function(){
   let list=document.querySelector("#list5")
   const position="beforeend";
   let id=0
   while(voiDrivers>0){
      let getDriverName=sessionStorage.getItem(`driverName${id}`)
      let item= `<div class="col-13 d-flex justify-content-around ">
            <button onclick="displayDriverVoiData(this.id)" name="${getDriverName}" id="${getDriverName}" class="btn btn-outline-light d-inline-block" style="width: 150px;">${getDriverName}</button>
        </div>`
      list.insertAdjacentHTML(position,item)
      id++
      voiDrivers--;
  }
})

function displayDriverVoiData(clicked){
 console.log("the voiDriver is working")
 let getDriverNameValue=document.getElementById(`${clicked}`).name
   let getDriverIds=sessionStorage.getItem(`${getDriverNameValue}`)
   let getDriverId=JSON.parse(getDriverIds)
   let url='/api/voi?a='+getDriverId.status.goodtrnid+'&b='+getDriverId.status.badtrnid+'&c='+getDriverId.status.goodootid+'&d='+getDriverId.status.badootid+'&e='+getDriverId.status.binsid
   console.log(url)
   let name="Driver"
   sessionStorage.setItem("modelOrDriver",name)
   let fileName= getDriverNameValue+"Voi"
   sessionStorage.setItem("fileName",fileName)
   sessionStorage.setItem("currentDisplayedData",getDriverNameValue)
   let xhr=new XMLHttpRequest();
   xhr.onreadystatechange=function(){
      if(xhr.readyState==4 && xhr.status==200){
         console.log("inside voi is working")
         let data =xhr.responseText;
         let dataName="VOI"
         sessionStorage.setItem("dataName",dataName);
         sessionStorage.setItem("modelData",data);
         console.log('responseText:' + data)
         if(xhr.responseText){
            window.open('/index5','popup','width=700,height=600'); 
         }
         else{
            console.log("it is not greater")
         }
      }
   };
   xhr.open("GET",url,true)
   xhr.send();
}

driverSummary.addEventListener("click",function(){
   let list=document.querySelector("#list6")
   const position="beforeend";
   let id=0
   while(summaryDrivers>0){
      let getDriverName=sessionStorage.getItem(`driverName${id}`)
      let item= `<div class="col-13 d-flex justify-content-around ">
            <button onclick="displayDriverSummaryData(this.id)" name="${getDriverName}" id="${getDriverName}" class="btn btn-outline-light d-inline-block" style="width: 150px;">${getDriverName}</button>
        </div>`
      list.insertAdjacentHTML(position,item)
      id++
      summaryDrivers--;
  }
})

function displayDriverSummaryData(clicked){
   console.log("the driverSummary button is working")
   let getDriverNameValue=document.getElementById(`${clicked}`).name
   let getDriverIds=sessionStorage.getItem(`${getDriverNameValue}`)
   let getDriverId=JSON.parse(getDriverIds)
   let url='/api/driversummary?a='+getDriverId.status.goodtrnid+'&b='+getDriverId.status.badtrnid+'&c='+getDriverId.status.goodootid+'&d='+getDriverId.status.badootid+'&e='+getDriverId.status.psitrnid+'&f='+getDriverId.status.psiootid+'&g='+getDriverId.status.binsid
   let name="Driver"
   sessionStorage.setItem("modelOrDriver",name)
   let fileName= getDriverNameValue+"Summary"
   sessionStorage.setItem("fileName",fileName)
   sessionStorage.setItem("currentDisplayedData",getDriverNameValue)
   let xhr=new XMLHttpRequest();
   xhr.onreadystatechange=function(){
      if(xhr.readyState==4 && xhr.status==200){
         console.log("inside summary is working")
         let data =xhr.responseText;
         let dataName="SUMMARY"
         sessionStorage.setItem("dataName",dataName);
         sessionStorage.setItem("modelData",data);
         console.log('responseText:' + data)
         if(xhr.responseText){
            window.open('/index4','popup','width=700,height=600'); 
         }
         else{
            console.log("it is not greater")
         }
      }
   };
   xhr.open("GET",url,true)
   xhr.send();
}

podModel.addEventListener("click",function(){
   let name="PDO"
   let xhr=new XMLHttpRequest();
   xhr.onreadystatechange=function(){
      if(xhr.readyState==4 && xhr.status==200){
      //   console.log()
         console.log("inside gini is working")
         let data =xhr.responseText;
         let dataName="PDO"
         let convertData=JSON.parse(data)
         console.log(convertData)
         // let giniData=Object.entries(data)
         sessionStorage.setItem("dataName",dataName);
         sessionStorage.setItem("modelData",data);
         let getModelData=sessionStorage.getItem("modelData")
         console.log(getModelData)
      //   let giniModelData=sessionStorage.getItem("giniData")
       //  console.log(giniModelData)
         console.log('responseText:' + data)
         if(xhr.responseText){
            window.open('/index6','popup','width=700,height=600'); 
         }
         else{
            console.log("it is not greater")
         }
      }
   };
   xhr.open("GET","/api/pdo",true)
   xhr.send();
})

let logout=document.querySelector("#logout")
logout.addEventListener("click",function(){
    sessionStorage.clear()
    window.location.reload(true);
  window.location.replace('/');
})

