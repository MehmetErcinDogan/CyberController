<template>
 <div class="container">
    <div class="up-profile">
      <div class="profile-photo">
        <img src="/profile.png" alt="Profile Photo">
      </div>
      <div class="other-profile-info">
        <h1 class="name">Adı:</h1>
        <h1 class="name">CANBERK</h1>
        <h1 class="surname">Soyadı:</h1>
        <h1 class="surname">ARMAN</h1>
        <h1 class="account-id">ID:</h1>
        <h1 class="account-id">11111</h1>
        <h1 class="position">Position:</h1>
        <h1 class="position">Student</h1>
        <div class="label-acc">
          <div class="label-acc11">
            
            <h1 class="tcp-ipp">TCP IP</h1>

          </div>
          <!-- Bu buttona basıldığında logout olup tekrardan giriş ekranına gitmesi gerekiyor. Bunun için fonksiyonu yazılmalı. -->
          <button class="logout" @click="logout">Logout</button>
        </div>
      </div>
    </div>
    <div class="History">
      <h1 class="h1">History</h1>
      <!-- Kullanıcının history kısmı  -->
      <div class="port-scanner-info">
        <div class="up-port">
          <div class="label1">
            <div class="table-texts">
              <h1 class="ProblemT">Problems</h1>
              <h1 class="ProblemT1">Names</h1>
            </div>
            <!-- Burdaki problemler kısmının içeriğini script kısmındaki problems arrayinden alıyor bunu jsondan almalı. -->
            <div v-for="(item, index) in problems" :key="index" class="Problem" @click="selectProblem(index)">
              <h1 :class="{'selected': selectedIndex === index}" class="Problems">{{ item.problem }}</h1>
              <h1 :class="{'selected': selectedIndex === index}" class="Names">{{ item.name }}</h1>
            </div>
          </div>
          <div class="buttons">
            <!-- Kullanıcının problemleri silmesi ve temizlemesi için koyduğum buttonlar. -->
            
            <button class="clear" @click="clearItems">Clear</button>
            <button class="delete" @click="deleteItem">Delete</button>
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
      localStorage.setItem('auth',false);
      localStorage.setItem('id',null);
      router.push('/login');
    }else{

    }
  };
  
  ws.onerror = function(error) {
    console.log("WebSocket error: ", error);
    localStorage.setItem('auth',false);
    localStorage.setItem('id',null);
    router.push('/login');
  };
  
  ws.onclose = function() {
    localStorage.setItem('auth',false);
    localStorage.setItem('id',null);
    location.reload();
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
  }catch(error){
    console.log("Error at onmounted");
    router.push("/");
  }
  sendMessage("#GETPROFILE");
});

// Bu fonksiyon order kısmında yeni kayıtları kaydedicek.











//Problemlerin bulunduğu array
const problems = ref([
  { problem: 'Problem1', name: 'Name1' },
  { problem: 'Problem2', name: 'Name2' },
  { problem: 'Problem3', name: 'Name3' },
  { problem: 'Problem4', name: 'Name4' },
])
//Problemi seçmek için fonksiyon
const selectedIndex = ref(null)
const selectProblem = (index) => {
  selectedIndex.value = index
}


// Problemleri clear etmek için
const clearItems = () => {
  problems.value = []
  selectedIndex.value = null

}
//Problemleri silmek için
const deleteItem = () => {
  if (selectedIndex.value !== null) {
    problems.value.splice(selectedIndex.value, 1)
    selectedIndex.value = null
  } else {
    alert('Please select a problem to delete.')
  }
}
const logout = () => {
  console.log('User logged out');
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
   /* Listing Devices başlığını bir miktar aşağı kaydır */
  display: flex;
}
.label-acc11{
  font-size: 10px;
  font-style: italic;
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

.clear{
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

.delete{
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
  font-family: sans-serif;
  font-size: 14px;
  
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
.tarih1{
  font-family: "Roboto Flex", sans-serif;
  font-weight: bold;
  font-size: 14px;
  color: #b4049c;
  font-style: italic;

}
.saat1{
  font-family: "Roboto Flex", sans-serif;
  font-weight: bold;
  font-size: 14px;
  color: #b4049c;
  font-style: italic;

}
.islem1{
  font-family: "Roboto Flex", sans-serif;
  font-weight: bold;
  font-size: 14px;
  color: #b4049c;
  font-style: italic;

}
.isim1{
  font-family: "Roboto Flex", sans-serif;
  font-weight: bold;
  font-size: 14px;
  color: #b4049c;
  font-style: italic;

}
.record1{
  font-family: "Roboto Flex", sans-serif;
  font-weight: bold;
  font-size: 14px;
  color: #baf5d7;
  font-style: italic;

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


</style>