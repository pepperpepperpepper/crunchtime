var Greeter = function Greeter() {
  "use strict";
};
($traceurRuntime.createClass)(Greeter, {sayHi: function() {
    "use strict";
    var name = arguments[0] !== (void 0) ? arguments[0] : 'Anonymous';
    console.log(("Hi " + name + "!"));
  }}, {});
var greeter = new Greeter();
greeter.sayHi();
