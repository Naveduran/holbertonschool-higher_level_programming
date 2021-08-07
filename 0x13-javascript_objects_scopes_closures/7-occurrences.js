#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (let step = 0; list[step]; step++) {
    if (searchElement === list[step]) {
      counter++;
    }
  }
  return (counter);
};
