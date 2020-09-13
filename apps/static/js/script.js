function login()
{
   
 var uname = document.querySelector("#email").value;
var pwd = document.querySelector("#pwd1").value;
    var displayIncorrect=document.querySelector("#incorrect");
  //  var filter = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
      var user1="nikhilkumar@gmail.com"
      var user2="nikhil@gmail.com"
      var user3="kumar@gmail.com"
      var user4="thota@gmail.com"
      var password="123456789"
     if(uname==user1 || uname==user2 || uname==user3 || uname==user4)
    {
      if(pwd!==password)
    {
       displayIncorrect.textContent=`Incorrect Password`
    }
    else
    {
          window.location="/index1";
        }
    }
    else{
      displayIncorrect.textContent="Username Not valid";
    }
        sessionStorage.setItem("uname",uname)

}