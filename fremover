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

var filesModified = 0;
var fileList = getFilesNamesThatMatchExpression(__dirname+"\\src", [match1, match2]);
console.log(`${fileList.length} Files Located`)
for(let i = 0; i < fileList.length; i++){
    let file = fileList[i];
    fs.readFile(file,(err,data) => {
        let fileContents = data.toString('utf8');
        let fitMatch = new RegExp(/fit\(/gi);
        let fdescribeMatch = new RegExp(/fdescribe\(/gi);
        if(fitMatch.test(fileContents) || fdescribeMatch.test(fileContents)){   
            console.log(`File: ${file}`) 
            var updatedFile = fileContents.replace(fitMatch, 'it(').replace(fdescribeMatch, 'describe(');
            fs.writeFile(file, updatedFile, err => {
                if(err){ console.log(err); }
            });
        }  
    });  
}
console.log(`${filesModified} files modified.`); 
