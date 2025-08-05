const studentsDB = ['Jordan', 'erick', 'john', 'michel']

const findstudent = (allStudents, studentName) =>{
    for (let i = 0; i < allStudents.length; i ++){
        if (allStudents[i] == studentName){
            console.log(`Found ${studentName}`);
            
        }
    }
}

findstudent(studentsDB, 'Jordan') 