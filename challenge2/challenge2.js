// =============================================================
// Created Date : 19/1/2017
// Name : challenge2.js
// Contributers : Ajay
// =============================================================

function increment() {
  var self = this;
  this.count = 0;
}

increment.prototype.init =function(){
  self.count += 1;  
  return 'The count is --> '+self.count;
};

increment();

// auto increment can be triggered by calling increment.prototype.init()

//OPTIONAL : encase increment.prototype.init() in another function  
function triggerIncrement(){
  return increment.prototype.init();
}
