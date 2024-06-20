<template>
  <div class="about">
    <div class="container">
      <div class="navbar">
        <ul class="nav-links">
          <li><router-link to="/list-lan-devices">List Lan Devices</router-link></li>
          <li><router-link to="/port-scanner">Port Scanner</router-link></li>
          
          <li><router-link to="/task-list">Task List</router-link></li>
          <li><router-link to="/sniffer">Sniffer</router-link></li>
          <li><router-link to="/ddos-attack">DDOS Attack</router-link></li>
          <li><router-link to="/encrypt-decrypt-file">Encrypt/Decrypt File</router-link></li>
          <li><router-link to="/profile">Profile</router-link></li>
          <li><router-link to="/login">Login</router-link></li>
        </ul>
      </div>
      <RouterView/>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';

const HandleConnection = () =>{
  var ws = new WebSocket("ws://localhost:5000");
  
  ws.onopen = function(){
    console.log("Sucessfully connected . . .");
    sendMessage(ws,"Logged in");
  }
  
  ws.onmessage = function(event){
    console.log(event.data);
  }
  return ws;
}

const sendMessage = (ws,msg) =>{
  ws.send(msg)
  console.log(msg," is sent . . .");
}

const router = useRouter();
onMounted(() => {
  router.beforeEach((to, from, next) => {
    localStorage.clear();
    next();
  });
  try{
    HandleConnection();
  }catch(error){
    console.log("There are error: ",error);
  }
  // Oturum durumunu kontrol et
  const isLoggedIn = localStorage.getItem('isLoggedIn');

  // Eğer kullanıcı daha önce giriş yapmışsa ana sayfaya yönlendir
  if (isLoggedIn) {
    console.log("logged in");
  } else {
    // Kullanıcı daha önce giriş yapmamışsa login sayfasına yönlendir
    router.push('/login');
  }
});
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto+Flex:opsz,wght@8..144,100..1000&display=swap');
* {
  margin: 0;
  padding: 0;
}
html, body {
  background: linear-gradient(135deg, #153677, #4e085f);
  padding: 0;
  
  margin: 0;
  height: 100%;
  width: 100%;
}
#app {
  height: 100%;
  width: 100%;
  margin: 0;
  padding: 0;
}
.about {
  height: 100vh;
}
.navbar {
  position: fixed;
  width: 100%;
  display: flex;
  justify-content: space-between; /* Linklerin arasındaki boşluğu dinamik olarak ayarlar */
  background-color: #222;
  padding: 15px 20px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
  z-index: 1000;
}
.nav-links {
  display: flex;
  justify-content: space-between;
  list-style-type: none;
  padding: 0;
  margin: 0;
  width: 100%;
}
.nav-links li {
  font-size: 15px;
  font-weight: bold;
  font-family: "Roboto Flex", sans-serif;
  white-space: nowrap; /* Metinlerin alt alta gelmesini engeller */
}
.nav-links li a {
  color: #fff;
  text-decoration: none;
  padding: 10px 15px;
  transition: background-color 0.3s ease, color 0.3s ease;
  border-radius: 5px;
}
.nav-links li a:hover {
  background-color: #ff5945;
  color: #fff;
}
.nav-links li a.active {
  background-color: #ff5945;
  color: #fff;
}


</style>