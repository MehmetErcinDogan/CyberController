<template>
  <div class="full-screen-container">
    <div class="up-container">
      <button class="btn1" @click="getLocalIPs">Button</button>
    </div>
    <div class="down-container">
      <div class="alt-label">
        <div class="a2">
          
          <table class="ip-table">
            <thead>
              <tr class="table-header">
                <th>Local IP</th>
                <th>Name</th>
              </tr>
            </thead>
            <tbody>
              <tr class="o1" v-for="item in localIPs" :key="item.ip">
                <td>{{ item.ip }}</td>
                <td>{{ item.name }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import { onMounted, ref } from 'vue';

// IP adreslerini tutacak ref değişkeni
const localIPs = ref([]);

const HandleConnection = () => {
  const ws = new WebSocket("ws://localhost:5000");
  
  ws.onopen = function() {
    console.log("Successfully connected...");
    ws.send("#INIT");
  };
  
  ws.onmessage = function(event) { 
    if (event.data === "#ALLOW"){
      console.log(event.data);
    } else if (event.data === "#DENY"){
      router.push("/login");
    } else {
      let msg = JSON.parse(event.data);
      localStorage.setItem("msg", msg);
      console.log(msg);
      localIPs.value = msg.map(item => ({ ip: item[0], name: item[1] }));
    }
    
  };

  ws.onerror = function(error) {
    console.log("WebSocket error: ", error);
    router.push('/');
  };
  
  ws.onclose = function() {
    console.log("WebSocket connection closed");
  };
  
  return ws;
};

const sendMessage = (ws, message) => {
  if (ws.readyState === WebSocket.OPEN) {
    ws.send(message);
    console.log(message, "is sent...");
  } else {
    ws.addEventListener('open', () => {
      ws.send(message);
      console.log(message, "is sent...");
    }, { once: true });
  }
};

let ws;

onMounted(()=>{
  try{
    ws = HandleConnection();
    sendMessage(ws,"#CHECK "+localStorage.id);
  } catch {
    console.log("Error handled");
  }
});

// IP adreslerini getiren fonksiyon
const getLocalIPs = () => {
  try{
    sendMessage(ws,"#LISTDEVICES ");
  } catch {
    console.log("Error at getLocalIPs");
  }
};

</script>
<style scoped>
.full-screen-container {
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  font-family: "Roboto Flex", sans-serif;
  overflow-x: hidden;
}

.up-container {
  display: flex;
  justify-content: flex-end;
  align-items: center;
  margin: 5% 5%;
}

.down-container {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-grow: 1;
  width: 100%;
}

.alt-label {
  width: 100%;
  height: 100%;
  border-radius: 5px;
<<<<<<< HEAD
  background-color: rgba(204, 31, 161, 0.245);
  margin: 20px 0;
=======
  background-color: #9e4a6c;
  margin: 20px 0; /* Yatay margin kaldırıldı */
>>>>>>> 35a721f (.)
  padding: 20px;
  border-radius: 15px;
}

.a2 {
  margin-top: 1%;
  margin-left: 2%;
  font-size: 18px;
}

.btn1 {
  border: none;
  outline: none;
  padding: 8px 20px;
  background: #ff5945;
  color: #fff;
  font-size: 18px;
  cursor: pointer;
  border-radius: 15px;
  transition: background 0.3s ease;
  height: 40px;
  margin-top: 3%;
}

.Lp2 {
  font-size: 18px;
  color: white;
}

.ip-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

.table-header {
  background-color: #45abff;
  color: white;
  font-weight: bold;
}
.o1{
  color: white;
}

.ip-table tbody tr {
  background-color: rgba(255, 255, 255, 0.1);
}

.ip-table td, .ip-table th {
  padding: 10px;
  text-align: center;
}

@media (max-width: 768px) {
  .up-container {
    margin: 5% 10%;
    justify-content: center;
  }

  .btn1 {
    font-size: 16px;
    height: 40px;
    padding: 5px 15px;
  }

  .down-container {
    margin: 10px 0;
  }

  .alt-label {
    width: 100%;
    height: auto;
  }

  .a2 {
    font-size: 16px;
  }
}
</style>