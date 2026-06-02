// Lógica para Torres de Hanoi
const pegs = { A: [], B: [], C: [] };
let nDiscos = 4;
let movesCount = 0;
let selected = null;
let animating = false;
let moveSequence = [];

function $(s){return document.querySelector(s)}
function $all(s){return Array.from(document.querySelectorAll(s))}

function init(){
	nDiscos = Math.max(1, Math.min(10, parseInt($('#numDiscos').value)||4));
	pegs.A = [];
	pegs.B = [];
	pegs.C = [];
	for(let i=nDiscos;i>=1;i--) pegs.A.push(i);
	movesCount = 0;
	selected = null;
	animating = false;
	moveSequence = [];
	render();
}

function render(){
	$('#moves').textContent = `Movimientos: ${movesCount}`;
	$all('.peg').forEach(p=>{
		const name = p.dataset.peg;
		const stack = p.querySelector('.stack');
		stack.innerHTML = '';
		pegs[name].forEach((size, idx)=>{
			const d = document.createElement('div');
			d.className = 'disk';
			const w = 30 + (size / nDiscos) * 60; // porcentaje ancho
			d.style.width = w + '%';
			d.style.background = `hsl(${size*30 % 360} 60% 40%)`;
			d.textContent = size;
			stack.appendChild(d);
		})
		p.classList.toggle('selected', selected===name);
	})
}

function canMove(from, to){
	const f = pegs[from];
	const t = pegs[to];
	if(f.length===0) return false;
	const disk = f[f.length-1];
	if(t.length===0) return true;
	return disk < t[t.length-1];
}

function move(from, to){
	if(!canMove(from,to)) return false;
	const disk = pegs[from].pop();
	pegs[to].push(disk);
	movesCount++;
	render();
	checkWin();
	return true;
}

function checkWin(){
	if(pegs.C.length === nDiscos){
		setTimeout(()=>alert('¡Ganaste!'),10);
	}
}

function handlePegClick(name){
	if(animating) return;
	if(!selected){
		if(pegs[name].length===0) return;
		selected = name;
		render();
		return;
	}
	if(selected === name){ selected = null; render(); return; }
	move(selected, name);
	selected = null;
}

function generateMoves(k, from, aux, to){
	if(k<=0) return;
	if(k===1){ moveSequence.push([from,to]); return; }
	generateMoves(k-1, from, to, aux);
	moveSequence.push([from,to]);
	generateMoves(k-1, aux, from, to);
}

function sleep(ms){ return new Promise(r=>setTimeout(r,ms)); }

async function animateSolution(){
	if(animating) return;
	animating = true;
	for(const [from,to] of moveSequence){
		await sleep(300);
		move(from,to);
	}
	animating = false;
}

// Event wiring
window.addEventListener('DOMContentLoaded', ()=>{
	$('#startBtn').addEventListener('click', ()=>{ init(); });
	$('#resetBtn').addEventListener('click', ()=>{ init(); });
	$('#solveBtn').addEventListener('click', ()=>{
		if(animating) return;
		moveSequence = [];
		generateMoves(nDiscos, 'A','B','C');
		animateSolution();
	});
	$all('.peg').forEach(p=>p.addEventListener('click', ()=>handlePegClick(p.dataset.peg)));
	$('#numDiscos').addEventListener('change', ()=>init());
	init();
});

