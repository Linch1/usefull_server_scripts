### Way 1

1.install jquery types
```
npm install --save-dev @types/jquery
```

2. add the jquery cdn at the top of your imports 
```
<script src="https://code.jquery.com/jquery-3.5.1.min.js" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script>
```

3. create the `myFile.ts` file to use 
```
jQuery(document).ready(function() {
    console.log(jQuery(".asd"))
});
```

4. import the relative compiled `myFile.js` file 


### Way 2

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

3. create the `myFile.ts` file to use 
```
const jquery: JQueryStatic = require("jquery");

jquery(document).ready(function() {
    console.log(jquery(".asd"))
});
```

4. import the relative compiled `myFile.js` file 
