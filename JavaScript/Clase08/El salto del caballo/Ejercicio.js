/*
	Salto del caballo (Tour del caballo)
*/

const n = 8;
const movimientos = [
	[2, 1], [1, 2], [-1, 2], [-2, 1],
	[-2, -1], [-1, -2], [1, -2], [2, -1]
];

function esValida(x, y, tablero){
	return x >= 0 && x < n && y >= 0 && y < n && tablero[y][x] === -1;
}

// Devuelve número de movimientos válidos desde (x,y)
function gradoMovimientos(x, y, tablero){
	let cnt = 0;
	for(const [dx, dy] of movimientos){
		const nx = x + dx, ny = y + dy;
		if(nx >= 0 && nx < n && ny >= 0 && ny < n && tablero[ny][nx] === -1) cnt++;
	}
	return cnt;
}

// Genera lista de movimientos ordenada por grado
function movimientosOrdenados(x, y, tablero){
	const siguiente = [];
	for(const [dx, dy] of movimientos){
		const nx = x + dx, ny = y + dy;
		if(esValida(nx, ny, tablero)) siguiente.push({x: nx, y: ny, deg: gradoMovimientos(nx, ny, tablero)});
	}
	siguiente.sort((a,b) => a.deg - b.deg);
	return siguiente;
}

function resolverRecursivo(x, y, movimientoNum, tablero){
	if(movimientoNum === n * n) return true;
	const sig = movimientosOrdenados(x, y, tablero);
	for(const m of sig){
		tablero[m.y][m.x] = movimientoNum;
		if(resolverRecursivo(m.x, m.y, movimientoNum + 1, tablero)) return true;
		tablero[m.y][m.x] = -1; // retroceso
	}
	return false;
}

function resolverSaltoCaballo(){
	const tablero = Array.from({length: n}, () => Array(n).fill(-1));
	const inicioX = 0, inicioY = 0;
	tablero[inicioY][inicioX] = 0;
	const ok = resolverRecursivo(inicioX, inicioY, 1, tablero);
	if(!ok){
		const msg = 'No se encontró solución.';
		console.log(msg);
		mostrarSalida(msg);
		return null;
	}
	imprimirTablero(tablero);
	return tablero;
}

function imprimirTablero(tablero){
	const lines = tablero.map(row => row.map(n => String(n).padStart(2,' ')).join(' '));
	const out = lines.join('\n');
	console.log(out);
	return out;
}

function mostrarSalida(html){
	if(typeof document === 'undefined') return; // Node: no DOM
	let el = document.getElementById('knight-tour-output');
	if(!el){
		el = document.createElement('div');
		el.id = 'knight-tour-output';
		el.style.whiteSpace = 'pre';
		document.body.appendChild(el);
	}
	el.innerHTML = html;
}

// Construye lista de posiciones ordenadas por número de movimiento
function construirRecorridoDesdeTablero(tablero){
	const total = n * n;
	const recorrido = Array(total);
	for(let y = 0; y < n; y++){
		for(let x = 0; x < n; x++){
			const idx = tablero[y][x];
			if(idx >= 0 && idx < total) recorrido[idx] = {x, y};
		}
	}
	return recorrido;
}

function renderizarRecorrido(recorrido, actual){
	if(typeof document === 'undefined') return;
	const container = document.getElementById('knight-tour-output');
	if(!container) return;
	let html = '<div>Movimiento: ' + actual + ' / ' + (recorrido.length - 1) + '</div>';
	html += '<table style="border-collapse:collapse;margin-top:0.5rem;">';
	// construir matriz de índices para render rápido
	const indices = Array.from({length: n}, () => Array(n).fill(-1));
	recorrido.forEach((p, i) => { if(p) indices[p.y][p.x] = i; });
	for(let y = 0; y < n; y++){
		html += '<tr>';
		for(let x = 0; x < n; x++){
			const moveNum = indices[y][x];
			const isCaballo = (recorrido[actual] && recorrido[actual].x === x && recorrido[actual].y === y);
			const bg = isCaballo ? '#ffeb3b' : ((x + y) % 2 === 0 ? '#eee' : '#bbb');
			const content = moveNum >= 0 ? ('<div style="font-size:12px;">' + moveNum + '</div>') : '';
			const caballoChar = isCaballo ? '<div style="font-size:20px;">♞</div>' : '';
			html += '<td style="width:48px;height:48px;border:1px solid #333;text-align:center;vertical-align:middle;background:' + bg + ';">' + caballoChar + content + '</td>';
		}
		html += '</tr>';
	}
	html += '</table>';
	container.innerHTML = html;
}

let _recorrido = null;
let _actual = 0;

function pasoSiguiente(){
	if(!_recorrido) return;
	if(_actual < _recorrido.length - 1) _actual++;
	renderizarRecorrido(_recorrido, _actual);
}

function reiniciarRecorrido(){
	if(!_recorrido) return;
	_actual = 0;
	renderizarRecorrido(_recorrido, _actual);
}

// Ejecutar automáticamente en navegador o Node
if(typeof window !== 'undefined' && typeof document !== 'undefined'){
	document.addEventListener('DOMContentLoaded', () => {
		const tablero = resolverSaltoCaballo();
		if(tablero){
			_recorrido = construirRecorridoDesdeTablero(tablero);
			_actual = 0;
			renderizarRecorrido(_recorrido, _actual);
			// Exponer funciones para el botón (nombres en español)
			window.pasoSiguiente = pasoSiguiente;
			window.reiniciarRecorrido = reiniciarRecorrido;
		}
	});
} else {
	// Node: imprimir en consola
	const tablero = resolverSaltoCaballo();
	if(tablero) console.log(imprimirTablero(tablero));
}

