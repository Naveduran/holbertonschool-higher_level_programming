#!/usr/bin/node
exports.esrever = function (list) {
  let other_list = [];
  for (let iterator = 0; list[iterator]; iterator++) {
    other_list.push(list[list.length - (iterator + 1)]);
  }
  return (other_list);
}