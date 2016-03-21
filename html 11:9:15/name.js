<h3><p id="name" style="position: absolute; bottom: 0px;"></p></h3>
<script>
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

function checkCookie() {
    var user = getCookie("username");
    if (user != "") {
        document.getElementById("name").innerHTML =
        "::browsing as " + user + "::";
    } else {
        user = prompt("Sign in to confirm ESCIRC membership to access this protected resource. \n\n Do not put Darty Jackson.","");
        user = user.toLowerCase();
        if (user != "" && user != null) {
            setCookie("username", user, 365);
        }
    }
}
</script>