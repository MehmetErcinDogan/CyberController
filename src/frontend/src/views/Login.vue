<template>
  <div class="full-screen-container">
    <RouterView/>
    <canvas ref="canvas"></canvas>
    <div class="form-modal">
      <div class="form-toggle">
        <button id="login-toggle" @click="toggleLogin" :style="{ backgroundColor: loginBgColor, color: loginColor }">Login</button>
      </div>
      <div id="login-form" v-show="showLoginForm">
        <form>
          <input type="text" placeholder="Enter email or username"/>
          <input type="password" placeholder="Enter password"/>
          <button type="button" class="btn login" @click="handleLogin">Login</button>
        </form>
      </div>
    </div>
    <div id="progressbar" :style="{ opacity: progressOpacity }">
      <div class="progress"></div>
    </div>
  </div>
</template>

<script setup>

import { ref, onMounted, onBeforeUnmount } from 'vue';
import { useRouter } from 'vue-router';

const canvas = ref(null);
const router = useRouter();

onMounted(() => {
  // websocket gonna connect



  const c = canvas.value;
  const ctx = c.getContext('2d');

  // Making the canvas full screen
  c.height = window.innerHeight;
  c.width = window.innerWidth;

  // Characters for the matrix effect
  const matrix = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789@#$%^&*()*&^%+-/~{[|`]}".split("");

  const font_size = 14;
  const columns = c.width / font_size; // Number of columns for the rain
  const drops = Array.from({ length: columns }, () => 1); // Initialize drops array

  // Function to draw the characters
  const draw = () => {
    // Black BG for the canvas, translucent BG to show trail
    ctx.fillStyle = "rgba(0, 0, 0, 0.04)";
    ctx.fillRect(0, 0, c.width, c.height);

    ctx.fillStyle = "#00ff00"; // Yeşil yazı rengi

    ctx.font = `${font_size}px arial`;

    // Loop over drops
    drops.forEach((drop, i) => {
      // Random character
      const text = matrix[Math.floor(Math.random() * matrix.length)];
      // x = i * font_size, y = value of drops[i] * font_size
      ctx.fillText(text, i * font_size, drop * font_size);

      // Sending the drop back to the top randomly after it has crossed the screen
      if (drop * font_size > c.height && Math.random() > 0.975) {
        drops[i] = 0;
      }

      // Incrementing Y coordinate
      drops[i]++;
    });
  };

  // Set interval to draw the matrix effect
  const intervalId = setInterval(draw, 35);

  // Cleanup on component unmount
  onBeforeUnmount(() => {
    clearInterval(intervalId);
  });
});

// TO DO: Yoruma aldığım metotlar ve değişkenler gerekli mi kontrol
// TO DO: onBeforeMount fonksitonu bir kere mi çalışıyor ve neden onMounted içinde tanımlanmış? O fonksiyonda başka işlevlerde olacak
// TO DO: localStorage sıfırlanması gerekli her sayfa açıldığında app vueda başlangıçta sıfırlasın. App vue refresh edildiğinde bir daha çağrılmıyor zaten değil mi?
// Check: Testere müziği sadece login sayfasında çalsın onun haricinde çalmasın. 
// TO DO: Tüm gereksiz yorumları fonksiyonları kaldır ve daha açık hale getir bro
// TO DO: Ben biraz değişiklik yaptım, viewlerın hepsinin çalışıp çalışmadığını da bir zahmet kontrol et bro

/* TO DO for Myself
 * validateUsernameandpassword gonna complete
 * websocket connections gonna handle
 * handle websockets and server side implent it for all pages
*/

// // Login related functions and variables
// const loginBgColor = ref('#57B846');
// const loginColor = ref('#fff');
const showLoginForm = ref(true);
// const progressOpacity = ref(0);
// const intervalId = ref(null);

const handleLogin = async () => {
  const isValid = await validateUsernameAndPassword();
  if (isValid) {
    setTimeout(() => {
      localStorage.setItem('isLoggedIn', true);
      router.push('/home');
    }, 5000); // 5 saniye bekledikten sonra ana sayfaya yönlendir
  } else {
    // Kullanıcı adı ve şifre yanlışsa işlemleri buraya ekleyebilirsiniz
  }
};

const validateUsernameAndPassword = async () => {
  return true; // Örnek olarak her zaman geçerli olduğunu varsayalım.
  // Bu kısma bir kullanıcı adı ve şifre kontrolü yapılacak.
};


// onBeforeUnmount(() => {
//   clearInterval(intervalId.value);
//   // gonna close websocket

  
// });
</script>

<style scoped>
body {
  background: black;
  overflow: hidden;
}
canvas {
  display: block;
  position: absolute;
  top: 0;
  left: 0;
}
.full-screen-container {
  position: relative;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
}
.form-modal {
  position:relative;
  width:40%;
  height:40%;
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
.form-modal button {
  cursor: pointer;
  position: relative;
  text-transform: capitalize;
  font-size:2em;
  z-index: 2;
  outline: none;
  background:#fff;
  transition:0.2s;
  font-family: "Roboto Flex", sans-serif;
}
.form-modal .btn {
  border-radius: 20px;
  border:none;
  font-weight: bold;
  font-size:1.3em;
  padding:0.8em 1em 0.8em 1em!important;
  transition:0.5s;
  border:1px solid #ebebeb;
  margin-bottom:0.5em;
  margin-top:0.5em;
  font-family: "Roboto Flex", sans-serif;
}
.form-modal .login {
  background:#57b846;
  color:#fff;
  font-family: "Roboto Flex", sans-serif;
}
.form-modal .login:hover {
  background:#222;
}
.form-toggle {
  position: relative;
  width:100%;
  height:auto;
}
.form-toggle button {
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
  background: linear-gradient(135deg, #153677, #4e085f);
  font-family: "Roboto Flex", sans-serif;
}
.form-toggle button:nth-child(1) {
  border-bottom-right-radius: 20px;
}
.form-toggle button:nth-child(2) {
  border-bottom-left-radius: 20px;
}
#login-toggle {
  background:#57b846;
  color:#ffff;
  font-family: "Roboto Flex", sans-serif;
}
.form-modal form {
  position: relative;
  width:90%;
  height:auto;
  left:50%;
  transform:translateX(-50%);  
}
#login-form {
  position:relative;
  width:100%;
  height:auto;
  padding-bottom:1em;
}
#login-form button {
  width:100%;
  margin-top:0.5em;
  padding:0.6em;
}
.form-modal input {
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
  font-family: "Roboto Flex", sans-serif;
}
.form-modal input:focus , .form-modal input:active {
  transform:scaleX(1.02);
}
.form-modal input::-webkit-input-placeholder {
  color:#222;
}
.form-modal p {
  font-size:16px;
  font-weight: bold;
}
.form-modal p a {
  color:#57b846;
  text-decoration: none;
  transition:0.2s;
}
.form-modal p a:hover {
  color:#567;
}
.form-modal i {
  position: absolute;
  left:10%;
  top:50%;
  transform:translateX(-10%) translateY(-50%); 
}
.-box-sd-effect:hover {
  box-shadow: 0 4px 8px hsla(210,2%,84%,.2);
}
@media only screen and (max-width:500px) {
  .form-modal {
    width:100%;
  }
}
@media only screen and (max-width:400px) {
  i {
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
