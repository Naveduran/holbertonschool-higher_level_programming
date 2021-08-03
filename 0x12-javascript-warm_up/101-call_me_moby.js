#!/usr/bin/node
const theFunction = (x, theFunction) => {
  for (let step = 0; step !== x; step++) {
    theFunction();
  }
};
exports.callMeMoby = theFunction;
