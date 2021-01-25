1. install jquery
```
npm install --save jquery
npm install --save-dev @types/jquery
```

2. Set in the tsconfig.json the following properties
```
"target": "es5",
"module": "es2015",
"moduleResolution": "node"
```

3. create the `.ts` file to use 
```
const jquery: JQueryStatic = require("jquery");

jquery(document).ready(function() {
    console.log(jquery(".asd"))
});
```
