
#HTML for the webpage


HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">
<title>Choppy Beeps</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:sans-serif;background:#111;color:#fff;min-height:100vh}
.screen{display:none;min-height:100vh;padding:20px;flex-direction:column;align-items:center}
.screen.active{display:flex}
h1{font-size:24px;margin:20px 0}
.grid{display:flex;flex-direction:column;gap:10px;width:90%;flex:1;padding-bottom:20px}
.card{flex:1;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:18px;font-weight:bold;min-height:80px}
.card:active{transform:scale(0.97)}
.druid{background:#ff2d9b}
.tank{background:#f5a500}
.wraith{background:#cc0000}
.oracle{background:#ffffff;color:#111}
.info-box{width:80%;aspect-ratio:1;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:48px;margin-top:30px}
.info-text{text-align:center;margin:30px 0}
.info-text h2{font-size:24px;margin-bottom:15px}
.info-text p{color:#aaa;line-height:1.8}
.btns{display:flex;gap:15px;margin-top:auto;padding-bottom:30px}
.btn{padding:15px 25px;border:none;border-radius:8px;font-size:14px;font-weight:bold}
.back{background:#444;color:#fff}
.play{background:#4a4;color:#fff}
.playing-box{width:90%;aspect-ratio:1;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:64px;animation:pulse 2s infinite}
@keyframes pulse{0%,100%{transform:scale(1)}50%{transform:scale(1.05)}}
.result{font-size:28px;text-align:center}
.win{color:#4f4}
.lose{color:#f44}
</style>
</head>
<body>

<div id="s1" class="screen active">
<h1>Choppy Beeps</h1>
<div class="grid">
<div class="card druid" onclick="info('druid')">DRUID</div>
<div class="card tank" onclick="info('tank')">TANK</div>
<div class="card wraith" onclick="info('wraith')">WRAITH</div>
<div class="card oracle" onclick="info('oracle')">ORACLE</div>
</div>
</div>

<div id="s2" class="screen">
<div id="ibox" class="info-box">?</div>
<div class="info-text">
<h2 id="iname">NAME</h2>
<p id="idesc">Desc</p>
</div>
<div class="btns">
<button class="btn back" onclick="back()">BACK</button>
<button class="btn play" onclick="play()">PLAY</button>
</div>
</div>

<div id="s3" class="screen">
<div id="pbox" class="playing-box">⚔</div>
<p style="margin-top:20px;color:#aaa">Playing...</p>
</div>

<div id="s4" class="screen">
<h1 class="result win">VICTORY!</h1>
<p style="margin-top:15px;color:#8f8">You won!</p>
</div>

<div id="s5" class="screen">
<h1 class="result lose">DEFEAT</h1>
<p style="margin-top:15px;color:#f88">AI wins</p>
</div>

<script>
var cur='druid';
var data={
druid:{c:'#ff2d9b',t:'#fff',i:'🌿',d:'Difficulty: 1<br>Bloodlust: Low<br>Standard rules'},
tank:{c:'#f5a500',t:'#fff',i:'🛡',d:'Difficulty: 2<br>Bloodlust: Medium<br>Needs 6 points on a hand to die'},
wraith:{c:'#cc0000',t:'#fff',i:'👻',d:'Difficulty: 3<br>Bloodlust: High<br>Can revive both hands once'},
oracle:{c:'#ffffff',t:'#111',i:'🔮',d:'Difficulty: ???<br>Bloodlust: High<br>-//I CAN SEE YOU//'}
};

function show(n){
document.querySelectorAll('.screen').forEach(function(s){s.classList.remove('active')});
document.getElementById('s'+n).classList.add('active');
}

function back(){show(1)}

function info(c){
cur=c;
var d=data[c];
var ibox=document.getElementById('ibox');
ibox.style.background=d.c;
ibox.style.color=d.t;
ibox.textContent=d.i;
document.getElementById('iname').textContent=c.toUpperCase();
document.getElementById('idesc').innerHTML=d.d;
show(2);
}

function play(){
var d=data[cur];
var pbox=document.getElementById('pbox');
pbox.style.background=d.c;
pbox.style.color=d.t;
pbox.textContent=d.i;
show(3);
fetch('/?m='+cur);
}

function check(){
fetch('/?status=1')
.then(function(r){return r.text()})
.then(function(t){
if(t.includes('win')){show(4);setTimeout(back,4000)}
else if(t.includes('lose')){show(5);setTimeout(back,4000)}
})
.catch(function(){});
}

setInterval(check,2000);
</script>

</body>
</html>
"""
