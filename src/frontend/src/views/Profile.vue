<template>
  <div class="container">
    <div class="up-profile">
      <div class="profile-photo">
        <img :src="userInfo.photo" alt="Profile Photo">
      </div>
      <div class="other-profile-info">
        <div v-for="(item, index) in userInfo.details" :key="index" class="profile-field">
          <h1 class="label">{{ item.label }}:</h1>
          <h1 class="value">{{ item.value }}</h1>
        </div>
        <div class="label-acc">
          <div class="label-acc11">
            <h1 class="tcp-ipp">{{ userInfo.tcpIp }}</h1>
          </div>
          <button class="logout" @click="logout">Logout</button>
        </div>
      </div>
    </div>
    <div class="History">
      <h1 class="h1">History</h1>
      <div class="port-scanner-info">
        <div class="up-port">
          <div class="label1">
            <div class="table-texts">
              <h1 class="ProblemT">Problems</h1>
              <h1 class="ProblemT1">Names</h1>
            </div>
            <div v-for="(item, index) in problems" :key="index" class="Problem" @click="selectProblem(index)">
              <h1 :class="{'selected': selectedIndex === index}" class="Problems">{{ item.problem }}</h1>
              <h1 :class="{'selected': selectedIndex === index}" class="Names">{{ item.name }}</h1>
            </div>
          </div>
          <div class="buttons">
            <button class="clear" @click="clearItems">Clear</button>
           
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import router from '@/router';
import { onMounted, ref } from 'vue'

let ws;

