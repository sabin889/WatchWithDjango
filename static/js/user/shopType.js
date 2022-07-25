const all = document.querySelector('.shop-all');
const neww = document.querySelector('.shop-new');
const old = document.querySelector('.shop-old');

const shopall = document.querySelector('.shop-list-all');
const shopneww = document.querySelector('.shop-list-new');
const shopold = document.querySelector('.shop-list-old');


all.classList.add("active-shop");

shopneww.classList.add('shop-list-display');
shopold.classList.add('shop-list-display');

all.addEventListener('click',()=>{
    all.classList.add("active-shop");
    neww.classList.remove("active-shop");
    old.classList.remove("active-shop");

    shopneww.classList.add('shop-list-display');
    shopold.classList.add('shop-list-display');
    shopall.classList.remove('shop-list-display');


});

neww.addEventListener('click',()=>{
    all.classList.remove("active-shop");
    neww.classList.add("active-shop");
    old.classList.remove("active-shop");

    shopneww.classList.remove('shop-list-display');
    shopold.classList.add('shop-list-display');
    shopall.classList.add('shop-list-display');


});
old.addEventListener('click',()=>{
    all.classList.remove("active-shop");
    neww.classList.remove("active-shop");
    old.classList.add("active-shop");

    shopneww.classList.add('shop-list-display');
    shopold.classList.remove('shop-list-display');
    shopall.classList.add('shop-list-display');



});
