
1. add an `index.ts` in the src folder that contains all the export of the functions/directories of the lib
```
export * from "./Abstracts";
export * from "./Decorators";
export * from "./Entities";
export * from "./Enums";
export * from "./files";
export * from "./Identifiers";
export * from "./Interfaces";
export * from "./ManageTheme";
export * from "./ManageVisual";
export * from "./Types";
```

2. add the following scripts to the `package.json` for make npm build the lib when installed
```
"prepare": "npm run build",
"build": "tsc"
```

3. enable the following settins in the `tsconfig.json` ( particularly `"declaration": true` )
```
{
  "compilerOptions": {
    "target": "es5",
    "module": "commonjs",
    "declaration": true,
    "outDir": "./src",
    "strict": true
  },
  "include": ["src"],
  "exclude": ["node_modules", "**/__tests__/*"]
}
```

4. install the repo `npm i --save git+{REPO-URL}`

