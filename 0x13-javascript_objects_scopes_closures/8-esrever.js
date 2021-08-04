#!/usr/bin/node
exports.esrever = function (list) {
  const otherList = [];
  for (let iterator = 0; list[iterator]; iterator++) {
    otherList.push(list[list.length - (iterator + 1)]);
  }
  return (otherList);
};
