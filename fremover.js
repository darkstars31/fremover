const fs = require('fs');

const match1 = new RegExp(/test/gi);
const match2 = new RegExp(/.spec.ts/gi);

getFilesNamesThatMatchExpression = (dir, matchArray, files_) => {
   files_ = files_ || [];
   let files = fs.readdirSync(dir);
   for (let file of files){
       let dirName = dir + '\\' + file;
       if (fs.statSync(dirName).isDirectory()){
        getFilesNamesThatMatchExpression(dirName, matchArray, files_);
       } else {
           let isMatch = false;
           isMatch = matchArray.some(match => match.test(file))
           if(isMatch){
               files_.push(dirName);
           }
       }
   }
   return files_;
}

removeFitAndFdescribes = (file) => {
    return new Promise((resolve,reject) => {
        fs.readFile(file,(err,data) => {
            let fileContents = data.toString('utf8');
            let fitMatch = new RegExp(/fit\(/gi);
            let fdescribeMatch = new RegExp(/fdescribe\(/gi);
            if(fitMatch.test(fileContents) || fdescribeMatch.test(fileContents)){   
                filesModified++;
                console.log(`Fixed file: ${file}`) 
                var updatedFile = fileContents.replace(fitMatch, 'it(').replace(fdescribeMatch, 'describe(');
                fs.writeFile(file, updatedFile, err => {
                    if(err){ console.log(err); }
                });
            }  
            return resolve();
        });      
    });
}

outputStats = () => {
    console.log(`${filesModified} files modified.`); 
}

console.log(`fremover - swatting those pesky f's hidden in your tests. Your builds should feel liberated.`);
console.log(`Written w/ <3 by Tony`);
var filesModified = 0;
var fileList = getFilesNamesThatMatchExpression(__dirname+"\\src", [match1, match2]);
console.log(`${fileList.length} Files Located`);
Promise.all(fileList.map(file => removeFitAndFdescribes(file))).then(() => {
    outputStats();
});
