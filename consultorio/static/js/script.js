var name = "João";
let age = 89;
let soma = age + 10;
let multi = age * 2;
let sub =multi-age;

if(age > 60){
    console.log("Idoso");
    alert("Idoso");
}else{
    alert("Futuro Idoso");
}

for(let i=0; i<age; i++){
    document.getElementById('output').innerText += " " + i ;
}

while(age>0){
    console.log('Menos um ponto');
    age--;
}

function over(){
    var aaa = document.getElementById('footer').style.backgroundImage="url('/static/image/urso.jpeg')";
    console.log(aaa);
}
function out(){
    document.getElementById('footer').style.backgroundImage="url('/static/image/image.jpeg')";
}
function saveAge(){
    var ageVar = document.getElementById('ageVar').value;
    age = ageVar;
    if(age > 60){
        console.log("Idoso");
        alert("Idoso");
    }else{
        alert("Futuro Idoso");
    }
}

function confirmDelete(name, id){
    if(confirm("Você tem certeza que quer deletar "+name+"?")==true){
        window.open("delete_person/"+id,'self')
    }
}