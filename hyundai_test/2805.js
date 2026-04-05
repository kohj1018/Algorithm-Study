const fs = require('fs')

const inputPath = process.platform === 'linux' ? '/dev/stdin' : 'input.txt'
const input = fs.readFileSync(inputPath).toString().trim().split(/\r?\n/)

const [N, M] = input.shift().split(' ').map(Number)
const tree_length = input[0].split(' ').map(Number)

let bottom = 0
let top = Math.max(...tree_length)

let max_height = 0

while (bottom <= top) {
    const mid = Math.floor((bottom + top) / 2)

    let tree_sum = 0
    for (const length of tree_length) {
        if (length > mid) {
            tree_sum += length - mid
        }
    }

    if (tree_sum >= M) {
        max_height = Math.max(max_height, mid)
        bottom = mid + 1
    } else {
        top = mid - 1
    }
}

console.log(max_height)