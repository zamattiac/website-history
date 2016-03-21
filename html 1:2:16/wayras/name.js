function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires="+d.toUTCString();
    document.cookie = cname + "=" + cvalue + "; " + expires;
}

function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i=0; i<ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1);
        if (c.indexOf(name) == 0) return c.substring(name.length, c.length);
    }
    return "";
}

//function checkCookie() {
//
//    var language = getCookie("language");
//
//
//    if (language != "") {
//        document.getElementById("name").innerHTML = "::browsing as " + user.toLowerCase() + "::";
//
//    }
//
//    else if (user === ""){
//        user = prompt("Enter compID to access this resource","mak2vr");
//        if (user === null){
//        window.history.back();
//        }
//        user = user.toLowerCase();
//
//        if (!checkCompID(user)) {
//            window.history.back();
//            setCookie("username","",1);
//        }
//
//        else {
//        setCookie("username",user,40);
//        document.location.reload(true);
//        }
//    }
//
//
//
//}
