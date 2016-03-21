string = """<a href="#jokes"></a></div>
                <div><a href="#events"></a></div>
                <div><a href="#names"></a></div>
                <div><a href="#discussion"></a></div>
                <div><a href="poop.html"></a></div>
                <div><a href="irc.html"></a></div>
                <div><a href="jrcirc.html"></a></div>
"""
print(string.replace("<div>","").replace("</div>","<br>"))