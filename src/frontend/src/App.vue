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
        </ul>
      </div>
      <RouterView/>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';

const HandleConnection = () => {
  const ws = new WebSocket("ws://172.16.0.229:5000");
  
  ws.onopen = function() {
    ws.send("#INIT");
  };
  
  ws.onmessage = function(event) {
    localStorage.setItem("msg", event.data);
  
    if (event.data === "#ALLOW") {
      router.push('/');
    } else {
      localStorage.setItem('id',null);
      localStorage.setItem('auth',false);
      router.push('/login');
    }
  };
  
  ws.onerror = function(error) {
    console.log("WebSocket error: ", error);
    localStorage.setItem('id',null);
    localStorage.setItem('auth',false);
    router.push('/login');
  };
  
  ws.onclose = function() {
    localStorage.setItem('id',null);
    localStorage.setItem('auth',false);
    router.push('/login');
  };
  
  return ws;
};

const sendMessage = (ws, message) => {
  if (ws.readyState === WebSocket.OPEN) {
    ws.send(message);
  } else {
    ws.addEventListener('open', () => {
      ws.send(message);
    }, { once: true });
  }
};

const router = useRouter();
onMounted(() => { 
  let ws;
  try {
    ws = HandleConnection();
  } catch {
    console.log("Error at connection");
    localStorage.setItem('id',null);
    localStorage.setItem('auth',false);
    router.push('/login');
    return;
  }

  // Oturum durumunu kontrol et
  const id = localStorage.getItem('id');
  if (!id) {
    localStorage.setItem('id',null);
    localStorage.setItem('auth',false);
    router.push('/login');
    return;
  }
  
  const msg = "#CHECK " + id;
  sendMessage(ws, msg);
});
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto+Flex:opsz,wght@8..144,100..1000&display=swap');
* {
  margin: 0;
  padding: 0;
}
html, body {
  background: linear-gradient(135deg, #2bcac4, #c82b9f);
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
  background-color: none;
  padding: 15px 20px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
  z-index: 1000;
}
.navbar:hover{
  background-color: #222;
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
  font-weight: bolder;
  font-family: "Roboto Flex", sans-serif;
  white-space: nowrap; /* Metinlerin alt alta gelmesini engeller */
  font-style: italic;
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