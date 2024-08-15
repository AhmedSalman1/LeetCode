/**
 * @return {Function}
 */

const createHelloWorld = () => {
    return (...args) => 'Hello World'
}

// var createHelloWorld = function() {
//     let a = 'Hello World'
//     return function(...args) {
//         return a        
//     }
// };

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */