window.addEventListener('load',()=>{
    const preload=document.querySelector('.preload');
    preload.classList.add('preload-finish');
    
})

var loading=[
    'An Apple A Day Makes You An Apple',
    'Chicken is Made out of Chicken',
    'labadeee labadooo',
    'Chonk Sploby',
    'Rhys is Going Crazy',
    'The old guy\'s name is Jim'

]



function newLoad(){
    var randomNumber=Math.floor(Math.random()*(loading.length));
    document.getElementById('loadingDisp').innerHTML=loading[randomNumber]
    
}
newLoad();


function enlarge(source){
    
    document.getElementById('imageCont').style.visibility='visible';

    document.getElementById('image').src=source.src;
    
   
}


    
function close(){
   
    document.getElementById('imageCont').style.visibility='hidden';
}

document.getElementById("close").addEventListener("click", close());


