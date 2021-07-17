// Selecting DOM Elements
let passfield = document.getElementById('password');
let repassfield = document.getElementById('repassword');
let regbtn = document.getElementById('regbtn');

regbtn.style.pointerEvents = 'none';
regbtn.style.cursor = 'not-allowed';
regbtn.style.opacity = '.4';


window.addEventListener('keydown', (e) => {
    if (e.key === 'U+00A' || e.key === 'Enter' || e.keyCode === 13){
        e.preventDefault();
        return false;
    }
    // console.log(e.keyCode)
}, true)

passfield.addEventListener('keyup', (e) => {
    let passvalue = e.target.value;
})

repassfield.addEventListener('keyup', (e) => {
    let repassvalue = e.target.value;
    let vpassfield = document.getElementById('password').value;
    let vrepassfield = document.getElementById('repassword').value;

    if (vpassfield === vrepassfield) {
        repassfield.style.border = '1px solid green';
        regbtn.style.pointerEvents = 'auto'
        regbtn.style.cursor = 'pointer'
        regbtn.style.opacity = '1'


    } else {
        repassfield.style.border = '1px solid red';
        regbtn.style.pointerEvents = 'none'
        regbtn.style.cursor = 'not-allowed'
        regbtn.style.opacity = '0.4'
    }

})

