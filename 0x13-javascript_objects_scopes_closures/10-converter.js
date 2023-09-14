#!/usr/bin/node
exports.converter = function (base) {
  return function convertNumberToBase (num) {
    return num.toString(base);
  };
};
