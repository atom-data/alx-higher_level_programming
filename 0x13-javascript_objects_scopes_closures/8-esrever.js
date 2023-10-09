#!/usr/bin/node

exports.esrever = function (list) {
  let k = list.length - 1;
  for (let i = 0; i < k; i++) {
    [list[i], list[k]] = [list[k], list[i]];
    k -= 1;
  }
  return list;
};