const HandleConnection = () => {
  const ws = new WebSocket("ws://172.16.0.229:5000");
  
  ws.onopen = function() {
    ws.send("#INIT");
  };
  
  ws.onmessage = function(event) {
    localStorage.setItem("msg", event.data);
    let params = event.data.split(" ");
    if (params[0] === "#ALLOW") {
      //pass
    } else if(params[0] === "#DENY"){
      router.push('/login');
    }else{
      let msg = JSON.parse(event.data);
      localStorage.setItem("msg", JSON.stringify(msg));

      console.log(JSON.stringify(msg));
      //msg = 
      //[username,[1, 5428393492, 'Erçin adres', 'Mühendis', 'D:\\Repos\\CyberController\\src\\frontend\\public\\profile.png'],[1, 'D:\\Repos\\CyberController\\data\\history1.dat', 'history1', 1],ip]
      updateUserInfo(msg);

    }
  };
  
  ws.onerror = function(error) {
    console.log("WebSocket error: ", error);
    router.push("/");
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

onMounted(()=>{
  try{
    ws = HandleConnection();
    sendMessage(ws,"#CHECK "+localStorage.id);
    sendMessage(ws,"#GETPROFILE");
  }catch(error){
    console.log("Error at onmounted");
    router.push("/");
  }
});

// Bu fonksiyon order kısmında yeni kayıtları kaydedicek.











//Problemlerin bulunduğu array
const problems = ref([
  { problem: 'Problem1', name: 'Name1' },
  { problem: 'Problem2', name: 'Name2' },
  { problem: 'Problem3', name: 'Name3' },
  { problem: 'Problem4', name: 'Name4' },
])
const userInfo = ref({
  photo: '/profile.png',
  details: [
    { label: "Adı", value: "CANBERK" },
    { label: "Soyadı", value: "ARMAN" },
    { label: "ID", value: "11111" },
    { label: "Position", value: "Student" }
  ],
  tcpIp: "TCP IP"
});
const updateUserInfo = (msg) => {
  const [username, userDetails, history, ip] = msg;
  userInfo.value = {
    photo: userDetails[4], // Photo URL
    details: [
      { label: "Name", value: userDetails[2] }, // Name
      { label: "Position", value: userDetails[3] }, // Position or Address
      { label: "ID", value: userDetails[1] }, // ID
      { label: "Address", value: userDetails[3] } // Position (or modify as per correct label)
    ],
    tcpIp: ip
  };
};
//Problemi seçmek için fonksiyon
const selectedIndex = ref(null)
const selectProblem = (index) => {
  selectedIndex.value = index
}


// Problemleri clear etmek için
const clearItems = () => {
  sendMessage(ws,"#CLEARHISTORY");
  updateUserInfo();
  return;
}
//Problemleri silmek için

const logout = () => {
  sendMessage(ws,"#EXIT");
  localStorage.setItem("id",null);
  localStorage.setItem("auth",false);
  location.reload();
  return true;
}


</script>

<style scoped>

.container{
    width: 100%;
    height: 100%;
    overflow: scroll;
    font-family: "Roboto Flex", sans-serif;
}
.container::-webkit-scrollbar {
  width: 10px;
  display: none;
}

.container::-webkit-scrollbar-thumb {
  background-color: #b0b0b0; /* Gümüş grisi renk */
  border-radius: 5px;
}

.container::-webkit-scrollbar-thumb:hover {
  background-color: #a0a0a0; /* Hover sırasında biraz daha koyu gri */
}

.container::-webkit-scrollbar-track {
  background-color: #f0f0f0; /* Açık gri arka plan */
}
.up-profile{
    display: flex;
    width: 100%;
    height: 30%;
    color: white;
}
.profile-photo{
    scale: 0.4;
}
.other-profile-info{
    margin-top: 100px;
    display: flex;
    gap: 20px;
    font-size: 12px;
    font-family: "Roboto Flex", sans-serif;
    font-style: italic;
}
.label-acc{
    margin-left: 50px;
    width: 300px;
    height: 100px;
    border-radius: 5px;
    font-family: "Roboto Flex", sans-serif;
    font-style: italic;
    margin-right: 20px;
    display: flex;
}
.label-acc11{
  font-size: 10px;
  font-style: italic;
}
.profile-field {
  display: flex;
  gap: 10px;
}
.logout {
    margin-left: 40%;
    border: none;
    outline: none;
    padding: 8px 20px; /* Buton boyutunu küçültmek için padding'i azaltın */
    background: #ff5945;
    color: #fff;
    font-size: 14px; /* Font boyutunu biraz küçültün */
    cursor: pointer;
    border-radius: 15px; /* Daha yuvarlak köşeler için border-radius'u artırın */
    transition: background 0.3s ease; /* Hover efektini yumuşak hale getirin */
    height: 30px;
    font-family: "Roboto Flex", sans-serif;
    font-style: italic;
}

.logout:hover {
    background: #a59290; /* Hover sırasında arka plan rengini değiştirin */
}
.btnpopup{
    border: none;
    outline: none;
    padding: 8px 20px; /* Buton boyutunu küçültmek için padding'i azaltın */
    background: #ff5945;
    color: #fff;
    font-size: 14px; /* Font boyutunu biraz küçültün */
    cursor: pointer;
    border-radius: 15px; /* Daha yuvarlak köşeler için border-radius'u artırın */
    transition: background 0.3s ease; /* Hover efektini yumuşak hale getirin */
    height: 30px;
    font-family: "Roboto Flex", sans-serif;
}
.History{
    margin-left: 50px;
    width: 100%;
    height: 100%;
    border-radius: 5px;
    background: linear-gradient(90deg,#00f2ff,#f17c9e);
    border-radius: 15px;
    margin-right: 20px;
    margin-bottom: 100px; /* Listing Devices başlığını bir miktar aşağı kaydır */
    color: white;
    font-family: "Roboto Flex", sans-serif;
    font-style: italic;
}
.up-port{
    width: 100%;
    height: 300px;
    display: flex;
}
.label1{
    width: 100%;
    height: 200px;
    border-radius: 15px;
    margin-top: 20px;
    background: linear-gradient(90deg,#2bc1c8,#f17c9e);
    gap: 20px;
    font-size: 12px;
    font-family: "Roboto Flex", sans-serif;
    font-style: italic;
}
.table-texts{
    display: flex;
    gap: 20px;
    font-family: "Roboto Flex", sans-serif;
    font-style: italic;
    margin-left: 10px;
}
.Problem{
    display: flex;
    gap: 20px;
    cursor: pointer;
    font-family: "Roboto Flex", sans-serif;
    font-style: italic;
    margin-left: 10px;
}
.clear, .delete{
    border: none;
    outline: none;
    padding: 16px 40px;
    background: #ff5945;
    color: #fff;
    font-size: 20px;
    cursor: pointer;
    border-radius: 40px;
    height: 40px;
    font-family: "Roboto Flex", sans-serif;
    font-style: italic;
}
.selected {
  background-color: rgba(65, 133, 65, 0.907);
}
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-content {
  background-color: black;
  color: white;
  padding: 20px;
  border-radius: 10px;
  width: 400px;
  max-height: 90%;
  font-family: "Roboto Flex", sans-serif;
}

.close-btn {
  border: none;
  outline: none;
  background: red;
  color: white;
  padding: 10px;
  cursor: pointer;
  border-radius: 5px;
  margin-bottom: 10px;
  margin-left: 300px;
  font-family: "Roboto Flex", sans-serif;
  font-style: italic;
}
.kaydet1{
  border: none;
  outline: none;
  padding: 16px 40px;
  background: #ff5945;
  color: #fff;
  font-size: 20px;
  cursor: pointer;
  border-radius: 40px;
  height: 40px;
  font-family: "Roboto Flex", sans-serif;
  margin-top: -1%;
  font-style: italic;
}
.menu1 {
  margin-left: 35%;
  border-radius: 10px;
  background-color: black;
  color: white;
  font-family: "Roboto Flex", sans-serif;
  font-style: italic;
}
.Order{
    margin-left: 50px;
    width: 100%;
    height: 500px;
    border-radius: 15px;
    background: linear-gradient(90deg,#00f2ff,#f17c9e);
    margin-right: 20px;
    margin-bottom: 10px; /* Listing Devices başlığını bir miktar aşağı kaydır */
    color: white;
    font-family: "Roboto Flex", sans-serif;
    font-style: italic;
}
.menu-components{
  display: flex;
  gap: 30px;
  font-family: "Roboto Flex", sans-serif;
  margin-top: 5%;
  font-style: italic;
}
.tarih1, .saat1, .islem1, .isim1, .record1 {
  font-family: "Roboto Flex", sans-serif;
  font-weight: bold;
  font-size: 14px;
  color: #b4049c;
  font-style: italic;
}
.record1 {
  color: #baf5d7;
}
.down-order{
  margin-top: 100px;
  display: flex;
}
.label1{
  width: 50%;
  border-radius: 15px;
}
.btndelete1{
  border: none;
  outline: none;
  padding: 16px 40px;
  background: #ff5945;
  color: #fff;
  font-size: 20px;
  cursor: pointer;
  border-radius: 40px;
  height: 40px;
  font-family: "Roboto Flex", sans-serif;
  margin-top: 5%;
  margin-left: 10%;
  font-style: italic;
}
.buttons{
  margin-left: 10%;
  margin-top: 5%;
  display: flex;
  gap: 50px;
  font-style: italic;
}

@media (max-width: 768px) {
  .up-profile {
    flex-direction: column;
    align-items: center;
  }
  .profile-photo {
    scale: 0.6;
  }
  .other-profile-info {
    margin-top: 20px;
    flex-direction: column;
    align-items: center;
  }
  .logout {
    margin-left: 0;
    margin-top: 20px;
  }
  .History {
    margin-left: 0;
    margin-right: 0;
  }
  .label-acc {
    margin-left: 0;
    margin-right: 0;
  }
}

@media (max-width: 480px) {
  .up-profile {
    flex-direction: column;
    align-items: center;
  }
  .profile-photo {
    scale: 0.8;
  }
  .other-profile-info {
    margin-top: 10px;
    flex-direction: column;
    align-items: center;
  }
  .logout {
    margin-left: 0;
    margin-top: 10px;
  }
  .History {
    margin-left: 0;
    margin-right: 0;
  }
  .label-acc {
    margin-left: 0;
    margin-right: 0;
  }
  .clear, .delete {
    padding: 8px 20px;
    font-size: 16px;
  }
}


</style>