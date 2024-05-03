<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { ref, onBeforeUnmount } from 'vue';

import { useRouter } from 'vue-router';
const router = useRouter();


const handleLogin = async () => {
  

  


  startProgress();
  const isValid = await validateUsernameAndPassword();
  
  if (isValid) {
    setTimeout(() => {
      
      router.push('/home');
    }, 5000);
  } else {
    // Kullanıcı adı ve şifre yanlışsa
    // İşlemleri buraya ekleyebilirsiniz
  }
};

const validateUsernameAndPassword = async () => {
  // Kullanıcı adı ve şifreyi kontrol et
  // Geçerli ise true, değilse false döndür
  return true; // Örnek olarak her zaman geçerli olduğunu varsayalım
};
const loginBgColor = ref('#57B846');
const loginColor = ref('#fff');

const showLoginForm = ref(true);

const progressOpacity = ref(0);
const intervalId = ref(null);





const toggleLogin = () => {
  loginBgColor.value = '#57B846';
  loginColor.value = '#fff';

  showLoginForm.value = true;
  
};

const startProgress = () => {
  progressOpacity.value = 1;
  intervalId.value = setInterval(rotateProgress, 50);
  
};

const rotateProgress = () => {
  const progressElement = document.querySelector('.progress');
  const rotation = 1;

  for (let i = 0; i < 361; i++) {
    progressElement.style.transform = `rotate(${50}deg)`;
    console.log('Dönme Açısı:', i);
  }
};

onBeforeUnmount(() => {
  clearInterval(intervalId.value);
});

</script>

<template>
    <div class="full-screen-container">

  <RouterView/>
  <div class="form-modal">
    
    <div class="form-toggle">
      <button id="login-toggle" @click="toggleLogin" :style="{ backgroundColor: loginBgColor, color: loginColor }">Login</button>
    
    </div>

    <div id="login-form" v-show="showLoginForm">
        <form>
            <input type="text" placeholder="Enter email or username"/>
            <input type="password" placeholder="Enter password"/>
            <button type="button" to="/home" class="btn login" @click.native="handleLogin">Login</button>

            
            
            
        </form>
    </div>

    

</div>
<div id="progressbar" :style="{ opacity: progressOpacity }">
      <div class="progress"></div>
    </div>
  </div>
 
 
</template>

<style>
body{
    
    background-image: url("giphy.gif");
    overflow: hidden; /* Gerektiğinde içeriği kırp */

}
.full-screen-container {
  position: relative;
  width: 100vw; /* Ekran genişliği kadar */
  height: 100vh; /* Ekran yüksekliği kadar */
  overflow: hidden; /* Gerektiğinde içeriği kırp */
}
header {
  line-height: 1.5;
  max-height: 100vh;
}
.form-modal{
    position:relative;
    width:650px;
    height:auto;
    margin-top:10em;
    margin-left: 150px;
    left:30%;
    transform:translateX(-50%);
    background: black;
    border-top-right-radius: 20px;
    border-top-left-radius: 20px;
    border-bottom-right-radius: 20px;
    box-shadow:0 3px 20px 0px rgba(0, 0, 0, 0.1)
}

.form-modal button{
    cursor: pointer;
    position: relative;
    text-transform: capitalize;
    font-size:2em;
    z-index: 2;
    outline: none;
    background:#fff;
    transition:0.2s;
}

.form-modal .btn{
    border-radius: 20px;
    border:none;
    font-weight: bold;
    font-size:1.3em;
    padding:0.8em 1em 0.8em 1em!important;
    transition:0.5s;
    border:1px solid #ebebeb;
    margin-bottom:0.5em;
    margin-top:0.5em;
    
}

.form-modal .login{
    background:#57b846;
    color:#fff;
}

.form-modal .login:hover{
    background:#222;
}

.form-toggle{
    position: relative;
    width:100%;
    height:auto;
}

.form-toggle button{
    width:100%;
    float:left;
    padding:1.5em;
    margin-bottom:1.5em;
    border:none;
    transition: 0.2s;
    font-size:1.3em;
    font-weight: bold;
    border-top-right-radius: 20px;
    border-top-left-radius: 20px;
}

.form-toggle button:nth-child(1){
    border-bottom-right-radius: 20px;
}

.form-toggle button:nth-child(2){
    border-bottom-left-radius: 20px;
}

#login-toggle{
    background:#57b846;
    color:#ffff;
}

.form-modal form{
    position: relative;
    width:90%;
    height:auto;
    left:50%;
    transform:translateX(-50%);  
}

#login-form{
    position:relative;
    width:100%;
    height:auto;
    padding-bottom:1em;
}




#login-form button{
    width:100%;
    margin-top:0.5em;
    padding:0.6em;
}

.form-modal input{
    position: relative;
    width:100%;
    font-size:1.2em;
    padding:1.2em 1.7em 1.2em 1.7em;
    margin-top:0.6em;
    margin-bottom:0.6em;
    border-radius: 20px;
    border:none;
    background:#ebebeb;
    outline:none;
    font-weight: bold;
    transition:0.4s;
}

.form-modal input:focus , .form-modal input:active{
    transform:scaleX(1.02);
}

.form-modal input::-webkit-input-placeholder{
    color:#222;
}


.form-modal p{
    font-size:16px;
    font-weight: bold;
}

.form-modal p a{
    color:#57b846;
    text-decoration: none;
    transition:0.2s;
}

.form-modal p a:hover{
    color:#567;
}


.form-modal i {
    position: absolute;
    left:10%;
    top:50%;
    transform:translateX(-10%) translateY(-50%); 
}



.-box-sd-effect:hover{
    box-shadow: 0 4px 8px hsla(210,2%,84%,.2);
}

@media only screen and (max-width:500px){
    .form-modal{
        width:100%;
    }
}

@media only screen and (max-width:400px){
    i{
        display: none!important;
    }
}
#progressbar {
  position: absolute;
  margin-top: 500px;
  margin-left: 500px;
  width: 100px;
  height: 100px;
  opacity: 0; /* Başlangıçta görünmez */
}

.progress {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border-radius: 50%;
  background-color: #57b846; /* Progress rengi */
  transform-origin: center;
  animation: rotate 2s linear infinite; /* Dönme animasyonu */
  
}



</style>
