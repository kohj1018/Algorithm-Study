const fs = require('fs');

const inputPath = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';
const input = fs.readFileSync(inputPath).toString().trim().split(/\r?\n/);

const [N, M] = input.shift().split(' ').map(Number);
const maze = input.map(row => row.split('').map(Number));

const queue = []
let head = 0

queue.push([0, 0])
maze[0][0] += 1

const dr = [0, 1, 0, -1]
const dc = [1, 0, -1, 0]

while (head < queue.length) {
    const current = queue[head++]

    const r = current[0]
    const c = current[1]

    for (let i = 0; i < 4; i++) {
        const nr = r + dr[i]
        const nc = c + dc[i]

        if (nr >= 0 && nr < N && nc >= 0 && nc < M) {
            if (maze[nr][nc] === 1) {
                maze[nr][nc] += maze[r][c]
                queue.push([nr, nc])
            }
        }
    }
}

console.log(maze[N-1][M-1] - 1)