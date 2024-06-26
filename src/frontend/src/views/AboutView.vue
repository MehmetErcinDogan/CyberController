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
      <!-- Dashboard içeriği buraya gelecek -->
      <RouterView/>

    </div>
  </div>
</template>
<script>
import { RouterLink, RouterView } from 'vue-router'

</script>

<style>
.about {
  /* Sayfa yüksekliğini ekran yüksekliği kadar yap */
  height: 100vh;
}

.container {
  /* Sayfa içeriğini tam ekran boyutuna uyacak şekilde ayarla */
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #333;
  color: #fff;
  padding: 10px 20px;
  left: 0;
}

.nav-links {
  list-style-type: none;
  display: flex;
}

.nav-links li {
  margin-right: 20px;
}

.nav-links li a {
  color: #fff;
  text-decoration: none;
}

</style>
