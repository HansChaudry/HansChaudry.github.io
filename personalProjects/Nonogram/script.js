// var board = [
//     Array.from({length: 10}, () => Math.floor(Math.random() * 2)),
//     Array.from({length: 10}, () => Math.floor(Math.random() * 2)),
//     Array.from({length: 10}, () => Math.floor(Math.random() * 2)),
//     Array.from({length: 10}, () => Math.floor(Math.random() * 2)),
//     Array.from({length: 10}, () => Math.floor(Math.random() * 2)),
//     Array.from({length: 10}, () => Math.floor(Math.random() * 2)),
//     Array.from({length: 10}, () => Math.floor(Math.random() * 2)),
//     Array.from({length: 10}, () => Math.floor(Math.random() * 2)),
//     Array.from({length: 10}, () => Math.floor(Math.random() * 2)),
//     Array.from({length: 10}, () => Math.floor(Math.random() * 2)),
//   ];

// console.log(board);

document.addEventListener('mousemove', function(e) {
    let body = document.querySelector('body');
    let circle = document.getElementById('circle');
    let left = e.offsetX;
    let top = e.offsetY;
    circle.style.left = left + 'px';
    circle.style.top = top + 'px';
    circle.style.display = 'block';
  });