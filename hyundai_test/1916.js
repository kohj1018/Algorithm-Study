const fs = require('fs')

const inputPath = process.platform === 'linux' ? '/dev/stdin' : 'input.txt'
const input = fs.readFileSync(inputPath).toString().trim().split(/\r?\n/)

const N = Number(input[0])
const M = Number(input[1])
const graph = Array.from({length: N + 1}, () => [])

for (let i = 2; i < M + 2; i++) {
    const [u, v, w] = input[i].split(' ').map(Number)
    graph[u].push({to: v, cost: w})
}

const [startCity, endCity] = input[M + 2].split(' ').map(Number)

const dist = Array(N + 1).fill(Infinity)
const visited = Array(N + 1).fill(false)

function getSmallestNode() {
    let min = Infinity
    let minIdx = 0
    for (let i = 1; i <= N; i++) {
        if (!visited[i] && dist[i] < min) {
            min = dist[i]
            minIdx = i
        }
    }
    return minIdx
}

dist[startCity] = 0

for (let i = 0; i < N; i++) {``
    const cur = getSmallestNode()

    if (dist[cur] === Infinity) break   // 앞에서 가장 smallest한 값을 찾았는데 Infinity라는건 갈 곳이 없다는 것

    visited[cur] = true

    for (const next of graph[cur]) {
        const nextCost = dist[cur] + next.cost

        if (nextCost < dist[next.to]) {
            dist[next.to] = nextCost
        }
    }
}

console.log(dist[endCity])