// Load from current module path
var Square = require('./square');

//Since the module exports a constructor function we
//have to create an instance before using it

var square = new Square(25);

console.log(square.area());