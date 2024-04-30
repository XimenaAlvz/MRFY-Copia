const login__form = document.querySelector('.login__form');
const register__form = document.querySelector('.register__form');
const login__link = document.querySelector('.login__link');
const register__link = document.querySelector('.register__link');

register__link.onclick = () => {
    register__form.classList.add('active');
    login__form.classList.add('active');
}
login__link.onclick = () => {
    register__form.classList.remove('active');
    login__form.classList.remove('active');
}