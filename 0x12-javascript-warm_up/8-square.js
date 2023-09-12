#!/usr/bin/node

const args = process.argv[2];
const shape = parseInt(args);

if (!isNaN(shape) && Number.isFinite(shape)) {
	for (let i = 0; i < shape; i++) {
		let row = '';
		for (let j = 0; j < shape; j++) {
			row += 'X';
		}
		console.log(row);
	}
} else {
	console.log('Missing size');
}
