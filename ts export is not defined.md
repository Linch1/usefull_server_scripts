### Way 1
1. Enable `webPreferences: { nodeintegration: true }` in electron window
2. change the script import 
`<script src="./dist/renderer.js"></script>`
to
```
<script>
    require("./dist/renderer.js");
</script>
```
3. It may not work at the start, try to reboot few times electron

### Way 2
1. Add the following script before importing your custom files
```
<script> var exports = {}; </script>
```
